# Text-Based RPG Game!
# The is a procedural approach to a text based RPG game
# There is a hero/protagonist
# And he/she must have a few options that dictate how the game goes!
from time import sleep
import os

print "WELCOME TO REAL LIFE."
human = raw_input("What's your name? ")
gameOn = True

def play():
    print "Hi, %s, welcome to adulthood. You have some choices to make." % human
    print "               "
    sleep(1)
    print "Life can be fun, but there are consequences. Who will win, you or life?"
    print "               "
    health = 10
    love = 10
    career = 10
    adventure = 10
    growth = 10
    finance = 10
    life = 60
    human_total = health + love + career + adventure + growth + finance

    while gameOn:
        print "You have six choices ahead of you that will determine if you succeed, or if life wins!"
        sleep(3)
        question = True
        print """
        You've got some money. Would you like to spend it on: a one year fitness studio membership,
        OR an all-inclusive trip (with bottomless drinks!) to the Bahamas? Enter F for fitness or B for Bahamas"
        """
        sleep(5)
        while question:
            user_choice = raw_input("> ").upper() 
            if user_choice == "F":
                health += 3
                growth += 2
                question = False
            elif user_choice == "B":
                health -= 3
                adventure += 1
                life += 5
                question = False
            else:
                print "Make a choice, terd, F or B! This isn't a buffet!"
                continue
            # what do i write here to let them re-enter their choice?
        human_total = health + love + career + adventure + growth + finance
        print "You: %d / Life: %d" % (human_total, life)
        
        question = True
        print """You've just met two people. One of them is wild and passionate (this won't last long but it WILL be fun),
        and the other is kind and stable (marriage material?)... who do you choose: P for passionate, or S for Stable """
        sleep(5)
        while question:
            user_choice = raw_input("> ").upper()
            if user_choice == "P":
                health -= 5
                adventure += 3
                love -= 2
                life =+ 5
                question = False
            elif user_choice == "S":
                health += 5
                adventure -= 3
                love += 5
                question = False
            else:
                print "Make a choice between the two. You can't have it all! (at least not yet)...F or S "
                continue
        human_total = health + love + career + adventure + growth + finance
        print "You: %d / Life: %d" % (human_total, life)

        question = True
        print """You've been given two offers: an entry level position that will put you on track to achieve your career goals, OR,
        an opportunity to live in Italy for 6 months, working at a vineyard and traveling on the weekends. Which do you choose?
        C for Career, or I for Italy """
        sleep(5)
        while question:
            user_choice = raw_input("> ").upper()
            if user_choice == "C":
                career += 10
                adventure -= 10
                growth += 5
                health += 3
                question = False
            elif user_choice == "I":
                career -= 10
                adventure += 15
                growth += 3
                health +- 3
                life += 5
                question = False
            else:
                print "Ummmm, what!? C or I "
                continue
        human_total = health + love + career + adventure + growth + finance
        print "You: %d / Life: %d" % (human_total, life)

        question = True
        print """It's time for some adventure. What would you like to do? S for skydiving (tandem of course!)
        or D for a day at your local amusement park? """
        sleep(5)
        while question:
            user_choice = raw_input("> ").upper()
            if user_choice == "S":
                adventure += 10
                growth += 2
                health -= 2
                question = False
            elif user_choice == "D":
                adventure -= 3
                life += 5
                question = False
            else:
                print "What will it be, buck-a-roo??? "
                continue
        human_total = health + love + career + adventure + growth + finance
        print "You: %d / Life: %d" % (human_total, life)



play()