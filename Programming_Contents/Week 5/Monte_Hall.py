import random
import copy

gates_org = ['A', 'B', 'C']
player_name = input("What is your name? ")

def monte_hall_checking(gates, player_name):
    doors = copy.deepcopy(gates)

    trophy = random.choice(doors)

    print("Hi", player_name,"!\t Welcome to the Monte Hall Game!")
    print("You have three doors out of which only one gate contains the Trophy.\nFind it now ...\n")
    choice1 = input("Enter your choice of gate (A/B/C): ").upper()

    if choice1 == trophy:
        doors.remove(choice1)
        deceit = random.choice(doors)
        print("{} gate opened... There's no trophy!\n".format(deceit))
    else:
        if choice1 in doors:
            doors.remove(choice1)
            deceit = random.choice(doors)
            while deceit == trophy:
                deceit = random.choice(doors)
            print("The {} gate opened... There's no trophy!\n".format(deceit))
        else:
            print("Invalid Choice! Retry from start...\n")
            monte_hall_checking(gates_org, player_name)

    choice2 = input("Do you want to swap your previous choice (Y/N): ").upper()

    if choice2 == 'Y':
        if choice1 == trophy:
            print("The {} gate opened... There's no trophy!\nYou missed it.\n".format(deceit))
        else :
            print("The {} gate opened... There's the trophy!\nYou won it.\n".format(choice1))
    elif choice2 == 'N':
        if choice1 == trophy:
            print("The {} gate opened... There's the trophy!\nYou won it.\n".format(choice1))
        else:
            print("The {} gate opened... There's no trophy!\nYou missed it.\n".format(deceit))
    else:
        print("Invalid Choice! Retry from start...\n")
        monte_hall_checking(gates_org, player_name)

    playAgain = input("Do you want to play again?\n1. Yes\t\t 2. No\nEnter your choice : ")
    if playAgain == "1":
        monte_hall_checking(gates_org, player_name)
    else:
        print("Thank you for playing! Have a good day!")

monte_hall_checking(gates_org, player_name)