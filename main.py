import random

import library
# quantum black jack
# gets the results for all possible decision trees of each hand and records the result



def build_deck(numdecks=1):
    suits = ['C', 'S', 'H', 'D']
    cards = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    # print(cards)
    deck = []
    for d in range(numdecks):
        for s in suits:
            for c in cards:
                deck.append(f'{s}_{c}')

    # print(len(deck))
    for i in range(7):
        # print('shuffle')
        random.shuffle(deck)
    # print(deck)
    return deck


def build_table(numPlayers=1):
    table = {}

    return table


def deal_cards(deck, table):
    print(deck[:28])
    for player, hand in table.items():
        print(player, hand)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    deck = build_deck(numdecks=7)
    table = build_table(numPlayers=7)
    player_1 = library.Player(name=0)
    print(player_1.name)
    #print(deck[:5])
    for i in range(5):
        card = deck.pop(0)
        player_1.deal_card(card)
    hand = player_1.get_hand()
    print(hand)




