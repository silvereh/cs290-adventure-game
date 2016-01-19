#!/usr/bin/env python
# -*-coding:Utf-8 -*

from Player import *
from Room import *
from pydispatch import dispatcher

class Game(object):
	"""docstring for Game"""
	def __init__(self):
		self.player = Player()
		self.room = Outside()
		self.command = {
			'q': self.quit,
			'h': self.help,
			'l': self.look,
			'n': self.north,
			's': self.south,
			'e': self.east,
			'w': self.west,
			'u': self.up,
			'd': self.down,
			'f': self.battle,
			'i': self.player.inventory
		}
		self.ennemy = ""
		self.switcherWeapon = [
			"Sword",
			"Boots",
			"Bow and Arrows"
		]
		self.fightMode = 0
		
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
		print("h: display this Help section.")
		print("Please note that this list is not exhaustive.")
		print("You might find some clues about other commands in the description of the room.")

	def look(self):
		"""The player looks around him/her in the room to find something interesting."""
		if (not self.player.isDead()):
			print self.room.look
			if self.room.name == "South Overgrowth":
				self.player.die()
			if self.room.name == "Library":
				self.player.inventory.add("Clue")
			if self.room.name == "Armory":
				if room.ennemyNumber > 0:
					self.battle()
				else:
					print("Now that the zombie Guardian is dead, you're free to explore the room, you find a few interesting things:")
					print("- the Key is still on the table.")
					if ("Sword" not in self.player.inventory):
						print("- you find a sword on the South-east corner which looks in a great shape.")
					if ("Bow and Arrows" not in self.player.inventory):
						print("- you see a bow and some arrows on the north-West corner.")
					if ("Boots" not in self.player.inventory):
						print("- there is a nice pair of boots on the East side of the room.")
			if self.room.name == "Observation Tower":
				if self.room.explored == True:
					print("You grab the lamp and put it in your backpack.")
					if "Oil" not in self.player.inventory:
						self.player.inventory.add("Lamp")
					else:
						self.player.inventory.remove("Oil")
						self.player.inventory.add("Lamp and Oil")
			if self.room.name == "Upper Hallway":
				if "Clue" in self.player.inventory:
					choise = raw_input("You had time to think about what you read in the book and you're now sure that there is a trap here. What will you do:\n- Turn the lamp.\n- Pull the lamp.\n- Nothing").lower()
					if choice == "t":
						room.trapRemoved = True
						print("As you slowly begin to turn the lamp you hear gears turning and the light begins to fade. In the distance you hear a machine begin to operate and a loud grinding noise. You look around you and everything is silent again.")
					elif choice == "p":
						print("as you slowly begin to pull the lamp you hear gears turning and the light begins to fade. In the distance you hear a machine begin to operate and a loud grinding noise. You look around you and everything is silent again.")
			if self.room.name == "Guest Room":
				if self.room.explored == True:
					print("You grab the oil and put it in your backpack.")
					if "Lamp" not in self.player.inventory:
						self.player.inventory.add("Oil")
					else:
						self.player.inventory.remove("Lamp")
						self.player.inventory.add("Lamp and Oil")
			self.room.explored = True

	def north(self):
		"""The player goes to the north."""
		if (not self.player.isDead()):
			if self.room.name == "Outside":
				self.room = Rubble()
			elif self.room.name == "Rubble":
				self.room = NorthRubble()
				print self.room.firstText
				self.player.die()
			elif self.room.name == "Overgrowth":
				self.room = Outside()
			elif self.room.name == "South Overgrowth":
				self.room = Overgrowth()
			elif self.room.name == "Hallway":
				self.room = Library()
			elif self.room.name == "Armory":
				self.room = Hall()
			elif self.room.name == "Trapped Room":
				self.room = HallUpper()
			elif self.room.name == "Guest Room":
				self.room = TrappedRoom()
		if (not self.player.isDead()):
			if room.count < 2:
				print self.room.firstText
			else:
				print self.room.text

	def south(self):
		"""The player goes to the south."""
		if (not self.player.isDead()):
			if self.room.name == "Outside":
				self.room = Overgrowth()
			elif self.room.name == "Rubble":
				self.room = Outside()
			elif self.room.name == "Overgrowth":
				self.room = SouthOvergrowth()
			elif self.room.name == "South Overgrowth":
				print self.room.look
				self.player.die()
			elif self.room.name == "Hallway":
				self.room = Armory()
			elif self.room.name == "Library":
				self.room = Hall()
			elif self.room.name == "Armory" and room.ennemyNumber < 1 and self.room.explored == True:
				if "Sword" not in inventory:
					print("You pick up the sword, it's some really good quality work, what a luck!")
					self.player.inventory.add("Sword")
				if "Bow and Arrows" not in inventory:
					print("You pick up the bow and the arrows, as you draw an arrow from the quiver, you notice that the number of arrows inside it didn't change. It's a magical quiver, therefore, you have unlimited ammunitions.")
					self.player.inventory.add("Bow and Arrows")
				if "Boots" not in self.player.inventory:
					print("You put on the boots. As you walk away, you feel lighter. Your movement speed is doubled.")
					self.player.inventory.add("Boots")
			elif self.room.name == "Upper Hallway":
				if room.trapRemoved == True:
					self.room = TrappedRoom()
				else:
					self.room = DeathChamber()
					self.player.die()
			elif self.room.name == "Trapped Room":
				self.room = Kitchen()
		if (not self.player.isDead()):
			if room.count < 2:
				print self.room.firstText
			else:
				print self.room.text

	def east(self):
		"""The player goes to the east."""
		if (not self.player.isDead()):
			if self.room.name == "Outside":
				self.room = Hall()
			elif self.room.name == "South Overgrowth":
				print self.room.look
				self.player.die()
			elif self.room.name == "Observation Tower":
				self.room = HallUpper()
			elif self.room.name == "Dark Corridor Entrance":
				self.room = HallLower()
			elif self.room.name == "Catacombs Entrance":
				self.room = HallLowerLight()
			elif self.room.name == "Catacombs":
				self.room = CatacombsEntrance()
		if (not self.player.isDead()):
			if room.count < 2:
				print self.room.firstText
			else:
				print self.room.text

	def west(self):
		"""The player goes to the west."""
		if (not self.player.isDead()):
			if self.room.name == "South Overgrowth":
				print self.room.look
				self.player.die()
			elif self.room.name == "Hallway":
				self.room = Outside()
			elif self.room.name == "Upper Hallway":
				self.room = LockedDoor()
				if self.room.unlocked == True:
					self.room = ObservationTower()
			elif self.room.name == "Lower Hallway":
				self.room = DarkCorridorEntrance()
			elif self.room.name == "Dark Corridor Entrance":
				self.room = Corridor()
				self.room.firstText
				self.player.die()
			elif self.room.name == "Lower Hallway Light":
				self.room = CatacombsEntrance()
			elif self.room.name == "Catacombs Entrance":
				self.room = Catacombs()
			elif self.room.name == "Catacombs":
				self.room = TreasureRoom()
		if (not self.player.isDead()):
			if room.count < 2:
				print self.room.firstText
			else:
				print self.room.text

	def up(self):
		"""The player goes up the stairs."""
		if (not self.player.isDead()):
			if self.room.name == "Hallway":
				self.room = HallUpper()
			elif self.room.name == "Lower Hallway":
				self.room = Hall()
			elif self.room.name == "Lower Hallway Light":
				print("As you walk up the stairs back to the light, you put your lamp back into your backpack.")
				self.room = Hall()
		if (not self.player.isDead()):
			if room.count < 2:
				print self.room.firstText
			else:
				print self.room.text

	def down(self):
		"""The player goes down the stairs."""
		if (not self.player.isDead()):
			if self.room.name == "Hallway":
				self.room = HallLower()
			elif self.room.name == "Upper Hallway":
				self.room = Hall()
		if (not self.player.isDead()):
			if room.count < 2:
				print self.room.firstText
			else:
				print self.room.text

	def battle(self):
		"""This methods runs a battle."""
		if (not self.player.isDead()):
			if self.room.name == "Armory":
				print("You start running around, looking for something useful in such a situation.")
				self.fightMode = self.runningPhase()

			if self.room.name == "Armory" or self.room.name == "Catacombs":
				while self.fightMode == 1:
					self.fightMode = self.fight()
					if self.fightMode == 0:
						self.fightMode = self.flee()
						if self.fightMode == 0:
							print("You manage to escape the fight.")
						elif self.fightMode == -1:
							self.player.die()
							print("As you run away, you sense that you are being bitten. This wound is unfortunately lethal and you will soon become a zombie yourself.")
					if self.fightMode == -1:
						self.player.die()
						print("In the melee, you suddenly sense a sharp bite. You keep fighting for a while but you will never recover from this wound and will become a zombie yourself.")
					if self.fightMode == 2:
						room.ennemyNumber -= 1
						print("You killed the zombie!")
						if room.ennemyNumber != 0:
							print("Unfortunately, It is replaced by another. You must continue to fight.")
							self.fightMode = 1

		def runningPhase(self):
			"""This function runs the beginning of the fight against the Zombie Guardian in the armory."""
			while switcherWeapon != []:
				# Die
				if self.flee() == 0:
					return -1
				self.findItem()
				command = raw_input("What are you going to do now? Continue to search for something else, Run away, Fight? ").lower()
				# Flee
				if command == 'r':
					return 0
				# Fight
				elif command == 'f':
					return 1
				# Continue to search
				else:
					pass
			return 1

		def flee(self):
			"""Lets the player trying to run away from a battle."""
			# if there is more than 3 ennemies, only 3 can attack at once.
			if room.ennemyNumber > 3:
				foes = 3
			else:
				foes = ennemyNumber
			# Die
			if self.player.bitten(foes, "flee"):
				return -1
			# Survive and Flee 
			else:
				return 0

		def findItem(self):
			"""This function determines what the player find while running away from the Zombie Guardian."""
			found = len(self.switcherWeapon)
			print("Suddenly, you see something on your side, it's a ... {}", format(self.switcherWeapon[found]))
			pick = raw_input("Do you take it? (y/n)").lower()
			if pick == 'y':
				self.player.inventory.add(Item(self.switcherWeapon[found]))
			self.switcherWeapon.remove(self.switcherWeapon[found])

		def fight(self):
			"""Lets the player fight."""
			# Hit
			if attack(self) == "Hit":
				return 2
			# Miss
			else:
				# Second attack if Boots
				if "Boots" in self.player.inventory:
					# Hit
					if attack(self) == "Hit":
						return 2
				# if there is more than 3 ennemies, only 3 can attack at once.
				if room.ennemyNumber > 3:
					foes = 3
				else:
					foes = ennemyNumber
				# Die
				if self.player.bitten(foes, "fight"):
					return -1
				# Survive and Fight 
				else:
					return 1

		def attack(self):
			"""Allow the player to attack the ennemy with whatever is available to him/her."""
			weapon = ""
			while weapon == "":
				if "Sword" in self.player.inventory and "Bow and Arrows" in self.player.inventory:
					message = "Select your weapon: Sword, Bow and arrows, Other"
				elif "Bow and Arrows" in self.player.inventory:
					message = "Select your weapon: Bow and arrows, Other"
				elif "Sword" in self.player.inventory:
					message = "Select your weapon: Sword, Other"
				else:
					message = "Select your weapon: Other"
				weapon = raw_input(message).upper()
				if weapon == 'B':
					if "Bow and Arrows" not in self.player.inventory:
						print("You don't possess such a weapon, please select something else.")
						weapon = ""
					else:
						weapon = "Bow and Arrows"
				if weapon == 'S':
					if "Sword" not in self.player.inventory:
						print("You don't possess such a weapon, please select something else.")
						weapon = ""
					else:
						weapon = "Sword"
				if weapon == 'O':
					self.player.inventory()

				if weapon == "Sword" or weapon == "Bow and Arrows":
					attack = randrange(2)
					if weapon == "Sword" and attack < 2 or weapon == "Bow and Arrows" and attack < 1:
						return "Hit"
					else:
						return "Missed"
				else:
					return "Missed"

		def handleLight(sender = self, signal = "Use Lamp and Oil"):
			if (not self.player.isDead()):
				if self.room.name == "Lower Hallway":
					self.room = HallLowerLight()
				if self.room.name == "Dark Corridor Entrance":
					self.room = CatacombsEntrance()
			if (not self.player.isDead()):
				if room.count < 2:
					room.firstText
				else:
					room.text

		def handleKey(sender = self, signal="Use Key"):
			if (not self.player.isDead()):
				if self.room.name == "Locked Door":
					LockedDoor.unlocked = True

		def handleBoom(sender = self, signal="Throw Lamp and Oil"):
			if (not self.player.isDead()):
				if self.room.name == "Armory" or self.room.name == "Catacombs":
					print("Deciding to act quickly you throw the lamp which sprays oil everywhere and the whole room begins to burn. Quickly stepping back you avoid getting burned in the process.")
					attack1 = randrange(9, 10)
					attack2 = randrange(9, 10)
					attack3 = randrange(9, 10)
					attack4 = randrange(9, 10)
					attack5 = randrange(9, 10)
					attack = attack1 + attack2 + attack3 + attack4 + attack5
					room.ennemyNumber -= attack
					if room.ennemyNumber > 0:
						print("After such an explosion, you are stumbled to see that a few zombies are still alive. Though, this won't prevent you from keeping on fighting.")
						self.fightMode = 1

		dispatcher.connect(handleLight, signal="Use Lamp and Oil", sender=self)
		dispatcher.connect(handleKey, signal="Use Key", sender=self)
		dispatcher.connect(handleBoom, signal = "Throw Lamp and Oil", sender=self)
