import sys
import pygame
import cmd 
import textwrap
import os 
import time 
import random
import pickle 
import re

# MMOption = Main Menu Option
# TMOption = Town Menu Option

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

##### SAVE GAME FUNCTION ##### 
def save():
    outfile = open('player.txt','wb')
    pickle.dump(player, outfile)
    outfile.close()

    print('Game Saved.')

    townMenu()

##### LOAD GAME FUNCTION #####
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

    townMenu() 

##### REST FUNCTION #####
def rest(option):
    player.hp = 20
    player.day += 1
    print('You are Fully Healed')
    townMenu()

#-------- Map --------#

def map():
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

    townMenu()

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

    # Prompt for user input 
    mainMenu_selection()

def mainMenu_selection():
    option = int(input("Enter your option: "))
    acceptable_options = [1,2,3]
    while option not in acceptable_options:
        print("Unknown option, please select 1-3.")
        option = int(input("Enter your option: "))
    if option == 1:
        # Display the town menu
        townMenu()
    elif option == 2:
        # Loads the game
        resume()
    elif option == 3: 
        # Exits the game
        sys.exit()

#-------- Town Menu --------#

def townMenu():
    ### add incremental day ####
    print("\nDay {}: You are in town.".format(player.day))
    print("[1] View Character")
    print("[2] View Map")
    print("[3] Move")
    print("[4] Rest")
    print("[5] Save Game")
    print("[6] Exit Game")
    townMenu_selection()

        
def townMenu_selection():

    action = input("Enter your option: ")
    acceptable_actions = ['1', '2', '3', '4', '5', '6']
    while action not in acceptable_actions:
        print("Unknown option, please select 1-6.")
        action = input("Enter your option: ")
    if action == '1':
        print(player.name, "\nDamage: {}\nDefence: {}\nHP: {}".format(player.damage, player.defence, player.hp))
        townMenu()
    elif action == '2': # Function to display map
        map()    
    elif action == '3': # Function to move
        print("do smth")
        townMenu()
    elif action == '4':  # Function to rest
        rest()
        townMenu()
    elif action == '5':  # Function to save
        save()
        townMenu()
    elif action == '6': # Function to exit
        sys.exit()


# Program starts here
mainMenu()
  
        


    

  
        


    
