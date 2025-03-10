import random
import matplotlib.pyplot as plt

money = 10000
turns_list = []
money_list = []

def betting_game(account):
    bet = random.randint(1,20)
    draw = random.randint(1,20)

    if bet == draw:
        print("The draw was", str(draw)+ ". Your pick was", bet, end=". ")
        print("You won! Reward : INR 1000/-")
        account = account - 100 + 1000
    else :
        print("The draw was", str(draw)+ ". Your pick was", bet, end=". ")
        print("You lost!")
        account = account - 100

    return account

plt.figure()
for i in range(365):
    money = betting_game(money)
    turns = i+1
    money_list.append(money)
    turns_list.append(turns)

plt.plot(turns_list,money_list)
plt.show()