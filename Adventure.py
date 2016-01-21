#!/usr/bin/env python
# -*-coding:Utf-8 -*

from Game import *
from Player import *
from Room import *
from random import randrange
import subprocess as sp

import os
import pickle

GAMEFILE = "adventure.game"

def loadGame():
	"""This function loads the latest saved game. 
	If the file doesn't exist, it starts a new game."""
	if os.path.exists(GAMEFILE):
		with open(GAMEFILE, 'rb') as gamefile:
			unpic = pickle.Unpickler(gamefile)
			game = unpic.load()
	else:
		game = Game()

	return game
def saveGame(game):
	"""This function saves the current game in the defined game file.
	It takes as a parameter the current game that we want to save."""
	try:
		with open(GAMEFILE, 'wb') as gamefile:
			pic = pickle.Pickler(gamefile)
			pic.dump(game)
		print("The game was saved with success!")
	except:
		print("Oops ... Something went wrong and we couldn't save your game")

load = save = ""
load = raw_input("Hello, welcome in this adventure. Do you want to Load an existing game? ").lower()
if load == "l":
	print("Loading game ...")
	game = loadGame()
else:
	game = Game()

tmp = sp.call('clear',shell=True)
game.help()
print game.room.firstText
x = raw_input().lower()
while x != "q":
	while(x not in game.command):
		x = raw_input("Invalid Command: type h for a list of available commands ...").lower()

	if x != "q":
		game.command[x]()
		x = raw_input()

save = raw_input("So sad to see you leave. Do you want to Save? ").lower()
if save == "s":
	saveGame(game)
exit(0)
