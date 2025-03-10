import random

def greeting():
    player1_name = input("Player-1, What is your name? ")
    print("Hello, " + player1_name + "! Welcome to the Snake & Ladder Game!\n")
    player2_name = input("Player-2, What is your name? ")
    print("Hello, " + player2_name + "! Welcome to the Snake & Ladder Game!\n")
    print("Rules and Regulations : ")
    print("1. You can choose between roll dice and surrender.")
    print("2. Ladder helps you jumping to higher position. Snake pulls you down to lower position.")
    print("3. One who reaches the end wins the game. If someone quits, other player wins also.")
    print("Let's start!\n")
    return player1_name, player2_name


def display(pos, players):
    nums = [[10 * j + i for i in range(1, 11)] for j in range(10)]
    for i in range(10):
        if i != 9:
            nums[0][i] = str(nums[0][i])+" "
        if i % 2 != 0:
            nums[i] = nums[i][::-1]

    ladder_list = [(0, 3), (1, 7), (3, 7), (4, 1), (4, 9), (6, 1), (7, 6)]
    snake_list = [(9, 1), (8, 8), (7, 4), (6, 5), (5, 6), (4, 2), (3, 0), (2, 6)]

    for element in ladder_list:
        nums[element[0]][element[1]] = "\033[1;32;40m" + str(nums[element[0]][element[1]]) + "\033[0m"
    for element in snake_list:
        nums[element[0]][element[1]] = "\033[1;31;40m" + str(nums[element[0]][element[1]]) + "\033[0m"

    print(" Board Status :\t\t" + "Positions -\t\033[0;35;40m", players[0], ":", pos[0], "\033[0m\t\033[0;36;40m", players[1], ":", pos[1], "\033[0m\n")
    print("  " + "-" * 119)
    for i in range(10):
        print("|\t", " \t|\t ".join(map(str, nums[len(nums) - 1 - i])), "\t|\t")
        print("  " + "-" * 119)


def roll_dice():
    print("Rolling dice...")
    val = random.randint(1, 6)
    print("The dice rolled is: ", val)
    return val


ladders = {4: 13, 25: 46, 33: 49, 42: 63, 50: 69, 62: 81, 74: 92}
snakes = {27: 5, 40: 3, 43: 18, 54: 31, 66: 45, 76: 58, 89: 53, 99: 41}

def ladder_snake_checker(pre_pos):
    if pre_pos in ladders:
        print("You got ladder! 🎯")
        return ladders[pre_pos]
    elif pre_pos in snakes:
        print("You got bitten by snake! 🐍")
        return snakes[pre_pos]
    return pre_pos


def action_control(players, pos, status):
    player_stat = [False, False]

    for i in range(2):
        print(players[i], " : Your Turn")
        while True:
            try:
                choice = int(input("What do you want to do?\n1. Roll dice\t2. Surrender\nEnter your choice (1/2): "))
                if choice in [1, 2]:
                    break
                print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if choice == 1:
            dice = roll_dice()
            pos[i] += dice
            pos[i] = ladder_snake_checker(pos[i])
            print("You moved to ", pos[i], ".")
        else:
            status = True
            player_stat[1 - i] = True

        if pos[i] >= 100:
            status = True
            player_stat[i] = True

    return status, player_stat


def conclusion(players, player_stat):
    print("\nGame Over!")
    if player_stat[0]:
        print(players[0], "wins!")
    elif player_stat[1]:
        print(players[1], "wins!")


def gamePlay():
    players = greeting()
    pos = [0, 0]
    display(pos, players)
    status = False

    while not status:
        status, player_stat = action_control(players, pos, status)
        display(pos, players)

    conclusion(players, player_stat)

    playAgain = input("Do you want to play again?\n1. Yes\t2. No\nEnter your choice: ")
    if playAgain == "1":
        gamePlay()
    else:
        print("Thank you for playing! Have a great day!")


gamePlay()