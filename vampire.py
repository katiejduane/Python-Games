from random import randint

from character import Character

class Vampire(Character):
    def __init__(self):
        super(Vampire, self).__init__('Vampire', 15, 4)
    #     random_power = randint(4,7)
    #     self.name = "Vampire"
    #     self.health = 15
    #     self.power = random_power
    # def take_damage(self, amount_of_damage):
    #     self.health -= amount_of_damage
    # def is_alive(self):
    #     return self.health > 0
    def make_girls_swoon(self):
        print "The skin of the Cullens flashes like diamonds!"

    
   