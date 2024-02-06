#this program lets you play the matrix game against a computer that plays completely randomly
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

winner = 0

#sets up the game

#finds the winner at the end of the game
def countup():
    global winner
    if np.linalg.det(matrix) == 0:
        winner = 0
    else: 
        winner = 1

#plays the game
def game(firstturn):
    if firstturn == 0:

        #first computer puts a 0 in the matrix somewhere
        while True:
            x = rng.integers(0, n)
            y = rng.integers(0, n)
            if matrix[x][y] == "-":
                matrix[x][y] = 0
                break
        
        if not any('-' in sublist for sublist in matrix):
            countup()
            return 0
        game(1)
        

    else:
        #second computer puts a 1 somewhere
        while True:
            x = rng.integers(0, n)
            y = rng.integers(0, n)
            if matrix[x][y] == "-":
                matrix[x][y] = 1
                break
        
        if not any('-' in sublist for sublist in matrix):
            countup()
            return 0
        game(0)



#plays the game many times and graphs the results
#note that average winrate is for the player placing 1s
iterations = 1000
max_n = 12
win_rate_zero = [0.5]*max_n
for n in range(1, max_n+1):
    results = [0.5] * iterations
    for i in range(iterations):
        matrix = [["-"]*n for j in range(n)]
        game(0)
        results[i] = winner
    win_rate_zero[n-1] = mean(results)


win_rate_one = [0.5]*max_n
for n in range(1, max_n+1):
    results = [0.5] * iterations
    for i in range(iterations):
        matrix = [["-"]*n for j in range(n)]
        game(1)
        results[i] = winner
    win_rate_one[n-1] = mean(results)


xpoints = range(1, n+1)

plt.plot(xpoints, win_rate_zero, "r", label = "0 goes first")
plt.plot(xpoints, win_rate_one, "g", label = "1 goes first")
plt.xlabel("Grid size")
plt.ylabel("Average winrate")

plt.legend()
plt.show()
    


