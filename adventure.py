import sys
import json

class Room:
    def __init__(self, name, desc, exits, items=None):
        self.name = name
        self.desc = desc
        self.exits = exits
        self.items = items if items else []

    def describe(self):
        room_info = f"> {self.name}\n\n{self.desc}\n"
        if self.items:
            room_info += "Items: " + ", ".join(self.items) + "\n"
        room_info += "Exits: " + " ".join(self.exits.keys()) + "\n"
        return room_info

class GameState:
    def __init__(self, rooms, start_room):
        self.rooms = {room.name: room for room in rooms}
        self.current_room = self.rooms[start_room]
        self.inventory = []
        self.commands = {
            "go": "go <direction>",
            "get": "get <item>",
            "look": "look",
            "inventory": "inventory",
            "drop": "drop <item>",
            "quit": "quit",
            "help": "help"
        }

    def process_command(self, command):
        command_parts = command.split()
        action = command_parts[0]
        args = command_parts[1:]

        if action in ['quit', 'exit']:
            print("Goodbye!")
            sys.exit(0)

        if action == "look":
            print(self.current_room.describe())
        elif action == "help":
            self.display_help()
        elif action == "inventory" or action == "inv":
            self.show_inventory()
        elif action == "go":
            self.handle_go(args)
        elif action == "get":
            self.handle_get(args)
        elif action == "drop":
            self.handle_drop(args)
        else:
            print("Unknown command. Type 'help' for a list of commands.")

    def show_inventory(self):
        if not self.inventory:
            print("You're not carrying anything.")
        else:
            print(f"Inventory:\n  {', '.join(self.inventory)}")

    def handle_go(self, args):
        if not args:
            print("Go where?")
            return
        arg = " ".join(args)
        matched_exits = [exit for exit in self.current_room.exits if exit.startswith(arg)]
        if len(matched_exits) == 1:
            self.move_to_room(matched_exits[0])
        elif len(matched_exits) > 1:
            print("Did you want to go " + " or ".join(matched_exits) + "?")
        else:
            print("There's no way to go " + arg + ".")

    def handle_get(self, args):
        if not args:
            print("Get what?")
            return
        arg = " ".join(args)
        matched_items = [item for item in self.current_room.items if arg in item]
        if len(matched_items) == 1:
            self.get_item(matched_items[0])
        elif len(matched_items) > 1:
            print("Did you want to get " + ", ".join(matched_items) + "?")
        else:
            print("There's no " + arg + " here.")

    def handle_drop(self, args):
        if not args:
            print("Drop what?")
            return
        item_name = " ".join(args)
        if item_name in self.inventory:
            self.inventory.remove(item_name)
            self.current_room.items.append(item_name)
            print(f"You dropped the {item_name}.")
        else:
            print(f"You don't have {item_name}.")

    def move_to_room(self, direction):
        next_room_name = self.current_room.exits[direction]
        next_room = self.rooms[next_room_name]
        self.current_room = next_room
        print(f"You go {direction}.\n")
        print(self.current_room.describe())

    def get_item(self, item_name):
        self.current_room.items.remove(item_name)
        self.inventory.append(item_name)
        print(f"You pick up the {item_name}.")

    def display_help(self):
        print("You can run the following commands:")
        for command, description in self.commands.items():
            print(f"  {command}: {description}")
        print()

def load_game_map(filename):
    try:
        with open(filename) as file:
            data = json.load(file)
            rooms = [Room(**room_data) for room_data in data['rooms']]
            start_room = data['start']
            return rooms, start_room
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 adventure.py [map filename]")
        sys.exit(1)

    map_filename = sys.argv[1]
    rooms, start_room = load_game_map(map_filename)
    game_state = GameState(rooms, start_room)

    print(game_state.current_room.describe())
    try:
        while True:
            command = input("What would you like to do? ").strip().lower()
            game_state.process_command(command)
    except EOFError:
        print("\nUse 'quit' to exit.")
        main()  # Restart the main loop to continue the game
    except KeyboardInterrupt:
        print("\nGoodbye!")  # Handle Ctrl-C to exit immediately
        sys.exit(0)

if __name__ == "__main__":
    main()



#comment