#!/usr/bin/env python
# -*-coding:Utf-8 -*        

class Room(object):
    """docstring for Room"""
    def __init__(self):
        self.name = ""
        self.text = ""
        self.look = ""

class Armory(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "Armory"

        self.text = "\nYou enter a room, shutting the door behind you with a *click*.\nImmediately a strong stench of rotting flesh fills your nostrils in the room.\nYou hear a moan, drawing your attention: directly across the room, further south, there’s a zombie ...\n"
        self.textAfterFight = "\nAfter this fight, you take a short pause to recover your breath.\n"

        self.altText = "\nAs you enter the room, the zombie jumps on you, the combat is inevitable.\n"
        self.altAfterFight = "\nAs you enter the room again the stench is still strong.\nNothing has changed within the armory.\n"

        self.look = "\nLooking around, you see several weapons and items around the room.\nYou must be in an armory.\nUnfortunately, the zombie has noticed your presence and is making its way towards you.\nWill you Fight?\n"
        self.lookAfterFight = "\nNow that the zombie Guardian is dead, you're free to explore the room. \nYou find a few interesting things:"

        self.findBoots = "- there is a nice pair of boots on the East side of the room."
        self.findBootsFight = "Suddenly, you see a beautiful pair of boots to the east ..."
        self.pickBoots = "You put on the boots.\nYou are immediately surprised about how comfortable they are.\nAs you walk away, you notice that you feel much lighter, these boots must be enchanted to cancel the effects of fatigue.\nYour movement speed is doubled.\n"
        self.pickBootsFight = "You quickly pick up the boots.\nThe increasing moaning of the zombie behind you makes you think that you can still pick them after the fight and you decide to drop them back.\n"

        self.findBow = "- you see a bow and some arrows on the north-West corner."
        self.findBowFight = "Suddenly, you see a bow with a quiver full of arrows to the west ..."
        self.pickBow = "You pick up the bow and the quiver next to it.\nThe bow is really heavy and might be hard to use.\nOn the bright side, as you draw an arrow from the quiver, you notice that there is still the same number of arrows inside it.\nThis quiver must be enchanted in some way, providing you with unlimited ammunitions.\n"

        self.findKey = "- the key fell unDer the table."
        self.pickKey = "You pick up the key, it might be useful later ...\n"

        self.findSword = "- you find a sword on the South-east corner which looks in a great shape."
        self.findSwordFight = "Suddenly, you see a sword to the south ..."
        self.pickSword = "You pick up the sword in a glance.\nFortunately, it's super light and you have no trouble wielding it. It looks like it was made for you.\n"

class Catacombs(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "Catacombs"

        self.text = "\nYou keep going through the corridor.\nSeeking through the darkness, you bump into something.\nPain begins to come to you and you realize you’re being bitten repeatedly.\nYou’re getting eaten! You will never know what killed you.\n"
        self.textAfterFight = "\nAfter this fight, you take a short pause to recover your breath.\n"
        self.light = "\nCurious about the figure in the distance you press forward.\nAs you slowly approach you see more and more figures.\nThe first figure turns around.\nAs you keep going through the corridor, you can see that it’s a zombie.\nThere are much more ...\nAre you going to Fight?\n"
        self.lightAfterFight = "\nDetail\n"
        self.burning = "\nThe bodies of the zombies are still burning, giving off a faint glow of light around you.\n"

        self.lightAltText = "\nAs you alredy noticed, the only thing that's left to do in the castle is to go past the zombies.\nYou decide to face them, you won't die without taking a few more of these creeps with you.\n"
        self.burningAltText = "\nYou see that there is still a couple zombies left, you decide to go straight to end them.\n"

        self.lightLook = "\nFor some reason, it seemed like a good idea to wait here while the zombies were coming at you.\nThey quickly surround you and there's so many of them.\nYou die with the horrible sensation of being eaten.\n"
        self.burningLook = "\nUnfortunately, you didn't notice that there was still a couple zombies standing.\nAs you turn around, yous sense a sharp scratch on your leg.\nYou look down to see the zombie taking a good bite in it.\nNothing is worse than the sensation of being eaten, and you're about to experience it.\n"

        self.lightLookAfterFight = "\nCatacombs Details\n"
        self.lookAfterFight = "\nBehind you is the catacomb entrance and before you lay another room which you have not yet entered.\n"

class CatacombsEntrance(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "CatacombsEntrance"

        self.firstText = "\nYou walk through the opening without being able to see.\nYou hear stifled moaning and groaning."
        self.lightFirstText = "\nGoing through the entrance your light begins to creep along the walls, slowly lighting the area around you.\nYour lamp dimly lights something in the distance.\nYou can see that it looks like a person or a statue of a person.\n"

        self.altLight = "\nAs you walk away, you hear that the moaning and groaning decrese in intensity.\nYour lamp dimly lights the zombies in the distance.\n"
        self.altBurning = "\nAs you walk away, you hear that the moaning and groaning decrese in intensity.\n"

        self.text = "You try to feel around again.\nYou only feel the entrance way to the East and the wall keeps on going.\n"
        self.light = "\nYour lamp dimly lights something in the distance.\nYou can see that it looks like a person or a statue of a person.\n"
        self.burning = "The remnants of the fire give these catacombs a surrealistic dimension, between beauty and horror.\n"

        self.look = "\nThe darkness is complete, you can't even see your feet.\n"
        self.altLook = "Thinking about it, you remember you have the lamp you found in your backpack.\nFortunately, you also found some oil to light it.\n"
        self.lightLook = "\nLooking around, you see the skulls and bones covering the walls.\nTo the east, you see the bottom of the stairs faintly in the flickering light.\nThe shadowy figure in front of you is just there in the middle of the catacomb.\n"
        self.burningLook = "\nBurning Catacombs Entrance Details\n"

class DeathChamber(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "DeathChamber"
        self.text = "\nUpon entering the room you feel the floor drop from beneath your feet.\nIT’S A TRAP! You begin falling and look down.\nYour last few thoughts are of home as you watch the spikes getting closer and closer.\nYou end up impaled on a spike.\n"

class GuestRoom(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "GuestRoom"

        self.text = "\nYou reach the door and push it open.\nYou enter into a small room.\nOn the right there is a bed.\nThe bed is neatly made and it seems as though no one, except a few bugs, has used it in a while.\n"
        self.altText = "To the left there is a small table where there appears to be a jar with some sort of liquid inside.\n"

        self.look = "\nThere is nothing interesting anymore in this bedroom.\n"
        self.altLook = "As you walk over to the table you see that the jar is full with oil.\n"

        self.pickOil = "You grab the jar of oil and put it in your backpack.\n"

class Hall(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "Hall"

        self.firstText = "\nYou approach the castle doors which are tall and wide.\nYou apply all of your might and pull the castle doors open.\nAfter entering inside of the castle you find yourself in a grand entrance hall."
        self.altText = "\nYou return to the entrance hall."
        self.downText = "As you walk up the stairs back to the light, you put your lamp back into your backpack.\n"

        self.text = "There are doors to the North and to the South and a grand staircase leading Up and Down.\n"

        self.look = "\nYou quickly begin to look around taking in more of the details.\nThere are several pictures on the north wall.\nLooking closer it seems like it’s the monarchs who ruled within this castle.\n"

class HallLower(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "HallLower"

        self.firstText = "\nThe farther you walk down the stairs the darker it gets.\nWhen it has become completely dark you reach the end of the stairs."
        self.altText = "\nYou return to the bottom of the stairs."

        self.text = "\nFrom what you can tell you are standing on a landing at the bottom of the stairs.\nYou are alone in the dark.\n"
        self.light = "\nYou see skulls lining the walls.\nYou realize you’ve just headed down into a catacomb.\nYou see an entrance straight across from you to the west.\nYour light reaches just past the entrance into the next room.\n"

        self.look = "\nIt is almost impossible to see your hand in front of your face.\nYou begin to feel around in the dark.\nYou feel the staircase to the east.\nFeeling the wall to the west you feel an opening.\n"
        self.altLook = "Thinking about it, you remember you have the lamp you found in your backpack.\nFortunately, you also found some oil to light it.\n"
        self.lightLook = "\nDetail\n"

class HallUpper(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "HallUpper"

        self.firstText = "\nYou decide to head upstairs.\nYour footsteps echo loudly as you walked up the big stone steps.\nAfter a short while you reach the top of the stairs.\nYou are in a corner and can see two closed doors.\nThere are two rooms.\nThe one to the south has a lamp that’s burning close to the door.\nThe one on the west is chained with a padlock.\n"

        self.text = "\nYou return to the top of the stairs.\nYou are in a corner and can see a door to the west and a door to the south.\n"

        self.look = "\nThis is just an upper level with nothing particular.\n"
        self.altLook = "You had time to think about what you read in the book and you're now sure that there is a trap here. What will you do:\n\tTurn the lamp.\n\tPull the lamp.\n\tNothing\n"
        self.altLookDoor = "That padlock looks pretty tough.\nNot getting in there without a key.\n"
        self.altLookTrap = "The lamp is burning brightly although it seems to have no fuel source.\nIt’s purely burning on the wall.\n"

        self.lampMoved = "\nAs you slowly begin to turn the lamp you hear gears turning and the light begins to fade.\nIn the distance you hear a machine begin to operate and a loud grinding noise.\nYou look around you and everything is silent again.\n"

class Library(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "Library"

        self.text = "\nYou push open the door and enter.\nUpon entering the room you notice it is a library.\nYou quickly begin to scan the whole room.\nThere are thousands of books lining on the shelves.\nIn the middle lies a desk that holds an open book.\n"

        self.look = "\nYou flip it over to see the title “A Beginner’s Guide to Necromancy: Starting with the Undead”.\nShocked with the title you begin to thumb through the pages.\nWhile flipping through you find many things such as:\n\t“…blood is the cause of life.”,\n\t“…feed and water daily.”,\n\t“…turn the light away from them.”,\n\t“…keep away from fire and heat”.\nConfused you set the book down.\n"

class LockedDoor(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "LockedDoor"

        self.text = "\nThe door is padlocked shut.\n"

        self.look = "\nThe door is padlocked shut.\n"
        self.altLook = "While looking at the lock, you notice that the key you found in the armory would fit.\n"

        self.doorUnlocked = "\nThe door is now unlocked.\n"

class ObservationTower(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "ObservationTower"

        self.text = "\nYou open the door to a staircase.\nYou begin to climb and slowly but surely you reach the top of the tower.\n"
        self.altText = "Hanging in the middle of the room is a lamp.\n"

        self.look = "\nYou look around you and can see what is surrounding the castle.\nThe only things that you see is the courtyard down below.\n"
        self.altLook = "Taking a closer look at the lamp, you see that it runs on oil, unfortunately, it's empty.\n"

        self.pickLamp = "You grab the lamp and put it in your backpack.\n"

class Outside(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "Outside"

        self.firstText = "\nYou enter into the courtyard of a castle."
        self.altText = "\nYou go back to the courtyard."

        self.text = "There is an entrance to the castle to the East, an overgrowth to the South and some rubble to the North.\n"

        self.look = "\nThe castle is tall with some of it in ruins to the North.\nIt looks like it has been a while since someone lived here or took care of the grounds as the overgrowth has consumed most of the south side of the building.\nTo the west is the gate that you entered to get to the courtyard.\nTo the east, the massive castle doors stand rusty and still.\n"

class Overgrowth(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "Overgrowth"

        self.text = "\nYou decide to walk towards the overgrowth.\nAs you walk closer you see that it has grown halfway up the castle wall.\n"
        self.altText = "\nYou finally succeed in untangle yourself.\n"

        self.look = "\nYou notice that it has grown so thick there is no possible way to move through it.\nHowever, upon closer inspection you see that there is a small opening just small enough to fit through.\n"

class OvergrowthSouth(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "OvergrowthSouth"

        self.text = "\nAs you attempt to crawl through the hole you notice it keeps getting smaller, blocking your path.\nThe only option now is to go back.\n"

        self.look = "\nAs you decide to look around you get further entangled in the bushes.\nOut of nowhere, a snake slithers along your back.\nThinking it’s another branch you keep wiggling to get free.\nYou feel a sharp pain as the snake has bitten you.\nYour vision fades as does your life.\nYou die.\n"

class Rubble(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "Rubble"

        self.text = "\nYou walk northward, closer to the rubble.\nThe pile of rubble is extremely large, there was clearly a battle here at one point, and it has been long since the castle was abandoned.\n"

        self.look = "\nYou see a number of rusty pikes sticking out of the rubble as evidence of the old battle.\n"

class RubbleNorth(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "RubbleNorth"

        self.text = "\nYou attempt to climb over the pile of rubble, and reach the top, steadying yourself on a large brick from the top of the castle.\nThis brick knocks loose and you slip, falling on a pike, impaling yourself.\nAfter a long time suffering in pain, you pass out.\nNobody will ever find you.\n"
        
class TrappedRoom(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "TrappedRoom"

        self.text = "\nYou open the door to find a hall.\nPaintings litter the walls.\nAt the other end of the hallway you see a doorway.\n"

        self.look = "\nWhile looking at the paintings on the wall you notice some strange things.\nThere is an empty frame that has inscribed “King Charles VI”.\n Another painting titled “The great war of 1332” has some disfigured and dismembered people fighting the king’s knights.\n"

class TreasureRoom(Room):
    def __init__(self):
        Room.__init__(self)
        self.name = "TreasureRoom"

        self.text = "\nYou begin to see the hall coming to an end.\nAt the end of the hall is “the treasure”.\nCongratulations you’ve won the game!!\n"
        self.burning = "\nYou walk west through the hall with a few flickers of flame still burning.\n"
