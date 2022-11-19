from player import Player
from counter import Counter
from globals import *

import numpy as np

class QLearningAgent(Player): #THE MEAT
    def __init__(self):
        self.qValues = Counter() #{(dealers_card_value, players_value, player_move): q_value}
        self.lastMove = "hit" # first move is always hit
        self.lastValue = 0 # first value always 0
        self.alpha = .2 #how much i want to weigh my last observation
        super(QLearningAgent, self).__init__()
        
    def reset(self):
        self.cards = []
        self.lastMove = "hit" # reset first move to hit
        self.lastValue = 0 # reset my last value to 0 for new game, dont want to update value from last game
    
    def get_move(self): # the hard stuff
        return self.computeActionFromQValues(self.dealer_card, self.hand_value())
    
    def getQValue(self, dealerVal, playerVal, action): # dictionary lookup function
        return float(self.qValues[(dealerVal, playerVal, action)])
    
    def receive_card(self, card): # overridden because I want to update the value of my last action based on my new state
        if printer: print("card recieved")
        self.cards.append(card)
        self.update() 
    
    def computeValueFromQValues(self, dealerVal, playerVal): 
        # looks through my actions and returns the value of the highest one
        maxQVal = float("-inf")
        legalActions = self.getLegalActions(playerVal)
        if len(legalActions) == 0:
            return 0.0
        for action in legalActions:
            maxQVal = max(maxQVal, self.getQValue(dealerVal, playerVal, action))
        return maxQVal
    
    def computeActionFromQValues(self, dealerVal, playerVal):
        # function that returns my move based on observed values of my actions
        if printer: print("getting action")
        maxQVal = float("-inf")
        maxAction = None
        legalActions = self.getLegalActions(playerVal)
        for action in self.getLegalActions(playerVal):
            tempQVal = self.getQValue(dealerVal, playerVal, action)
            if tempQVal > maxQVal:
                maxQVal = tempQVal
                maxAction = action
            elif tempQVal == maxQVal:
                maxAction = np.random.choice([maxAction, action])
        if np.random.random() < .5: #random exploration
            maxAction = np.random.choice(legalActions)
        if printer: print("   ", maxAction)
        self.lastMove = maxAction
        if printer: print("    updating Last move in get action", self.lastMove)
            
        if maxAction == "stand": # if we stand, update because it wont get called again
            self.update()

        return maxAction
    
    def update(self):
        # just update value in dictionary
        # based off pacman homework
        if printer: print("Updating q val")
        # called when the player recieves a new card so values can be updated
        playerOldVal = self.lastValue
        action = self.lastMove
        playerNewVal = self.hand_value()
        
        if playerNewVal == -1: #if i busted
            playerNewVal = -4
            
        
        if printer: print("    Last Move: ", self.lastMove)
        #no discount because # of cards doesnt matter, just winning
        
        if action != "stand":
            sample = playerNewVal + self.computeValueFromQValues(self.dealer_card, playerNewVal)
            self.qValues[(self.dealer_card, playerOldVal, action)] = ((1 - self.alpha)*self.getQValue(self.dealer_card, playerOldVal, action)) + (self.alpha * sample)
        else:
            # if i stand, the value of standing in my state is just the value of my hand
            self.qValues[(self.dealer_card, playerOldVal, action)] = playerOldVal
        self.lastValue = playerNewVal
        
    def getLegalActions(self, state):
        # dumb function
        return ["hit", "stand"]