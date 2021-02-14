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

#-------- Saved Player Class --------#
class SavedPlayer:  # Player starts game with these stats
    def __init__(self):   # Defining parameters
        self.name = 'SavedData' #Default value of SavedData, will change when savegame function is called
        self.damage = 'SavedData' #Default value of SavedData, will change when savegame function is called
        self.minDamage = 2
        self.maxDamage = 4
        self.defence = 'SavedData' #Default value of SavedData, will change when savegame function is called
        self.hp = 'SavedData' #Default value of SavedData, will change when savegame function is called
        self.day = 'SavedData' #Default value of SavedData, will change when savegame function is called
        self.positionX = 0
        self.positionY = 0
        self.location = 'You are in a Town'
        self.locationTag = 'H'

    def is_alive(self): 
        return self.hp > 0

savedplayer = SavedPlayer()

#-------- Resumed Player Class --------#
class ResumePlayer:  # Player starts game with these stats
    def __init__(self):   # Defining parameters
        self.name = 'ResumeData' #Default value of ResumeData, will change when resumegame function is called
        self.damage = 'ResumeData' #Default value of ResumeData, will change when resumegame function is called
        self.minDamage = 2
        self.maxDamage = 4
        self.defence = 'ResumeData' #Default value of ResumeData, will change when resumegame function is called
        self.hp = 'ResumeData' #Default value of ResumeData, will change when resumegame function is called
        self.day = 'ResumeData' #Default value of ResumeData, will change when resumegame function is called
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
        self.minDamage = 1  #changed attribute name
        self.maxDamage = 3  #changed attribute name
        self.defence = 1
        self.hp = 8  
        self.location = 'a2'
    
rat = Rat()

class RatKing(object): 
    def __init__(self):
        self.name = 'Rat King'
        self.damage = '8-12'
        self.minDamage = 8  #changed attribute name
        self.maxDamage = 12  #changed attribute name
        self.defence = 5
        self.hp = 25 
        self.location = 'h8'
    
ratking = RatKing()

#--------- Resume Game Feature ---------#
def resumegame():
    #Attempt to read saveddata.csv file, if succeed, it will carry out the codes below
    try:
        with open("saveddata.csv",'r') as infile:
                reader = csv.reader(infile, delimiter=",") #Reading of csv file data
                header = next(reader)
                for row in reader: #Iterate through rows          
                    if row[5] != "Yes": #Check if save game status in csv file is not "Yes"
                        print("No saved data found, creating new one instead") #Error message shown
                        dataList=["The Hero", "2-4", "1", "20","1","No"] #Default player value dataList to write into csv
                        headerList=['Name','Damage','Defence','HP','Day','Saved'] #Default headers to write into csv
                        with open('saveddata.csv','w',newline="") as csvfile: #Open csv file to write into
                            writer=csv.writer(csvfile) 
                            writer.writerow(headerList) #Writing Data
                            writer.writerow(dataList) #Writing Data
                            csvfile.close() #Close csv file
                        resumeplayer.name == row[0] #Assign value to variable for resumeplayer
                        resumeplayer.damage ==row[1] #Assign value to variable for resumeplayer
                        resumeplayer.defence==row[2] #Assign value to variable for resumeplayer
                        resumeplayer.hp==row[3] #Assign value to variable for resumeplayer
                        resumeplayer.day==row[4] #Assign value to variable for resumeplayer
                        #Return value of resumeplayer for pytest checks
                        return(resumeplayer.name,resumeplayer.damage,resumeplayer.defence,resumeplayer.hp,resumeplayer.day)
                    else:
                        ##Return value of resumeplayer for pytest checks
                        return(resumeplayer.name,resumeplayer.damage,resumeplayer.defence,resumeplayer.hp,resumeplayer.day)
                        print("Saved data found, resuming game") #Success message
                        break #Break out of loop
    except: #If saveddata.csv is not found, this creates the file with the default player value and header
        dataList=["The Hero", "2-4", "1", "20","1","No"]
        headerList=['Name','Damage','Defence','HP','Day','Saved']
        with open('saveddata.csv','w',newline="") as csvfile: #Create csv called saveddata.csv and writes dataList and headerList
            writer=csv.writer(csvfile)
            writer.writerow(headerList)
            writer.writerow(dataList)
            csvfile.close() #Close csv
        print("No saved data file found, creating one now") #Print alternate success message


#-------- Exit game feature --------#
#This feature is used to reset all values to the original default value if the programme is closed completely
def exitgame():
    dataList=["The Hero", "2-4", "1", "20","1","No"] #Default player value
    headerList=['Name','Damage','Defence','HP','Day','Saved'] #Default header for csv
    with open('saveddata.csv','w',newline="") as csvfile: #Opens / creates (if file does not exist or has been deleted) saveddata.csv.
            writer=csv.writer(csvfile)
            writer.writerow(headerList) #Write headerList into csv
            writer.writerow(dataList) #Write dataList into csv
            csvfile.close() #Close csv
    
    sys.exit()

#-------- View Character feature --------#
def herostats():
    # Display hero stats and return hero stats
    stats = player.name + "\nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(player.damage, player.defence, player.hp, player.day)
    print(stats)
    return stats

#-------- Display Rat Stats --------#
def ratstats():
    # Display rat stats when encountered by one
    stats = "Damage: {}\nDefence: {}\nHP: {}".format(rat.damage, rat.defence, rat.hp)
    print(stats)
    return stats


#-------- View Map feature --------#
world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]

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
#------- New game -------#
def newgame():
    player.name = 'The Hero'
    player.damage = '2-4'
    player.minDamage = 2
    player.maxDamage = 4
    player.defence = 1
    player.hp = 20
    player.day = 1
    player.positionX = 0
    player.positionY = 0
    player.location = 'You are in a Town'
    player.locationTag = 'H'
    dataList=["The Hero", "2-4", "1", "20", "1","No"] #Default player value
    headerList=['Name','Damage','Defence','HP','Day','Saved'] #Default header for csv
    with open ("saveddata.csv",'r') as infile:
        reader = csv.reader(infile, delimiter=",")
        header = next(reader)
        for row in reader:

            if row[0] == "The Hero":
                with open('saveddata.csv','w',newline="") as csvfile: #Opens / creates (if file does not exist or has been deleted) saveddata.csv
                    writer = csv.writer(csvfile)
                    writer.writerow(headerList) #Write headerList into csv
                    writer.writerow(dataList) #Write dataList into csv
                    csvfile.close() #Close csv
                print("New game started")
            else:
                with open('saveddata.csv','w',newline="") as csvfile: #Create csv called saveddata.csv and writes dataList and headerList
                    writer=csv.writer(csvfile)
                    writer.writerow(headerList)
                    writer.writerow(dataList)
                    csvfile.close() #Close csv
                print("No saved data file found, creating one now") #Print alternate success message
#-------- Move feature --------#

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

# Modify Location based on Hero's Location
def modifyLocation():
    if player.locationTag == 'T':
        player.location = 'You are in Town'
    
    elif player.locationTag == 'K' or ' ':
        player.location = 'You are out in the Open'

# Movement input 
def movementInput():
    movementInput = input('Your Move: ') # Prompt user to input "W, A, S, D" to move 
    movementInput = movementInput.upper()
    acceptable_move_actions = ['W','A','S','D']
    while movementInput not in acceptable_move_actions:
        print('You have entered an invalid option. Enter "W", "A", "S" or "D" to move.')
        movementInput = input('Your Move: ') # Prompt user to input "W, A, S, D" to move 
        movementInput = movementInput.upper()
    else:
        if movementInput == 'W':
            moveUp()
        if movementInput == 'A':
            moveLeft()
        if movementInput == 'S':
            moveDown()
        if movementInput == 'D':
            moveRight()

# To move up 
def moveUp(): # W
    numList = [0,1,2,3,4,5,6,7] # The map has 8 grids and this is to ensure the hero does not move out of map
    player.positionY -= 1 
    if player.positionY < 0 and player.positionX in numList: # This prevents the hero from moving out of the map 
        player.positionY += 1
        player.day -= 1
        print('You are not allowed to move out of the map')
        print()
        updateLocation() # Updates the hero location in the map
        
    return (player.positionY, player.positionY+1)

# To move down
def moveDown(): # S
    numList = [0,1,2,3,4,5,6,7] # The map has 8 grids and this is to ensure the hero does not move out of map
    player.positionY += 1
    if player.positionY > 7 and player.positionX in numList: # This prevents the hero from moving out of the map 
        player.positionY -= 1
        player.day -= 1
        print('You are not allowed to move out of the map')
        print()
        updateLocation() # Updates the hero location in the map
    return (player.positionY, player.positionY-1)

# To move left 
def moveLeft(): # A
    numList = [0,1,2,3,4,5,6,7] # The map has 8 grids and this is to ensure the hero does not move out of map
    player.positionX -= 1
    if player.positionX < 0 and player.positionX not in numList: # This prevents the hero from moving out of the map 
        player.positionX += 1
        player.day -= 1
        print('You are not allowed to move out of the map')
        print()
        updateLocation() # Updates the hero location in the map
    return (player.positionX, player.positionX+1)

# To move right
def moveRight(): # D
    numList = [0,1,2,3,4,5,6,7] # The map has 8 grids and this is to ensure the hero does not move out of map
    player.positionX += 1
    if player.positionX > 7 and player.positionX not in numList: # This prevents the hero from moving out of the map 
        player.positionX -= 1
        player.day -= 1
        print('You are not allowed to move out of the map')
        print()
        updateLocation() # Updates the hero location in the map

    return (player.positionX, player.positionX-1)

# Call function to Move
def move():
        display_map() # Call function to print map 
        print('W = up; A = left; S = down; D = right')
        print()  
        player.day += 1 # Increments Day by 1

        movementInput() 


#-------- Rest feature --------#
def rest():
    player.hp = 20
    currentday = player.day
    player.day = player.day + 1
    print('You are Fully Healed')


    return player.hp, currentday, player.day

#-------- Save Game feature --------#
def savegame():
    savedplayer.name = player.name #Assign savedplayer.name with player.name for saving feature
    savedplayer.damage = player.damage #Assign savedplayer.damage with player.damage for saving feature
    savedplayer.defence = player.defence #Assign savedplayer.defence with player.defence for saving feature
    savedplayer.hp = player.hp #Assign savedplayer.hp with player.hp for saving feature
    savedplayer.day = player.day #Assign savedplayer.day with player.day for saving feature

    #dataList and headerList contains information in list to be written into csv to save and resume game.
    dataList=[savedplayer.name,savedplayer.damage,savedplayer.defence,savedplayer.hp, savedplayer.day, "Yes"]

    #Last column adds the value "Yes" under the header of "Saved" in csv. This is for resumegame() function validation
    headerList=['Name','Damage','Defence','HP','Day', 'Saved']

    #Reading saveddata.csv file if it exist and to write data into the csv file
    try:
        with open("saveddata.csv",'r') as infile:
            reader = csv.reader(infile, delimiter=",") #Reading of file data
            header =next(reader)
            for row in reader: #Iterates through the row of data
                playername=row[0]
                playerdamage=row[1]
                playerdefence=row[2]
                playerhp=row[3]
                if playername != null:
                    #Opens saveddata.csv to write
                    with open('saveddata.csv','w',newline="") as csvfile:
                        writer=csv.writer(csvfile)
                        writer.writerow(headerList)
                        writer.writerow(dataList)
                        csvfile.close() #Closes csv file
                        savedstats = savedplayer.name + "\nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(savedplayer.damage, 
                        savedplayer.defence, savedplayer.hp, savedplayer.day)
                        print("\nGame saved. Character stats: \n" + savedstats) #Success message printed
                        #Returns value for check with pytest
                        return (savedplayer.name, savedplayer.damage, savedplayer.defence, savedplayer.hp, savedplayer.day)
                        
                #If csv is new and there is no header / data, this writes the initial header and data.    
                elif playername == null:
                    with open('saveddata.csv','w',newline="") as csvfile: #Open csv file to write into
                        writer=csv.writer(csvfile)
                        writer.writerow(headerList)
                        writer.writerow(dataList)
                        csvfile.close() #Close csv file
                        savedstats = savedplayer.name + "\nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(savedplayer.damage, savedplayer.defence, savedplayer.hp, 
                        savedplayer.day)
                        #Success message and stats printed
                        print("\nGame saved. Character stats: \n" + savedstats)
                        #Value returned for check with pytest"
                        return (savedplayer.name, savedplayer.damage, savedplayer.defence, savedplayer.hp, savedplayer.day)
                else:
                    pass
    except:
        #If there is no csv file created at all or is accidentally deleted, 
        #this creates the csv file with the default player value written inside.
        with open('saveddata.csv','w',newline="") as csvfile: #This opens csv file to write into
            writer=csv.writer(csvfile)
            writer.writerow(headerList)
            writer.writerow(dataList)
            csvfile.close() #Closes csv file
            savedstats = savedplayer.name + "\nDamage: {}\nDefence: {}\nHP: {}\nDay: {}".format(savedplayer.damage, savedplayer.defence, savedplayer.hp, savedplayer.day)
            #Print success message and display stats
            print("\nGame saved. Character stats: \n" + savedstats)
            #Return values for pytest checks
            return (savedplayer.name, savedplayer.damage, savedplayer.defence, savedplayer.hp, savedplayer.day)
       
#-------- Run feature --------#
def run():

    print() # New Line
    print('You run and hide.')
    rat.hp = 8 # Restore the Rat's HP to full when player runs away
    openMenu() # To display the Open Menu 

#-------- Attack feature --------#
def attack ():
    while rat.hp > 0: 

        # Hero Damage Calculation 
        playerOriginalDamage = random.randint(player.minDamage, player.maxDamage) # Randomizing Hero's damage (2-4)
        playerFinalDamage = playerOriginalDamage - rat.defence # Hero's final damage = Hero's original damage after deducting Rat's defence
        rat.hp = rat.hp - playerFinalDamage # Deducting Rat's HP from Hero's final damage 

        # Rat Damage Calculation 
        ratOriginalDamage = random.randint(rat.minDamage, rat.maxDamage) # Randomizing Rat's damage (1-3)
        ratFinalDamage = ratOriginalDamage - player.defence # Rat's final damage = Hero's original damage after deducting Hero's defence
        player.hp = player.hp - ratFinalDamage # Deducting Player's HP from Rat's final damage

        print()
        print('You deal {} damage to the Rat'.format(playerFinalDamage)) # Print Final Damage dealt from Hero to Rat 
        print('Ouch! The Rat hit you for {} damage!'.format(ratFinalDamage)) # Print Final Damage dealt from Rat to Hero 
        print('You have {} HP left.'.format(player.hp)) # Print Hero's HP after taking damage

        print()

        if player.hp < 1: 
            print('You are dead')
            sys.exit() # End program once Hero is dead
        
        if rat.hp < 1: 
            print('The Rat is Dead. You are Victorious!') # Print victory message after killing the rat 
            print()
            rat.hp = 8 # New Rat's HP
            openMenu()

        break 

    return rat.hp, playerFinalDamage



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

def mainmenuuseroption():
    # Get user input in Main Menu and validate
    action = int(input("Enter choice: "))
    acceptable_actions=[1,2,3]
    while action not in acceptable_actions:
        print("Unknown option, please select 1-3.")
        action = int(input("Enter choice: "))
    else:
        pass
    # Return user input
    return action

def useroption():
    action = input("Enter choice: ")
    acceptable_actions = ['1', '2', '3', '4', '5', '6']
    while action not in acceptable_actions:
        print("Unknown option, please select 1-6.")
        action = input("Enter choice: ")
    else:
        pass
    return action

# def useroptiontownmenu():
#     action = input("Enter your option: ")
#     acceptable_actions=['1','2','3']
#     while action not in acceptable_actions:
#         print("Unknown option, please select 1-6.")
#         action = input("Enter your option: ")
#     else:
#         pass
#     return action


# def mainMenu_selection():
#     option = int(input("Enter your option: "))
#     # if option == 1:
#     #     # Display the town menu
#     #     townMenu()
#     # elif option == 2:
#     #     # Loads the game
#     #     print('do smth')
#     # elif option == 3: 
#     #     # Exits the game
#     #     sys.exit()
    
#     return option
   

def menu():
    print("\nDay {}: You are in town.".format(player.day))
    print("[1] View Character")
    print("[2] View Map")
    print("[3] Move")
    print("[4] Rest")
    print("[5] Save Game")
    print("[6] Exit Game")
    townMenu_selection()
#-------- Town Menu --------#

def townMenu(MMoption):
    ### add incremental day ####
    
    if MMoption == 1:
        
        newgame()
        menu()
        # Display the town menu
    elif MMoption == 2:
        # Loads the game
        resumegame()
        menu()
    elif MMoption == 3: 
        # Exits the game
        exitgame()
    # option = useroptiontownmenu()
    townMenu_selection()

def townmenuuseroption():
    # Get user input in Town Menu and validate
    action = int(input("Enter choice: "))
    acceptable_actions = [1, 2, 3, 4, 5, 6]
    while action not in acceptable_actions:
        print("Unknown option, please select 1-6.")
        action = int(input("Enter choice: "))
    else:
        pass
    # Return user input
    return action

def townMenu_selection():
    TMoption = townmenuuseroption()
    # action = input("Enter your option: ")
    acceptable_actions = [1, 2, 3, 4, 5, 6]
    while TMoption not in acceptable_actions:
        print("Unknown option, please select 1-6.")
    #   action = input("Enter your option: ")
        TMoption = townmenuuseroption()
    if TMoption == 1:
        print()
        herostats()
        menu()
    elif TMoption == 2:
        print()
        display_map() 
        menu()        
    elif TMoption == 3:
        print()
        move()
        display_map() # to display map after player has chosen to move
        modifyLocation()
        combatMenu()
        menu()
        # combatMenu() # to display combat menu 
    elif TMoption == 4:
        print()
        rest()
        menu()
    elif TMoption == 5:
        print()
        savegame()
        menu()
    elif TMoption == 6:
        mainMenu()
    
#------------------------ START OF NEW CODES  ------------------------#   
#-------- Combat Menu --------# 
def combatMenu():
    combatMenu_selection()

def combatMenu_selection():
    
    print()
    for y in range(8): 
        for x in range(8): # 'while loop' 
            if player.locationTag == ' ': # if player is out in the open
                print('Day {}:'.format(player.day),player.location) # to display day and location text
                print('Encounter! - Rat') 
                # To display Rat stats
                print('Damage: {}'.format(rat.damage))
                print('Defence: {}'.format(rat.defence))
                print('HP: {}'.format(rat.hp))
                print("1) Attack")
                print("2) Run")

                combatmenuuseroption()

            else: 
                menu()

def combatmenuuseroption():
    action = int(input('Enter choice: ')) # to prompt for user input
    while action not in [1,2]: # to validate user input 
        print('Please enter a valid option.')
        action = int(input('Enter choice: '))
    if action == 1:
        attack() # to call attack function
    if action == 2: 
        run() # to call run function

#-------- Open Menu --------# 
def openMenu():
    print('1) View Character')
    print('2) View Map')
    print('3) Move')
    print('4) Exit Game')

    openMenu_selection()

def openMenu_selection():
    OMoption = openmenuuseroption()

    if OMoption == 1:
        print() # New Line
        herostats()
        combatMenu() 
    if OMoption == 2: 
        print() # New Line
        display_map()
        print() # New Line
        combatMenu() 
    if OMoption == 3: 
        print() # New Line
        move()
        display_map() # to display map after player has chosen to move
        modifyLocation()
        print() # New Line
    if OMoption == 4: 
        exitgame()

def openmenuuseroption():
    # Get user input in Town Menu and validate
    action = int(input("Enter choice: "))
    acceptable_actions = [1, 2, 3, 4]
    while action not in acceptable_actions:
        print("Unknown option, please select 1-4.")
        action = int(input("Enter choice: "))
    else:
        pass
    # Return user input
    return action

#------------------------ END OF NEW CODES  ------------------------# 

# ##### GAME FUNCTIONALITY #####
# def start_game():
#     return

# Program starts here
mainMenu()
