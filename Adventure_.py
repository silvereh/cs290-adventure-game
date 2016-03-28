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
    print("l, look:\texpLore the current room.")
    print("n, north:\tmove to the North.")
    print("s, south:\tmove to the South.")
    print("e, east:\tmove to the East.")
    print("w, west:\tmove to the West.")
    print("u, up:  \tmove Up.")
    print("d, down:\tmove Down.")
    print("p, pick:\tPick an item.")
    print("i, inventory:\tuse an item in your Inventory.")
    print("q, quit:\tQuit the game.")
    print("b, save:\tSave the current game.")
    print("h, help:\tdisplay this Help section.")
    print("r, restart:\tRestart the game.")
    print("Please note that this list is not exhaustive.")
    print("You might find some clues about other commands in the text.\n")

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
        "up": gamestate['game'].up,
        "l": gamestate['game'].look,
        "look": gamestate['game'].look,
        "d": gamestate['game'].down,
        "down": gamestate['game'].down,
        "e": gamestate['game'].east,
        "east": gamestate['game'].east,
        "w": gamestate['game'].west,
        "west": gamestate['game'].west,
        "n": gamestate['game'].north,
        "north": gamestate['game'].north,
        "s": gamestate['game'].south,
        "south": gamestate['game'].south,
        "f": gamestate['game'].battle,
        "fight": gamestate['game'].battle,
        "i": gamestate['game'].useItem,
        "inventory": gamestate['game'].useItem,
        "p": gamestate['game'].pickItem,
        "pick": gamestate['game'].pickItem,
        "turn": gamestate['game'].turnLamp,
        "pull": gamestate['game'].pullLamp
    }

    gamestate['game'].start()
    loop = True
    while loop:
        x = raw_input().lower()
        if x == "q" or x == "quit":
            exit(0)
        elif x == "h" or x == "help":
            displayHelp()
        elif x == "r" or x == "restart":
            displayHelp()
            gamestate = initGame()
        elif x == "b" or x == "save":
            saveGame()
        else:
            if x in command:
                command[x]()

def main():
    """Main function. Check if a savegame exists, and if so, load it. Otherwise
    initialize the game state with defaults. Finally, start the game.
    """
    global gamestate

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hello, welcome in this adventure.")

    loopGame()

if __name__ == '__main__':
    main()