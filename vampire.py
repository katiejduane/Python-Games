from random import randint

class Vampire(object):
    def __init__(self):
        random_power = randint(4,7)
        self.name = "Vampire"
        self.health = 15
        self.power = random_power
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
    def make_girls_swoon(self):
        print "The skin of the Cullens flashes like diamonds!"