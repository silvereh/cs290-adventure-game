#!/usr/bin/env python
# -*-coding:Utf-8 -*

from Player import *
from Room import *

import random
import subprocess as sp

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
			"Bow"
		]
		self.fightMode = 0

	def restart(self):
		tmp = sp.call('clear',shell=True)
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
			"Bow"
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
			if self.room.name == "South Overgrowth":
				print self.room.look
				self.player.die()
			elif self.room.name == "Library":
				print self.room.look
				self.player.inventory.append("Clue")
			elif self.room.name == "Armory":
				if Armory.ennemyNumber > 0:
					print self.room.look
					self.battle()
				elif Armory.numItems != 0 and self.switcherWeapon != []:
					Armory.explored = True
					print("Now that the zombie Guardian is dead, you're free to explore the room. \nYou find a few interesting things:")
					if "Key" not in self.player.inventory:
						print("- the key fell unDer the table.")
					if "Sword" not in self.player.inventory:
						print("- you find a sword on the South-east corner which looks in a great shape.")
					if "Bow" not in self.player.inventory:
						print("- you see a bow and some arrows on the north-West corner.")
					if "Boots" not in self.player.inventory:
						print("- there is a nice pair of boots on the East side of the room.")
				else:
					print("There is nothing more in the armory.")
			elif self.room.name == "Upper Hallway":
				print self.room.look
				if "Clue" in self.player.inventory:
					print("You had time to think about what you read in the book and you're now sure that there is a trap here. What will you do:\n\tTurn the lamp.\n\tPull the lamp.\n\tNothing\n")
				choice = raw_input().lower()
				if choice == "t":
					HallUpper.trapRemoved = True
					print("As you slowly begin to turn the lamp you hear gears turning and the light begins to fade.\nIn the distance you hear a machine begin to operate and a loud grinding noise. You look around you and everything is silent again.")
				elif choice == "p":
					print("as you slowly begin to pull the lamp you hear gears turning and the light begins to fade.\nIn the distance you hear a machine begin to operate and a loud grinding noise. You look around you and everything is silent again.")
			elif self.room.name == "Locked Door":
				if LockedDoor.unlocked == False and LockedDoor.explored == False:
					print self.room.look
					if "Key" in self.player.inventory:
						print("While looking at the Lock, you notice that the key you found in the armory would fit.")
						LockedDoor.explored = True
				elif "Key" in self.player.inventory and LockedDoor.unlocked == False:
					LockedDoor.unlocked = True
					print("You decide to try using the key you found in the armory. \nYou insert it into the lock and gently turn it, then you hear a 'Click' and the chain falls.")
				elif LockedDoor.unlocked == True:
					print("The door is now unlocked.")
			elif self.room.name == "Observation Tower":
				if ObservationTower.explored == False:
					print self.room.look
					ObservationTower.explored = True
				elif ObservationTower.numItems == 0:
					print("There is nothing more in this room.")
				else:
					print("You grab the lamp and put it in your backpack.\n")
					if "Oil" not in self.player.inventory:
						self.player.inventory.append("Lamp")
					else:
						self.player.inventory.append("Lamp and Oil")
						self.player.inventory.remove("Oil")
						print("You decide to pour the oil you found in the guest room into the lamp.\n")
					ObservationTower.numItems = 0
			elif self.room.name == "Guest Room":
				if GuestRoom.explored == False:
					print self.room.look
					GuestRoom.explored = True
				elif GuestRoom.numItems == 0:
					print("There is nothing more in this room.")
				else:
					if "Lamp" not in self.player.inventory:
						print("You grab the jar of oil and put it in your backpack.\n")
						self.player.inventory.append("Oil")
					else:
						self.player.inventory.append("Lamp and Oil")
						self.player.inventory.remove("Lamp")
						print("You pour the oil into the lamp you find in the observation tower.\n")
					GuestRoom.numItems = 0
			elif self.room.name == "Lower Hallway":
				if "Lamp and Oil" not in self.player.inventory or HallLower.explored == False:
					print self.room.look
					if "Lamp and Oil" in self.player.inventory:
						print("You can barely see anything, thinking about it, you remember you have the Lamp you found in your backpack. \nFortunately, you also found some oil to light it.\n")
					HallLower.explored = True
				elif "Lamp and Oil" in self.player.inventory and HallLower.explored == True:
					print("You grab the lamp in your backpack to lighten the surroundings.\n")
					self.room = HallLowerLight()
					if HallLowerLight.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			elif self.room.name == "Dark Corridor Entrance":
				if "Lamp and Oil" not in self.player.inventory or DarkCorridorEntrance.explored == False:
					print self.room.look
					if "Lamp and Oil" in self.player.inventory:
						print("You can barely see anything, thinking about it, you remember you have the Lamp you found in your backpack.\nFortunately, you also found some oil to light it.\n")
					DarkCorridorEntrance.explored = True
				elif "Lamp and Oil" in self.player.inventory and DarkCorridorEntrance.explored == True:
					print("You grab the lamp in your backpack to lighten the surroundings.\n")
					self.room = CatacombsEntrance()
					if CatacombsEntrance.count < 2:
						print self.room.firstText
					else:
						print self.room.text
			else:
				print self.room.look

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
					print("You pick up the sword in a glance.\nFortunately, it's super light and you have no trouble wielding it. It looks like it was made for you.")
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
					print("You put on the boots.\nYou are immediately surprised about how comfortable they are.\nAs you walk away, you notice that you feel much lighter, these boots must be enchanted to cancel the effects of fatigue.\nYour movement speed is doubled.")
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
				if "Bow" not in self.player.inventory:
					print("You pick up the bow and the quiver next to it.\nThe bow is really heavy and might be hard to use.\nOn the bright side, as you draw an arrow from the quiver, you notice that there is still the same number of arrows inside it.\nThis quiver must be enchanted in some way, providing you with unlimited ammunitions.")
					self.player.inventory.append("Bow")
			elif self.room.name == "Upper Hallway":
				self.room = LockedDoor()
				if LockedDoor.unlocked == True:
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
			elif self.room.name == "Locked Door":
				if LockedDoor.unlocked == True:
					self.room = ObservationTower()
					if (not self.player.isDead):
						if ObservationTower.count < 2:
							print self.room.firstText
						else:
							print self.room.text
				else:
					if (not self.player.isDead):
						print self.room.firstText
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
					Armory.numItems = Armory.numItems - 1
					if Armory.numItems < 0:
						Armory.numItems = 0
			elif self.room.name == "Upper Hallway":
				self.room = Hall()
				if (not self.player.isDead):
					if Hall.count < 2:
						print self.room.firstText
					else:
						print self.room.text

	def battle(self):
		"""This methods runs a battle."""
		if not self.player.isDead:
			if self.room.name == "Armory":
				print("You start running around, looking for something useful in such a situation.")
				self.runningPhase(Armory.ennemyNumber)
				if not self.player.isDead:
					print("Now that you have a weapon to defend yourself, you turn around, resolved to face that zombie.\n")
					choice = ""
					while not self.player.isDead and Armory.ennemyNumber > 0 and choice != "r":
						deadZombies = self.fight(Armory.ennemyNumber)
						if not self.player.isDead and deadZombies < 0:
							print("In the melee, you suddenly sense a sharp bite.\nThe zombie has got you and your vision soon starts to fade ...")
							self.player.die()
						else:
							Armory.ennemyNumber -= deadZombies
							if not self.player.isDead:
								if Armory.ennemyNumber > 0:
									if not self.player.bitten(Armory.ennemyNumber, "fight"):
										choice = raw_input("What will you do now, Fight or Run away? ")
									else:
										print("In the melee, you suddenly sense a sharp bite.\nThe zombie has got you and your vision soon starts to fade ...")
										self.player.die()
					if not self.player.isDead and Armory.ennemyNumber <= 0:
						print ("You are now in the armory.")
						Armory.ennemyNumber = 0
					elif choice == "r":
						if self.runAway(Armory.ennemyNumber):
							self.room = Hall()
							if Hall.count < 2:
								print self.room.firstText
							else:
								print self.room.text
						else:
							print("In the rush, you suddenly sense a sharp bite.\nThe zombie has got you and your vision soon starts to fade ...")
							self.player.die()

			if self.room.name == "Catacombs":
				print("Thrilled by an adrenaline rush, you fly at the zombies...")
				choice = ""
				while not self.player.isDead and Catacombs.ennemyNumber > 0 and choice != "r":
					deadZombies = self.fight(Catacombs.ennemyNumber)
					if not self.player.isDead and deadZombies < 0:
						print("In the melee, you suddenly sense a sharp bite.\nThe zombie has got you and your vision soon starts to fade ...")
						self.player.die()
					else:
						Catacombs.ennemyNumber -= deadZombies
						if not self.player.isDead and Catacombs.ennemyNumber > 0 and "Boots" in self.player.inventory:
							deadZombies = self.fight(Catacombs.ennemyNumber)
							if not self.player.isDead and deadZombies < 0:
								print("In the melee, you suddenly sense a sharp bite.\nThe zombie has got you and your vision soon starts to fade ...")
								self.player.die()
							else:
								Catacombs.ennemyNumber -= deadZombies

						if not self.player.isDead:
							if Catacombs.ennemyNumber > 0:
								if not self.player.bitten(Catacombs.ennemyNumber, "fight"):
									choice = raw_input("What will you do now, Fight or Run away? ")
								else:
									print("In the melee, you suddenly sense a sharp bite.\nThe zombie has got you and your vision soon starts to fade ...")
									self.player.die()
				if not self.player.isDead and Catacombs.ennemyNumber <= 0:
					print ("You are now in the catacombs.")
					Catacombs.ennemyNumber = 0
				elif choice == "r":
					if self.runAway(Catacombs.ennemyNumber):
						self.room = Hall()
						if Hall.count < 2:
							print self.room.firstText
						else:
							print self.room.text
					else:
						print("In the rush, you suddenly sense a sharp bite.\nThe zombie has got you and your vision soon starts to fade ...")
						self.player.die()

	def runningPhase(self, ennemyNumber):
		"""This function runs the beginning of the fight against the Zombie Guardian in the armory."""
		command = ""
		while command == "" and not self.player.isDead:
			# Dodge the attack.
			if self.runAway(ennemyNumber):
				self.findItem()
				command = raw_input("What are you going to do now? Run away, Fight, Continue to search for something else? ").lower()
				if command == "r" or command == "f":
					pass
				# Continue to search
				elif self.switcherWeapon != []:
					print("You continue running around, hoping you will find something more useful.\n")
					command = ""
				elif self.switcherWeapon == []:
					print("There is nothing else to find in this room.\n")
					command = "f"
			else:
				self.player.die()
				print("As you run around, you sense that you are being bitten. This wound is unfortunately lethal and you will soon become a zombie yourself.\n")
		# Run Away
		if command == "r":
			if self.runAway():
				self.room = Hall()
				if Hall.count < 2:
					print self.room.firstText
				else:
					print self.room.text

	def findItem(self):
		"""This function determines what the player find while running away from the Zombie Guardian."""
		numItems = len(self.switcherWeapon)
		found = random.randrange(numItems)
		item = self.switcherWeapon[found]
		print("Suddenly, you see something on your side, ... {}".format(str(item)))
		pick = raw_input("Do you take it? (y/n)").lower()
		if pick == 'y':
			if item == "Sword":
				print("You pick up the sword in a glance.\nFortunately, it's super light and you have no trouble wielding it. It looks like it was made for you.")
				self.player.inventory.append(item)
				self.switcherWeapon.remove(item)
			elif item == "Bow":
				print("You pick up the bow and the quiver next to it.\nThe bow is really heavy and might be hard to use.\nOn the bright side, as you draw an arrow from the quiver, you notice that there is still the same number of arrows inside it.\nThis quiver must be enchanted in some way, providing you with unlimited ammunitions.")
				self.player.inventory.append(item)
				self.switcherWeapon.remove(item)
			elif item == "Boots":
				print("You quickly pick up the boots.\nThe increasing moaning of the zombie behind you makes you think that you can still pick them after the fight and you decide to drop them back.")

	def runAway(self, ennemyNumber):
		"""Let the player try to run away from a battle."""
		# if there is more than 3 ennemies, only 3 can attack at once.
		if ennemyNumber > 3:
			foes = 3
		else:
			foes = ennemyNumber
		# Survive
		if not self.player.bitten(foes, "flee"):
			return True
		# Die 
		else:
			return False

	def fight(self, ennemyNumber):
		"""Let the player fight."""
		weapon = self.selectWeapon()
		deadZombies = 0
		# Attack with the Sword
		if weapon == "Sword":
			attack = random.randrange(2)
			if attack > 0:
				print("You swing your sword and you see a zombie's head flying around.")
				return 1
			else:
				print("You swing your sword with all your might, but all you encounter is nothing, your ennemy has already moved.")
		# Attack with the Bow
		elif weapon == "Bow":
			attack = random.randrange(2)
			if attack == 2:
				print("You band your bow and release an arrow ...\nThe arrow goes straight through the zombie's eye and continues its route, blowing half its head in the process.")
				return 1
			else:
				print("You band your bow and release an arrow ...\nThe arrow goes straight into the wall.\nThe ennemy is already on you.")
		# Throw the Lamp: Big explosion
		elif weapon == "Lamp and Oil":
			print("Deciding to act quickly you throw the lamp which sprays oil everywhere and the whole room begins to burn.\nQuickly stepping back you avoid getting burned in the process.")
			attack1 = random.randrange(9, 10)
			attack2 = random.randrange(9, 10)
			attack3 = random.randrange(9, 10)
			attack4 = random.randrange(9, 10)
			attack5 = random.randrange(9, 10)
			attack = attack1 + attack2 + attack3 + attack4 + attack5
			print("At the same time, you see {} zombies being reduced in dust.\n".format(str(attack)))
			return attack
		# No weapon: Die
		elif weapon == "Nothing" or weapon == "":
			print("For some reason plunging straight into the zombies with no weapon seemed like a good idea. \n")
			return -1
		else:
			pass

	def selectWeapon(self):
		"""Allow the player to attack the ennemy with whatever is available to him/her."""
		choice = ""
		weapon = ""
		while choice == "":
			if "Sword" in self.player.inventory and "Bow" in self.player.inventory:
				message = "Select your weapon: Sword, Bow, Other "
			elif "Sword" in self.player.inventory:
				message = "Select your weapon: Sword, Other "
			elif "Bow" in self.player.inventory:
				message = "Select your weapon: Bow, Other "
			else:
				message = "Select your weapon: Other "
			choice = raw_input(message).upper()
			if choice == 'S':
				if "Sword" not in self.player.inventory:
					print("You don't possess such a weapon, please select something else.\n")
					choice = ""
				else:
					weapon = "Sword"
			elif choice == 'B':
				if "Bow" not in self.player.inventory:
					print("You don't possess such a weapon, please select something else.\n")
					choice = ""
				else:
					weapon = "Bow"
			elif choice == 'O':
				if self.player.inventory == []:
					weapon = "Nothing"
				else:
					while weapon == "":
						self.player.showInventory()
						weapon = raw_input("Type the full name of what you want to use. ")
						if weapon not in self.player.inventory:
							print("You don't have this item in your inventory, please select something else.\n")
							weapon = ""
			else:
				choice = ""

		return weapon
