#Text-Based Adventure Game
#Name:Akhila Gadhiraju
#Stevens Login: agadhira@stevens.edu
#GitHub Repository: 
#Project Overview
 This project is a text-based adventure game implemented in Python. Players navigate through various rooms, each uniquely described, by executing text commands that interact with the environment and items within the game world.

#Time Investment
 I spent approximately 15 hours developing, testing, and refining this game.

#Testing
 The code was tested both manually and using automated scripts. For automated tests, I used Python's subprocess module to simulate game sessions with predefined inputs and compared the results against expected outputs. This helped ensure that the game behaves as intended under various scenarios. Manual testing was performed by playing the game with all possible inputs as per project guidelines, ensuring that all features work seamlessly.

#Bugs and Issues
 No unresolved bugs or issues are present at the time of this writing. All identified issues have been addressed during the development process.

#Challenging Issue
In text-based adventure games, players often use abbreviated commands for efficiency and ease, especially for common actions like navigation. The challenge in this project arose when implementing abbreviated direction commands (e.g., 'n' for 'north', 's' for 'south', etc.). The issue became particularly complex when rooms had multiple exits in similar directions, such as 'north' and 'northeast'. The initial implementation allowed for simple abbreviations, but did not adequately handle situations where these abbreviations could refer to multiple possible directions. 

#Extensions Implemented
 1.Help Command: In text-based adventure games, especially ones with a variety of possible actions and commands, it can be challenging for players to remember all available interactions. The Help command is designed to assist players by listing all valid commands they can use at any point during gameplay. 
 2.Drop Command: The Drop command is essential for managing the player's inventory and interacting with the game's environment. It allows the player to remove items from their inventory and leave them in the current room, providing strategic gameplay elements related to item management.When players pick up items with the get command, these items are added to their inventory. If the inventory becomes overloaded, or if the player wishes to use or leave an item for later retrieval, they can use the drop command to place an item back into the room.
 3.Win Condition: The win condition is fulfilled in the "Boss room." The player must arrive with both a "sword" and a "magic wand" to succeed. The "sword" is located in the "Blue room" and the "magic wand" in the "Green room," which strategically requires navigating multiple rooms to collect these items before confronting the final challenge.

