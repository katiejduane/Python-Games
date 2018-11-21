# Hero Class/Object!

class Hero(object):
    def __init__(self, name, power = 8): # power = 8 defines it as 8 only if they don't put in their own parameter.
        #You only need to pass additional variables when their data will change. 
        # But ALL of our heros will have a health of 10 and a power of 5...
        self.name = name
        self.health = 10
        self.power = power
    def cheer_hero(self):
       print "Welcome, %s, you steamy turd!" % self.name
    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0