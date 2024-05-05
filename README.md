#Text-Based Adventure Game
#Name:Akhila Gadhiraju
#Stevens Login: agadhira@stevens.edu
#GitHub Repository: https://github.com/akhilagadhiraju/adventure.git
#Project Overview
 This project is a text-based adventure game implemented in Python. Players navigate through various rooms, each uniquely described, by executing text commands that interact with the environment and items within the game world.

#Time Investment
 I spent approximately 16 hours developing, testing, and refining this game.

#Testing
 The code was tested both manually and using automated scripts. For automated tests, I used Python's subprocess module to simulate game sessions with predefined inputs and compared the results against expected outputs. This helped ensure that the game behaves as intended under various scenarios. Manual testing was performed by playing the game with all possible inputs as per project guidelines, ensuring that all features work seamlessly.

 For loop.map,I have tested using all the directions including northeast,northwest,southeast and southwest.

#Bugs and Issues
 No

#Challenging Issue
In text-based adventure games, players often use abbreviated commands for efficiency and ease, especially for common actions like navigation. The challenge in this project arose when implementing abbreviated direction commands (e.g., 'n' for 'north', 's' for 'south', etc.). The issue became particularly complex when rooms had multiple exits in similar directions, such as 'north' and 'northeast'. The initial implementation allowed for simple abbreviations, but did not adequately handle situations where these abbreviations could refer to multiple possible directions. 

#Extensions Implemented
 1.Help Command: In text-based adventure games, especially ones with a variety of possible actions and commands, it can be challenging for players to remember all available interactions. The Help command is designed to assist players by listing all valid commands they can use at any point during gameplay.I have mentioned the usage of 'help' command below.
Usage: python adventure.py [map filename]
PS C:\Users\Lenovo\Desktop\adventurefoc\adventure> python3 adventure.py loop.map                                                                    
> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? help
You can run the following commands:
  go [direction] - Move to the room in the specified direction.
  get [item] - Pick up an item from the room.
  look - Describe the current room, listing items and exits.
  inventory, inv - Display items currently in your inventory.
  drop [item] - Remove an item from your inventory and leave it in the room.
  quit - Exit the game.
  help - Display this help message.

 2.Drop Command: The Drop command is essential for managing the player's inventory and interacting with the game's environment. It allows the player to remove items from their inventory and leave them in the current room, providing strategic gameplay elements related to item management.When players pick up items with the get command, these items are added to their inventory. If the inventory becomes overloaded, or if the player wishes to use or leave an item for later retrieval, they can use the drop command to place an item back into the room.I have mentioned the usage of 'drop' command below.
 > A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? go east
> A red room

This room is fancy. It's red!

Items: rose
Exits: north west east

What would you like to do? get rose
You pick up the rose.
> A red room

This room is fancy. It's red!

Exits: north west east

What would you like to do? drop rose
You drop the rose.
> A red room

This room is fancy. It's red!

Items: rose
Exits: north west east

What would you like to do?

 3.Win Condition: The win condition is fulfilled in the "Boss room." The player must arrive with both a "sword" and a "magic wand" to succeed. The "sword" is located in the "Blue room" and the "magic wand" in the "Green room," which strategically requires navigating multiple rooms to collect these items before confronting the final challenge.I have mentioned the usage of 'win' command below.
 
 > A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? go north
> A blue room

This room is simple, too, but with blue walls.

Items: sword
Exits: east south

What would you like to do? get sword
You pick up the sword.
> A blue room

This room is simple, too, but with blue walls.

Exits: east south

What would you like to do? go east
> A green room

You are in a simple room, with bright green walls.

Items: magic wand, banana, bandana, bellows, deck of cards
Exits: west south

What would you like to do? get magic wand
You pick up the magic wand.
> A green room

You are in a simple room, with bright green walls.

Items: banana, bandana, bellows, deck of cards
Exits: west south

What would you like to do? inv
Inventory:
  sword
  magic wand
> A green room

You are in a simple room, with bright green walls.

Items: banana, bandana, bellows, deck of cards
Exits: west south

What would you like to do? go south
> A red room

This room is fancy. It's red!

Items: rose
Exits: north west east

What would you like to do? go east
Congratulations! You have defeated the dark force with the sword and magic wand.

These are the three extensions I have implemented in the text based adventure game.
