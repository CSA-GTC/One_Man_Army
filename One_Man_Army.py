
"""This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>. """


#Gregory Clarke
#Computer Programming
#5/14/2018

#all imports
import os
import time
import math
import random
import pygame

#all globals
global SCORE
global PHEALTH
global LHEALTH
global MHEALTH
global HHEALTH
global EHEALTH

#the globals defined
PHEALTH=100
LHEALTH=50
DHEALTH=60
MHEALTH=75
HHEALTH=90
CHEALTH=125
EHEALTH=150

pygame.mixer.init()
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.music.load("krackatoa_-_09_-_Mariachi_Bandits_of_Gatling_Gun_Ridge.mp3")
pygame.mixer.music.play(1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class Player: #player class. Contains all player related actions except for the decision to hide or attack
    def __init__(self,health):
        self.health=health
    
    def light_attack(self):
        print("""
    Enemy action: You lose 5 health
    """)
        self.new_health=self.health - 10
        return self.new_health
        
    def medium_attack(self):
        print("""
    Enemy action: You lose 15 health
    """)
        self.new_health=self.health - 25
        return self.new_health

    def heavy_attack(self):
        print("""
    Enemy action: You lose 30 health
    """)
        self.new_health=self.health - 40
        return self.new_health

    def miss(self):
        print("""
    Enemy action: The enemy misses
    """)
        self.new_health=self.health

    def check_life(self):
        if self.new_health <= 0:
            clear_screen()
            print("You have been killed. Your fathers soul wanders endlessly unavenged...")
            time.sleep(3)
            clear_screen()
            startup()
        else:
            print(self.new_health)
        
class Minion_class:
    def __init__(self,health):
        self.health=health
        
    def light_attack(self):
        print("""
    Your Action: The minion loses 10 health
    """)
        self.new_health=self.health - 10
        return self.new_health
    
    def medium_attack(self):
        print("""
    Your Action: The minion loses 25 health
    """)
        self.new_health=self.health - 25
        return self.new_health
    
    def heavy_attack(self):
        print("""
    Your Action: The minion loses 40 health
    """)
        self.new_health=self.health - 40
        return self.new_health
    
    def miss(self):
        print("""
    Your Action: You miss the minion
    """)
        self.new_health=self.health
    
    def check_life(self):
        if self.new_health <= 0:
            print("""
    Your Action: The minion is dead
    """)
            small_heal()
            clear_screen()
            second_enemy()
        else:
            print(self.new_health)


class Dealer_class:
    def __init__(self, health):
        self.health = health

    def light_attack(self):
        print("""
    Your Action: The dealer loses 10 health
    """)
        self.new_health = self.health - 10
        return self.new_health

    def medium_attack(self):
        print("""
    Your Action: The dealer loses 25 health
    """)
        self.new_health = self.health - 25
        return self.new_health

    def heavy_attack(self):
        print("""
    Your Action: The dealer loses 40 health
    """)
        self.new_health = self.health - 40
        return self.new_health

    def miss(self):
        print("""
    Your Action: You miss the dealer
    """)
        self.new_health = self.health

    def check_life(self):
        if self.new_health <= 0:
            print("""
    Your Action: The dealer is dead
    """)
            dealer_heal()
            clear_screen()
            third_enemy()
        else:
            print(self.new_health)
                        
class Soldier_class:
    
    def __init__(self,health):
        self.health=health
        
    def light_attack(self):
        print("""
    Your Action: The soldier loses 10 health
    """)
        self.new_health=self.health - 10
        return self.new_health
    
    def medium_attack(self):
        print("""
    Your Action: The soldier loses 25 health
    """)
        self.new_health=self.health - 25
        return self.new_health
    
    def heavy_attack(self):
        print("""
    Your Action: The soldier loses 40 health
    """)
        self.new_health=self.health - 40
        return self.new_health

    def miss(self):
        print("""
    Your Action: You miss the soldier
    """)
        self.new_health=self.health
    
    def check_life(self):
        if self.new_health <= 0:
            print("""
    Your Action: The soldier is dead
    """)
            medium_heal()
            clear_screen()
            fourth_enemy()
        else:
            print(self.new_health)

class Mercenary_class:
    
    def __init__(self,health):
        self.health=health
        
    def light_attack(self):
        print("""
    Your Action: The mercenary loses 10 health
    """)
        self.new_health=self.health - 10
        return self.new_health
    
    def medium_attack(self):
        print("""
    Your Action: The mercenary loses 25 health
    """)
        self.new_health=self.health - 25
        return self.new_health
    
    def heavy_attack(self):
        print("""
    Your Action: The mercenary loses 40 health
    """)
        self.new_health=self.health - 40
        return self.new_health

    def miss(self):
        print("""
    Your Action: You miss the mercenary
    """)
        self.new_health=self.health
    
    def check_life(self):
        if self.new_health <= 0:
            print("""
    Your Action: The mercenary is dead
    """)
            large_heal()
            clear_screen()
            fifth_enemy()
        else:
            print(self.new_health)

class Champion_class:
    def __init__(self, health):
        self.health = health

    def light_attack(self):
        print("""
    Your Action: The champion loses 10 health
    """)
        self.new_health = self.health - 10
        return self.new_health

    def medium_attack(self):
        print("""
    Your Action: The champion loses 25 health
    """)
        self.new_health = self.health - 25
        return self.new_health

    def heavy_attack(self):
        print("""
    Your Action: The champion loses 40 health
    """)
        self.new_health = self.health - 40
        return self.new_health

    def miss(self):
        print("""
    Your Action: You miss the champion
    """)
        self.new_health = self.health

    def check_life(self):
        if self.new_health <= 0:
            print("""
    Your Action: The champion is dead
    """)
            champion_heal()
            clear_screen()
            boss_enemy()
        else:
            print(self.new_health)

class Eddy:
    global PHEALTH
    
    def __init__(self,health,PHEALTH):
        self.health=health
        self.PHEALTH=PHEALTH
        
    def light_attack(self):
        print("""
    Your Action: Eduardo loses 10 health
    """)
        self.new_health=self.health - 10
        return self.new_health
    
    def medium_attack(self):
        print("""
    Your Action: Eduardo loses 25 health
    """)
        self.new_health=self.health - 25
        return self.new_health
    
    def heavy_attack(self):
        print("""
    Your Action: Eduardo loses 40 health
    """)
        self.new_health=self.health - 40
        return self.new_health

    def miss(self):
        print("""
    Your Action: You miss Eduardo
    """)
        self.new_health=self.health
    
    def check_life(self,PHEALTH):
        if self.new_health <= 0:
            clear_screen()
            print("...You've done it.....................................")
            time.sleep(2)
            print("..................he's dead...........................")
            time.sleep(2)
            print("............................your father is avenged....")
            time.sleep(2)
            clear_screen()
            print("You Won! Your Score was "+str(self.PHEALTH)+"!")
            score=self.PHEALTH
            score_append(score)
            PHEALTH=100
            time.sleep(2)
            startup()
        else:
            print(self.new_health)
            
def small_heal():
    global PHEALTH
    print("You gain 50 health for defeating the enemy")
    PHEALTH+=50
    time.sleep(2)
    
def dealer_heal():
    global PHEALTH
    print("You gain 60 health for defeating the enemy")
    PHEALTH+=60
    time.sleep(2)
    

def medium_heal():
    global PHEALTH
    print("You gain 75 health for defeating the enemy")
    PHEALTH+=75
    time.sleep(2)

def large_heal():
    global PHEALTH
    print("You gain 100 health for defeating the enemy")
    PHEALTH+=100
    time.sleep(2)

def champion_heal():
    global PHEALTH
    print("You gain 125 health for defeating the enemy")
    PHEALTH+=125
    time.sleep(2)
    
def score_append(score):
    with open("scores.txt","a") as scores:
        scores.write("\n")
        scores.write(str(score))

def main(): #This opens the file for the scores. If there is no file, it makes one and returns 'No Highscore'.
    try:        
        max_num = 0
        with open('scores.txt', 'r') as data: 
            for line in data.readlines(): # read the lines as a generator
                try:
                    val = int(line.split(",")[0])
                except ValueError:
                    val = 0
                if val > max_num: # logic
                    max_num = val
            return max_num #result
    except IOError:
        with open('scores.txt', 'w') as data:
            data.write(str(0))
        return "No Highscore"
def Minion():
    global LHEALTH
    global PHEALTH
    minion=Minion_class(LHEALTH)
    player1=Player(PHEALTH)
    print("""
The minion readys himself""")
    print("""
    1. Light Attack
    2. Medium Attack
    3. Heavy Attack
    """)
    new_in=input("What attack would you like to perform?: ")
    if new_in=="1":
        clear_screen()
        chance1=random.randint(1,4)
        if chance1 >=1 and chance1 <=3:
            minion.light_attack()
            LHEALTH=minion.new_health
        elif chance1==4:
            minion.miss()
        print("Minion health:")
        minion.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Minion()
    elif new_in=="2":
        clear_screen()
        chance1=random.randint(1,6)
        if chance1 >=1 and chance1 <=4:
            minion.medium_attack()
            LHEALTH=minion.new_health
        elif chance1==5 or chance1==6:
            minion.miss()
        print("Minion health:")
        minion.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Minion()
    elif new_in=="3":
        clear_screen()
        chance1=random.randint(1,8)
        if chance1 >=1 and chance1 <=3:
            minion.heavy_attack()
            LHEALTH=minion.new_health
        elif chance1 >=4 and chance1 <=8:
            minion.miss()
        print("Minion health:")
        minion.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Minion()
    else:
        print("Please enter '1','2', or '3'")
        Minion()

def Dealer():
    global DHEALTH
    global PHEALTH
    dealer=Dealer_class(DHEALTH)
    player1=Player(PHEALTH)
    print("""
The dealer readys himself""")
    print("""
    1. Light Attack
    2. Medium Attack
    3. Heavy Attack
    """)
    new_in=input("What attack would you like to perform?: ")
    if new_in=="1":
        clear_screen()
        chance1=random.randint(1,4)
        if chance1 >=1 and chance1 <=3:
            dealer.light_attack()
            DHEALTH=dealer.new_health
        elif chance1==4:
            dealer.miss()
        print("Dealer health:")
        dealer.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Dealer()
    elif new_in=="2":
        clear_screen()
        chance1=random.randint(1,6)
        if chance1 >=1 and chance1 <=4:
            dealer.medium_attack()
            DHEALTH=dealer.new_health
        elif chance1==5 or chance1==6:
            dealer.miss()
        print("Dealer health:")
        dealer.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Dealer()
    elif new_in=="3":
        clear_screen()
        chance1=random.randint(1,8)
        if chance1 >=1 and chance1 <=3:
            dealer.heavy_attack()
            DHEALTH=dealer.new_health
        elif chance1 >=4 and chance1 <=8:
            dealer.miss()
        print("Dealer health:")
        dealer.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Dealer()
    else:
        print("Please enter '1','2', or '3'")
        Dealer()
    
def Soldier():
    global MHEALTH
    global PHEALTH
    soldier=Soldier_class(MHEALTH)
    player1=Player(PHEALTH)
    print("""
The soldier readys himself""")
    print("""
    1. Light Attack
    2. Medium Attack
    3. Heavy Attack
    """)
    new_in=input("What attack would you like to perform?: ")
    if new_in=="1":
        clear_screen()
        chance1=random.randint(1,4)
        if chance1 >=1 and chance1 <=3:
            soldier.light_attack()
            MHEALTH=soldier.new_health
        elif chance1==4:
            soldier.miss()
        print("Soldier health:")
        soldier.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Soldier()
    elif new_in=="2":
        clear_screen()
        chance1=random.randint(1,6)
        if chance1 >=1 and chance1 <=4:
            soldier.medium_attack()
            MHEALTH=soldier.new_health
        elif chance1==5 or chance1==6:
            soldier.miss()
        print("Soldier health:")
        soldier.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Soldier()
    elif new_in=="3":
        clear_screen()
        chance1=random.randint(1,8)
        if chance1 >=1 and chance1 <=3:
            soldier.heavy_attack()
            MHEALTH=soldier.new_health
        elif chance1 >=4 and chance1 <=8:
            soldier.miss()
        print("Soldier health:")
        soldier.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Soldier()
    else:
        print("Please enter '1','2', or '3'")

def Mercenary():
    global HHEALTH
    global PHEALTH

    mercenary=Mercenary_class(HHEALTH)
    player1=Player(PHEALTH)
    print("""
The mercenary readys himself""")
    print("""
    1. Light Attack
    2. Medium Attack
    3. Heavy Attack
    """)
    new_in=input("What attack would you like to perform?: ")
    if new_in=="1":
        clear_screen()
        chance1=random.randint(1,4)
        if chance1 >=1 and chance1 <=3:
            mercenary.light_attack()
            HHEALTH=mercenary.new_health
        elif chance1==4:
            mercenary.miss()
        print("Mercenary health:")
        mercenary.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Mercenary()
    elif new_in=="2":
        clear_screen()
        chance1=random.randint(1,6)
        if chance1 >=1 and chance1 <=4:
            mercenary.medium_attack()
            HHEALTH=mercenary.new_health
        elif chance1==5 or chance1==6:
            mercenary.miss()
        print("Mercenary health:")
        mercenary.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4) 
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Mercenary()
    elif new_in=="3":
        clear_screen()
        chance1=random.randint(1,8)
        if chance1 >=1 and chance1 <=3:
            mercenary.heavy_attack()
            HHEALTH=mercenary.new_health
        elif chance1 >=4 and chance1 <=8:
            mercenary.miss()
        print("Mercenary health:")
        mercenary.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Mercenary()
    else:
        print("Please enter '1','2', or '3'")
        Mercenary()

def Champion():
    global CHEALTH
    global PHEALTH
    champion=Champion_class(CHEALTH)
    player1=Player(PHEALTH)
    print("""
The Champion readys herself""")
    print("""
    1. Light Attack
    2. Medium Attack
    3. Heavy Attack
    """)
    new_in=input("What attack would you like to perform?: ")
    if new_in=="1":
        clear_screen()
        chance1=random.randint(1,4)
        if chance1 >=1 and chance1 <=3:
            champion.light_attack()
            CHEALTH=champion.new_health
        elif chance1==4:
            champion.miss()
        print("Champion health:")
        champion.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Champion()
    elif new_in=="2":
        clear_screen()
        chance1=random.randint(1,6)
        if chance1 >=1 and chance1 <=4:
            champion.medium_attack()
            CHEALTH=champion.new_health
        elif chance1==5 or chance1==6:
            champion.miss()
        print("Champion health:")
        champion.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Champion()
    elif new_in=="3":
        clear_screen()
        chance1=random.randint(1,8)
        if chance1 >=1 and chance1 <=3:
            champion.heavy_attack()
            CHEALTH=champion.new_health
        elif chance1 >=4 and chance1 <=8:
            champion.miss()
        print("Champion health:")
        champion.check_life()
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Champion()
    else:
        print("Please enter '1','2', or '3'")
        Champion()

def Eddyuardo():
    global EHEALTH
    global PHEALTH
    eduardo=Eddy(EHEALTH,PHEALTH)
    player1=Player(PHEALTH)
    print("""
Eduardo readys himself""")
    print("""
    1. Light Attack
    2. Medium Attack
    3. Heavy Attack
    """)
    new_in=input("What attack would you like to perform?: ")
    if new_in=="1":
        clear_screen()
        chance1=random.randint(1,4)
        if chance1 >=1 and chance1 <=3:
            eduardo.light_attack()
            EHEALTH=eduardo.new_health
        elif chance1==4:
            eduardo.miss()
        print("Eduardo's health:")
        eduardo.check_life(PHEALTH)
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Eddyuardo()
    elif new_in=="2":
        clear_screen()
        chance1=random.randint(1,6)
        if chance1 >=1 and chance1 <=4:
            eduardo.medium_attack()
            EHEALTH=eduardo.new_health
        elif chance1==5 or chance1==6:
            eduardo.miss()
        print("Eduardo's health:")
        eduardo.check_life(PHEALTH)
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Eddyuardo()
    elif new_in=="3":
        clear_screen()
        chance1=random.randint(1,8)
        if chance1 >=1 and chance1 <=3:
            eduardo.medium_attack()
            EHEALTH=eduardo.new_health
        elif chance1 >=4 and chance1 <=8:
            eduardo.miss()
        print("Eduardo's health:")
        eduardo.check_life(PHEALTH)
        chance2=random.randint(1,3) #decides what attack the enemy uses
        if chance2==1:
            chance3=random.randint(1,4)
            if chance3 >=1 and chance3 <=3:
                player1.light_attack()
                PHEALTH=player1.new_health
            elif chance3==4:
                player1.miss()
        if chance2==2:
            chance3=random.randint(1,6)
            if chance3 >=1 and chance3 <=4:
                player1.medium_attack()
                PHEALTH=player1.new_health
            elif chance3==5 or chance3==6:
                player1.miss()
        if chance2==3:
            chance3=random.randint(1,8)
            if chance3 >=1 and chance3 <=3:
                player1.heavy_attack()
                PHEALTH=player1.new_health
            elif chance3>=4 and chance3 <=8:
                player1.miss()
        print("Your health:")
        player1.check_life()
        Eddyuardo()
    else:
        print("Please enter '1','2', or '3'")
        Eddyuardo()
   
def startup():
    global PHEALTH
    PHEALTH=100
    print("""
Highscore:
""")
    print(main())
    print("""
    1. Play
    2. Tutorial (recommended for first playthrough)
    3. Quit
    """)
    user_in=input("Choice: ")
    if user_in=="1":
        clear_screen()
        intro()
    elif user_in=="2":
        tutorial()
    elif user_in=="3":
        print("Quitting...")
        time.sleep(1)
        quit()
    else:
        print("Please enter either '1' or '2'")
        startup()

def intro(): # This function gives the player some lore and asks if they are ready to begin. If they continue to say "no" it will restart the game
    print("""
    Welcome to One Man Army! Your objective is to defeat
    the warlord Eduardo because he killed you father. You
    must either fight your way through his minions or sneak
    your way past them.
    """)
    
    print("Yes or No")
    User_input=input("Are you ready to begin?: ")
    if User_input.lower()== "yes":
        clear_screen()
        first_enemy()
    elif User_input.lower()=="no":
        print("Okay then")
        time.sleep(3)
        new_input=input("How about now?: ")
        if new_input.lower()=="yes":
            clear_screen()
            first_enemy()
        elif new_input.lower()== "no":
            print("Alright then...")
            clear_screen()
            time.sleep(2)
            startup()
    elif User_input=="1214":
        print("Aw, you special snowflake. Your the best!")
        time.sleep(2)
        clear_screen()
        intro()
    elif User_input.lower()=="cheats" or User_input.strip(" ").lower()=="cheatcodes":
        print("'Psst. Dont tell anyone, but there are more'")
        time.sleep(3)
        clear_screen()
        intro()
    elif User_input=="1860":
        print("Yes, hi Ammaar :D")
        time.sleep(1)
        clear_screen()
        intro()
    elif User_input.lower()=="davis":
        print("Yes, he is my favorite teacher")
        time.sleep(3)
        clear_screen()
        intro()
    elif User_input.lower()=="admin" or User_input.lower().strip=="adminmenu":
        print("Sorry, there is no admin command menu. Try Jacob's game.")
        time.sleep(3)
        clear_screen()
        intro()
    elif User_input.lower()=="upupdowndownleftrightleftrightbastart":
        print("Wow, it must have taken a while to write that. Sorry this is the wrong game for that one.")
        time.sleep(5)
        clear_screen()
        intro()
    else:
        print("Just answer yes or no please.")
        intro()

def tutorial():
    clear_screen()
    print("""
    In One Man Army, there are 5 enemies randomly generated before the
    final boss, varying in difficulty.

    As you encounter enemies, you will have the option to ATTACK or
    HIDE. Attacking can get you killed; however, hiding has the chance
    to go unsuccessfully. When hiding is unsuccessful, you must engage
    the enemy.
    
    You have 3 different attacks you can perform: Light attack, Medium
    attack, and Heavy attack.
        - Light attack: This attack has a high chance to do low damage.
        - Medium attack: This attack has a medium chance to do moderate
                         damage.
        - Heavy attack: This attack has a low chance to do high damage.

    Every time you defeat an enemy, you gain health equal to or greater
    than that of the enemy you defeated.

    At the end of the game, when you have defeated the boss, your health
    will be the final score you receive. The maximum score is 325.    
    """)
    user_in=input("When you are ready, enter '1': ")
    if user_in=="1":
        clear_screen()
        startup()
    else:
        print("Please enter '1'")
        time.sleep(1)
        clear_screen()
        tutorial()

def first_enemy():
    global PHEALTH
    global LHEALTH
    LHEALTH=50
    print("""
    You wake up in your hovel in Juarez, Mexico. Being poor, you have
    little; however, you hunger for vengeance. You will find a way to
    kill Eduardo.""")
    time.sleep(3)
    print("""
    You start your journey of retribution by walking the trail leading
    up to his fortress. As you are walking, you spot a teenage boy
    hardly younger than yourself. It's one of Eduardo's minions.
    """)
    time.sleep(3)
    print("Your Health: "+str(PHEALTH))
    print("ATTACK or HIDE?")
    user_input1=input("What do you do?: ")
    if user_input1.lower()=="attack":
        clear_screen()
        Minion()
        
    elif user_input1.lower()=="hide":
        chance1=random.randint(1,2)
        if chance1==1:
            clear_screen()
            print("As you crawl through bushes, a stick snaps underfoot and the minion is alerted.")
            time.sleep(4)
            clear_screen()
            Minion()
        elif chance1==2:
            print("You sneak around unnoticed")
            time.sleep(2)
            clear_screen()
            second_enemy()
    else:
        clear_screen()
        print("Please enter either 'attack' or 'hide'")
        first_enemy()

def second_enemy():
    global PHEALTH
    global DHEALTH
    DHEALTH=60
    print("""
    As you keep walking, you come upon a shady figure that seems 
    to be selling something to a local serf. This must be one of 
    Eduardo's team of drug dealers.
    """)
    time.sleep(3)
    print("Your Health: " + str(PHEALTH))
    print("ATTACK or HIDE?")
    user_input1 = input("What do you do?: ")
    if user_input1.lower() == "attack":
        clear_screen()
        Dealer()

    elif user_input1.lower() == "hide":
        chance1=random.randint(1,2)
        if chance1==1:
            clear_screen()
            print("The dealer recognizes you from the 'Eduardo's Exclusive Monthly' and prepares to fight.")
            time.sleep(4)
            clear_screen()
            Dealer()
        elif chance1==2:
            print("You sneak around unnoticed")
            time.sleep(2)
            clear_screen()
            third_enemy()
    else:
        clear_screen()
        print("Please enter either 'attack' or 'hide'")
        second_enemy()
    
def third_enemy():
    global PHEALTH
    global MHEALTH
    MHEALTH=75
    print("""
    You begin walking again. A while later, you spot another person
    standing in the road. This man looks to have been hardened by
    adversity. This is a soldier.
    """)
    time.sleep(3)
    print("Your Health: "+str(PHEALTH))
    print("ATTACK or HIDE?")
    user_input1=input("What do you do?: ")
    if user_input1.lower()=="attack":
        clear_screen()
        Soldier()
        
    elif user_input1.lower()=="hide":
        chance1=random.randint(1,2)
        if chance1==1:
            clear_screen()
            print("The costume you were using to avoid detection slips down to your ankles and exposes you (darn masking tape).")
            time.sleep(4)
            clear_screen()
            Soldier()
        elif chance1==2:
            print("You sneak around unnoticed")
            time.sleep(2)
            clear_screen()
            fourth_enemy()
    else:
        clear_screen()
        print("Please enter either 'attack' or 'hide'")
        third_enemy()

def fourth_enemy():
    global PHEALTH
    global HHEALTH
    HHEALTH=90
    print("""
    The day goes on as you progress up the trail. It's midday when
    you come upon another figure. By the way the man holds himself,
    you can tell he has killed many men in his lifetime and wouldn't
    hesitate to kill another. This is a mercenary of the inner ring
    assigned to Eduardo's personal protection.
    """)
    time.sleep(5)
    print("Your Health: "+str(PHEALTH))
    print("ATTACK or HIDE?")
    user_input1=input("What do you do?: ")
    if user_input1.lower()=="attack":
        clear_screen()
        Mercenary()
        
    elif user_input1.lower()=="hide":
        chance1=random.randint(1,2)
        if chance1==1:
            clear_screen()
            print("Unfortunately, this isn't Assassin's Creed, and the mercenary spots you through the crowd that you were trying to blend into.")
            time.sleep(5)
            clear_screen()
            Mercenary()
        elif chance1==2:
            print("You sneak around unnoticed")
            time.sleep(2)
            clear_screen()
            fifth_enemy()
    else:
        clear_screen()
        print("Please enter either 'attack' or 'hide'")
        fourth_enemy()

def fifth_enemy():
    global PHEALTH
    global CHEALTH
    CHEALTH=125
    print("""
    Shadows stretch across the ground as you tread up the trail. A
    small figure stands in your way and to your confusion, you see a
    young girl. The only thing to suggest that she wasn't a schoolgirl
    on her way home was the gauntlets strapped to her hands the
    deadpan look in her eyes.
    """)
    time.sleep(4)
    print("""
    You recognise her as the Champion, a famed and feared fighter who
    has killed men thrice her size. Her real name is Shaniqua, and she
    is from Louisiana, but you don't have time to ponder this as she
    seems to have sensed someting. Being Eduardo's Champion, she is
    trained to hunt and kill.
    """)
    time.sleep(4)
    print("Your Health: " + str(PHEALTH))
    print("ATTACK or HIDE?")
    user_input1 = input("What do you do?: ")
    if user_input1.lower() == "attack":
        clear_screen()
        Champion()

    elif user_input1.lower() == "hide":
        chance1=random.randint(1,3)
        if chance1==1 or chance1==2:
            clear_screen()
            print("""
Using her eagle vision, the Champion spots you as you run through the trees (she
also holds records in the 100 meter dash, so you don't outrun her).""")
            time.sleep(6)
            clear_screen()
            Champion()
        elif chance1==3:
            print("You sneak around unnoticed")
            time.sleep(2)
            clear_screen()
            boss_enemy()
    else:
        clear_screen()
        print("Please enter either 'attack' or 'hide'")
        fifth_enemy()

def boss_enemy():
    global PHEALTH
    global EHEALTH
    EHEALTH = 150
    print("""
    You arrive at the gate of Eduardo's fortress. There is only one
    thing left to do.
    """)
    print("Your Health: "+str(PHEALTH))
    print("ATTACK or WAIT?")
    user_input1=input("What do you do?: ")
    if user_input1.lower()=="attack":
        clear_screen()
        Eddyuardo()
        
    elif user_input1.lower()=="wait":
        print("You're ready. Seize your momment")
        time.sleep(1)
        clear_screen()
        boss_enemy()
    else:
        clear_screen()
        print("Please enter either 'attack' or 'wait'")
        boss_enemy()
    
startup()
