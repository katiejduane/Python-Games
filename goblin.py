from random import randint

class Goblin(object):
    def __init__(self):
        random_power = randint(2,5)
        self.name = "Goblin"
        self.health = 6
        self.power = random_power
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
