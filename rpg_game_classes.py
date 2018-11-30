# Classes for rpg text game

class Human(object):
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.career = 10
        self.adventure = 10
        self.love = 10
        self.finance = 10
        self.growth = 10
        self.total = self.health + self.career + self.adventure + self.love + self.finance + self.growth
    def __repr__(self):
        return "Levels --> Health: %d, Career: %d, Adventure: %d, Love: %s, Finance: %d, Growth: %d " % (self.health, self.career, self.adventure, self.love, self.finance, self.growth)
    def health_adjust(self, health_change):
        self.health += health_change
    def career_adjust(self, career_change):
        self.career += career_change
    def adv_adjust(self, adventure_change):
        self.adventure = self.adventure + adventure_change
    def love_adjust(self, love_change):
        self.love += love_change
    def finance_adjust(self, finance_change):
        self.finance += finance_change
    def growth_adjust(self, growth_change):
        self.growth += growth_change
    def print_warning(self):
        print "Be careful about the choices your make, levels are getting low!"
    def print_congrats(self):
        print "Way to go, doll, you're doin' alright!"
    def update_total(self):
        self.total = self.health + self.career + self.adventure + self.love + self.finance + self.growth


class Life(object):
    def __init__(self, person):
        self.power = 60
        self.person = person # CAN I PASS IT AN OBJ HERE? A HUMAN WHO IT AFFECTS
    def adjust_power(self, adjust):
        self.power += adjust

class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Store(object): #I'D LIKE TO MAKE A MORE GENERAL BLUE PRINT BUT I CAN'T FIGURE OUT HOW TO DO IT IF I WANT SPECIFIC FUNCTIONS FOR EACH ITEM (THE PRINT ASCII ART ONES)
    def __init__(self, gym, wine, nightclass, garden):
        self.gym = gym
        self.wine = wine
        self.nightclass = nightclass
        self.garden = garden
    def add_item(self):
        pass
    def go_gym(self):
        def __str__(self):
            print 
            """
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
======================================================David Riley)
        """
    def go_wine(self):
        print 
        """
    _____
   /.---.\
   |`````|
   \     /
    `-.-'           ____
      |    /\     .'   /\
    __|__  |K----;    |  |
jgs`-----` \/     '.___\/
        """
    def go_nightclass(self):
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

    def go_garden(self):
        print  
        """ 
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

# class Item(object):
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value
#     def __str__(self):
#         return "The item is: %s. The value is %d" % (self.name, self.value)
#     def effect_human(self, human):
#         human.health_adjust(self.value)

class Opportunities(object):
    def __init__(self, opportunity, value):
        self.opportunity = opportunity
        self.value = value
        pass
class Relationships(object):
    def __init__(self):
        pass

class Fun(object):
    def __init__(self):
        pass

class Therapy(object):
    pass