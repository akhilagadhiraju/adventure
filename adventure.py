import json
import sys

def load_map(filename):
    try:
        with open(filename, 'r') as file:
            game_map = json.load(file)
        
        # Validate map
        if "start" not in game_map or "rooms" not in game_map:
            raise ValueError("Map must have 'start' and 'rooms' keys")

        room_names = {room['name'] for room in game_map['rooms']}
        if len(room_names) != len(game_map['rooms']):
            raise ValueError("Duplicate room names found")

        for room in game_map['rooms']:
            for exit in room['exits'].values():
                if exit not in room_names:
                    raise ValueError(f"Invalid exit reference: {exit}")

        return game_map
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)

def game_loop(game_map):
    current_room = game_map['start']
    inventory = []
    commands = {
        "go": "go ...",
        "look": "look",
        "get": "get ...",
        "inventory": "inventory",
        "quit": "quit",
        "drop": "drop ...",
        "help": "help"
    }

    def display_room_info(room):
        print(f"> {room['name']}\n")
        print(room['desc'] + "\n")
        if 'items' in room and room['items']:
            print("Items: " + ", ".join(room['items']))
        print("Exits: " + " ".join(room['exits'].keys()) + "\n")

    while True:
        room_info = next(room for room in game_map['rooms'] if room['name'] == current_room)
        display_room_info(room_info)
        command = input("What would you like to do? ").strip().lower()

        if command in ["quit", "exit"]:
            print("Goodbye!")
            break
        elif command.startswith("go "):
            direction = command.split()[1]
            if direction in room_info['exits']:
                current_room = room_info['exits'][direction]
            else:
                print(f"There's no way to go {direction}.")
        elif command == "look":
            continue
        elif command.startswith("get "):
            item = command.split(maxsplit=1)[1]
            if "items" in room_info and item in room_info['items']:
                inventory.append(item)
                room_info['items'].remove(item)
                print(f"You pick up the {item}.")
            else:
                print(f"There's no {item} anywhere.")
        elif command == "inventory":
            if inventory:
                print("Inventory:\n  " + "\n  ".join(inventory))
            else:
                print("You're not carrying anything.")
        elif command.startswith("drop "):
            item = command.split(maxsplit=1)[1]
            if item in inventory:
                inventory.remove(item)
                room_info.setdefault('items', []).append(item)
                print(f"You drop the {item}.")
            else:
                print(f"You don't have {item} to drop.")
        elif command == "help":
            print("You can run the following commands:")
            for cmd in commands.values():
                print(f"  {cmd}")
        else:
            print("Unknown command.")

        # Check win condition in the Boss room
        if current_room == "Boss room" and set(["sword", "magic wand"]).issubset(set(inventory)):
            print("Congratulations! You have defeated the dark force with the sword and magic wand.")
            break
        elif current_room == "Boss room":
            print("You feel an overwhelming force push you out. You are not ready yet.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python adventure.py [map filename]")
        sys.exit(1)

    game_map = load_map(sys.argv[1])
    game_loop(game_map)


#comment