class Deck: #class representing deck of cards
    def __init__(self):
        self.J, self.Q, self.K, self.A = 10, 10, 10, 11
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, self.J, self.Q, self.K, self.A] * 4
        self.shuffle()
        
    def shuffle(self):
        np.random.shuffle(self.cards)
        
    def reset(self): #cards for new game
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, self.J, self.Q, self.K, self.A] * 4
        self.shuffle()
    
    def hit(self):
        return self.cards.pop()