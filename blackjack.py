from globals import *
from deck import Deck
from dealer import Dealer

class BlackJack: #class implementing actual blackjack game and rules
    
    def __init__(self, player): #argument is instance of class that is being played
        self.deck = Deck()
        self.player = player
        self.dealer = Dealer()
        self.wins = [] # 1 = player won, 0 is dealer, used to keep track of winrate
        self.winrate = 0 # total cumilitave winrate
        
    def play(self): 
        dealerWins = 0
        playerWins = 0
        for _ in range(10000): #plays 10,000 games
            self.dealer_draw() # dealer draws first
            self.turn(self.player)
            self.turn(self.dealer)
            winner = self.eval_winner()
            
            if winner == "dealer": #update the averages to keep track of data
                dealerWins += 1
                self.wins.append(0)
            elif winner == "player":
                playerWins += 1
                self.wins.append(1)
            
            self.deck.reset() #reset the 2 players and the deck of cards
            self.player.reset()
            self.dealer.reset()
            if printer: print(self.player.qValues)
        
        self.winrate = playerWins/(dealerWins + playerWins)
        print(self.winrate)
        if printer: pp.pprint(self.player.qValues)
        
    def dealer_draw(self): #dealer draws first
        card = self.deck.hit()
        self.dealer.receive_card(card) #give dealer his card
        self.player.receive_dealers_card(card) #let player know what card the dealer got
        if printer: print("dealer received card with value of ", card)
        
    def turn(self, player): #function representing 1 players turn
        playerMove = "hit"
        while playerMove == "hit":#give the player their card as long as they keep asking for it
            card = self.deck.hit()
            player.receive_card(card)
            val = player.hand_value()
            # if the player busts or gets blackjack, their turn is done
            if val == -1:
                # print("Busted")
                player.update()
                break
            elif val == 21:
                # print("BlackJack")
                break
            else: 
                playerMove = player.get_move()
    
    def eval_winner(self): # function to decide which player won
        playerVal = self.player.hand_value()
        dealerVal = self.dealer.hand_value()
        
        if playerVal == -1 or dealerVal > playerVal: #the dealer wins if the player busts
            return "dealer"
        elif playerVal >= dealerVal:
            # print("player won!")
            return "player"
        else:
            # print("tie")
            return "tie"