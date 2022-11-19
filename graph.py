#make pretty graphs
def graph_it(wins, winrate, x, y, title):
    sums = []
    for i in range(1, len(wins)):
        sums.append(sum(wins[0:i])/i)
    plt.plot(sums)
    plt.plot([winrate for _ in range(1, len(wins))], 'y-', alpha= .75)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.show()

# how to play the actual game
game = BlackJack(QLearningAgent())
game.play()
graph_it(game.wins, game.winrate, "Game #", "Q Learning Agent Winrate", "Q Learning Agent Winrate over Time")
array = game.player.qValues
game = BlackJack(TrainedQLearner(array))
game.play()
graph_it(game.wins, game.winrate, "Game #", "Trained Agent Winrate", "Trained Agent Winrate over Time")
game = BlackJack(RandomPlayer())
game.play()
graph_it(game.wins, game.winrate, "Game #", "Random Agent Winrate", "Random Agent Winrate over Time")
# pp.pprint(array)