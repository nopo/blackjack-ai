class RandomPlayer(Player): #player that randomly hits or stands (used for baseline stats)
    def get_move(self):
        return np.random.choice(["hit", "stand"])