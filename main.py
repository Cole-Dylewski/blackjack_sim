import random


#quantum black jack
#gets the results for all possible decision trees of each hand and records the result

def build_deck(numdecks=1):
    suits = ['C','S','H','D']
    cards = [i for i in range(2,11)]+['J','Q','K','A']
    #print(cards)
    deck = []
    for d in range(numdecks):
        for s in suits:
            for c in cards:
                deck.append(f'{s}_{c}')

    print(len(deck))
    for i in range(7):
        print('shuffle')
        random.shuffle(deck)
    #print(deck)
    return deck
build_deck(7)
print(364/52)