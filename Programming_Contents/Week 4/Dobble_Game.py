import string
import random

symbols = list(string.ascii_letters)
same_symbol = random.choice(symbols)
symbols.remove(same_symbol)

pos1=random.randint(0,4)
pos2=random.randint(0,4)

card1 = [0,0,0,0,0]
card2 = [0,0,0,0,0]

if pos1 == pos2:
    card2[pos1] = same_symbol
    card1[pos1] = same_symbol
else:
    card1[pos1] = same_symbol
    card2[pos2] = same_symbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])

i = 0
while i < 5:
    if i != pos1 and i != pos2:
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i=i+1
print(card1)
print(card2)