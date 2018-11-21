# Rob's example Goblin Game
# The hero has the option to: 
# 1. Fight
# 2. Dance
# 3. Flee

# Ger the os module from python
import os
# os.system() will take any linux command and if python can run it, it will

from hero import Hero

hero_name = raw_input("What is thy name, brave adventurer? ")

the_Hero = (hero_name, 10)

def fight():
    print "Welcome %s. Thou art brave!" % hero_name
    print "Fight the goblin"
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    # Run the game while BOTH the hero and the goblin have health > 0
    while hero_health > 0 and goblin_health > 0:
        print """
        You have %d health and %d power.
        The goblin has %d health and %d power. 
        What do you want to do?
        1. Fight!
        2. Dance!
        3. Fleeeeeeeeee!
        > """ % (hero_health, hero_power, goblin_health, goblin_power)
        
        user_input = raw_input()

        if user_input == "1":
            goblin_health -= hero_power
            print "You have done %d damage to the goblin!" % hero_power
        elif user_input == "2":
            hero_health += 10
            print "The goblin stares at you in disbelief! But this makes you soooo healthy." 
            print "Your health is now %d." % hero_health
        elif user_input == "3":
            print "Goodbye, you cowardly terd!" 
            break
        else: 
            print "Thou fool, you must enter 1, 2, or 3!"

         # Now it's the goblin's turn!
        if goblin_health > 0:
             hero_health -= goblin_power
             print "The goblin hits you for %d damage!" % goblin_power
             if hero_health <= 0:
                 print "Thou hast been slain!"
                 break
        raw_input("Hit enter to continue: ")
        os.system("clear")

fight()