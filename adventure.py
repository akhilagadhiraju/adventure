import json
import sys

def load_map(filename):
    try:
        with open(filename, 'r') as file:
            game_map = json.load(file)
        
        # Basic validation (omitted for brevity)
        return game_map
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)

def resolve_abbreviation(input, choices, full_forms):
    if input in full_forms:
        full_input = full_forms[input]
        if full_input in choices:
            return full_input, None  # Direct match to full form
    matches = [choice for choice in choices if choice.startswith(input)]
    if len(matches) == 1:
        return matches[0], None
    elif len(matches) > 1:
        return None, f"Did you mean {' or '.join(matches)}?"
    return None, f"No valid options for '{input}'"

def game_loop(game_map):
    current_room = game_map['start']
    inventory = []
    valid_commands = ["go", "get", "look", "inventory", "quit", "drop", "help"]
    direction_abbreviations = {
        'n': 'north', 'e': 'east', 'w': 'west', 's': 'south',
        'ne': 'northeast', 'nw': 'northwest', 'sw': 'southwest', 'se': 'southeast'
    }

    while True:
        room_info = next(room for room in game_map['rooms'] if room['name'] == current_room)
        print(f"> {room_info['name']}\n{room_info['desc']}\n")
        if 'items' in room_info and room_info['items']:
            print("Items: " + ", ".join(room_info['items']))
        print("Exits: " + " ".join(room_info['exits'].keys()) + "\n")
        
        command = input("What would you like to do? ").strip().lower()
        command_parts = command.split()
        if not command_parts:
            continue

        cmd = command_parts[0]
        if cmd in direction_abbreviations and len(command_parts) == 1:
            cmd = "go"
            command_parts = ["go", direction_abbreviations[command_parts[0]]]

        if cmd not in valid_commands and cmd not in direction_abbreviations:
            print("Unknown command.")
            continue

        if cmd == "quit":
            print("Goodbye!")
            break
        elif cmd in ["go", "drop", "get"] and len(command_parts) < 2:
            print(f"Please specify where or what to {cmd}.")
        elif cmd == "go":
            direction, error = resolve_abbreviation(command_parts[1], room_info['exits'].keys(), direction_abbreviations)
            if error:
                print(error)
            elif direction:
                current_room = room_info['exits'][direction]
        elif cmd == "look":
            continue
        elif cmd == "get":
            item, error = resolve_abbreviation(command_parts[1], room_info.get('items', []), {})
            if error:
                print(error)
            elif item:
                inventory.append(item)
                room_info['items'].remove(item)
                print(f"You pick up the {item}.")
        elif cmd == "inventory":
            if inventory:
                print("Inventory:\n  " + "\n  ".join(inventory))
            else:
                print("You're not carrying anything.")
        elif cmd == "drop":
            item, error = resolve_abbreviation(command_parts[1], inventory, {})
            if error:
                print(error)
            elif item:
                inventory.remove(item)
                room_info.setdefault('items', []).append(item)
                print(f"You drop the {item}.")
        elif cmd == "help":
            print("Available commands: go, get, look, inventory, quit, drop, help")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python adventure.py [map filename]")
        sys.exit(1)
    game_map = load_map(sys.argv[1])
    game_loop(game_map)



#comment