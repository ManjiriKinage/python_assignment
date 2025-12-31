import random
card=["Heart","Diamond","Club","Spade"]
value=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck =[]
for c in card:
    for v in value :
        deck.append(v + " of "+ c)
random.shuffle(deck)

for c in deck:
    print(c)
