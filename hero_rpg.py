#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__(self, hero_power, hero_health):
        self.hero_power = hero_power
        self.hero_health = hero_health

class Goblin:
    def __init__(self, goblin_power, goblin_health):
        self.goblin_power = goblin_power
        self.goblin_health = goblin_health

def main():
    heroObj = Hero(10, 9)# Hero Object
    goblinObj = Goblin(1, 20)# Goblin Object
    
    
    while goblinObj.goblin_power > 0 and heroObj.hero_power > 0:
        print(f"You have {heroObj.hero_health} health and {heroObj.hero_power} power.")
        print(f"The goblin has {goblinObj.goblin_health} health and {goblinObj.goblin_power} power.")
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            goblinObj.goblin_health -= heroObj.hero_power
            print(f"You do {heroObj.hero_power} damage to the goblin.")
            if goblinObj.goblin_health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblinObj.goblin_health > 0:
            # Goblin attacks hero
            heroObj.hero_health -= goblinObj.goblin_power
            print(f"The goblin does {goblinObj.goblin_power} damage to you.")
            if heroObj.hero_health <= 0:
                print("You are dead.")

main()
