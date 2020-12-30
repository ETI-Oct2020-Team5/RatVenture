import sys
import pygame
import cmd 
import textwrap
import os 
import time 
import random
import pickle 

import csv
from random import randint

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

#--------Saved Player Class --------#
class SavedPlayer:  # Player starts game with these stats
    def __init__(self):   # Defining parameters
        self.name = 'SavedData'
        self.damage = 'SavedData'
        self.minDamage = 2
        self.maxDamage = 4
        self.defence = 'SavedData'
        self.hp = 'SavedData'
        self.day = 'SavedData'
        self.positionX = 0
        self.positionY = 0
        self.location = 'You are in a Town'
        self.locationTag = 'H'

    def is_alive(self): 
        return self.hp > 0

savedplayer = SavedPlayer()

#--------Resumed Player Class --------#
class ResumePlayer:  # Player starts game with these stats
    def __init__(self):   # Defining parameters
        self.name = 'ResumeData'
        self.damage = 'ResumeData'
        self.minDamage = 2
        self.maxDamage = 4
        self.defence = 'ResumeData'
        self.hp = 'ResumeData'
        self.day = 'ResumeData'
        self.positionX = 0
        self.positionY = 0
        self.location = 'You are in a Town'
        self.locationTag = 'H'

    def is_alive(self): 
        return self.hp > 0

resumeplayer = ResumePlayer()

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

#-------Save Game-------#
def savegame():
    savedplayer.name = player.name
    savedplayer.damage = player.damage
    savedplayer.defence = player.defence
    savedplayer.hp = player.hp
    savedplayer.day = player.day

    dataList=[savedplayer.name,savedplayer.damage,savedplayer.defence,savedplayer.hp, savedplayer.day, "Yes"]
    headerList=['Name','Damage','Defence','HP','Day', 'Saved']

    try:
        with open("saveddata.csv",'r') as infile:
            reader = csv.reader(infile, delimiter=",")
            header =next(reader)
            for row in reader:
                playername=row[0]
                playerdamage=row[1]
                playerdefence=row[2]
                playerhp=row[3]
                if playername != null:
                    
                    with open('saveddata.csv','w',newline="") as csvfile:
                        writer=csv.writer(csvfile)
                        writer.writerow(headerList)
                        writer.writerow(dataList)
                        csvfile.close()
                        #print("Game saved successfully")
                        savedstats = savedplayer.name + "\nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(savedplayer.damage, savedplayer.defence, savedplayer.hp, savedplayer.day)
                        print("\nGame saved. Character stats: \n" + savedstats)
                        #return savedstats
                        return (savedplayer.name, savedplayer.damage, savedplayer.defence, savedplayer.hp, savedplayer.day)
                        
                    
                elif playername == null:
                    with open('saveddata.csv','w',newline="") as csvfile:
                        writer=csv.writer(csvfile)
                        writer.writerow(headerList)
                        writer.writerow(dataList)
                        csvfile.close()
                        #print("Game saved successfully")
                        savedstats = savedplayer.name + "\nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(savedplayer.damage, savedplayer.defence, savedplayer.hp, savedplayer.day)
                        print("\nGame saved. Character stats: \n" + savedstats)
                        #return savedstats
                        return (savedplayer.name, savedplayer.damage, savedplayer.defence, savedplayer.hp, savedplayer.day)
                else:
                    pass
    except:
        
        with open('saveddata.csv','w',newline="") as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(headerList)
            writer.writerow(dataList)
            csvfile.close()
            #print("Game saved successfully")
            savedstats = savedplayer.name + "\nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(savedplayer.damage, savedplayer.defence, savedplayer.hp, savedplayer.day)
            print("\nGame saved. Character stats: \n" + savedstats)
            #return savedstats
            return (savedplayer.name, savedplayer.damage, savedplayer.defence, savedplayer.hp, savedplayer.day)


def resumegame():
    try:
        with open("saveddata.csv",'r') as infile:
                reader = csv.reader(infile, delimiter=",")
                header =next(reader)
                for row in reader:          
                    if row[5] != "Yes":
                        print("No saved data found, creating new one instead")
                        dataList=["The Hero", "2-4", "1", "20","1","No"]
                        headerList=['Name','Damage','Defence','HP','Day','Saved']
                        with open('saveddata.csv','w',newline="") as csvfile:
                            writer=csv.writer(csvfile)
                            writer.writerow(headerList)
                            writer.writerow(dataList)
                            csvfile.close()
                        resumeplayer.name == row[0]
                        resumeplayer.damage ==row[1]
                        resumeplayer.defence==row[2]
                        resumeplayer.hp==row[3]
                        resumeplayer.day==row[4]
                        return(resumeplayer.name,resumeplayer.damage,resumeplayer.defence,resumeplayer.hp,resumeplayer.day)
                    else:
                        return(resumeplayer.name,resumeplayer.damage,resumeplayer.defence,resumeplayer.hp,resumeplayer.day)
                        print("Saved data found, resuming game")
                        break
    except:
        dataList=["The Hero", "2-4", "1", "20","1","No"]
        headerList=['Name','Damage','Defence','HP','Day','Saved']
        with open('saveddata.csv','w',newline="") as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(headerList)
            writer.writerow(dataList)
            csvfile.close()
        print("No saved data file found, creating one now")
        
                        
    
    




def exitgame():
    dataList=["The Hero", "2-4", "1", "20","1","No"]
    headerList=['Name','Damage','Defence','HP','Day','Saved']
    with open('saveddata.csv','w',newline="") as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(headerList)
            writer.writerow(dataList)
            csvfile.close()
    
    sys.exit()

##### REST FUNCTION #####
def rest():
    player.hp = 20
    currentday = player.day
    player.day = player.day + 1
    print('You are Fully Healed')


    return player.hp, currentday, player.day

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

    # Prompt for user input and display appropriate menu
    useroption = mainmenuuseroption()
    townMenu(useroption)

def townmenuuseroption():
    # Get user input in Town Menu and validate
    action = int(input("Enter your option: "))
    acceptable_actions = [1, 2, 3, 4, 5, 6]
    while action not in acceptable_actions:
        print("Unknown option, please select 1-6.")
        action = int(input("Enter your option: "))
    else:
        pass
    # Return user input
    return action

def mainmenuuseroption():
    # Get user input in Main Menu and validate
    action = int(input("Enter your option: "))
    acceptable_actions=[1,2,3]
    while action not in acceptable_actions:
        print("Unknown option, please select 1-3.")
        action = int(input("Enter your option: "))
    else:
        pass
    # Return user input
    return action

def herostats():
    # Display hero stats and return hero stats
    stats = player.name + "\nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(player.damage, player.defence, player.hp, player.day)
    print(stats)
    return stats



def useroption():
    action = input("Enter your option: ")
    acceptable_actions = ['1', '2', '3', '4', '5', '6']
    while action not in acceptable_actions:
        print("Unknown option, please select 1-6.")
        action = input("Enter your option: ")
    else:
        pass
    return action
def useroptiontownmenu():
    action = input("Enter your option: ")
    acceptable_actions=['1','2','3']
    while action not in acceptable_actions:
        print("Unknown option, please select 1-6.")
        action = input("Enter your option: ")
    else:
        pass
    return action



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

def display_map():
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
    
    

    #map()    


#-------- Town Menu --------#

def townMenu(MMoption):
    ### add incremental day ####
    
    if MMoption == 1:
        print("\nDay {}: You are in town.".format(player.day))
        print("[1] View Character")
        print("[2] View Map")
        print("[3] Move")
        print("[4] Rest")
        print("[5] Save Game")
        print("[6] Exit Game")
        # Display the town menu
    elif MMoption == 2:
        # Loads the game
        resumegame()
        townMenu(1)
    elif MMoption == 3: 
        # Exits the game
        exitgame()
    # option = useroptiontownmenu()
    townMenu_selection()


def townMenu_selection():
    TMoption = townmenuuseroption()
    # action = input("Enter your option: ")
    acceptable_actions = [1, 2, 3, 4, 5, 6]
    while TMoption not in acceptable_actions:
        print("Unknown option, please select 1-6.")
    #   action = input("Enter your option: ")
        TMoption = townmenuuseroption()
    if TMoption == 1:
        herostats()
        townMenu(1)
    elif TMoption == 2:
        display_map()
        townMenu(1)        
    elif TMoption == 3:
        print("do smth")
    elif TMoption == 4:
        rest()
        townMenu(1)
    elif TMoption == 5:
        savegame()
        townMenu(1)
    elif TMoption == 6:
        mainMenu()
        
        
        
    # elif action == '2': # Function to display map
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
    #     townMenu(1)
    #     print()

    #     #map()    
    # elif action == '3': # Function to move
    #     print("do smth")
    #     townMenu(1)
    # elif action == '4':  # Function to rest
    #     print("You are fully healed")
    #     townMenu(1)
    # elif action == '5':  # Function to save
    #     print("Game saved.")
    #     townMenu(1)
    # elif action == '6': # Function to exit
    #     sys.exit()

def townMenu_selection1():
    herostats()
    return (player.name + "\nDamage: {}\nDefence: {}\nHP: {}".format(player.damage, player.defence, player.hp))
    
##### SAVE GAME FUNCTION ##### 
### GAME FUNCTIONALITY ### 
def start_game():
    return

# # Program starts here
#mainMenu()

