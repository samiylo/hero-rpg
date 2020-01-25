#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random
import time

class Charachter:
    def __init__(self, name, power, prehealth, armor, coins):
        self.name = name
        self.power = power
        self.health = prehealth + armor
        self.coins = coins
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def supertonic(self):
        if self.coins >= 20:
            self.coins -= 20
            self.health += 20
            print("You have purchased Super Tonic and gained 20 hp.")
            print(self.coins)
        else:
            print("You dont have enough coins for this item.")
            print(self.coins)


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
            print(f"{enemy.name} does {enemy.power} damage to you.")
        elif enemy.health <= 0:
            print(f"{enemy.name} is dead.")
            self.coins += enemy.coins
            print(f"You gained a bounty of {enemy.coins} coins.")
            print(f"You have {self.coins} coins.")
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
    heroObj = Hero("Hero", 5, 10, 0, 30)# 
    goblinObj = Goblin("Goblin", 1, 20, 0, 10)# Name, power, health, armor, coins
    zombieObj = Goblin("Zombie", 5,1000, 0, 40)# Name, power, health, armor, coins
    medicObj = Goblin("Medic", 2, 20, 0, 60)# Name, power, health, armor, coins
    shadowObj = Goblin("Shadow", 0, 1, 0, 10)# Name, power, health, armor, coins
    
    while heroObj.alive() == True:
        heroObj.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight Goblin")
        print("2. Fight Medic")
        print("3. Fight Shadow")
        print("4. Run like the baby you are")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == "1":
            if goblinObj.alive() == True:
                if heroObj.health <= 8:
                    choice = int(input(f"Your health is {heroObj.health} \nwould you like to purchase a Super Tonic?\n1. Yes\n2. No\n>"))
                    if choice == 1:
                        heroObj.supertonic()
                else:
                    pass
                heroObj.attack(goblinObj)# Hero attacks goblin
                print("--------------------------------")
                goblinObj.print_status()
                
            else:
                print("Goblin is alreadu dead. Attack someone else.")
        elif raw_input == "2":
            if medicObj.alive() == True:
                if heroObj.health <= 8:
                    choice = int(input(f"Your health is {heroObj.health} \nwould you like to purchase a Super Tonic?\n1. Yes\n2. No\n>"))
                    if choice == 1:
                        heroObj.supertonic()
                else:
                    pass
                heroObj.attack(medicObj)# Hero attacks Medic
                print("--------------------------------")
                medicObj.print_status()
            else:
                print("Medic is already dead. Attack someone else.")
        elif raw_input == "3":
            hit_chance = random.randint(1,10)
            if shadowObj.alive() == True:
                if heroObj.health <= 8:
                    choice = int(input(f"Your health is {heroObj.health} \nwould you like to purchase a Super Tonic?\n1. Yes\n2. No\n>"))
                    if choice == 1:
                        heroObj.supertonic()
                else:
                    pass
                if hit_chance == 1:
                    heroObj.attack(shadowObj)
                    print("--------------------------------")
                    shadowObj.print_status()
                else:
                    print("Your attacked missed!\n Try again!")
            else:
                print("Shadow is already dead. Attack someone else")

        elif raw_input == "4":
            outro_chance = random.randint(1, 5)
            if outro_chance == 1:
                print("--------------------------------")
                print("Dont act like you have better things to do! Youl be back!")
                print("--------------------------------")
                break
            elif outro_chance == 2:
                print("--------------------------------")
                print("How dare you leav so early?")
                print("--------------------------------")
                break
            elif outro_chance == 3:
                print("--------------------------------")
                print("Are you gonna cheat on me with another game?")
                print("--------------------------------")
                break
            elif outro_chance == 4:
                print("--------------------------------")
                print("Fine leave! Terrible user anyway!")
                print("--------------------------------")
                break
            elif outro_chance == 5:
                print("--------------------------------")
                print("NOOOOooooo dont turn me ooof...")
                print("--------------------------------")
                break
        else:
            print("Invalid input {}".format(raw_input))

    if heroObj.alive() == False:
        print("--------------------------------")
        print("You have died. Booo Hooo let me\nplay a sad tune on the smallest violin.")
        print("--------------------------------")

main()
