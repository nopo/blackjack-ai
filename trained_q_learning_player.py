class TrainedQLearner(Player):
    # this is just a player that takes the qLearningAgents value dictionary and plays off of that, no more updates
    def __init__(self, qValues):
        self.qValues = qValues
        super(TrainedQLearner, self).__init__()
        
    def update(self):
        return
    
    def get_move(self):
        return self.computeActionFromQValues()
    
    def getQValue(self, dealerVal, playerVal, action):
        return float(self.qValues[(dealerVal, playerVal, action)])
        
    def computeValueFromQValues(self, dealerVal, playerVal):
        maxQVal = float("-inf")
        legalActions = ["hit", "stand"]
        for action in legalActions:
            maxQVal = max(maxQVal, self.getQValue(dealerVal, playerVal, action))
        return maxQVal
    
    def computeActionFromQValues(self):
        if printer: print("getting action")
        maxQVal = float("-inf")
        maxAction = None
        dealerVal = self.dealer_card
        playerVal = self.hand_value()
        for action in ["hit", "stand"]:
            tempQVal = self.getQValue(dealerVal, playerVal, action)
            if tempQVal > maxQVal:
                maxQVal = tempQVal
                maxAction = action
            elif tempQVal == maxQVal:
                maxAction = np.random.choice([maxAction, action])
        if printer: print("   ", maxAction)
        self.lastMove = maxAction
        if printer: print("    updating Last move in get action", self.lastMove)

        return maxAction
    
    def getLegalActions(self, state):
        return ["hit", "stand"]