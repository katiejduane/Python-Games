#My CLASSified txt RPG:

from time import sleep
import os

from rpg_game_classes import Human
from rpg_game_classes import Life
from rpg_game_classes import Store

Katie = Human("Katie")
Katies_Life = Life(Katie)
My_Store = Store("Gym", "Wine", "Class", "Garden")

gameOn = True

while gameOn:
    print "Hi %s, welcome to second, second life..." % Katie.name
    sleep (1)
    print """
    The choices we make either help us win at life, or allow life to beat us to a pulp. 
    What will your choices do to you?""" 
    sleep (4)
    
    print """
    You've got six choices ahead of you that will determine whether or not you can win at life.
    Don't worry, there's an emergency store if you really need to re-up on something...!"""
    print "                  "

    raw_input("Hit enter to continue... ")
    os.system("clear")

    # Question 1: Career/Adventure/Finance
    question = True
    print """
    You're in between jobs (for undisclosed reasons) and you've been given a couple of opportunities: to work abroad at an Italian vineyard, 
    or an internship at a company aligned with your long-term professional goals. What'll it be? 
    V for vineyard, or I for internship"""
    print "             "
    while question:
        career_answer = raw_input("> ").upper()
        if career_answer == "V":
            print """
            Well aren't you the adventurous little lush. You get points for guts and whimsy, but you'll have to lose points
            for financial and professional capriciousness."""
            print " "
            #logic to deduct and add power points from Human and Life objects
            Katie.career_adjust(-5), Katie.adv_adjust(8), Katie.finance_adjust(-5), Katies_Life.adjust_power(3)
            question = False
        elif career_answer == "I":
            print """
            You might want all the pats on the back, but life is a lot less interesting when you do the RIGHT thing every
            time. Don't be afraid to be BAD once in a while!"""
            print " "
            #logic to deduct and add power points from Human and Life objects
            Katie.career_adjust(5), Katie.adv_adjust(-2), Katie.finance_adjust(5)
            question = False
        else:
            print "Hey silly, you get two choices: V or I!"
            continue
        print Katie
        print " "
        raw_input("Hit enter to go to the next question: ")
    os.system("clear")
        
    # Question 2: Love
    question = True
    print """
    Let's take a look at looooovvvve. You've just met two people: one is passionate, mysterious and wild... but 
    the other is kind, and you could totally bring home to mom. Who do you choose? P for passionate, M for Mom's approval,
    or B for somehow going after both..."""
    print "             "
    while question:
        love_answer = raw_input("> ").upper()
        if love_answer == "B":
            print "You want to have your cake and eat it to? Fine, but you'll lose growth points!"
            print " "
            # logic
            Katie.love_adjust(2), Katie.growth_adjust(-3), Katies_Life.adjust_power(4)
            question = False
        elif love_answer == "P":
            print "Oh you KNOW how this always ends..."
            print " "
            # logic
            Katie.love_adjust(3), Katies_Life.adjust_power(3)
            question = False
        elif love_answer == "M":
            print "Just make sure you approve of this person as much as your mom does! Who wants eternal bordeom!?"
            print " "
            # logic
            Katie.love_adjust(10), Katies_Life.adjust_power(2)
            question = False
        else:
            print "This isn't a buffet, doll. T, M, or B!"
            print " "
            continue
        print Katie
        print " "
        raw_input("Hit enter to go to the next question: ")
    os.system("clear")

    # Question 3: Adventure, Health
    question = True
    print """
    It's time for a little adventure. All activities are totally paid for, so choose what excites you the most:
    Enter B for a trip to the beach, M for a hike in the mountains, A for a jaunt into the Amazon Jungle, or S for skydiving! """
    print "             "
    while question:
        adv_answer = raw_input("> ").upper()
        if adv_answer == "B":
            print "The beach is nice, but... not exactly exciting..."
            print " "
            # logic
            Katie.adv_adjust(2), Katies_Life.adjust_power(2)
            question = False
        elif adv_answer == "M":
            print "Don't forget your portable hammock!"
            print " "
            # logic
            Katie.adv_adjust(4)
            question = False
        elif adv_answer == "A":
            print "Make sure the piranhas are sleeping before you go for a swim..."
            print " "
            # logic
            Katie.adv_adjust(6)
            question = False
        elif adv_answer == "S":
            print "Is there anything more beautiful than floating back down to earth through the clouds?"
            print " "
            # logic
            Katie.adv_adjust(10), Katie.health_adjust(-2)
            question = False
        else:
            print "Are these adventures not exciting enough for you!? B, M, A or S!"
            print " "
            continue
        print Katie
        print " "
        raw_input("Hit enter to go to the next question: ")
    os.system("clear")

    # Question 4: The Store; Finances, Health, Growth, Career
    question = True
    print """
    Shopping Trip! Based on your current levels, and how you feel about your life decisions thus far, make the
    purchase that you feel best suits your present needs: G for a gym membership. W for Wine of the month for a WHOLE YEAR.
    C for an evening class to expand your horizons. S for seeds to plant a garden at home."""
    print "             "
    while question:
        store_answer = raw_input("> ").upper()
        if store_answer == "G":
            print "You've just earned yourself some serious health points!"
            print " "
            # logic
            Katie.health_adjust(10), Katie.adv_adjust(-2)
            print """
            _                             _
           | |                           | |
         =H| |========mn=======nm========| |H=
           |_|        ( \     / )        |_|
                       \ )(")( /
                       ( /\_/\ )
                        \     /
                         )=O=(
                        /  _  \
                       /__/ \__\
                       | |   | |
                       |_|   |_|
                       (_)   (_)
====================================================== David Riley)
        """
            question = False
        elif store_answer == "W":
            print "You might have good taste, but what's that your liver is whispering?"
            print " "
            # logic
            Katie.health_adjust(-10), Katie.adv_adjust(2)
            print """
    _____
   /.---.\
   |`````|
   \     /
    `-.-'           ____
      |    /\     .'   /\
    __|__  |K----;    |  |
jgs`-----` \/     '.___\/
        """
            question = False
        elif store_answer == "C":
            print "They say boredom is for the BORING. Looks like you're not!"
            print " "
            # logic
            Katie.career_adjust(5), Katie.health_adjust(1)
            print
            """
      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
                dwb `---`
        """
            question = False
        elif store_answer == "S":
            print "Creating beauty AND spending time out of doors. GOOD CHOICE!"
            print " "
            # logic
            Katie.health_adjust(5), Katie.love_adjust(2)
            print  """ 
        _____
	  /  ___  \
    /  /  _  \  \
  /( /( /(_)\ )\ )\
 (  \  \ ___ /  /  )
 (    \ _____ /    )
 /(               )\
|  \             /  |
|    \ _______ /    |
 \    / \   / \    /
   \/    | |    \/
         | |
         | |
         |_| """
            question = False
        else:
            print "Try again! G, W, C or S!"
            print " "
            continue
        print Katie
        print " "
        raw_input("Hit enter to go to the next question: ")
    os.system("clear")


    # Question 5: Growth, Health, Career
    question = True
    print """
    You're not happy with yourself, your life, your job everything in general just feels... wrong. What do you do?
    See your options below:"""
    print "             "
    sleep(3)
    print "E for escape: quit your job, leave your city, dump that nice person your mom approved of. Don't think, just run!"
    sleep(2)
    print "T for therapy. Find someone to talk about your feelings with, or maybe help you reprioritize."
    sleep(2)
    print "W for where was that wine store again? And maybe I'll buy a new car or new clothes. Yes, new things will make me feel better!"
    sleep(2)
    print "G for getaway. Go to the beach for a weekend. Spain for a couple weeks. Maybe the mountains. Anywhere but here."
    while question:
        growth_answer = raw_input("> ").upper()
        if growth_answer == "E":
            print "I've done this before. It doesn't work... at least, not for long!"
            print " "
            # logic
            Katies_Life.adjust_power(10), Katie.growth_adjust(-10), Katie.adv_adjust(5), Katie.finance_adjust(-5)
            question = False
        elif growth_answer == "T":
            print "The least fun, but the longest lasting. Go you!"
            print " "
            # logic
            question = False
            Katie.growth_adjust(10), Katie.love_adjust(5), Katie.health_adjust(5)
        elif growth_answer == "W":
            print "This... never works."
            print " "
            # logic
            Katie.growth_adjust(-5), Katie.health_adjust(-5), Katies_Life.adjust_power(5)
            question = False
        elif growth_answer == "G":
            print "You'll feel better while your away, but then you'll return to...your life!"
            print " "
            # logic
            Katie.adv_adjust(5), Katie.growth_adjust(-5), Katie.health_adjust(-5), Katies_Life.adjust_power(5), Katie.finance_adjust(-2)
            question = False
        else:
            print "Try again! E, T, W or G! "
            print " "
            continue
        print Katie
        print " "
        raw_input("Hit enter to go to the next question: ")
    os.system("clear")

    # Question 6: Finance
    question = True
    print """
    Let's take a look at your paycheck. You can roll $100.00 more every two weeks into your 401K, or, roll $100.00 every two weeks
    into your 'I want to go to X country fund. Where do you send the money? F for 401K, X for that exotic trip abroad!"""
    print "             "
    while question:
        career_answer = raw_input("> ").upper()
        if career_answer == "X":
            print """
            Really, I can't blame you. I do this, too. Every GD time."""
            print " "
            #logic 
            Katie.finance_adjust(-10)
            question = False
        elif career_answer == "F":
            print """
            Yes, I get it, you're SUPER responible. Just don't forget that you could DIE AT ANY TIME and, you know,
            it's important to have fun being alive, once in a while """
            print " "
            #logic to deduct and add power points from Human and Life objects
            Katie.finance_adjust(10)
            question = False
        else:
            print "Hey silly, you get two choices: F or X!"
            continue
        print Katie
        print " "
        raw_input("Hit enter to go to the next question: ")
    os.system("clear")

    print "Calculating score..."
    sleep(5)
    os.system("clear")

    print Katie
    print "Your total: "  
    print Katie.total
    print "Life total: " 
    print Katies_Life.power
    print "    "
    if Katie.total > Katies_Life.power:
        print "Congratulations! You didn't let life get you down. Just make sure you're also having some fun. We're all headed to the same place, after all: the great black abyss!!"
        sleep(2)
        play_again = raw_input("Would you like to play again? Y for yes, N for no: ")
        if play_again == "Y":
            continue
        else:
            print "Thanks for playing!"
            gameOn = False

    elif Katie.total == Katies_Life.power:
        print "A little close..."
        sleep(2)
        play_again = raw_input("Would you like to play again? Y for yes, N for no: ")
        if play_again == "Y":
            continue
        else:
            print "Thanks for playing!"
            gameOn = False
    else:
        print "Yikes, life beat you! if you could do it all over again, would you change anything? Or do you like learning the hard way? (I for one, prefer the latter)"
        sleep(2)
        play_again = raw_input("Would you like to play again? Y for yes, N for no: ")
        if play_again == "Y":
            gameOn = True
        else:
            print "Thanks for playing!"
            gameOn = False
    
    
