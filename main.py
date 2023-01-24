import random
import pandas as pd
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
        #print(deck)
    # print(len(deck))
    for i in range(7):
        # print('shuffle')
        random.shuffle(deck)
    # print(deck)
    return deck


def build_table(numPlayers=1):
    table = {}
    for i in range(numPlayers):
        table[str(i)] = library.Player(name=i)

    table['DEALER'] = library.Dealer()
    return table

def get_subhand(hand):
    cards = [card.split('_')[1] for card in hand]
    cards.sort()
    handSum = 0
    soft = cards.count('A')
    for i, card in enumerate(cards):
        if card.isnumeric():
            handSum += int(card)
        else:
            if card.lower() != 'a':
                handSum += 10
    if handSum + soft > 21:
        return handSum + soft
    else:
        for s in range(soft, -1, -1):
            high = s * 11
            low = soft - s
            # print(handSum, high, low, (handSum + high + low))
            if (handSum + high + low) <= 21:
                return (handSum + high + low)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    dfRecord = pd.DataFrame()
    table = build_table(numPlayers=1)

    #print(player_1.name)
    #deck = ['D_5', 'D_4', 'H_A', 'C_A','S_A','H_A']
    #print(deck[:5])
    for i in range(1):
        deck = build_deck(numdecks=1)
        record={
            'Dealer Face Card': '',
            'Dealer Hand':[],
            'Player Hand':[],
            'Outcome':''
        }
        for j in range(2):
            for k,v in table.items():
                #if k != 'DEALER':
                v.deal_card(deck.pop(0))
                #print(k,v.name)
        #table['DEALER'].deal_card('S_A')
        #table['DEALER'].deal_card('S_K')

        for k, v in table.items():
            print(k, v.name, v.get_hand(), v.status)

        record['Dealer Face Card'] = table['DEALER'].get_facecard()
        #if dealer has blackjack, end deal
        if table['DEALER'].get_facecard().lower() == 'a' and table['DEALER'].status == 'BLACKJACK':
            record['Dealer Hand'] = table['DEALER'].get_hand()[1]
            record['Player Hand'] = table['0'].get_hand()[1]
            print(table['0'].status)
            if table['0'].status == table['DEALER'].status:
                record['Outcome'] = 0
            else:
                record['Outcome'] = -1
        else:
            for k, v in table.items():
                if k != 'DEALER':
                    while v.status not in [False ,'BLACKJACK']:
                        print(v.get_hand())
                        v.deal_card(deck.pop(0))
                    print(v.get_hand())
                print(k, v.name, v.get_hand(), v.status)

        print(record)
    #print('final hand',player_1.get_hand())



