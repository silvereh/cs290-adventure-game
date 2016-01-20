#!/usr/bin/env python
# -*-coding:Utf-8 -*		

class Room(object):
	"""docstring for Room"""

class Outside(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Outside"
		self.firstText = "\nYou enter into the courtyard of a castle.\nThere is an entrance to the castle to the East, an overgrowth to the South and rubble to the North.\n"
		self.text = "\nYou return to the middle of the courtyard.\n"
		self.look = "\nThe castle is tall with some of it in ruins to the North.\nIt looks like it has been a while since someone lived here or took care of the grounds as the overgrowth has consumed most of the south side of the building.\nBehind you is the gate that you entered to get to the courtyard.\nBefore you the massive castle doors stand rusty and still.\n"
		Outside.count += 1

class Rubble(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Rubble"
		self.firstText = "\nYou walk northward, closer to the rubble.\nThe pile of rubble is extremely large, there was clearly a battle here at one point, and it has been long since the castle was abandoned.\n"
		self.text = "\nYou find yourself back at the rubble.\n"
		self.look = "\nYou see a number of rusty pikes sticking out of the rubble as evidence of the old battle.\n"
		Rubble.count += 1

class NorthRubble(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "North Rubble"
		self.firstText = "\nYou attempt to climb over the pile of rubble, and reach the top, steadying yourself on a large brick from the top of the castle.\nThis brick knocks loose and you slip, falling on a pike, impaling yourself.\nAfter some time in pain, you pass out and die.\n"
		
class Overgrowth(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Overgrowth"
		self.firstText = "\nYou decide to walk towards the overgrowth.\nAs you walk closer you see that it has grown halfway up the castle wall.\n"
		self.text = "\nYou find yourself back at the overgrowth.\n"
		self.look = "\nYou notice that it has grown so thick there is no possible way to move through it.\nHowever, upon closer inspection you see that there is a small opening just small enough to fit through.\n"
		Overgrowth.count += 1

class SouthOvergrowth(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "South Overgrowth"
		self.firstText = "\nAs you attempt to crawl through the hole you notice it keeps getting smaller, blocking your path.\nThe only option now is to go back.\n"
		self.look = "\nAs you decide to look around you get further entangled in the bushes.\nOut of nowhere, a snake slithers along your back.\nThinking it’s another branch you keep wiggling to get free.\nYou feel a sharp pain as the snake has bitten you.\nYour vision fades as does your life.\nYou die.\n"
		
class Hall(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Hallway"
		self.firstText = "\nYou approach the castle doors which are tall and wide.\nYou apply all of your might and pull the castle doors open.\nAfter entering inside of the castle you find yourself in a grand entrance hall.\nThere is a door to the North and South and a grand staircase leading Up and Down.\n"
		self.text = "\nYou return to the entrance Hall.\n"
		self.look = "\nYou quickly begin to look around taking in more of the details.\nThere are several pictures on the north wall.\nLooking closer it seems like it’s the monarchs who ruled within this castle.\n"
		Hall.count += 1

class Library(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Library"
		self.firstText = "\nYou push open the door and enter.\nUpon entering the room you notice it is a library.\nYou quickly begin to scan the whole room.\nThere are thousands of books lining the shelves.\nIn the middle lies a desk that holds an open book.\n"
		self.text = "\nYou return to the library.\n"
		self.item = "Clue"
		self.look = "\nThe book was wide open.\nYou flip it over to see the title “A Beginner’s Guide to Necromancy: Starting with the Undead”.\nShocked with the title you begin to thumb through the pages.\nWhile flipping through you find many things such as:\n\t“…blood is the cause of life.”,\n\t“…feed and water daily.”,\n\t“…turn the light away from them.”,\n\t“…keep away from fire and heat”.\nConfused you set the book down.\n"
		Library.count += 1

class Armory(Room):
	count = 0
	explored = False
	ennemyNumber = 1
	def __init__(self):
		Room.__init__(self)
		self.name = "Armory"
		self.firstText = "\nYou enter a room, shutting the door behind you with a *click*.\nImmediately a strong stench of rotting flesh fills your nostrils in the room.\nYou hear a moan, drawing your attention: directly across the room, further south, there’s a zombie ...\n"
		self.text = "\nAs you enter the room again the stench is strong.\nNothing has changed within the armory.\n"
		self.item = "Key"
		self.meleeWeapon = "Sword"
		self.rangeWeapon = "Bow and Arrows"
		self.stuff = "Boots"
		self.ennemy = "Zombie Guardian"
		self.look = "\nLooking around, you see several weapons and items around the room.\nYou must be in an armory.\nUnfortunately, the zombie has noticed your presence and is making its way towards you.\n"
		Armory.count += 1

class HallUpper(Room):
	count = 0
	explored = False
	trapRemoved = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Upper Hallway"
		self.firstText = "\nYou decide to head upstairs.\nYour footsteps echo loudly as you walked up the big stone steps.\nAfter a short while you reach the top of the stairs.\nYou are in a corner and can see two closed doors.\nThere are two rooms.\nThe one to the south has a lamp that’s burning close to the door.\nThe one on the west is chained with a padlock.\n"
		self.text = "\nYou find yourself back at the top of the stairs.\n"
		self.look = "\nThe lamp is burning brightly although it seems to have no fuel source.\nIt’s purely burning on the wall.\nThat padlock looks pretty tough.\nNot getting in there without a key.\n"
		HallUpper.count += 1

class LockedDoor(Room):
	count = 0
	explored = False
	unlocked = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Locked Door"
		self.firstText = "\nThe door is padlocked shut.\n"
		self.look = "\nThe door is padlocked shut.\n"
		
class ObservationTower(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Observation Tower"
		self.firstText = "\nAfter unlocking the door you open it to a staircase.\nYou begin to climb and slowly but surely you reach the top of the tower.\nHanging in the middle of the room is a lamp.\n"
		self.text = "\nYou find yourself back in the observation tower.\n"
		self.item = "Lamp"
		self.look = "\nIt looks like this Lamp runs on oil.\nYou look around you and can see what is surrounding the castle.\nThere is nothing around the castle.\nThe only things that you see is the courtyard down below.\n"
		ObservationTower.count += 1

class TrappedRoom(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Trapped Room"
		self.firstText = "\nYou open the door to find a hall.\nPaintings litter the walls.\nAt the other end of the hallway you see a doorway.\n"
		self.text = "\nYou find yourself back into the painted corrider.\n"
		self.look = "\nWhile looking at the paintings on the wall you notice some strange things.\nThere is an empty frame that has inscribed “King Charles VI”.\n Another painting titled “The great war of 1332” has some disfigured and dismembered people fighting the king’s knights.\n"
		TrappedRoom.count += 1

class GuestRoom(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Guest Room"
		self.firstText = "\nYou reach the door and push it open.\nYou enter into a small room.\nOn the right there is a bed.\nThe bed is neatly made and it seems as though no one, except a few bugs, has used it in a while.\nTo the left there is a small table where there appears to be a jar with some sort of liquid inside.\n"
		self.text = "\nYou find yourself back in the guest room.\n"
		self.item = "Oil"
		self.look = "\nAs you walk over to the table you see that the jar is full with oiL.\n"
		GuestRoom.count += 1

class HallLower(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Lower Hallway"
		self.firstText = "\nThe farther you walk down the stairs the darker it gets.\nWhen it has become completely dark you reach the end of the stairs.\nFrom what you can tell you are standing on a landing at the bottom of the stairs.\nYou are alone in the dark.\n"
		self.text = "\nYou find yourself back at the bottom of the staircase.\n"
		self.look = "\nIt is almost impossible to see your hand in front of your face.\nYou begin to feel around in the dark.\nYou feel the staircase to the east.\nFeeling the wall to the west you feel an opening.\n"
		HallLower.count += 1

class DarkCorridorEntrance(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Dark Corridor Entrance"
		self.firstText = "\nYou walk through the opening without being able to see.\nYou hear stifled moaning and groaning.\nYou try to feel around again.\nYou only feel the entrance way to the East and the wall keeps on going.\n"
		self.text = "\nYou find yourself back in the dark corridor entrance.\n"
		self.look = "\nDetail"
		DarkCorridorEntrance.count += 1

class DarkCorridor(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Dark Corridor"
		self.firstText = "\nYou keep going through the corridor.\nSeeking through the darkness, you bump into something.\nPain begins to come to you and you realize you’re being bitten repeatedly.\nYou’re getting eaten! You will never know what killed you.\n"

class HallLowerLight(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Lower Hallway Light"
		self.firstText = "\nYou see skulls lining the walls.\nYou realize you’ve just headed down into a catacomb.\nYou see an entrance straight across from you to the east.\nYour light reaches just past the entrance into the next room.\n"
		self.text = "\nYou find yourself back at the bottom of the staircase.\n"
		self.look = "\n\n"
		HallLowerLight.count += 1

class CatacombsEntrance(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Catacombs Entrance"
		self.firstText = "\nGoing through the entrance your light begins to creep along the walls, slowly lighting the area around you.\nYour lamp dimly lights something in the distance.\nYou can see that it looks like a person or a statue of a person.\n"
		self.text = "\nYou find yourself back in the catacombs entrance.\n"
		self.look = "\nDetail"
		CatacombsEntrance.count += 1

class Catacombs(Room):
	count = 0
	explored = False
	ennemyNumber = 50
	def __init__(self):
		Room.__init__(self)
		self.name = "Catacombs"
		self.firstText = "\nCurious about the figure in the distance you press forward.\nAs you slowly approach you see more and more figures.\nThe first figure turns around.\nAs you keep going through the corridor, you can see that it’s a zombie.\nThere are much more ...\nAre you going to Fight?\n"
		self.text = "\n"
		self.ennemy = "Zombie"
		self.look = "\nFor some reason plunging straight into the zombies with no weapon seemed like a good idea.\nYou start getting bitten and your vision fades to black...\n"
		Catacombs.count += 1

class TreasureRoom(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Treasure Room"
		self.firstText = "\nYou walk west through the hall with a few flickers of flame still burning.\nYou begin to see the hall coming to an end.\nAt the end of the hall is “the treasure”.\nCongratulations you’ve won the game!!\n"

class DeathChamber(Room):
	count = 0
	explored = False
	def __init__(self):
		Room.__init__(self)
		self.name = "Death Chamber"
		self.firstText = "\nUpon entering the room you feel the floor drop from beneath your feet.\nIT’S A TRAP! You begin falling and look down.\nYour last few thoughts are of home as you watch the spikes getting closer and closer.\nYou end up impaled on a spike.\nYou have died.\n"
