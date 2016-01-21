#!/usr/bin/env python
# -*-coding:Utf-8 -*		

import random

class Player(object):
	"""docstring for Player"""
	def __init__(self):
		self.inventory = []
		self.isDead = False

	def showInventory(self):
		"""Display the inventory, possibility of using or throwing items.
		Note that a thrown item is forever lost."""
		if not self.isDead:
			if self.inventory != []:
				print("Here is the content of your inventory:")
				for item in self.inventory:
					print("\t{}").format(str(item))
			else:
				print("Your have nothing.")

	def die(self):
		"""The player is dead, it's the end of the game."""
		self.isDead = True

	def isDead(self):
		"""The player is dead, it's the end of the game."""
		return self.isDead

	def bitten(self, foes, state):
		"""This function determine if the player has been bitten by a zombie, if so, the player is dead."""
		if foes < 1:
			return False
		elif foes == 1:
			if state == "flee":
				hit = random.randrange(7)
			else:
				hit = random.randrange(14)

			# print ("you hit a {}".format(str(hit)))
			# print "you hit a: %s" %(hit)
			if hit == 0:
				return True
			else:
				return False
		elif foes == 2:
			return self.bitten(1, state) or self.bitten(1, state)
		else:
			return self.bitten(1, state) or self.bitten(1, state) or self.bitten(1, state)
