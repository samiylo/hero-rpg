#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random
import time

class Charachter:
    def __init__(self,power, health):
        self.power = power
        self.health = health
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Hero(Charachter):
    
    def attack(self, enemy):
        self.enemy = enemy
        bonus_damage = random.randint(1, 10)
        if bonus_damage < 9:
            enemy.health-= self.power
            print(f"You do {self.power} damage to the goblin.")
        elif bonus_damage >= 9:
            enemy.health -= self.power * 2
            print(f"You do {self.power} damage to the goblin.")
            print(f"You did DOUBLE damage!")
        if enemy.health <= 0:
            print("The goblin is dead.")
    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")


class Goblin(Charachter):

    def attack(self, defender):
        self.defender = defender

        defender.health -= self.power
        print(f"The goblin does {self.power} damage to you.")
        if defender.health <= 0:
            print("You are dead.")
    def print_status(self):
        print(f"The Goblin has {self.health} health and {self.power} power.")



def main():
    heroObj = Hero(10, 9)# Hero Object
    goblinObj = Goblin(1, 20)# Goblin Object
    zombieObj = Goblin(5,1000)# Zombie Object
    
    while goblinObj.alive() == True and heroObj.alive() == True:
        goblinObj.print_status()
        heroObj.print_status()
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
