import numpy as np

symbol_1 = "X"
player_1 = False
symbol_2 = "O"
player_2 = False
place_holder = np.array([["-","-","-"],["-","-","-"],["-","-","-"]])

def display(place_holder):
    for i in range(len(place_holder)):
        print(' '.join(map(str,place_holder[i])))

def check(place_holder,player_1,player_2):
    if len(set(place_holder(axis=0))) == 1:
        if set(place_holder(axis=0)) == symbol_1:
            player_1 = True
            return player_1,player_2
        elif set(place_holder(axis=0)) == symbol_2:
            player_2 = True
            return player_1,player_2
    elif len(set(place_holder(axis=1))) == 1:
        if set(place_holder(axis=1)) == symbol_1:
            player_1 = True
            return player_1,player_2
        elif set(place_holder(axis=1)) == symbol_2:
            player_2 = True
            return player_1,player_2

def entry():
    global symbol_1
    global symbol_2
    global place_holder