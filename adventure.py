import sys
import json

def load_map(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def display_room(room_id, rooms):
    room = rooms[room_id]
    room_desc = room['desc']
    exits_desc = 'Exits: ' + ' '.join(room['exits'].keys())
    items_desc = 'Items: ' + ' '.join(room.get('items', []))
    return f"> {room_id}\n\n{room_desc}\n\n{exits_desc}\n\n{items_desc}\n\nWhat would you like to do?"

def resolve_abbreviation(input_str, options, type="general"):
    if input_str == '':
        return '', False
    matches = [opt for opt in options if opt.startswith(input_str)]
    if len(matches) == 1:
        return matches[0], True
    elif not matches:
        return input_str, False
    elif type == "verb" and len(matches) > 1:
        return f"Did you want to {input_str} {' or '.join(matches)}?", False
    return ', '.join(matches), False

def go(direction, current_room, rooms, inventory):
    if not direction:
        return "Sorry, you need to 'go' somewhere.", current_room
    
    direction_map = {"n": "north", "s": "south", "e": "east", "w": "west",
                     "ne": "northeast", "nw": "northwest", "se": "southeast", "sw": "southwest"}
    full_direction = direction_map.get(direction, direction)
    resolved_direction, success = resolve_abbreviation(full_direction, rooms[current_room]['exits'].keys())
    if success:
        new_room = rooms[current_room]['exits'][resolved_direction]
        return display_room(new_room, rooms), new_room
    return f"Did you want to go {resolved_direction}?", current_room

def get(item, current_room, rooms, inventory):
    if not item:
        return "Sorry, you need to 'get' something.", inventory

    possible_items = rooms[current_room].get('items', [])
    resolved_item, success = resolve_abbreviation(item, possible_items)
    if success:
        inventory.append(resolved_item)
        rooms[current_room]['items'].remove(resolved_item)
        return f"You pick up the {resolved_item}.", inventory
    else:
        return f"Did you want to get {resolved_item}?", inventory

def look(current_room, rooms):
    return display_room(current_room, rooms), current_room

def inventory_display(inventory):
    if inventory:
        return "Inventory:\n  " + "\n  ".join(inventory)
    else:
        return "You're not carrying anything."

def drop(item, current_room, rooms, inventory):
    if item in inventory:
        inventory.remove(item)
        rooms[current_room].setdefault('items', []).append(item)
        return f"You drop the {item}.", inventory
    else:
        return f"You don't have a {item} to drop.", inventory

def help_command():
    return ("You can run the following commands:\n"
            "  go ...\n"
            "  get ...\n"
            "  look\n"
            "  inventory\n"
            "  drop ...\n"
            "  quit\n"
            "  help")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]")
        sys.exit(1)
    
    game_map = load_map(sys.argv[1])
    current_room = game_map['start']
    rooms = {room['name']: room for room in game_map['rooms']}
    inventory = []

    print(display_room(current_room, rooms))
    while True:
        command = input().strip().lower()
        parts = command.split()
        verb = parts[0]
        argument = ' '.join(parts[1:]) if len(parts) > 1 else ""

        if verb in ["quit", "q"]:
            print("Goodbye!")
            break
        elif verb in ["go", "g"]:
            output, current_room = go(argument, current_room, rooms, inventory)
            print(output)
        elif verb in ["look", "l"]:
            output, current_room = look(current_room, rooms)
            print(output)
        elif verb in ["get", "g"]:
            output, inventory = get(argument, current_room, rooms, inventory)
            print(output)
        elif verb in ["drop", "d"]:
            output, inventory = drop(argument, current_room, rooms, inventory)
            print(output)
        elif verb in ["inventory", "i"]:
            print(inventory_display(inventory))
        elif verb == "help":
            print(help_command())
        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    main()





#comment