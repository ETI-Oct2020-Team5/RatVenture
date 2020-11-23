import sys

def mainMenu():
    print("Welcome to RatVenture!")
    print("----------------------")
    print("[1] New Game")
    print("[2] Resume")
    print("[3] Exit")

def townMenu():
    print("Day 1: You are in town. \n"
            "[1] View Character \n" 
            "[2] View Map \n"
            "[3] Move \n"
            "[4] Rest \n"
            "[5] Save Game \n"
            "[6] Exit Game \n\n")

def heroStats():
    print("The Hero \n"
            "Damage: 2-4 \n"
            "Defence:1 \n"
            "HP:20")

mainMenu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        townMenu()
        option = int(input("Enter your option: "))   

        while option != 0: 
            if option == 1: 
                heroStats()
                option = int(input("Enter your option: "))   
                break

            elif option == 2: 
                print('map')
                break
        break
    elif option == 2:
        print("Resume game function")
        break
    elif option == 3:
        print("Thank you for playing, goodbye")
        sys.exit()
        break
    else:
        menu()
        option=int(input("Please enter a number between 1-3: "))
    
        


    
