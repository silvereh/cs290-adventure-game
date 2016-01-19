#!/usr/bin/env python
# -*-coding:Utf-8 -*		

class Room(object):
	"""docstring for Room"""
	def __init__(self):
		self.look = ""
		self.name = ""
		self.text = ""
		self.firstText = ""
		self.explored = False
	# Get
	def _getLook(self):
		print(self.look)
	def _getName(self):
		print(self.name)
	def _getText(self):
		print(self.text)
	def _getFirstText(self):
		print(self.firstText)
	# Set
	def _setLook(self, newLook):
		self.look = newLook
	def _setName(self, newName):
		self.name = newName
	def _setText(self, newText):
		self.text = newText
	def _setFirstText(self, newFirstText):
		self.firstText = newFirstText
	# Properties
	look = property(_getLook, _setLook)
	name = property(_getName, _setName)
	text = property(_getText, _setText)
	firstText = property(_getFirstText, _setFirstText)

class Outside(Room):
	count = 0
	def __init__(self):
		self.name = "Outside"
		self.firstText = "You enter into the courtyard of a castle. There is an entrance to the castle to the East, an overgrowth to the South and rubble to the North."
		self.text = "You return to the middle of the courtyard."
		self.look = "Detail"
		Outside.count += 1

class Rubble(Room):
	count = 0
	def __init__(self):
		self.name = "Rubble"
		self.firstText = "You walk northward, closer to the rubble. The pile of rubble is extremely large, there was clearly a battle here at one point, and it has been long since the castle was abandoned."
		self.text = "You find yourself back at the rubble."
		self.look = "You see a number of rusty pikes sticking out of the rubble as evidence of the old battle."
		Rubble.count += 1

class NorthRubble(Room):
	count = 0
	def __init__(self):
		self.name = "North Rubble"
		self.firstText = "You attempt to climb over the pile of rubble, and reach the top, steadying yourself on a large brick from the top of the castle. This brick knocks loose and you slip, falling on a pike, impaling yourself. After some time in pain, you pass out and die."
		
class Overgrowth(Room):
	count = 0
	def __init__(self):
		self.name = "Overgrowth"
		self.firstText = "You decide to walk towards the overgrowth. As you walk closer you see that it has grown halfway up the castle wall."
		self.text = "You find yourself back at the overgrowth."
		self.look = "You notice that it has grown so thick there is no possible way to move through it. However, upon closer inspection you see that there is a small opening just small enough to fit through."
		Overgrowth.count += 1

class SouthOvergrow(Room):
	count = 0
	def __init__(self):
		self.name = "South Overgrow"
		self.firstText = "As you attempt to crawl through the hole you notice it keeps getting smaller, blocking your path. The only option now is to go back."
		self.look = "As you decide to look around you get further entangled in the bushes. Out of nowhere, a snake slithers along your back. Thinking it’s another branch you keep wiggling to get free. You feel a sharp pain as the snake has bitten you. Your vision fades as does your life. You die."
		
class Hall(Room):
	count = 0
	def __init__(self):
		self.name = "Hallway"
		self.firstText = "You approach the castle doors which are tall and wide. You apply all of your might and pull the castle doors open. After entering inside of the castle you find yourself in a grand entrance hall. There is a door to the North and South and a grand staircase leading Up and Down."
		self.text = "You return to the entrance Hall."
		self.look = "You quickly begin to look around taking in more of the details. There are several pictures on the north wall. Looking closer it seems like it’s the monarchs who ruled within this castle."
		Hall.count += 1

class Library(Room):
	count = 0
	def __init__(self):
		self.name = "Library"
		self.firstText = "You push open the door and enter. Upon entering the room you notice it is a library. You quickly begin to scan the whole room. There are thousands of books lining the shelves. In the middle lies a desk that holds an open book."
		self.text = "You return to the library."
		self.item = "Clue"
		self.look = "The book was wide open. You flip it over to see the title “A Beginner’s Guide to Necromancy: Starting with the Undead”. Shocked with the title you begin to thumb through the pages. While flipping through you find many things such as “…blood is the cause of life.”, “…feed and water daily.”, “…turn the light away from them.”, and “…keep away from fire and heat”. Confused you set the book down."
		Library.count += 1

class Armory(Room):
	count = 0
	ennemyNumber = 1
	def __init__(self):
		self.name = "Armory"
		self.firstText = "Armory"
		self.text = "You find yourself back in the armory."
		self.item = "Key"
		self.meleeWeapon = "Sword"
		self.rangeWeapon = "Bow and Arrows"
		self.stuff = "Boots"
		self.ennemy = "Zombie Guardian"
		self.look = "Detail"
		Armory.count += 1

class HallUpper(Room):
	count = 0
	trapRemoved = False
	def __init__(self):
		self.name = "Upper Hallway"
		self.firstText = "You decide to head upstairs. Your footsteps echo loudly as you walked up the big stone steps. After a short while you reach the top of the stairs. You are in a corner and can see two closed doors. There are two rooms. The one to the south has a lamp that’s burning close to the door. The one on the west is chained with a padlock."
		self.text = "You find yourself back at the top of the stairs."
		self.look = "The lamp is burning brightly although it seems to have no fuel source. It’s purely burning on the wall. That padlock looks pretty tough. Not getting in there without a key."
		HallUpper.count += 1

class LockedDoor(Room):
	count = 0
	unlocked = False
	def __init__(self):
		self.name = "Locked Door"
		self.firstText = "The door is padlocked shut."
		
class ObservationTower(Room):
	count = 0
	def __init__(self):
		self.name = "Observation Tower"
		self.firstText = "After unlocking the door you open it to a staircase. You begin to climb and slowly but surely you reach the top of the tower. Hanging in the middle of the room is a lamp."
		self.text = "You find yourself back in the observation tower."
		self.item = "Lamp"
		self.look = "It looks like this Lamp runs on oil. You look around you and can see what is surrounding the castle. There is nothing around the castle. The only things that you see is the courtyard down below."
		ObservationTower.count += 1

class TrappedRoom(Room):
	count = 0
	def __init__(self):
		self.name = "Trapped Room"
		self.firstText = "You open the door to find a hall. Paintings litter the walls. At the other end of the hallway you see a doorway."
		self.text = "You find yourself back into the painted corrider."
		self.look = "While looking at the paintings on the wall you notice some strange things. There is an empty frame that has inscribed “King Charles VI”.  Another painting titled “The great war of 1332” has some disfigured and dismembered people fighting the king’s knights."
		TrappedRoom.count += 1

class GuestRoom(Room):
	count = 0
	def __init__(self):
		self.name = "Guest Room"
		self.firstText = "You reach the door and push it open. You enter into a small room. On the right there is a bed. The bed is neatly made and it seems as though no one, except a few bugs, has used it in a while. To the left there is a small table where there appears to be a jar with some sort of liquid inside."
		self.text = "Guest Room"
		self.item = "Oil"
		self.look = "As you walk over to the table you see that the jar is full with oiL."
		GuestRoom.count += 1

class HallLower(Room):
	count = 0
	def __init__(self):
		self.name = "Lower Hallway"
		self.firstText = "The farther you walk down the stairs the darker it gets. When it has become completely dark you reach the end of the stairs. From what you can tell you are standing on a landing at the bottom of the stairs. You are alone in the dark."
		self.text = "You find yourself back at the bottom of the staircase."
		self.look = "It is almost impossible to see your hand in front of your face. You begin to feel around in the dark. You feel the staircase to the east. Feeling the wall to the west you feel an opening."
		HallLower.count += 1

class DarkCorridorEntrance(Room):
	count = 0
	def __init__(self):
		self.name = "Dark Corridor Entrance"
		self.firstText = "You walk through the opening without being able to see. You hear stifled moaning and groaning. You try to feel around again. You only feel the entrance way to the East and the wall keeps on going."
		self.text = "You find yourself back in the dark corridor entrance."
		self.look = "Detail"
		DarkCorridorEntrance.count += 1

class DarkCorridor(Room):
	count = 0
	def __init__(self):
		self.name = "Dark Corridor"
		self.firstText = "You keep going through the corridor. Seeking through the darkness, you bump into something. Pain begins to come to you and you realize you’re being bitten repeatedly. You’re getting eaten! You will never know what killed you."

class HallLowerLight(Room):
	count = 0
	def __init__(self):
		self.name = "Lower Hallway Light"
		self.firstText = "You see skulls lining the walls. You realize you’ve just headed down into a catacomb. You see an entrance straight across from you to the east. Your light reaches just past the entrance into the next room."
		self.text = "You find yourself back at the bottom of the staircase."
		self.look = ""
		HallLowerLight.count += 1

class CatacombsEntrance(Room):
	count = 0
	def __init__(self):
		self.name = "Catacombs Entrance"
		self.firstText = "Going through the entrance your light begins to creep along the walls, slowly lighting the area around you. Your lamp dimly lights something in the distance. You can see that it looks like a person or a statue of a person."
		self.text = "You find yourself back in the catacombs entrance."
		self.look = "Detail"
		CatacombsEntrance.count += 1

class Catacombs(Room):
	count = 0
	ennemyNumber = 50
	def __init__(self):
		self.name = "Catacombs"
		self.firstText = "Curious about the figure in the distance you press forward. As you slowly approach you see more and more figures. The first figure turns around. As you keep going through the corridor, you can see that it’s a zombie. There are much more ... Are you going to Fight?"
		self.text = ""
		self.ennemy = "Zombie"
		self.look = "For some reason plunging straight into the zombies with no weapon seemed like a good idea. You start getting bitten and your vision fades to black..."
		Catacombs.count += 1

class TreasureRoom(Room):
	count = 0
	def __init__(self):
		self.name = "Treasure Room"
		self.firstText = "You walk west through the hall with a few flickers of flame still burning. You begin to see the hall coming to an end. At the end of the hall is “the treasure”. Congratulations you’ve won the game!!"

class DeathChamber(Room):
	count = 0
	def __init__(self):
		self.name = "Death Chamber"
		self.firstText = "Upon entering the room you feel the floor drop from beneath your feet. IT’S A TRAP! You begin falling and look down. Your last few thoughts are of home as you watch the spikes getting closer and closer. You end up impaled on a spike. You have died."
