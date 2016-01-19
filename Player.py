#!/usr/bin/env python
# -*-coding:Utf-8 -*		

from pydispatch import dispatcher

class Player(object):
	"""docstring for Player"""
	def __init__(self):
		self.inventory = []
		self.isDead = False

	def inventory(self):
		"""Display the inventory, possibility of using or throwing items.
		Note that a thrown item is forever lost."""
		if (not self.player.isDead()):
			pass
			print("Here is the content of your inventory:")
			for item in inventory:
				print("\titem")
			command = raw_input("Select an item by typing its full name, you can also type 'quit' to exit the inventory without doing anything: ")
			if command in inventory:
				what = raw_input("What do you want to do with it? (Use/Trow/Exit)").lower()
				if what == 't':
					self.inventory.remove(command)
					signal = "Throw {}".format(what)
				elif what == 'u':
					signal = "Use {}".format(what)
			dispatcher.send(signal = signal)

	def die(self):
		"""The player is dead, it's the end of the game."""
		self.isDead = True

	def isDead(self):
		"""The player is dead, it's the end of the game."""
		return self.isDead

	def bitten(foes, state):
		"""This function determine if the player has been bitten by a zombie, if so, the player is dead."""
		if foes < 1:
			return False
		elif foes == 1:
			if state == "flee":
				hit = randrange(4)
			elif state == "fight":
				hit = randrange(9)
			if hit == 0:
				return True
			else:
				return False
		elif foes == 2:
			return bitten(1, state) or bitten(1, state)
		else:
			return bitten(1, state) or bitten(1, state) or bitten(1, state)
