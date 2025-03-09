import numpy as np

symbol_1 = "X"
symbol_2 = "O"

def greeting():
    player1_name = input("Player-1, What is your name? ")
    print("Hello, " + player1_name + "! Welcome to the Tic-Tac-Toe Game... Your symbol is 'X'!\n")
    player2_name = input("Player-2, What is your name? ")
    print("Hello, " + player2_name + "! Welcome to the Tic-Tac-Toe Game... Your symbol is 'O'!\n")
    print("Rules and Regulations : ")
    print("1. Column and Row indices are 0,1,2 respectively.")
    print("2. Only enter your choice at valid locations.")
    print("3. Three consecutive symbols in any direction win the game.")
    print("Let's start!\n")
    return player1_name, player2_name

def display(place_holder):
    print("\n    0   1   2 ")
    print("  -------------")
    for i in range(3):
        print(i, "|", " | ".join(place_holder[i]), "|")
        print("  -------------")
    print("\n")

def action_control(place_holder, players, turn, status):
    global symbol_1, symbol_2
    position = [0, 0]

    print(players[0], " : Turn-" + str(turn), "\n")
    display(place_holder)
    position[0] = int(input("Enter your row choice (0/1/2): "))
    position[1] = int(input("Enter your column choice (0/1/2): "))
    update(place_holder, position, symbol_1)

    if check(place_holder):
        return True, (True, False), place_holder

    print(players[1], " : Turn-" + str(turn), "\n")
    display(place_holder)
    position[0] = int(input("Enter your row choice (0/1/2): "))
    position[1] = int(input("Enter your column choice (0/1/2): "))
    update(place_holder, position, symbol_2)

    if check(place_holder):
        return True, (False, True), place_holder

    contains_dash = np.any(place_holder == "-")
    if not contains_dash:
        status = True

    return status, (False, False), place_holder

def update(place_holder, position, symbol):
    if place_holder[position[0]][position[1]] == "-":
        place_holder[position[0]][position[1]] = symbol
    else:
        print("Invalid move! This spot is already taken. Try again.")

def check(place_holder):
    global symbol_1, symbol_2

    for row in place_holder:
        if np.all(row == symbol_1):
            return True
        if np.all(row == symbol_2):
            return True

    for col in place_holder.T:
        if np.all(col == symbol_1):
            return True
        if np.all(col == symbol_2):
            return True

    if np.all(np.diag(place_holder) == symbol_1) or np.all(np.diag(np.fliplr(place_holder)) == symbol_1):
        return True
    if np.all(np.diag(place_holder) == symbol_2) or np.all(np.diag(np.fliplr(place_holder)) == symbol_2):
        return True

    return False

def conclusion(players, player_stat):
    print("\nGame Over!")
    if player_stat[0]:
        print(players[0], "wins!")
    elif player_stat[1]:
        print(players[1], "wins!")
    else:
        print("It's a draw!")

def gamePlay():
    place_holder = np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])
    players = greeting()
    display(place_holder)
    status = False
    turn = 0

    while not status:
        turn += 1
        status, player_stat, place_holder = action_control(place_holder, players, turn, status)

    conclusion(players, player_stat)

    playAgain = input("Do you want to play again?\n1. Yes\t2. No\nEnter your choice: ")
    if playAgain == "1":
        gamePlay()
    else:
        print("Thank you for playing! Have a great day!")

gamePlay()