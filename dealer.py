class Dealer(Player):
    
    def get_move(self): #dealer hits if < 17
        hand = self.hand_value()
        if hand < 17:
            return "hit"
        elif hand >= 17:
            return "stand"