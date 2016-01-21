#!/usr/bin/env python
# -*-coding:Utf-8 -*

from Game import *
from Player import *
from Room import *
from random import randrange
import subprocess as sp

import os
import pickle

tmp = sp.call('clear',shell=True)
game = Game()
game.help()
print game.room.firstText
x = raw_input().lower()
while x != "q":
	while(x not in game.command):
		x = raw_input("Invalid Command: type h for a list of available commands ...").lower()

	if x != "q":
		game.command[x]()
		x = raw_input()

print("So sad to see you leave.")
exit(0)
