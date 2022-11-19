import blackjack
import q_learning_player
import trained_q_learning_player
import random_player
import matplotlib.pyplot as plt


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

if __name__ == "__main__":
# how to play the actual game
    game = blackjack.BlackJack(q_learning_player.QLearningAgent())
    game.play()
    graph_it(game.wins, game.winrate, "Game #", "Q Learning Agent Winrate", "Q Learning Agent Winrate over Time")
    array = game.player.qValues
    game = blackjack.BlackJack(trained_q_learning_player.TrainedQLearner(array))
    game.play()
    graph_it(game.wins, game.winrate, "Game #", "Trained Agent Winrate", "Trained Agent Winrate over Time")
    game = blackjack.BlackJack(random_player.RandomPlayer())
    game.play()
    graph_it(game.wins, game.winrate, "Game #", "Random Agent Winrate", "Random Agent Winrate over Time")
