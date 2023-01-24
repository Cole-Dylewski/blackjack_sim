


class Player:
    def __init__(self, name):
        self.name = 'Player_' + str(name+1)
        self.status = True
        self.hand = []
    def print_hand(self):
        print(self.hand)
    def deal_card(self, card):
       self.hand.append(card)
       self.get_hand()
    def new_hand(self):
        self.hand = []
    def get_hand(self):
        #print(f"{self.name}:{self.hand}")
        cards = [card.split('_')[1] for card in self.hand]

        cards.sort()
        if len(cards)==2:
            if cards[0]=='A' and cards[1] in ['J', 'Q', 'K']:
                self.status = 'BLACKJACK'
                return 21, self.hand
        handSum = 0
        soft=cards.count('A')
        #print(cards,soft)
        for i, card in enumerate(cards):
            if card.isnumeric():
                handSum+= int(card)
            else:
                if card.lower() != 'a':
                    handSum+=10
        if handSum + soft > 21:
            self.status = False
            return handSum + soft ,self.hand
        else:
            for s in range(soft,-1,-1):
                high = s*11
                low = soft-s
                #print(handSum, high, low, (handSum + high + low))
                if (handSum+high+low)<=21:
                    return (handSum+high+low),self.hand

class Dealer(Player):

    def __init__(self):
        self.name = 'Dealer'
        self.status = True
        self.hand = []
        self.facecard=''
    def hit_or_stay(self):
        if self.get_hand()[0]<18:
            return True
        else:
            False
    def get_facecard(self):
        cards = [card.split('_')[1] for card in self.hand]
        return cards[0]
