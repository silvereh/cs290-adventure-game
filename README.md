# cs290-adventure-game

This game is a textual story where the player must find a treasure chest in an old and abandoned castle. 
This game was realized in collaboration with Jacob White and D Wood. 
You can also see the Github repository for this project at: https://github.com/silvereh/cs290-adventure-game

Note: to run the game, you will need to install the library jsonpickle: https://pypi.python.org/pypi/jsonpickle

The requirements for this projects were: 
 - Minimum 12 rooms.
 	- The map shouldn't be just a line of rooms.
 - Having items.
 	- Items must have uses.
 		- An example is a key that can open doors.
 		- Another example is a weapon.
 - Combat system.
 	- Monsters can attack player.
 	- Player can attack monsters.
 	- Dead monsters stay dead.
 	- Game over when player dies.
 - Bunus: Room data loaded from separate file(s).

 Update V 2.0: Created another version of the game where the user can actually load and save a game.

 Update V 2.0.1: Remove restart option(which doesn't exist) in help function.

 Update V 2.0.2: Added some missing text in lower floor.
 				 Fixed a bug which was causing crash when the player was dying in combat.