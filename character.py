# character class!

# This will be our SUPER/parent class for all the characters in the game!

class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def is_alive(self):
        return self.health > 0
    def take_damage(self, ammount_of_damage):
        self.health -= amount_of_damage