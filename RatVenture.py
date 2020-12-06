import sys
import pygame
import cmd 
import textwrap
import os 
import time 
import random
import pickle 
import re

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

    townMenu(option)

##### LOAD GAME FUNCTION #####
def resume():
    global player
    fileObject = open('player.txt','rb') 
    overwrite = pickle.load(fileObject)
    fileObject.close()   

    player.name = overwrite['Name'] 
    player.positionY = overwrite['positionY']
    player.positionX = overwrite['positionX']
    player.damage = overwrite['Damage']
    player.minDamage = overwrite['minDamage']
    player.maxDamage = overwrite['maxDamage']
    player.defence = overwrite['Defence']
    player.day = overwrite['Day']
    player.location = overwrite['location']
    player.hp = overwrite['HP']
    player.locationTag = overwrite['locationtag']

    townMenu(option) 

##### REST FUNCTION #####
def rest(option):
    player.hp = 20
    player.day += 1
    print('You are Fully Healed')
    townMenu(option)

#-------- Map --------#

# def map():
#     row = ''
#     for y in range(8):
#         print('+---+---+---+---+---+---+---+---+')
#         for x in range(8):
#             if player.positionX == x and player.positionY == y:
#                 if world_map[y][x] == ' ':
#                     row = row + '| H' + ' '
#                 else: 
#                     row = row + '|H/' + str(world_map[y][x]) + ''

#                 if world_map[y][x] == 'T':
#                     player.locationTag = 'T'
                
#                 elif world_map[y][x] == 'K':
#                     player.locationTag = 'K'

#                 elif world_map[y][x] == ' ':
#                     player.locationTag = ' '
#             else: 
#                 row = row + '| ' + str(world_map[x][y]) + ' '
#         print(row + '|')
#         row = ''
    
#     print('+---+---+---+---+---+---+---+---+')
#     print()

#     townMenu(a)

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
    townMenu(mainMenu_selection())

def mainMenu_selection():
    option = int(input("Enter your option: "))
    # if option == 1:
    #     # Display the town menu
    #     townMenu()
    # elif option == 2:
    #     # Loads the game
    #     print('do smth')
    # elif option == 3: 
    #     # Exits the game
    #     sys.exit()
    
    return option


#-------- Town Menu --------#

def townMenu(option):
    ### add incremental day ####

    if option == 1:
        print("\nDay {}: You are in town.".format(player.day))
        print("[1] View Character")
        print("[2] View Map")
        print("[3] Move")
        print("[4] Rest")
        print("[5] Save Game")
        print("[6] Exit Game")
        # Display the town menu
    elif option == 2:
        # Loads the game
        print('do smth')
    elif option == 3: 
        # Exits the game
        sys.exit()
    else: 
        print("Unknown option, please select 1-3.")
        

    townMenu_selection(option)

        
def townMenu_selection(option):

    action = input("Enter your option: ")
    acceptable_actions = ['1', '2', '3', '4', '5', '6']
    while action not in acceptable_actions:
        print("Unknown option, please select 1-6.")
        action = input("Enter your option: ")
    if action == '1':
        print(player.name, "\nDamage: {}\nDefence: {}\nHP: {}".format(player.damage, player.defence, player.hp))
        townMenu(option)
    elif action == '2': # Function to display map
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

        townMenu(option)
        #map()    
    elif action == '3': # Function to move
        print("do smth")
        townMenu(option)
    elif action == '4':  # Function to rest
        rest(option)
    elif action == '5':  # Function to save
        print("Game saved.")
        townMenu(option)
    elif action == '6': # Function to exit
        sys.exit()


    

### GAME FUNCTIONALITY ### 
def start_game():
    return

# Program starts here
mainMenu()