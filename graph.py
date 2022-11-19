import matplotlib.pyplot as plt

#make pretty graphs

def graph(wins, winrate, x, y, title):
    sums = []
    for i in range(1, len(wins)):
        sums.append(sum(wins[0:i])/i)
    plt.plot(sums)
    plt.plot([winrate for _ in range(1, len(wins))], 'y-', alpha= .75)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.show()
