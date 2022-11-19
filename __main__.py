import blackjack
import q_learning_player
import trained_q_learning_player
import random_player
import graph

if __name__ == "__main__":
# how to play the actual game
    game = blackjack.BlackJack(q_learning_player.QLearningAgent())
    game.play()
    graph.graph(game.wins, game.winrate, "Game #", "Q Learning Agent Winrate", "Q Learning Agent Winrate over Time")
    array = game.player.qValues
    game = blackjack.BlackJack(trained_q_learning_player.TrainedQLearner(array))
    game.play()
    graph.graph(game.wins, game.winrate, "Game #", "Trained Agent Winrate", "Trained Agent Winrate over Time")
    game = blackjack.BlackJack(random_player.RandomPlayer())
    game.play()
    graph.graph(game.wins, game.winrate, "Game #", "Random Agent Winrate", "Random Agent Winrate over Time")
