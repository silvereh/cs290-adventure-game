#!/usr/bin/env python
# -*-coding:Utf-8 -*

from Game import *

def run(game):
	"""This function runs the beginning of the fight against the Zombie Guardian in the armory."""
	while switcherWeapon != []:
		# Die
		if flee() == 0:
			return -1
		find(game)
		command = raw_input("What are you going to do now? Continue to run to find something else, Flee, Battle? ").lower()
		# Flee
		if command == 'f':
			return 0
		# Fight
		elif command == 'b':
			return 1
	return 1

def find(game):
	"""This function determines what the player find while running away from the Zombie Guardian."""
	found = len(game.switcherWeapon)
	print("Suddenly, you see something on your side, it's a ... {}", format(game.switcherWeapon[found]))
	pick = raw_input("Do you take it? (y/n)").lower()
	if pick == 'y':
		game.player.inventory.add(new Item(game.switcherWeapon[found]))
	game.switcherWeapon.remove(game.switcherWeapon[found])

def dead(ennemy, state):
	"""This function determine if the player has been hit by a zombie, if so, the player is dead."""
	if ennemy.number < 1:
		return False
	elif g.ennemy.number == 1:
		if state == "flee":
			hit = randrange(4)
		elif state == "fight":
			hit = randrange(9)
		if hit == 0:
			return True
		else:
			return False
	else:
		count = 0:
		for foe in ennemy.number:
			if count < 2:
				dead(foe, state)
			count += 1

def flee(game):
	"""Lets the player trying to run away from a battle."""
	# Die
	if dead(game.ennemy, "flee"):
		return -1
	# Flee 
	else:
		return 0

def fight(game):
	"""Lets the player fight."""
	# Hit
	if attack(game) == "Hit":
		return 2
	# Boom
	elif attack(game) == "Boom";
		return 3
	# Miss
	else:
		# Second attack if Boots
		if "Boots" in game.player.inventory:
			# Hit
			if attack(game) == "Hit":
				return 2
			# Boom
			elif attack(game) == "Boom";
				return 3
		# Die
		if dead(game.ennemy, "fight"):
			return -1
		# Fight 
		else:
			return 1

def attack(game):
	"""Allow the player to attack the ennemy with whatever is available to him/her."""
	weapon = ""
	while weapon == "":
		pass
		if "Sword" in game.player.inventory and "Bow and Arrows" in game.player.inventory:
			message = "Select your weapon: Sword, Bow and arrows, Other"
		elif "Bow and Arrows" in game.player.inventory:
			message = "Select your weapon: Bow and arrows, Other"
		elif "Sword" in game.player.inventory:
			message = "Select your weapon: Sword, Other"
		else:
			message = "Select your weapon: Other"
		weapon = raw_input(message).upper()
		if weapon == 'B':
			if "Bow and Arrows" not in game.player.inventory:
				print("You don't possess such a weapon, please select something else.")
				weapon = ""
			else:
				weapon = "Bow and Arrows"
		if weapon == 'S':
			if "Sword" not in game.player.inventory:
				print("You don't possess such a weapon, please select something else.")
				weapon = ""
			else:
				weapon = "Sword"
		if weapon == 'O':
			game.player.inventory()

		if weapon == "Sword" or weapon == "Bow and Arrows":
			attack = randrange(2)
			if weapon == "Sword" and attack < 2 or weapon == "Bow and Arrows" and attack < 1:
				return "Hit"
			else:
				return "Missed"
		elif weapon == "Lamp and Oil":
			return "Boom"
		else:
			return "Missed"
