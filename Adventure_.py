#!/usr/bin/env python
# -*-coding:Utf-8 -*

from Game_ import *
from Player_ import *
from Room_ import *
from random import randrange
import subprocess as sp

import os
import jsonpickle

GAMEFILE = "adventure.json"

gamestate = dict()


def saveGame():
    """This function saves the current game in the defined game file."""
    global gamestate

    try:
        with open(GAMEFILE, 'w') as savegame:
            savegame.write(jsonpickle.encode(gamestate))
        print("The game was saved with success!")
    except:
        print("Oops ... Something went wrong and we couldn't save your game")

def loadGame():
    """This function loads the latest saved game. 
    If the file doesn't exist, it starts a new game."""
    if os.path.exists(GAMEFILE):
        print("Loading game ...\n")
        with open(GAMEFILE, 'r') as savegame:
            state = jsonpickle.decode(savegame.read())
    else:
        print("There is no saved game ...\n")
        state = initGame()
    return state

def initGame():
    game = Game()
    state = dict()
    state['game'] = game
    return state

def displayHelp():
    """Displays a list of available commands."""
    print("\nHere is a non exhaustive list of available commands:")
    print("l: expLore the current room.")
    print("n: move to the North.")
    print("s: move to the South.")
    print("e: move to the East.")
    print("w: move to the West.")
    print("u: move Up.")
    print("d: move Down.")
    print("p: Pick an item.")
    print("i: display your Inventory.")
    print("q: Quit the game.")
    print("m: Use an iteM in your inventory.")
    print("save: Save the current game.")
    print("h: display this Help section.")
    print("Please note that this list is not exhaustive.")
    print("You might find some clues about other commands in the description of the room.\n")

def loopGame():
    """Main loop of the game, run as long as the player doesn't type q."""
    global gamestate

    displayHelp()
    load = raw_input("Do you want to load an existing game? (y/n) ").lower()
    if load == "y":
        gamestate = loadGame()
    else:
        gamestate = initGame()

    command = {
        "u": gamestate['game'].up,
        "l": gamestate['game'].look,
        "d": gamestate['game'].down,
        "e": gamestate['game'].east,
        "w": gamestate['game'].west,
        "n": gamestate['game'].north,
        "s": gamestate['game'].south,
        "f": gamestate['game'].battle,
        "m": gamestate['game'].useItem,
        "p": gamestate['game'].pickItem,
        "turn": gamestate['game'].turnLamp,
        "pull": gamestate['game'].pullLamp,
        "i": gamestate['game'].player.showInventory
    }

    gamestate['game'].start()
    loop = True
    while loop:
        x = raw_input().lower()
        if x == "q":
            exit(0)
        elif x == "h":
            displayHelp()
        elif x == "r":
            displayHelp()
            gamestate = initGame()
        elif x == "save":
            saveGame()
        else:
            if x in command:
                command[x]()

def main():
    """Main function. Check if a savegame exists, and if so, load it. Otherwise
    initialize the game state with defaults. Finally, start the game.
    """
    global gamestate

    tmp = sp.call('clear',shell=True)
    print("Hello, welcome in this adventure.")

    loopGame()

if __name__ == '__main__':
    main()