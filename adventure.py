import json
import sys

class AdventureGame:
    def __init__(self, filename):
        self.game_map = self.load_map(filename)
        self.rooms = {room['name']: room for room in self.game_map['rooms']}
        self.current_room = self.rooms[self.game_map['start']]
        self.inventory = []
        self.running = True
        self.commands = {
            "go": "go [direction] - Move in the specified direction.",
            "get": "get [item] - Pick up an item from the room.",
            "drop": "drop [item] - Drop an item from your inventory into the room.",
            "look": "look - Re-describe the current room.",
            "inventory": "inventory - Show items in your inventory.",
            "quit": "quit - Exit the game.",
            "help": "help - Show this help message."
        }

    def load_map(self, filename):
        try:
            with open(filename, 'r') as file:
                game_map = json.load(file)
            self.validate_map(game_map)
            return game_map
        except Exception as e:
            sys.exit(f"Error loading map: {e}")

    def validate_map(self, game_map):
        if "start" not in game_map or "rooms" not in game_map:
            raise ValueError("Map must include 'start' and 'rooms'")
        if not isinstance(game_map['rooms'], list) or not all("name" in room for room in game_map['rooms']):
            raise ValueError("Each room must be a dictionary with a 'name' key")

    def describe_room(self):
        room = self.current_room
        print(f"\n> {room['name']}\n")
        print(f"{room['desc']}\n")
        
        if 'items' in room and room['items']:
            print("Items in the room: " + ", ".join(room['items']) + "\n")

        exits_formatted = ' '.join(room['exits'].keys())
        print(f"Exits: {exits_formatted}\n")

    def parse_command(self, command):
        if command.startswith('go '):
            self.handle_go(command[3:])
        elif command.startswith('get '):
            self.handle_get(command[4:])
        elif command.startswith('drop '):
            self.handle_drop(command[5:])
        elif command == 'look':
            self.describe_room()
        elif command == 'inventory':
            self.show_inventory()
        elif command == 'quit':
            self.running = False
            print("Goodbye!")
        elif command == 'help':
            self.show_help()
        else:
            print("I don't understand that command.")

    def handle_go(self, direction):
        if direction in self.current_room['exits']:
            new_room_name = self.current_room['exits'][direction]
            self.current_room = self.rooms[new_room_name]
        else:
            print("You can't go that way.")

    def handle_get(self, item):
        if 'items' in self.current_room and item in self.current_room['items']:
            self.inventory.append(item)
            self.current_room['items'].remove(item)
            print(f"You picked up the {item}.")
        else:
            print(f"There is no {item} here to pick up.")

    def handle_drop(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            if 'items' not in self.current_room:
                self.current_room['items'] = []
            self.current_room['items'].append(item)
            print(f"You dropped the {item}.")
        else:
            print(f"You do not have a {item} to drop.")

    def show_inventory(self):
        if self.inventory:
            print("You are carrying: " + ", ".join(self.inventory))
        else:
            print("You are not carrying anything.")

    def show_help(self):
        print("You can run the following commands:")
        for desc in self.commands.values():
            print(f"  {desc}")

    def run(self):
        while self.running:
            self.describe_room()
            command = input("What would you like to do? ").strip().lower()
            self.parse_command(command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]")
        sys.exit(1)

    game = AdventureGame(sys.argv[1])
    game.run()


#  comment