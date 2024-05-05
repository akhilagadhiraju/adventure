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
    direction_mapping = {
        "n": "north",
        "s": "south",
        "e": "east",
        "w": "west",
        "ne": "northeast",
        "nw": "northwest",
        "se": "southeast",
        "sw": "southwest"
    }

    def display_room_info(room):
        print(f"> {room['name']}\n")
        print(room['desc'] + "\n")
        if 'items' in room and room['items']:
            print("Items: " + ", ".join(room['items']))
        print("Exits: " + " ".join(room['exits'].keys()) + "\n") # Detailed exits

    while True:
        room_info = next(room for room in game_map['rooms'] if room['name'] == current_room)
        display_room_info(room_info)
        command = input("What would you like to do? ").strip().lower()

        if command in ["quit", "exit"]:
            print("Goodbye!")
            break
        elif command in direction_mapping:
            full_direction = direction_mapping[command]
            if full_direction in room_info['exits']:
                current_room = room_info['exits'][full_direction]
            else:
                print(f"There's no way to go {full_direction}.")
        elif command.startswith("go "):
            direction = command.split()[1]
            full_direction = direction_mapping.get(direction, direction)  # Maps abbreviation or uses as-is
            if full_direction in room_info['exits']:
                current_room = room_info['exits'][full_direction]
            else:
                print(f"There's no way to go {full_direction}.")
        elif command.startswith("get "):
            prefix = command.split(maxsplit=1)[1]
            if 'items' in room_info:
                matching_items = [item for item in room_info['items'] if item.startswith(prefix)]
                if matching_items:
                    if len(matching_items) == 1:
                        item = matching_items[0]
                        inventory.append(item)
                        room_info['items'].remove(item)
                        print(f"You pick up the {item}.")
                    else:
                        response = input(f"Did you mean {' or '.join(matching_items)}? ").strip().lower()
                        if response in matching_items:
                            inventory.append(response)
                            room_info['items'].remove(response)
                            print(f"You pick up the {response}.")
                        else:
                            print("Invalid item. Try again.")
                else:
                    print(f"No item starting with '{prefix}'.")
            else:
                print("There are no items in this room.")
        elif command in ["inventory", "inv"]:
            if inventory:
                print("Inventory:\n  " + "\n  ".join(inventory))
            else:
                print("You're not carrying anything.")
        elif command == "look":
            display_room_info(room_info)
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
            print("  go [direction] - Move to the room in the specified direction.")
            print("  get [item] - Pick up an item from the room.")
            print("  look - Describe the current room, listing items and exits.")
            print("  inventory, inv - Display items currently in your inventory.")
            print("  drop [item] - Remove an item from your inventory and leave it in the room.")
            print("  quit - Exit the game.")
            print("  help - Display this help message.")
        else:
            print("Unknown command. Type 'help' for a list of commands.")

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
