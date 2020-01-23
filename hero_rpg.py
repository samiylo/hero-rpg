#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__(self, hero_power, hero_health):
        self.hero_power = hero_power
        self.hero_health = hero_health
    
    def attack(self, enemy):
        self.enemy = enemy
        enemy.goblin_health-= self.hero_power
        print(f"You do {self.hero_power} damage to the goblin.")
        if enemy.goblin_health <= 0:
            print("The goblin is dead.")
    def alive(self):
        if self.hero_health > 0:
            return True
        else:
            return False
    def print_status(self):
        print(f"You have {self.hero_health} health and {self.hero_power} power.")


class Goblin:
    def __init__(self, goblin_power, goblin_health):
        self.goblin_power = goblin_power
        self.goblin_health = goblin_health

    def attack(self, defender):
        self.defender = defender

        defender.hero_health -= self.goblin_power
        print(f"The goblin does {self.goblin_power} damage to you.")
        if defender.hero_health <= 0:
            print("You are dead.")
    
    def alive(self):
        if self.goblin_health > 0:
            return True
        else:
            return False
    
    def print_status(self):
        print(f"The Goblin has {self.goblin_health} health and {self.goblin_power} power.")



def main():
    heroObj = Hero(10, 9)# Hero Object
    goblinObj = Goblin(1, 20)# Goblin Object
    
    
    while goblinObj.alive() == True and heroObj.alive() == True:
        goblinObj.print_status()# print(f"You have {heroObj.hero_health} health and {heroObj.hero_power} power.")
        heroObj.print_status()# print(f"The goblin has {goblinObj.goblin_health} health and {goblinObj.goblin_power} power.")
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == "1":
            heroObj.attack(goblinObj)# Hero attacks goblin
            
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblinObj.alive() > 0:
            # Goblin attacks hero
            goblinObj.attack(heroObj)

main()
