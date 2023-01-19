import random


# quantum black jack
# gets the results for all possible decision trees of each hand and records the result

class Player:


    def __init__(self, name):
        self.name = 'Player_' + str(name+1)
        self.status = True
        self.hand = []

    def __str__(self):
        print(self.hand)

    def deal_card(self, card):
        #print(card)
        self.hand.append(card)
        #print(self.hand)
    def new_hand(self):
        self.hand = []

    def get_hand(self):
        #print(self.hand)
        return self.hand


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


deck = build_deck(numdecks=7)
table = build_table(numPlayers=7)
player_1 = Player(name=0)
player_1.deal_card('c_j')
player_1.deal_card('c_k')

hand = player_1.get_hand()
print(hand)
player_1.new_hand()
hand = player_1.get_hand()
print(hand)