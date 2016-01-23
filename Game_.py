
# -*-coding:Utf-8 -*

from Player_ import *
from Room_ import *

import random
import subprocess as sp

class Game(object):
    """docstring for Game"""
    def __init__(self):
        self.player = Player()
        self.room = Outside()
        self.item = ""
        self.switcherWeapon = [
            "Boots",
            "Bow",
            "Sword"
        ]
        self.roomExplored = {
            "Armory": False,
            "Catacombs": False,
            "GuestRoom": False,
            "HallLower": False,
            "HallUpper": False,
            "LockedDoor": False,
            "ObservationTower": False,
            "CatacombsEntrance": False
        }
        self.roomEnnemyNumber = {
            "Armory": 1,
            "Catacombs": 50
        }
        self.roomNumberItems = {
            "Armory": 1,
            "GuestRoom": 1,
            "ObservationTower": 1
        }
        self.roomSpecialFeatures = {
            "LampMoved": False,
            "TrapRemoved": False,
            "DoorUnlocked": False,
            "LightCatacombs": False,
            "BurningCatacombs": False,
            "ArmoryFightStarted": False,
            "ArmoryFightFinished": False,
            "CatacombsFightStarted": False
        }
        self.previousRoom = ""

    def __getitem__(self, key):
        return self

    def start(self):
        if   self.room.name == "Armory":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "Hall":
                if self.roomEnnemyNumber["Armory"] > 0:
                    if not self.roomSpecialFeatures["ArmoryFightStarted"]:
                        print self.room.text
                    else:
                        print self.room.altText
                        self.battle()
                else:
                    print self.room.altAfterFight
        elif self.room.name == "Catacombs":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "CatacombsEntrance":
                if   self.roomEnnemyNumber > 0:
                    if   self.roomSpecialFeatures["BurningCatacombs"]:
                        print self.room.burning
                        print self.room.burningAltText
                    elif self.roomSpecialFeatures["LightCatacombs"]:
                        if not self.roomSpecialFeatures["CatacombsFightStarted"]:
                            print self.room.lightAltText
                        else:
                            print self.room.light
                    else:
                        print self.room.text
                        self.player.die()
                else:
                    # if   self.roomSpecialFeatures["BurningCatacombs"]:
                    print self.room.burning
                    # elif self.roomSpecialFeatures["LightCatacombs"]:
                    #     print self.room.lightAfterFight
        elif self.room.name == "CatacombsEntrance":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "Catacombs":
                if   self.roomSpecialFeatures["BurningCatacombs"]:
                    print self.room.altBurning
                    print self.room.burning
                elif self.roomSpecialFeatures["LightCatacombs"]:
                    print self.room.altLight
            elif self.previousRoom == "HallLower":
                if   self.roomSpecialFeatures["BurningCatacombs"]:
                    print self.room.burning
                elif self.roomSpecialFeatures["LightCatacombs"]:
                    print self.room.lightFirstText
                else:
                    print self.room.firstText
        elif self.room.name == "GuestRoom":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "TrappedRoom":
                print self.room.text
                if self.roomNumberItems["GuestRoom"] > 0:
                    print self.room.altText
        elif self.room.name == "Hall":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "Armory":
                print self.room.altText
                print self.room.text
            elif self.previousRoom == "Library":
                print self.room.altText
                print self.room.text
            elif self.previousRoom == "Outside":
                print self.room.firstText
                print self.room.text
            elif self.previousRoom == "HallLower":
                print self.room.downText
                print self.room.text
            elif self.previousRoom == "HallUpper":
                print self.room.altText
                print self.room.text
        elif self.room.name == "HallLower":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "CatacombsEntrance":
                print self.room.altText
                if self.roomSpecialFeatures["LightCatacombs"]:
                    print self.room.light
                else:
                    print self.room.text
            elif self.previousRoom == "Hall":
                print self.room.firstText
                if self.roomSpecialFeatures["LightCatacombs"]:
                    print self.room.light
                else:
                    print self.room.text
        elif self.room.name == "HallUpper":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "TrappedRoom":
                print self.room.text
            elif self.previousRoom == "LockedDoor":
                print self.room.text
            elif self.previousRoom == "ObservationTower":
                print self.room.text
            elif self.previousRoom == "Hall":
                print self.room.firstText
        elif self.room.name == "Library":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "Hall":
                print self.room.text
        elif self.room.name == "LockedDoor":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "HallUpper":
                if not self.roomSpecialFeatures["DoorUnlocked"]:
                    print self.room.text
                else:
                    print self.room.doorUnlocked
        elif self.room.name == "ObservationTower":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "LockedDoor":
                print self.room.text
                if self.roomNumberItems["ObservationTower"] > 0:
                    print self.room.altText
        elif self.room.name == "Outside":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "Overgrowth":
                print self.room.altText
                print self.room.text
            elif self.previousRoom == "Rubble":
                print self.room.altText
                print self.room.text
            elif self.previousRoom == "Hall":
                print self.room.altText
                print self.room.text
            elif self.previousRoom == "":
                print self.room.firstText
                print self.room.text
        elif self.room.name == "Overgrowth":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "OvergrowthSouth":
                print self.room.altText
            elif self.previousRoom == "Outside":
                print self.room.text
        elif self.room.name == "OvergrowthSouth":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "Overgrowth":
                print self.room.text
        elif self.room.name == "Rubble":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "Outside":
                print self.room.text
        elif self.room.name == "TrappedRoom":
            if self.previousRoom == self.room.name:
                self.look()
            elif self.previousRoom == "GuestRoom":
                print self.room.text
            elif self.previousRoom == "":
                print self.room.text

    def pickItem(self):
        if not self.player.isDead:
            if self.item != "":
                self.player.inventory.append(self.item)
                if self.item == "Lamp":
                    print self.room.pickLamp
                    self.roomNumberItems["ObservationTower"] = 0
                if self.item == "Oil":
                    print self.room.pickOil
                    self.roomNumberItems["GuestRoom"] = 0
                self.item = ""

    def useItem(self):
        if not self.player.isDead:
            self.player.showInventory()
            item = raw_input("What item do you want to use? ").lower()
            if   item == "key":
                if "Key" in self.player.inventory:
                    if self.room.name == "LockedDoor":
                        if self.roomExplored["LockedDoor"]:
                            if not self.roomSpecialFeatures["DoorUnlocked"]:
                                self.roomSpecialFeatures["DoorUnlocked"] = True
                                print("You decide to try using the key you found in the armory. \nYou insert it into the lock and gently turn it, then you hear a 'Click' and the chain falls.")
            elif item == "lamp":
                if "Lamp" in self.player.inventory and "Oil" in self.player.inventory:
                    if self.room.name == "HallLower" or self.room.name == "CatacombsEntrance":
                        if self.roomExplored["HallLower"] or self.roomExplored["CatacombsEntrance"]:
                            self.roomSpecialFeatures["LightCatacombs"] = True
                            print("You grab the lamp in your backpack to lighten the surroundings.\n")

    def turnLamp(self):
        if not self.player.isDead and self.room.name == "HallUpper" and self.roomExplored["HallUpper"] and not self.roomSpecialFeatures["TrapRemoved"] and not self.roomSpecialFeatures["LampMoved"]:
            self.roomSpecialFeatures["TrapRemoved"] = True
            self.roomSpecialFeatures["LampMoved"] = True
            print self.room.lampMoved

    def pullLamp(self):
        if not self.player.isDead and self.room.name == "HallUpper" and self.roomExplored["HallUpper"] and not self.roomSpecialFeatures["TrapRemoved"] and not self.roomSpecialFeatures["LampMoved"]:
            self.roomSpecialFeatures["LampMoved"] = True
            print self.room.lampMoved

    def look(self):
        """The player looks around him/her in the room to find something interesting."""
        self.item = ""
        self.previousRoom = self.room.name
        if not self.player.isDead:
            if   self.room.name == "Armory":
                if self.roomEnnemyNumber["Armory"] > 0:
                    print self.room.look
                    self.roomExplored["Armory"] = True
                elif self.roomNumberItems != 0 and self.switcherWeapon != []:
                    self.roomExplored["Armory"] = True
                    print self.room.lookAfterFight
                    if "Key" not in self.player.inventory:
                        print self.room.findKey
                    if "Bow" not in self.player.inventory:
                        print self.room.findBow
                    if "Boots" not in self.player.inventory:
                        print self.room.findBoots
                    if "Sword" not in self.player.inventory:
                        print self.room.findSword
                else:
                    print("There is nothing more in the armory.")
            elif self.room.name == "Catacombs":
                if self.roomEnnemyNumber["Catacombs"] > 0:
                    if   self.roomSpecialFeatures["BurningCatacombs"]:
                        print self.room.burningLook
                    elif self.roomSpecialFeatures["LightCatacombs"]:
                        print self.room.lightLook
                else:
                    print self.room.lookAfterFight
            elif self.room.name == "CatacombsEntrance":
                # if   self.roomSpecialFeatures["BurningCatacombs"]:
                #     print self.room.burningLook
                if self.roomSpecialFeatures["LightCatacombs"]:
                    print self.room.lightLook
                else:
                    print self.room.look
                    if "Lamp" in self.player.inventory and "Oil" in self.player.inventory:
                        print self.altLook
                    self.roomExplored["CatacombsEntrance"] = True
            elif self.room.name == "GuestRoom":
                print self.room.look
                if   self.roomNumberItems["GuestRoom"] > 0:
                    print self.room.altLook
                    self.roomExplored["GuestRoom"] = True
                    self.item = "Oil"
            elif self.room.name == "ObservationTower":
                print self.room.look
                if   self.roomNumberItems["ObservationTower"] > 0:
                    print self.room.altLook
                    self.roomExplored["ObservationTower"] = True
                    self.item = "Lamp"
            elif self.room.name == "HallLower":
                if   self.roomSpecialFeatures["LightCatacombs"]:
                    print self.room.lightLook
                else:
                    print self.room.look
                    if "Lamp" in self.player.inventory and "Oil" in self.player.inventory:
                        print self.room.altLook
                    self.roomExplored["HallLower"] = True
            elif self.room.name == "HallUpper":
                print self.room.look
                if not self.roomSpecialFeatures["DoorUnlocked"]:
                    print self.room.altLookDoor
                if not self.roomSpecialFeatures["LampMoved"]:
                    print self.room.altLookTrap
                    if self.player.hasClue:
                        print self.room.altLook
                self.roomExplored["HallUpper"] = True
            elif self.room.name == "Library":
                print self.room.look
                self.player.hasClue = True
            elif self.room.name == "LockedDoor":
                if not self.roomSpecialFeatures["DoorUnlocked"]:
                    print self.room.look
                    if "Key" in self.player.inventory:
                        print self.room.altLook
                else:
                    print self.room.doorUnlocked
                self.roomExplored["LockedDoor"] = True
            elif self.room.name == "OvergrowthSouth":
                print self.room.look
                self.player.die()
            else:
                print self.room.look

    # Functions for the moves.
    def north(self):
        """The player goes to the north."""
        self.item = ""
        if not self.player.isDead:
            if   self.room.name == "Armory":
                self.previousRoom = "Armory"
                self.room = Hall()
                print self.room.altText
                print self.room.text
            elif self.room.name == "GuestRoom":
                self.previousRoom = "GuestRoom"
                self.room = TrappedRoom()
                print self.room.text
            elif self.room.name == "Hall":
                self.previousRoom = "Hall"
                self.room = Library()
                print self.room.text
            elif self.room.name == "Outside":
                self.previousRoom = "Outside"
                self.room = Rubble()
                print self.room.text
            elif self.room.name == "Overgrowth":
                self.previousRoom = "Overgrowth"
                self.room = Outside()
                print self.room.altText
                print self.room.text
            elif self.room.name == "OvergrowthSouth":
                self.previousRoom = "OvergrowthSouth"
                self.room = Overgrowth()
                print self.room.altText
            elif self.room.name == "Rubble":
                self.previousRoom = "Rubble"
                self.room = RubbleNorth()
                print self.room.text
                self.player.die()
            elif self.room.name == "TrappedRoom":
                self.previousRoom = "TrappedRoom"
                self.room = HallUpper()
                print self.room.text
            else:
                print "There is nothing in this direction"

    def south(self):
        """The player goes to the south."""
        self.item = ""
        if not self.player.isDead:
            if   self.room.name == "Armory" and self.roomEnnemyNumber["Armory"] < 1 and self.roomExplored["Armory"] and "Sword" in self.switcherWeapon:
                print self.room.pickSword
                self.player.inventory.append("Sword")
                self.switcherWeapon.remove("Sword")
            elif self.room.name == "Hall":
                self.previousRoom = "Hall"
                self.room = Armory()
                if self.roomEnnemyNumber["Armory"] > 0:
                    if not self.roomSpecialFeatures["ArmoryFightStarted"]:
                        print self.room.text
                    else:
                        print self.room.altText
                        self.battle()
                else:
                    print self.room.altAfterFight
            elif self.room.name == "HallUpper":
                if self.roomSpecialFeatures["TrapRemoved"]:
                    self.room.previousRoom = "HallUpper"
                    self.room = TrappedRoom()
                    print self.room.text
                else:
                    self.room = DeathChamber()
                    print self.room.text
                    self.player.die()
            elif self.room.name == "Library":
                self.previousRoom = "Library"
                self.room = Hall()
                print self.room.altText
                print self.room.text
            elif self.room.name == "Outside":
                self.previousRoom = "Outside"
                self.room = Overgrowth()
                print self.room.text
            elif self.room.name == "Overgrowth":
                self.previousRoom = "Overgrowth"
                self.room = OvergrowthSouth()
                print self.room.text
            elif self.room.name == "OvergrowthSouth":
                print self.room.look
                self.player.die()
            elif self.room.name == "Rubble":
                self.previousRoom = "Rubble"
                self.room = Outside()
                print self.room.altText
                print self.room.text
            elif self.room.name == "TrappedRoom":
                self.previousRoom = "TrappedRoom"
                self.room = GuestRoom()
                print self.room.text
                if self.roomNumberItems["GuestRoom"] > 0:
                    print self.room.altText
            else:
                print "There is nothing in this direction"

    def east(self):
        """The player goes to the east."""
        self.item = ""
        if not self.player.isDead:
            if   self.room.name == "Armory" and self.roomEnnemyNumber["Armory"] < 1 and self.roomExplored["Armory"] and "Boots" in self.switcherWeapon:
                print self.room.pickBoots
                self.player.inventory.append("Boots")
                self.switcherWeapon.remove("Boots")
            elif self.room.name == "Catacombs":
                self.previousRoom = "Catacombs"
                self.room = CatacombsEntrance()
                if   self.roomSpecialFeatures["BurningCatacombs"]:
                    print self.room.altBurning
                    print self.room.burning
                elif self.roomSpecialFeatures["LightCatacombs"]:
                    print self.room.altLight
            elif self.room.name == "CatacombsEntrance":
                self.previousRoom = "CatacombsEntrance"
                self.room = HallLower()
                print self.room.altText
                if self.roomSpecialFeatures["LightCatacombs"]:
                    print self.room.light
                else:
                    print self.room.text
            elif self.room.name == "LockedDoor":
                self.previousRoom = "LockedDoor"
                self.room = HallUpper()
                print self.room.text
            elif self.room.name == "ObservationTower":
                self.previousRoom = "ObservationTower"
                self.room = HallUpper()
                print self.room.text
            elif self.room.name == "Outside":
                self.previousRoom = "Outside"
                self.room = Hall()
                print self.room.firstText
                print self.room.text
            elif self.room.name == "OvergrowthSouth":
                print self.room.look
                self.player.die()
            else:
                print "There is nothing in this direction"

    def west(self):
        """The player goes to the west."""
        self.item = ""
        if not self.player.isDead:
            if   self.room.name == "Armory" and self.roomEnnemyNumber["Armory"] < 1 and self.roomExplored["Armory"] and "Bow" in self.switcherWeapon:
                print self.room.pickBow
                self.player.inventory.append("Bow")
                self.switcherWeapon.remove("Bow")
            elif self.room.name == "Catacombs":
                self.previousRoom = "Catacombs"
                self.room = TreasureRoom()
                if self.roomSpecialFeatures["BurningCatacombs"]:
                    print self.room.burning
                print self.room.text
                exit(0)
            elif self.room.name == "CatacombsEntrance":
                self.previousRoom = "CatacombsEntrance"
                self.room = Catacombs()
                if   self.roomEnnemyNumber > 0:
                    if   self.roomSpecialFeatures["BurningCatacombs"]:
                        print self.room.burning
                        print self.room.burningAltText
                    elif self.roomSpecialFeatures["LightCatacombs"]:
                        if self.roomSpecialFeatures["CatacombsFightStarted"]:
                            print self.room.lightAltText
                        else:
                            print self.room.light
                    else:
                        print self.room.text
                        self.player.die()
                else:
                    # if   self.roomSpecialFeatures["BurningCatacombs"]:
                    print self.room.burning
                    # elif self.roomSpecialFeatures["LightCatacombs"]:
                    #     print self.room.lightAfterFight
            elif self.room.name == "Hall":
                self.previousRoom = "Hall"
                self.room = Outside()
                print self.room.altText
                print self.room.text
            elif self.room.name == "HallLower":
                self.previousRoom = "HallLower"
                self.room = CatacombsEntrance()
                if   self.roomSpecialFeatures["BurningCatacombs"]:
                    print self.room.burning
                elif self.roomSpecialFeatures["LightCatacombs"]:
                    print self.room.lightFirstText
                else:
                    print self.room.firstText
            elif self.room.name == "HallUpper":
                self.previousRoom = "HallUpper"
                self.room = LockedDoor()
                if not self.roomSpecialFeatures["DoorUnlocked"]:
                    print self.room.text
                else:
                    print self.room.doorUnlocked
            elif self.room.name == "LockedDoor":
                self.previousRoom = "LockedDoor"
                self.room = ObservationTower()
                print self.room.text
                if self.roomNumberItems["ObservationTower"] > 0:
                    print self.room.altText
            elif self.room.name == "OvergrowthSouth":
                print self.room.look
                self.player.die()
            else:
                print "There is nothing in this direction"

    def up(self):
        """The player goes up the stairs."""
        self.item = ""
        if not self.player.isDead:
            if   self.room.name == "Hall":
                self.previousRoom = "Hall"
                self.room = HallUpper()
                print self.room.firstText
            elif self.room.name == "HallLower":
                self.previousRoom = "HallLower"
                self.room = Hall()
                print self.room.downText
                print self.room.text
            else:
                print "There is nothing in this direction"

    def down(self):
        """The player goes down the stairs."""
        self.item = ""
        if not self.player.isDead:
            if   self.room.name == "Armory" and self.roomEnnemyNumber["Armory"] < 1 and self.roomExplored["Armory"] and self.roomNumberItems > 0:
                print self.room.pickKey
                self.player.inventory.append("Key")
                self.roomNumberItems["Armory"] -= 1
                if self.roomNumberItems["Armory"] < 0:
                    self.roomNumberItems["Armory"] = 0
            elif self.room.name == "Hall":
                self.previousRoom = "Hall"
                self.room = HallLower()
                print self.room.firstText
                if self.roomSpecialFeatures["LightCatacombs"]:
                    print self.room.light
                else:
                    print self.room.text
            elif self.room.name == "HallUpper":
                self.previousRoom = "HallUpper"
                self.room = Hall()
                print self.room.altText
                print self.room.text
            else:
                print "There is nothing in this direction"

    # Functions for the combats.
    def battle(self):
        """This methods runs a battle."""
        self.item = ""
        if not self.player.isDead:

            # If we are in the Armory.
            if   self.room.name == "Armory" and self.roomExplored["Armory"]:
                print "battle"
                self.roomSpecialFeatures["ArmoryFightStarted"] = True
                print("\nYou start running around, looking for something useful in such a situation.")
                self.runningPhase()
                if not self.player.isDead and self.room.name == "Armory":
                    print("\nNow that you have a weapon to defend yourself, you turn around, resolved to face that zombie.\n")
                    self.fightLoop()

            # If we are in the Catacombs.
            elif self.room.name == "Catacombs":
                self.roomSpecialFeatures["CatacombsFightStarted"] = True
                print("\nThrilled by an adrenaline rush, you fly at the zombies...\n")
                self.fightLoop()

    def runningPhase(self):
        """Begins the fight in the armory. Runs until the player run away or decide to face the ennemy."""
        command = ""
        while command == "" and not self.player.isDead:
            # Dodge the attack.
            self.player.bitten(self.roomEnnemyNumber[self.room.name], "flee")
            self.findItem()
            command = raw_input("What are you going to do now? Run away, Fight, Continue to search for something else? ").lower()

            # Continue to search
            if command != "r" and command != "f":
                pass

        # Run Away
        if command == "r":
            self.runAway()

    def findItem(self):
        """This function determines what the player find while running away from the Zombie Guardian."""
        if self.room.name == "Armory":
            numItems = len(self.switcherWeapon)
            found = random.randrange(numItems)
            item = self.switcherWeapon[found]
            if   item == "Bow":
                print self.room.findBowFight
            elif item == "Boots":
                print self.room.findBootsFight
            elif item == "Sword":
                print self.room.findSwordFight
            pick = raw_input("Do you take it? (y/n) ").lower()
            print "\n"
            if pick == 'y':
                if   item == "Bow":
                    print self.room.pickBow
                    self.player.inventory.append(item)
                    self.switcherWeapon.remove(item)
                elif item == "Boots":
                    print self.room.pickBootsFight
                elif item == "Sword":
                    print self.room.pickSword
                    self.player.inventory.append(item)
                    self.switcherWeapon.remove(item)

    def fightLoop(self):
        """Main loop of the fight. Runs as long as there are ennemies left or the player run away"""
        choice = ""
        # Loop while player is not dead and there is ennemies and player doesn't run away.
        while not self.player.isDead and self.roomEnnemyNumber[self.room.name] > 0 and choice != "r":
            deadZombies = self.fight()
            self.roomEnnemyNumber[self.room.name] -= deadZombies

            # Second attack if player has the boots.
            if not self.player.isDead and self.roomEnnemyNumber[self.room.name] > 0 and "Boots" in self.player.inventory:
                deadZombies = self.fight()
                self.roomEnnemyNumber[self.room.name] -= deadZombies

            # Player survived the round, let the ennemy attack if it's still alive.
            if not self.player.isDead and self.roomEnnemyNumber[self.room.name] > 0:

                self.player.bitten(self.roomEnnemyNumber[self.room.name], "fight")
                choice = raw_input("What will you do now, Fight or Run away? ")

        # No more ennemies.
        if not self.player.isDead and self.roomEnnemyNumber[self.room.name] <= 0:
            self.roomEnnemyNumber[self.room.name] = 0
            print "\nAfter this fight, you take a short pause to recover your breath.\n"

        # Player runs away.
        if choice == "r":
            self.runAway()

    def runAway(self):
        """Let the player try to run away from a battle."""
        self.player.bitten(self.roomEnnemyNumber[self.room.name], "flee")
        if   self.room.name == "Armory":
            self.north()
        elif self.room.name == "Catacombs":
            self.east()

    def fight(self):
        """The player attacks the ennemy."""
        weapon = self.selectWeapon().lower()
        # Attack with the Sword
        if   weapon == "sword":
            attack = random.randrange(2)
            if attack > 0:
                print("\nYou swing your sword and you see a zombie's head flying around.\n")
                return 1
            else:
                print("\nYou swing your sword with all your might, but all you encounter is nothing, your ennemy has already moved.\n")
                return 0
        # Attack with the Bow
        elif weapon == "bow":
            attack = random.randrange(2)
            if attack == 2:
                print("\nYou band your bow and release an arrow ...\nThe arrow goes straight through the zombie's eye and continues its route, blowing half its head in the process.\n")
                return 1
            else:
                print("\nYou band your bow and release an arrow ...\nThe arrow goes straight into the wall.\nThe ennemy is already on you.\n")
                return 0
        # Throw the Lamp: Big explosion
        elif weapon == "lamp":
            print("\nDeciding to act quickly you throw the lamp which sprays oil everywhere and the whole room begins to burn.\nQuickly stepping back you avoid getting burned in the process.")
            self.roomSpecialFeatures["BurningCatacombs"] = True
            attack1 = random.randrange(9, 10)
            attack2 = random.randrange(9, 10)
            attack3 = random.randrange(9, 10)
            attack4 = random.randrange(9, 10)
            attack5 = random.randrange(9, 10)
            attack = attack1 + attack2 + attack3 + attack4 + attack5
            print("At the same time, you see {} zombies being reduced in dust.\n".format(str(attack)))
            return attack
        else:
            print("You throw {} at the closest zombie but it's useless, at least it made it step back a little.")
            return 0

    def selectWeapon(self):
        """Allow the player to attack the ennemy with whatever is available to him/her."""
        choice = ""
        weapon = ""
        while choice == "":
            if   "Sword" in self.player.inventory and "Bow" in self.player.inventory:
                message = "Select your weapon: Sword, Bow, Other "
            elif "Sword" in self.player.inventory:
                message = "Select your weapon: Sword, Other "
            elif "Bow" in self.player.inventory:
                message = "Select your weapon: Bow, Other "
            else:
                message = "Select your weapon: Other "
            choice = raw_input(message).upper()
            if   choice == 'S':
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
                    print("\nFor some reason plunging straight into the zombies with no weapon seemed like a good idea.\nIn the melee, you suddenly sense a sharp bite.\nThe zombie has got you and your vision soon starts to fade ...\n")
                    self.player.die()
                else:
                    while weapon == "":
                        self.player.showInventory()
                        weapon = raw_input("Type the full name of what you want to use. ").capitalize()
                        if weapon not in self.player.inventory:
                            print("You don't have this item in your inventory, please select something else.\n")
                            weapon = ""
                        elif weapon == "Lamp" and "Oil" not in self.player.inventory:
                            self.player.inventory.remove(weapon)
                            weapon = "empty lamp"
                        elif weapon == "Lamp" and "Oil" in self.player.inventory:
                            self.player.inventory.remove("Oil")
                            self.player.inventory.remove(weapon)
                        else:
                            self.player.inventory.remove(weapon)
            else:
                choice = ""

        return weapon
