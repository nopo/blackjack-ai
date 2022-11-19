class Player: #this is a base class for the player, allows user to type hit or stand and actually play blackjack
    
    def __init__(self):
        self.cards = [] #keeps track of the cards in the players hand
        
    def reset(self):
        self.cards = [] #player starts with no cards
        
    def update(self): #used for q-learning updates, not used by base class
        return
        
    def receive_dealers_card(self, card):#keep track of the dealers card
        self.dealer_card = card
    
    def get_move(self): #function that game calls to get if player is standing or hitting again
        #hit or stop
        inp = ""
        while inp != "hit" and inp != "stand":
            print("Enter hit or stand: ")
            inp = input()
        return inp
    
    def receive_card(self, card): # after hitting, i add the card to my hand
        self.cards.append(card)
    
    def hand_value(self): # returns best hand value (Aces make things hard)
        # returns hard values when available ie the max possible hand value that isnt above 21
        if len(self.cards) == 0: #if i dont have any cards i dont have any value
            return 0
        value = [] # value is an array of values of the current hand
        for card in self.cards:
            if card != 11:
                if len(value) != 0:
                    for _ in range(len(value)):
                        value[_] += card
                else:
                    value = [card]
            else:
                if len(value) != 0:
                    newValue = []
                    for _ in value:
                        newValue.append(_ + 1)
                        newValue.append(_ + 11)
                    value = newValue
                else:
                    value = [1, 11]
        value = [val for val in value if val <= 21]
        if 21 in value: #if i have a blackjack i for sure want to have that be my value
            return 21
        elif len(value) == 0: #if i busted, value array wont have any possible values
            return -1
        else:
            return max(value)