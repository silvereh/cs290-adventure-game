#!/usr/bin/env python
# -*-coding:Utf-8 -*

from Player import *
from Room import *

import random

class Game(object):
	"""docstring for Game"""
	def __init__(self):
		self.player = Player()
		self.room = Outside()
		self.command = {
			"q": self.quit,
			"r": self.restart,
			"h": self.help,
			"l": self.look,
			"n": self.north,
			"s": self.south,
			"e": self.east,
			"w": self.west,
			"u": self.up,
			"d": self.down,
			"f": self.battle,
			"i": self.player.showInventory
		}
		self.ennemy = ""
		self.switcherWeapon = [
			"Sword",
			"Boots",
			"Bow and Arrows"
		]
		self.fightMode = 0

	def restart(self):
		self.player = Player()
		self.room = Outside()
		self.command = {
			"q": self.quit,
			"r": self.restart,
			"h": self.help,
			"l": self.look,
			"n": self.north,
			"s": self.south,
			"e": self.east,
			"w": self.west,
			"u": self.up,
			"d": self.down,
			"f": self.battle,
			"i": self.player.showInventory
		}
		self.ennemy = ""
		self.switcherWeapon = [
			"Sword",
			"Boots",
			"Bow and Arrows"
		]
		self.fightMode = 0
		Outside.count = 0
		Rubble.count = 0
		NorthRubble.count = 0
		Overgrowth.count = 0
		SouthOvergrowth.count = 0
		Hall.count = 0
		Library.count = 0
		Armory.count = 0
		HallUpper.count = 0
		LockedDoor.count = 0
		ObservationTower.count = 0
		TrappedRoom.count = 0
		GuestRoom.count = 0
		HallLower.count = 0
		HallLowerLight.count = 0
		DarkCorridor.count = 0
		DarkCorridorEntrance.count = 0
		TreasureRoom.count = 0
		DeathChamber.count = 0
		Catacombs.count = 0
		CatacombsEntrance.count = 0

		Armory.ennemyNumber = 1
		Catacombs.ennemyNumber = 50

		HallUpper.trapRemoved = False
		LockedDoor.unlocked = False
		print self.room.firstText
		
	def quit(self):
		"""Quit the game."""
		save = raw_input("So sad to see you leave. Do you want to save? (y/n)").lower()
		if save == "y":
			saveGame(self)

	def help(self):
		"""Displays a list of available commands."""
		print("Here is a non exhaustive list of available commands:")
		print("l: expLore the current room.")
		print("n: move to the North.")
		print("s: move to the South.")
		print("e: move to the East.")
		print("w: move to the West.")
		print("i: display your Inventory.")
		print("q: Quit the game.")
		print("r: Restart the game.")
		print("h: display this Help section.")
		print("Please note that this list is not exhaustive.")
		print("You might find some clues about other commands in the description of the room.")

	def look(self):
		"""The player looks around him/her in the room to find something interesting."""
		if (not self.player.isDead):
			print self.room.look
			if self.room.name == "South Overgrowth":
				self.player.die()
			if self.room.name == "Library":
				self.player.inventory.append("Clue")
			if self.room.name == "Armory":
				if Armory.ennemyNumber > 0:
					self.battle()
				else:
					Armory.explored = True
					print("Now that the zombie Guardian is dead, you're free to explore the room. \nYou find a few interesting things:")
					if "Key" not in self.player.inventory:
						print("- the key fell unDer the table.")
					if "Sword" not in self.player.inventory:
						print("- you find a sword on the South-east corner which looks in a great shape.")
					if "Bow and Arrows" not in self.player.inventory:
						print("- you see a bow and some arrows on the north-West corner.")
					if "Boots" not in self.player.inventory:
						print("- there is a nice pair of boots on the East side of the room.")
			if self.room.name == "Locked Door":
				if "Key" in self.player.inventory and LockedDoor.explored == True and LockedDoor.unlocked == False:
					LockedDoor.unlocked = True
					print("You decide to try using the key you found in the armory. \nYou insert it into the lock and gently turn it, then you hear a 'Click' and the chain falls.")
					self.room = ObservationTower()
					print self.room.firstText
				elif "Key" in self.player.inventory:
					print("While looking at the Lock, you notice that the key you found in the armory would fit.")
					LockedDoor.explored = True
			if self.room.name == "Observation Tower":
				if ObservationTower.explored == True:
					if "Lamp" not in self.player.inventory:
						print("You grab the lamp and put it in your backpack.")
						if "Oil" not in self.player.inventory:
							self.player.inventory.append("Lamp")
						else:
							self.player.inventory.remove("Oil")
							self.player.inventory.append("Lamp and Oil")
				else:
					ObservationTower.explored = True
			if self.room.name == "Upper Hallway":
				if "Clue" in self.player.inventory:
					choice = raw_input("You had time to think about what you read in the book and you're now sure that there is a trap here. What will you do:\n- Turn the lamp.\n- Pull the lamp.\n- Nothing\n").lower()
					if choice == "t":
						HallUpper.trapRemoved = True
						print("As you slowly begin to turn the lamp you hear gears turning and the light begins to fade. \nIn the distance you hear a machine begin to operate and a loud grinding noise. You look around you and everything is silent again.")
					elif choice == "p":
						print("as you slowly begin to pull the lamp you hear gears turning and the light begins to fade. \nIn the distance you hear a machine begin to operate and a loud grinding noise. You look around you and everything is silent again.")
				HallUpper.explored = True
			if self.room.name == "Guest Room":
				if GuestRoom.explored == True:
					if "Oil" not in self.player.inventory:
						print("You grab the oil and put it in your backpack.")
						if "Lamp" not in self.player.inventory:
							self.player.inventory.append("Oil")
						else:
							self.player.inventory.remove("Lamp")
							self.player.inventory.append("Lamp and Oil")
				else:
					GuestRoom.explored = True
			if self.room.name == "Lower Hallway":
				if "Lamp and Oil" in self.player.inventory and HallLower.explored == True:
					self.room = HallLowerLight()
					if HallLowerLight.count < 2:
						print self.room.firstText
					else:
						print self.room.text
				elif "Lamp and Oil" in self.player.inventory:
					print("You can barely see anything, thinking about it, you remember you have the Lamp you found in your backpack. \nFortunately, you also found some oil to light it.")
				HallLower.explored = True
			if self.room.name == "Dark Corridor Entrance":
				if "Lamp and Oil" in self.player.inventory and self.room.explored == True:
					self.room = CatacombsEntrance()
					if CatacombsEntrance.count < 2:
						print self.room.firstText
					else:
						print self.room.text
				elif "Lamp and Oil" in self.player.inventory:
					print("You can barely see anything, thinking about it, you remember you have the Lamp you found in your backpack. \nFortunately, you also found some oil to light it.")
				DarkCorridorEntrance.explored = True

	def north(self):
		"""The player goes to the north."""
		if (not self.player.isDead):
			if self.room.name == "Outside":
				self.room = Rubble()
				if (not self.player.isDead):
					if Rubble.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Rubble":
				self.room = NorthRubble()
				print self.room.firstText
				self.player.die()
			elif self.room.name == "Overgrowth":
				self.room = Outside()
				if (not self.player.isDead):
					if Outside.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "South Overgrowth":
				self.room = Overgrowth()
				if (not self.player.isDead):
					if Overgrowth.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Hallway":
				self.room = Library()
				if (not self.player.isDead):
					if Library.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Armory":
				self.room = Hall()
				if (not self.player.isDead):
					if Hall.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Trapped Room":
				self.room = HallUpper()
				if (not self.player.isDead):
					if HallUpper.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Guest Room":
				self.room = TrappedRoom()
				if (not self.player.isDead):
					if TrappedRoom.count < 2:
						print self.room.firstText
					else:
						print self.room.text

	def south(self):
		"""The player goes to the south."""
		if (not self.player.isDead):
			if self.room.name == "Outside":
				self.room = Overgrowth()
				if (not self.player.isDead):
					if Overgrowth.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Rubble":
				self.room = Outside()
				if (not self.player.isDead):
					if Outside.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Overgrowth":
				self.room = SouthOvergrowth()
				if (not self.player.isDead):
					if SouthOvergrowth.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "South Overgrowth":
				print self.room.look
				self.player.die()
			elif self.room.name == "Hallway":
				self.room = Armory()
				if (not self.player.isDead):
					if Armory.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Library":
				self.room = Hall()
				if (not self.player.isDead):
					if Hall.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Armory" and Armory.ennemyNumber < 1 and Armory.explored == True:
				if "Sword" not in self.player.inventory:
					print("You pick up the sword, it's some really good quality work, what a luck!")
					self.player.inventory.append("Sword")
			elif self.room.name == "Upper Hallway":
				if HallUpper.trapRemoved == True:
					self.room = TrappedRoom()
					if (not self.player.isDead):
						if TrappedRoom.count < 2:
							print self.room.firstText
						else:
							print self.room.text
				else:
					self.room = DeathChamber()
					print self.room.firstText
					self.player.die()
			elif self.room.name == "Trapped Room":
				self.room = GuestRoom()
				if (not self.player.isDead):
					if GuestRoom.count < 2:
						print self.room.firstText
					else:
						print self.room.text

	def east(self):
		"""The player goes to the east."""
		if (not self.player.isDead):
			if self.room.name == "Outside":
				self.room = Hall()
				if (not self.player.isDead):
					if Hall.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "South Overgrowth":
				print self.room.look
				self.player.die()
			elif self.room.name == "Armory" and Armory.ennemyNumber < 1 and Armory.explored == True:
				if "Boots" not in self.player.inventory:
					print("You put on the boots. As you walk away, you feel lighter. \nYour movement speed is doubled.")
					self.player.inventory.append("Boots")
			elif self.room.name == "Observation Tower":
				self.room = HallUpper()
				if (not self.player.isDead):
					if HallUpper.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Locked Door":
				self.room = HallUpper()
				if (not self.player.isDead):
					if HallUpper.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Dark Corridor Entrance":
				self.room = HallLower()
				if (not self.player.isDead):
					if HallLower.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Catacombs Entrance":
				self.room = HallLowerLight()
				if (not self.player.isDead):
					if HallLowerLight.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Catacombs":
				self.room = CatacombsEntrance()
				if (not self.player.isDead):
					if CatacombsEntrance.count < 2:
						print self.room.firstText
					else:
						print self.room.text

	def west(self):
		"""The player goes to the west."""
		if (not self.player.isDead):
			if self.room.name == "South Overgrowth":
				print self.room.look
				self.player.die()
			elif self.room.name == "Hallway":
				self.room = Outside()
				if (not self.player.isDead):
					if Outside.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Armory" and Armory.ennemyNumber < 1 and Armory.explored == True:
				if "Bow and Arrows" not in self.player.inventory:
					print("You pick up the bow and the arrows. \nAs you draw an arrow from the quiver, you notice that the number of arrows inside it didn't change. \nIt's a magical quiver, therefore, you have unlimited ammunitions.")
					self.player.inventory.append("Bow and Arrows")
			elif self.room.name == "Upper Hallway":
				self.room = LockedDoor()
				if self.room.unlocked == True:
					self.room = ObservationTower()
					if (not self.player.isDead):
						if ObservationTower.count < 2:
							print self.room.firstText
						else:
							print self.room.text
				else:
					if (not self.player.isDead):
						if LockedDoor.count < 2:
							print self.room.firstText
						else:
							print self.room.text
			elif self.room.name == "Lower Hallway":
				self.room = DarkCorridorEntrance()
				if (not self.player.isDead):
					if DarkCorridorEntrance.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Dark Corridor Entrance":
				self.room = DarkCorridor()
				print self.room.firstText
				self.player.die()
			elif self.room.name == "Lower Hallway Light":
				self.room = CatacombsEntrance()
				if (not self.player.isDead):
					if CatacombsEntrance.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Catacombs Entrance":
				self.room = Catacombs()
				if (not self.player.isDead):
					if Catacombs.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Catacombs":
				self.room = TreasureRoom()
				if (not self.player.isDead):
					print self.room.firstText

	def up(self):
		"""The player goes up the stairs."""
		if (not self.player.isDead):
			if self.room.name == "Hallway":
				self.room = HallUpper()
				if (not self.player.isDead):
					if HallUpper.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Lower Hallway":
				self.room = Hall()
				if (not self.player.isDead):
					if Hall.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Lower Hallway Light":
				print("As you walk up the stairs back to the light, you put your lamp back into your backpack.")
				self.room = Hall()
				if (not self.player.isDead):
					if Hall.count < 2:
						print self.room.firstText
					else:
						print self.room.text

	def down(self):
		"""The player goes down the stairs."""
		if (not self.player.isDead):
			if self.room.name == "Hallway":
				self.room = HallLower()
				if (not self.player.isDead):
					if HallLower.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Armory" and Armory.ennemyNumber < 1 and self.room.explored == True:
				if "Key" not in self.player.inventory:
					print("You pick up the key, it might be useful later ...")
					self.player.inventory.append("Key")
			elif self.room.name == "Upper Hallway":
				self.room = Hall()
				if (not self.player.isDead):
					if Hall.count < 2:
						print self.room.firstText
					else:
						print self.room.text

	def battle(self):
		"""This methods runs a battle."""
		if (not self.player.isDead):
			if self.room.name == "Armory":
				print("You start running around, looking for something useful in such a situation.")
				self.fightMode = self.runningPhase(Armory.ennemyNumber)
				if self.fightMode == -1:
					self.player.die()
					print("As you run around, you sense that you are being bitten. This wound is unfortunately lethal and you will soon become a zombie yourself.")

			if self.room.name == "Armory":
				while self.fightMode == 1:
					self.fightMode = self.fight(Armory.ennemyNumber)
					if self.fightMode == 0:
						self.fightMode = self.flee(Armory.ennemyNumber)
						if self.fightMode == 0:
							print("You manage to escape the fight.")
						elif self.fightMode == -1:
							self.player.die()
							print("As you run away, you sense that you are being bitten. This wound is unfortunately lethal and you will soon become a zombie yourself.")
					if self.fightMode == -1:
						self.player.die()
						print("In the melee, you suddenly sense a sharp bite. You keep fighting for a while but you will never recover from this wound and will become a zombie yourself.")
					if self.fightMode == 2:
						Armory.ennemyNumber -= 1
						print("You killed the zombie!")
						if Armory.ennemyNumber != 0:
							print("Unfortunately, It is replaced by another. You must continue to fight.")
							self.fightMode = 1
					if self.fightMode == 3:
						print("Deciding to act quickly you throw the lamp which sprays oil everywhere and the whole room begins to burn. Quickly stepping back you avoid getting burned in the process.")
						attack1 = random.randrange(9, 10)
						attack2 = random.randrange(9, 10)
						attack3 = random.randrange(9, 10)
						attack4 = random.randrange(9, 10)
						attack5 = random.randrange(9, 10)
						attack = attack1 + attack2 + attack3 + attack4 + attack5
						Armory.ennemyNumber -= attack
						if Armory.ennemyNumber > 0:
							print("After such an explosion, you are stumbled to see that a few zombies are still alive. Though, this won't prevent you from fighting.")
							self.fightMode = 1
				if not self.player.isDead:
					print ("You are now in the armory.")

			if self.room.name == "Catacombs":
				self.fightMode = 1
				while self.fightMode == 1:
					self.fightMode = self.fight(Catacombs.ennemyNumber)
					if self.fightMode == 0:
						self.fightMode = self.flee(Catacombs.ennemyNumber)
						if self.fightMode == 0:
							print("You manage to escape the fight.")
						elif self.fightMode == -1:
							self.player.die()
							print("As you run away, you sense that you are being bitten. This wound is unfortunately lethal and you will soon become a zombie yourself.")
					if self.fightMode == -1:
						self.player.die()
						print("In the melee, you suddenly sense a sharp bite. You keep fighting for a while but you will never recover from this wound and will become a zombie yourself.")
					if self.fightMode == 2:
						Catacombs.ennemyNumber -= 1
						print("You killed the zombie!")
						if Catacombs.ennemyNumber != 0:
							print("Unfortunately, It is replaced by another. You must continue to fight.")
							self.fightMode = 1
					if self.fightMode == 3:
						print("Deciding to act quickly you throw the lamp which sprays oil everywhere and the whole room begins to burn. Quickly stepping back you avoid getting burned in the process.")
						attack1 = random.randrange(9, 10)
						attack2 = random.randrange(9, 10)
						attack3 = random.randrange(9, 10)
						attack4 = random.randrange(9, 10)
						attack5 = random.randrange(9, 10)
						attack = attack1 + attack2 + attack3 + attack4 + attack5
						Catacombs.ennemyNumber -= attack
						if Catacombs.ennemyNumber > 0:
							print("After such an explosion, you are stumbled to see that a few zombies are still alive. Though, this won't prevent you from fighting.")
							self.fightMode = 1
				if not self.player.isDead:
					print ("You are now in the catacombs.")

	def runningPhase(self, ennemyNumber):
		"""This function runs the beginning of the fight against the Zombie Guardian in the armory."""
		while self.switcherWeapon != []:
			# Die
			if self.flee(ennemyNumber) == 0:
				return -1
			self.findItem()
			command = raw_input("What are you going to do now? Continue to search for something else, Run away, Fight? ").lower()
			# Flee
			if command == "r":
				return 0
			# Fight
			elif command == "f":
				return 1
			# Continue to search
			elif command == "c":
				print("You continue running around, hoping you will find something more useful.")
		return 1

	def flee(self, ennemyNumber):
		"""Lets the player trying to run away from a battle."""
		# if there is more than 3 ennemies, only 3 can attack at once.
		if ennemyNumber > 3:
			foes = 3
		else:
			foes = ennemyNumber
		# Die
		if not self.player.bitten(foes, "flee"):
			return -1
		# Survive and Flee 
		else:
			return 0

	def findItem(self):
		"""This function determines what the player find while running away from the Zombie Guardian."""
		numItems = len(self.switcherWeapon)
		found = random.randrange(numItems)
		item = self.switcherWeapon[found]
		print("Suddenly, you see something on your side, ... {}".format(str(item)))
		pick = raw_input("Do you take it? (y/n)").lower()
		if pick == 'y':
			self.player.inventory.append(item)
		self.switcherWeapon.remove(item)

	def fight(self, ennemyNumber):
		"""Lets the player fight."""
		# Hit
		if self.attack() == "Hit":
			return 2
		elif self.attack() == "Boom":
			return 3
		# Miss
		else:
			# if there is more than 3 ennemies, only 3 can attack at once.
			if ennemyNumber > 3:
				foes = 3
			else:
				foes = ennemyNumber
			# Die
			if not self.player.bitten(foes, "fight"):
				return -1
			# Survive and Fight 
			else:
				return 1

	def attack(self):
		"""Allow the player to attack the ennemy with whatever is available to him/her."""
		weapon = ""
		while weapon == "":
			if "Sword" in self.player.inventory and "Bow and Arrows" in self.player.inventory:
				message = "Select your weapon: Sword, Bow and arrows, Other "
			elif "Bow and Arrows" in self.player.inventory:
				message = "Select your weapon: bow and Arrows, Other "
			elif "Sword" in self.player.inventory:
				message = "Select your weapon: Sword, Other "
			else:
				message = "Select your weapon: Other "
			weapon = raw_input(message).upper()
			if weapon == 'A':
				if "Bow and Arrows" not in self.player.inventory:
					print("You don't possess such a weapon, please select something else.\n")
					weapon = ""
				else:
					weapon = "Bow and Arrows"
			if weapon == 'S':
				if "Sword" not in self.player.inventory:
					print("You don't possess such a weapon, please select something else.\n")
					weapon = ""
				else:
					weapon = "Sword"
			if weapon == 'O':
				if self.player.inventory == []:
					print("For some reason plunging straight into the zombies with no weapon seemed like a good idea. \nYou start getting bitten and your vision fades to black...\n")
					self.player.die()
				else:
					self.player.showInventory()
					weapon = raw_input("Type the full name of what you want to use. ")
					if weapon not in self.player.inventory:
						print("You don't have this item in your inventory, please select something else.\n")
						weapon = ""

			if weapon == "Sword" or weapon == "Bow and Arrows":
				attack = random.randrange(2)
				if weapon == "Sword" and attack < 2 or weapon == "Bow and Arrows" and attack < 1:
					return "Hit"
				else:
					return "Missed"
			elif weapon in self.player.inventory:
				print("You throw {} at your oponent.".format(str(weapon)))
				self.player.inventory.remove(weapon)
				if weapon == "Lamp and Oil":
					return "Boom"
				else:
					return "Missed"
			else:
				return "Missed"
