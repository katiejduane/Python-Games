# Rob's example Goblin Game
# The hero has the option to: 
# 1. Fight
# 2. Dance
# 3. Flee

hero_name = raw_input("What is thy name, brave adventurer?")

def fight():
    print "Welcome %s. Thou art brave!" % hero_name
    print "Fight the goblin"
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2
