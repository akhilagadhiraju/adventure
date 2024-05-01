import json
import sys

class AdventureGame:
    def __init__(self, filename):
        self.visited_exits = {}
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
        except FileNotFoundError:
            sys.exit("Error: The map file was not found.")
        except json.JSONDecodeError:
            sys.exit("Error: The map file is not a valid JSON.")
        except Exception as e:
            sys.exit(f"Error loading map: {e}")

    def validate_map(self, game_map):
        if "start" not in game_map or "rooms" not in game_map:
            raise ValueError("Map must include 'start' and 'rooms'")
        if not isinstance(game_map['rooms'], list) or not all(isinstance(room, dict) and "name" in room for room in game_map['rooms']):
            raise ValueError("Each room must be a dictionary with at least a 'name' key")
        room_names = [room['name'] for room in game_map['rooms']]
        if len(room_names) != len(set(room_names)):
            raise ValueError("Room names must be unique")
        if game_map['start'] not in room_names:
            raise ValueError("Start room must be one of the rooms")
        if any(set(room.get('exits', {}).values()) - set(room_names) for room in game_map['rooms']):
            raise ValueError("All exits must point to existing rooms")

    def describe_room(self):
        print(f"\n> {self.current_room['name']}\n{self.current_room['desc']}")
        if 'items' in self.current_room and self.current_room['items']:
            print("Items in the room: " + ", ".join(self.current_room['items']))
        print("Exits: " + ', '.join(self.current_room['exits'].keys()))

    def parse_command(self, command):
        args = command.split()
        action = args[0]
        options = ' '.join(args[1:])
        handler = getattr(self, f'handle_{action}', lambda: print("I don't understand that command."))
        handler(options)

    def handle_go(self, direction):
        if direction in self.visited_exits.get(self.current_room['name'], {}):
            print("You have already visited this exit in this direction.")
            return

        if self.current_room['exits'].get(direction):
            self.visited_exits[self.current_room['name']][direction] = self.current_room
            self.current_room = self.rooms[self.current_room['exits'][direction]]
            self.describe_room()
        else:
            print("You can't go that way.")

    def handle_get(self, item):
        if item in self.current_room['items']:
            self.current_room['items'].remove(item)
            self.inventory.append(item)
            print(f"You picked up the {item}.")
        else:
            print(f"There is no {item} here to pick up.")

    def handle_drop(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_room['items'].append(item)
            print(f"You dropped the {item}.")
        else:
            print(f"You do not have a {item} to drop.")

    def handle_look(self):
        self.describe_room()

    def handle_inventory(self):
        if self.inventory:
            print("You are carrying: " + ", ".join(self.inventory))
        else:
            print("You are not carrying anything.")

    def handle_help(self):
        print("You can run the following commands:")
        for desc in self.commands.values():
            print(f"  {desc}")

    def handle_quit(self):
        self.running = False
        print("Goodbye!")

    def run(self):
        self.visited_exits = {}
        self.describe_room()
        while self.running:
            command = input("What would you like to do? ").strip().lower()
            if command == "quit":
                self.handle_quit()
                break
            self.parse_command(command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map filename]")
        sys.exit(1)

    game = AdventureGame(sys.argv[1])
    game.run()



#comment