import sys
import pygame
import cmd 
import textwrap
import os 
import time 
import random
import pickle 
import re

# MM_Option = Main Menu Option
# TM_Option = Town Menu Option

# Map Layout    
world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]

##### CLASSES #####

#-------- Player Class --------#
class Player:  # Player starts game with these stats
    def __init__(self):   # Defining parameters
        self.name = 'The Hero'
        self.damage = '2-4'
        self.minDamage = 2
        self.maxDamage = 4
        self.defence = 1
        self.hp = 20
        self.day = 1
        self.positionX = 0
        self.positionY = 0
        self.location = 'You are in a Town'
        self.locationTag = 'H'

    def is_alive(self): 
        return self.hp > 0

player = Player()

#-------- Rat Class --------#
class Rat(object): 
    def __init__(self):
        self.name = 'Rat'
        self.damage = '1-3'
        self.damage_min = 1 
        self.damage_max = 3
        self.defence = 1
        self.hp = 8 
        self.location = 'a2'
    
rat = Rat()

#-------- View Character --------#
# View Character Function
def viewChar(TM_Option):
    if TM_Option == '1':
        print()
        print(player.name, "\nDamage: {}\nDefence: {}\nHP: {}".format(player.damage, player.defence, player.hp))
        townMenu()

#-------- Move --------#

# Update Player's Location 
def updateLocation():
    for y in range(8):
        for x in range(8):
            if player.positionX == x and player.positionY == y:
                if world_map[y][x] == 'T':
                    player.locationTag == 'T'
                elif world_map[y][x] == 'K':
                    player.locationTag == 'K'
                elif world_map[y][x] == ' ':
                    player.locationTag == ' '

# Move Function
def move(TM_Option):
    if TM_Option == '3':
        map('2') # Call function to print map 
        print('W = up; A = left; S = down; D = right')
        print()
        movementInput = input('Your Move: ') # Prompt user to input "W, A, S, D" to move 
        movementInput = movementInput.upper()  
        player.day += 1 # Increments Day by 1

        numList = [0,1,2,3,4,5,6,7]
        if movementInput == 'W':
            player.positionY -= 1
            if player.positionY < 0 and player.positionX in numList:
                player.positionY += 1
                player.day -= 1
                print('You are not allowed to move out of the map')
                print()
                updateLocation()

        if movementInput == 'A':
            player.positionX += 1
            if player.positionX < 0 and player.positionY in numList:
                player.positionY += 1
                player.day -= 1
                print('You are not allowed to move out of the map')
                print()
                updateLocation()

        if movementInput == 'S':
            player.positionY += 1
            if player.positionY > 7 and player.positionX in numList:
                player.positionY += 1
                player.day -= 1
                print('You are not allowed to move out of the map')
                print()
                updateLocation()

        if movementInput == 'D':
            player.positionX += 1
            if player.positionY > 7 and player.positionX in numList:
                player.positionY += 1
                player.day -= 1
                print('You are not allowed to move out of the map')
                print()
                updateLocation()

    townMenu()

#-------- View Map --------#
# Map Function 
def map(TM_Option):
    if TM_Option == '2':
        row = ''
        for y in range(8):
            print('+---+---+---+---+---+---+---+---+')
            for x in range(8):
                if player.positionX == x and player.positionY == y:
                    if world_map[y][x] == ' ':
                        row = row + '| H' + ' '
                    else: 
                        row = row + '|H/' + str(world_map[y][x]) + ''

                    if world_map[y][x] == 'T':
                        player.locationTag = 'T'
                    
                    elif world_map[y][x] == 'K':
                        player.locationTag = 'K'

                    elif world_map[y][x] == ' ':
                        player.locationTag = ' '
                else: 
                    row = row + '| ' + str(world_map[x][y]) + ' '
            print(row + '|')
            row = ''
        
        print('+---+---+---+---+---+---+---+---+')
        print()

#-------- Rest --------#
# Function to allow player to rest
def rest(TM_Option):
    if TM_Option == '4':
        player.hp = 20
        player.day += 1
        print('You are Fully Healed')
        townMenu()

#-------- Save --------#
# Function to save game
# def save(TM_Option):
#     if TM_Option == '5':
#         outfile = open('player.txt','wb')
#         pickle.dump(player, outfile)
#         outfile.close()

#     print('Game Saved.')

#     townMenu()

#-------- Load --------#
# Function to resume game state
def resume():
    global player
    fileObject = open('player.txt','rb') 
    overwrite = pickle.load(fileObject)
    fileObject.close()   

    player.name = overwrite[player.name]
    player.positionY = overwrite[player.positionY]
    player.positionX = overwrite[player.positionX]
    player.damage = overwrite[player.damage]
    player.minDamage = overwrite[player.minDamage]
    player.maxDamage = overwrite[player.maxDamage]
    player.defence = overwrite[player.defence]
    player.day = overwrite[player.day]
    player.location = overwrite[player.location]
    player.hp = overwrite[player.hp]
    player.locationTag = overwrite[player.locationTag]

    townMenu(option) 

#-------- Exit --------#
# Function to exit game
def exit(TM_Option):
    if TM_Option == '6':
        sys.exit()

##### GAME INTERACTIVITY #####

#-------- Main Menu --------#

def mainMenu():
    # Clears the terminal for the game to start
    os.system('cls')

    print("Welcome to RatVenture!")
    print("----------------------")
    print("[1] New Game")
    print("[2] Resume")
    print("[3] Exit")

    MM_Option = int(input("Enter your option: "))

    # Prompt for user input 
    mainMenu_selection(MM_Option)

def mainMenu_selection(MM_Option):
    acceptable_options = [1,2,3]
    while MM_Option not in acceptable_options:
        print("Unknown option, please select 1-3.")
        MM_Option = int(input("Enter your option: "))
    if MM_Option == 1:
        # Display the town menu
        townMenu()
    elif MM_Option == 2:
        # Loads the game
        resume()
    elif MM_Option == 3: 
        # Exits the game
        sys.exit()


#-------- Town Menu --------#

def townMenu():
    print("\nDay {}: You are in town.".format(player.day))
    print("[1] View Character")
    print("[2] View Map")
    print("[3] Move")
    print("[4] Rest")
    print("[5] Save Game")
    print("[6] Exit Game")
    
    TM_Option = input("Enter your option: ")

    townMenu_selection(TM_Option)

        
def townMenu_selection(TM_Option):
    acceptable_actions = ['1', '2', '3', '4', '5', '6']
    while TM_Option not in acceptable_actions:
        print("Unknown option, please select 1-6.")
        TM_Option = input("Enter your option: ")
    if TM_Option == '1':
        viewChar(TM_Option)
    elif TM_Option == '2': # Function to display map
        map(TM_Option)  
        townMenu()  
        print()
    elif TM_Option == '3': # Function to move
        move(TM_Option)
        print()
    elif TM_Option == '4':  # Function to rest
        rest(TM_Option)
    elif TM_Option == '5':  # Function to save
        #save(TM_Option)
        print()
    elif TM_Option == '6': # Function to exit
        exit(TM_Option)
    

# Program starts here
mainMenu()