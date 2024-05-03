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
[Describe a challenging bug you encountered and how you resolved it. This section should detail the problem, your approach to solving it, and the solution.]

#Extensions Implemented
 1.Help Command: To assist players, the help command provides a list of all valid commands. This is crucial for guiding players on how to interact with the game.
 2.Drop Command: The drop feature allows players to remove items from their inventory and leave them in the current room, mirroring the functionality of the get command but in reverse.
 3.Win Condition: The win condition is fulfilled in the "Boss room." The player must arrive with both a "sword" and a "magic wand" to succeed. The "sword" is located in the "Blue room" and the "magic wand" in the "Green room," which strategically requires navigating multiple rooms to collect these items before confronting the final challenge.

