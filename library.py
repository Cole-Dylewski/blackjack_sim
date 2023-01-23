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
        print(self.hand)

        cards = [card.split('_')[1] for card in self.hand]
        cards.sort()
        handSum = 0
        soft=cards.count('A')
        print(cards,soft)
        for i, card in enumerate(cards):
            if card.isnumeric():
                handSum+= int(card)
                #print('card is numeric', card)
            else:
                if card.lower() != 'a':
                    handSum+=10
        if handSum + soft >= 21:
            return handSum + soft
        else:
            for s in range(soft,0,-1):
                high = s*11
                low = soft-s
                print(high,low)
            print(handSum)
        return self.hand