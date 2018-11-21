# Rob's CLASSES text rpg game
import os
from random import randint

# os.system() will take any linux command and if python can run it, it will

# from [file name] import [class]
from hero import Hero
# There can only be one hero
from goblin import Goblin
# There are many, many goblins!
from vampire import Vampire

hero_name = raw_input("What is your name? ")
the_Hero = Hero(hero_name, 10)

while the_Hero.is_alive:
    randMonster = randint(1,2)
    if randMonster ==1:
        monster = Goblin()
    else:
        monster = Vampire()
    while(the_Hero.is_alive() and monster.is_alive()): # main game loop
        print "Welcome %s, you steamy turd!" % hero_name
        print "You have encountered a %s" % monster.name
        # Run the game while BOTH the hero and the goblin have health > 0
        while the_Hero.health > 0 and monster.health > 0:
            message = """
            You have %d health and %d power.
            The monster has %d health and %d power. 
            What do you want to do?
            1. Fight!
            2. Dance!
            3. Fleeeeeeeeee!
            > """ 
            print message % (the_Hero.health, the_Hero.power, monster.health, monster.power)
            
            user_input = raw_input("> ")

            if user_input == "1":
                monster.take_damage(the_Hero.power)
                print "You have done %d damage to the monster!" % the_Hero.power
            elif user_input == "2":
                the_Hero.health += 5
                print "The monster stares at you in disbelief! But this makes you soooo healthy." 
                print "Your health is now %d." % the_Hero.health
            elif user_input == "3":
                print "Goodbye, you cowardly turd!" 
                break
            else: 
                print "Thou fool, you must enter 1, 2, or 3!"

            # Now it's the monster's turn!
            if monster.is_alive:
                the_Hero.take_damage(monster.power)
                print "The monster hits you for %d damage!" % monster.power
                if not the_Hero.is_alive():
                    print "Thou hast been slain!"
                    break
                else: 
                    print "You have killed the monster!"
            raw_input("Hit enter to continue: ")
            os.system("clear")
