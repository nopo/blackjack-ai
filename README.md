# Blackjack!
This project implements multiple different types of agents in blackjack.
The first type of agent is the dealer who will hit if their score is lower than 17.
There is the random player that will randomly decide to hit or stand.
The Q-learning agent that decides based on the weights of prior actions in the same situation according to the q-learning algorithm:
  https://towardsdatascience.com/q-learning-algorithm-from-explanation-to-implementation-cdbeda2ea187
The trained q-learning agent takes the final weights of the trained q-learning agent to take what the agent learned and play the best it can.

Here are the graphed results:

![random_agent_winrate](https://user-images.githubusercontent.com/35900807/202857441-88d63d84-ba8e-456d-a363-f89e447ed4f4.png)
![q_learning_agent_winrate](https://user-images.githubusercontent.com/35900807/202857440-c6c45b57-7f46-4a34-b8cd-a625ca0fd2c0.png)
![trained_q_learning_agent_winrate](https://user-images.githubusercontent.com/35900807/202857442-15bb2d02-437d-4e81-98b9-76788cdc23de.png)
