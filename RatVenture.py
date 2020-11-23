def menu():
    print("Welcome to RatVenture")
    print("-----------------------")
    print("[1] New Game")
    print("[2] Resume")
    print("[3] Exit")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        print("New game function")
        break
    elif option == 2:
        print("Resume game function")
        break
    elif option ==3:
        print("Thank you for playing, goodbye")
        break
    else:
        menu()
        option=int(input("Please enter a number between 1-3: "))
    
        


    
