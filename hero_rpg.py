#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random
import time

class Charachter:
    def __init__(self, name, power, health):
        self.name = name
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
            enemy.health -= self.power
            print(f"You do {self.power} damage to the enemy.")
            if enemy.name == "Medic":
                heal = random.randint(1, 10)
                if heal >= 9:
                    enemy.health += 2
                    print(f"Enemy heals up with {heal} points.")

        elif bonus_damage >= 9:
            enemy.health -= self.power * 2
            print(f"You do {self.power} damage to the enemy.")
            print(f"You did DOUBLE damage!")
        if enemy.health > 0:
            self.health -= enemy.power
            print(f"{enemy.name} does {enemy.power} damage to you")
        elif enemy.health <= 0:
            print(f"{enemy.name} is dead.")
    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")


class Goblin(Charachter):

    def attack(self, defender):
        self.defender = defender

        defender.health -= self.power
        print(f"The {self.name} does {self.power} damage to you.")
        if defender.health <= 0:
            print("You are dead.")
    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")



def main():
    heroObj = Hero("Hero", 5, 10)# Hero Object
    goblinObj = Goblin("Goblin", 1, 20)# Goblin Object
    zombieObj = Goblin("Zombie", 5,1000)# Zombie Object
    medicObj = Goblin("Medic", 2, 20)# Medic Object
    shadowObj = Goblin("Shadow", 0, 1)# Shadow Object
    
    while heroObj.alive() == True:
        heroObj.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. fight medic")
        print("3. fight shadow")
        print("4. flee")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == "1":
            if goblinObj.alive() == True:
                heroObj.attack(goblinObj)# Hero attacks goblin
                goblinObj.print_status()
            else:
                print("Goblin is alreadu dead. Attack someone else.")
        elif raw_input == "2":
            if medicObj.alive() == True:
                heroObj.attack(medicObj)# Hero attacks Medic
                medicObj.print_status()
            else:
                print("Medic is already dead. Attack someone else.")
        elif raw_input == "3":
            hit_chance = random.randint(1,10)
            if shadowObj.alive() == True:
                if hit_chance == 1:
                    heroObj.attack(shadowObj)
                    shadowObj.print_status()
                else:
                    print("Your attacked missed!\n Try again!")
            else:
                print("Shadow is already dead. Attack someone else")

        elif raw_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

    if heroObj.alive() == False:
        print(" ")
        print("You have died. Booo Hooo let me play a sad tune on the smallest violin.")

main()
