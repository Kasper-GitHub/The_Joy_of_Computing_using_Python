import random
import numpy as np

movie_list = ["INCEPTION", "INTERSTELLAR","GLADIATOR","PARASITE","JOKER","SUPERMAN","TITANIC","AVATAR","MINIONS","BATMAN"]

def get_random_movie(movie_list):
    return random.choice(movie_list)

def greeting(movie):
    player_name = input("What is your name? ")
    print("\nHello, " + player_name, "! Welcome to the Guess Movie Name Challenge!")
    print("I am thinking of a movie and I will give you a chance to guess.\n")
    print("Rules and Regulations : ")
    print("1. You will be given the number of letters in the movie to guess.")
    print("2. You will enter a letter and if it is there it will be shown on the screen in correct position.")
    print("3. You have no attempts limit to make a guess but more the attempts lesser the score. ")
    print("So, Let's start !\n")
    print(player_name, ", your movie name is : ", " _ "*len(movie), "[ ", len(movie), " Letters ]")
    print("Start Guessing...")
    return player_name

def guess_letter(z,movie,pos, movie_dashed):
    pos_temp = np.where(movie == z)[0]
    if len(pos_temp) == 0:
        print("Sorry, you didn't guess the letter in the movie name correctly.")
    else:
        print("You guessed the letter in the movie name correctly.")
        for i in pos_temp:
            movie_dashed[i] = z
        pos = np.sort(np.concatenate((pos, pos_temp), axis = None))
    return pos, movie_dashed

def guess_movie(z,movie):
    status = np.array_equal(movie, z)
    if status == True:
        print("You guessed the movie name correctly.")
    else:
        print("Sorry, you didn't guess the movie name correctly.")
    return status

def conclusion(player_name,movie,attempt,movie_dashed):
    print("Well Played, ",player_name,"!")
    print("Finally you guessed the movie name correctly. It's ", end='')
    print(''.join(map(str, movie))," !")

    guessometer = len(np.where(movie_dashed == "_")[0])
    if guessometer == 0:
        score = 4 - attempt/len(movie)
    elif guessometer < len(movie)/2:
        score = 8 - attempt / len(movie)
    elif guessometer < len(movie):
        score = 10 - attempt / len(movie)
    else:
        score = 10

    print("Your Score = ",score, " on a scale of 10.\n\n")

def action_control(movie,pos,movie_dashed,status):
    print("Current Status : ", end=' ')
    print(' '.join(map(str, movie_dashed)))
    action = input("\nWhat do you want to do? \n1. Guess Letter\t\t 2. Guess Movie Name\nEnter your choice : ")
    if action == "1":
        z = input("Guess Letter : ").upper()
        info = guess_letter(z,movie,pos,movie_dashed)
        pos = info[0]
        movie_dashed = info[1]
        if len(np.where(movie_dashed == "_")[0]) == 0:
            status = True
    elif action == "2":
        z = np.array(list(input("Guess Movie Name : ").upper()))
        status = guess_movie(z,movie)
    else:
        print("Invalid Input")
        action_control(movie,pos,movie_dashed,status)
    return status,pos,movie_dashed

def gamePlay():
    movie = np.array(list(get_random_movie(movie_list)))
    movie_dashed = np.array(list("_" * len(movie)))
    status = False
    attempt = 0
    pos = np.array([])
    player = greeting(movie)

    while (status == False):
        attempt += 1
        print("\nAttempt Counter : ", attempt)
        control = action_control(movie, pos, movie_dashed, status)
        status = control[0]
        pos = control[1]
        movie_dashed = control[2]

    conclusion(player, movie, attempt, movie_dashed)
    playAgain = input("Do you want to play again?\n1. Yes\t\t 2. No\nEnter your choice : ")
    if playAgain == "1":
        gamePlay()
    else:
        print("Thank you for playing! Have a good day!")

gamePlay()