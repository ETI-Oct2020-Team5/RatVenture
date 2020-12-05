import sys
import pygame
import cmd 
import textwrap
import os 
import time 
import random
import pickle

# def heroStats():
#     print("\nThe Hero")
#     print("Damage: 2-4")
#     print("Defence:1")
#     print("HP:20")

##### PLAYER SETUP #####
# class player: 
#     def __init__(self):
#         self.name = 'The Hero'
#         self.damage = '2-4'
#         self.defence = 1 
#         self.hp = 20
#         self.location = 'a1'
#         self.game_over = False
#     myPlayer = player()

##### RAT STATS #####
# class rat: 
#     def __init__(self):
#         self.name = 'Rat'
#         self.damage = '1-3'
#         self.defence = 1
#         self.hp = 10
#         self.location = 'a2' 
#     myEnemy = rat()

##### GAME INTERACTIVITY #####

##### MAIN MENU #####

def main_menu_selection():
    option = int(input("Enter your option: "))
    if option == 1:
        start_game()
        town_menu()
    elif option == 2:
        print('do smth')
        # resume_game()
    elif option == 3: 
        sys.exit()

def main_menu():
    os.system('cls')
    print("Welcome to RatVenture!")
    print("----------------------")
    print("[1] New Game")
    print("[2] Resume")
    print("[3] Exit")
    main_menu_selection()

##### TOWN MENU #####

def town_menu():
    ### add incremental day ####
    print("\nDay 1: You are in town.")
    print("[1] View Character")
    print("[2] View Map")
    print("[3] Move")
    print("[4] Rest")
    print("[5] Save Game")
    print("[6] Exit Game")
    town_menu_selection()

# def view_map():
#     print('\n' + ('#' + (4 + len(myPlayer.locaton))))

def town_menu_selection():
    action = input("Enter your option: ")
    acceptable_actions = ['1', '2', '3', '4', '5', '6']
    while action not in acceptable_actions:
        print("Unknown option, please select 1-6.")
        action = input("Enter your option: ")
    if action == '1':
        print("\nThe Hero")
        print("Damage: 2-4")
        print("Defence:1")
        print("HP:20")
        town_menu()
        action = input("Enter your option: ")
    elif action == '2': ### DISPLAY MAP ###
        print("do smth")
        town_menu()
    elif action == '3': ### MOVE ###
        print("do smth")
        town_menu()
    elif action == '4':  ### REST ###
        print("do smth")
        town_menu()
    elif action == '5':  ### SAVE ###
        print("do smth")
        town_menu()
    elif action == '6': ### EXIT ####
        sys.exit()


    

### GAME FUNCTIONALITY ### 
def start_game():
    return

# def main_game_loop():
#     while myPlayer.game_over is False: 
#         prompt_townMenu()

#main_game_loop()

main_menu()


    # option = ''

    # while option != '0':

    #     mainMenu()
    #     option = int(input("Enter your option: "))  
    #     if option == 1:
    #         townMenu()

    #         while option != '0': 
    #             if option == 1: 
    #                 heroStats()
    #                 option = int(input("Enter your option: "))   
    #                 break

    #             elif option == 2: 
    #                 map()
    #                 townMenu()
    #                 option = int(input("Enter your option: "))   
    #                 break
    #         break
    #     elif option == 2:
    #         print("Resume game function")
    #         break
    #     elif option == 3:
    #         print("Thank you for playing, goodbye")
    #         sys.exit()
    #         break
    #     else:
    #         menu()
    #         option=int(input("Please enter a number between 1-3: "))
    
        


    
