#!/usr/bin/env python
# -*-coding:Utf-8 -*        

import random

class Player(object):
    """docstring for Player"""
    def __init__(self):
        self.inventory = []
        self.isDead = False
        self.hasClue = False

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
        print("Game Over")
        exit(0)

    def isDead(self):
        """The player is dead, it's the end of the game."""
        return self.isDead

    def bitten(self, foes, state):
        """This function determine if the player has been bitten by a zombie, if so, the player is dead."""
        # If there is more than 3 ennemies, only 3 can attack at once.
        if foes > 3:
            foes = 3

        # Ennemies attacks
        for x in xrange(1,foes):
            pass
            if state == "flee":
                hit = random.randrange(7)
            else:
                hit = random.randrange(14)

            if hit == 0:
                if state == "fight":
                    print("\nIn the melee, you suddenly sense a sharp bite.\nThe zombie has got you and your vision soon starts to fade ...\n")
                else:
                    print("\nIn the rush, you suddenly sense a sharp bite.\nThe zombie has got you and your vision soon starts to fade ...\n")
                self.player.die()
