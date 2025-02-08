import random

word_list = ["THUNDER", "EXTRAVAGANT","VIGILANT","PARASITE","JOKER","CURIOUS","SINCERITY","AVIATION","MINIONS","OSCILLATION"]

def get_random_word(word_list):
    return random.choice(word_list)

def jumble(word):
    temp = random.sample(word, len(word))
    return ''.join(map(str, temp))

def greeting():
    player1_name = input("Player-1, What is your name? ")
    print("Hello, " + player1_name, "! Welcome to the Find the Jumbled Word Challenge!\n")
    player2_name = input("Player-2, What is your name? ")
    print("Hello, " + player2_name, "! Welcome to the Find the Jumbled Word Challenge!\n")
    print("I am thinking of words for both of you and I will give you a chance to rearrange them..\n")
    print("Rules and Regulations : ")
    print("1. You will be given the jumbled word to rearrange.")
    print("2. You will have to enter the rearranged word.")
    print("3. Each correct answer gets you a point. Highest scorer wins.")
    print("So, Let's start !\n")
    return player1_name, player2_name

def conclusion(players,points):
    print("Well Played, ", players[0]," & ", players[1],"!")
    print("Score-Board :")
    print(players[0]," : ",points[0])
    print(players[1], " : ", points[1])

    if points[0] > points[1]:
        print(players[0], "wins!")
    elif points[0] < points[1]:
        print(players[1], "wins!")
    else:
        print("Match Tied!")

def action_control(players,word,points,turn,status):
    print(players[0], " : Turn-"+str(turn), " \n------------------------------\n" )
    print("Your jumbled word is: ", word[0])
    action = input("\nWhat do you want to do? \n1. Guess Word\t\t 2. Surrender\nEnter your choice : ")
    if action == "1":
        z = input("Guessed Word : ").upper()
        if word[2] == z:
            print("Correct Answer!\n")
            points[0] += 1
            word[2] = get_random_word(word_list)
            word[0] = jumble(word[2])
        else:
            print("Incorrect Answer! Retry in next turn.\n")
    elif action == "2":
        print(players[0], "surrendered!")
        print("The rearranged word is: ", word[2])
        status = True
    else:
        print("Invalid Choice! Skipping Turn...\n")

    print(players[1], " : Turn-" + str(turn), " \n------------------------------\n")
    print("Your jumbled word is: ", word[1])
    action = input("\nWhat do you want to do? \n1. Guess Word\t\t 2. Surrender\nEnter your choice : ")
    if action == "1":
        z = input("Guessed Word : ").upper()
        if word[3] == z:
            print("Correct Answer!\n")
            points[1] += 1
            word[3] = get_random_word(word_list)
            word[1] = jumble(word[3])
        else:
            print("Incorrect Answer! Retry in next turn.\n")
    elif action == "2":
        print(players[1], "surrendered!")
        print("The rearranged word is: ", word[3])
        status = True
    else:
        print("Invalid Choice! Skipping Turn...\n")
    return status,points,word


def gamePlay():
    players = greeting()
    points = [0,0]
    status = False
    turn = 0

    word1 = get_random_word(word_list)
    word2 = get_random_word(word_list)
    word = [jumble(word1),jumble(word2),word1,word2]

    while status==False:
        turn += 1
        control = action_control(players, word, points, turn, status)
        status = control[0]
        points = control[1]
        word = control[2]

    conclusion(players,points)
    playAgain = input("Do you want to play again?\n1. Yes\t\t 2. No\nEnter your choice : ")
    if playAgain == "1":
        gamePlay()
    else:
        print("Thank you for playing! Have a good day!")

gamePlay()