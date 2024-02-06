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

def printmatrix():
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print("\n", end = "")
    print("")

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
        #second computer puts a 1 according to our strategy
        #tests for almost-zero rows and columns and places a 1 if needed
        i=0
        while i < n:
            count = 0
            gap = -1
            for j in range(0, n):
                if matrix[i][j] == 0:
                    count += 1
                elif matrix[i][j] == "-":
                    gap = j
            if count == n-1 and gap != -1:
                matrix[i][gap] = 1
                break
            i += 1
        
        if i == n:
            i = 0
            while i < n:
                count = 0
                gap = -1
                for j in range(0, n):
                    if matrix[j][i] == 0:
                        count += 1
                    elif matrix[j][i] == "-":
                        gap = j
                if count == n-1 and gap != -1:
                    matrix[gap][j] = 1
                    break
                i += 1
        
        #if all tests fail, places a 1 randomly
        if i == n:
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
max_n = 10
win_rate_zero = [0.5]*(max_n-1)
for n in range(2, max_n+1):
    results = [0.5] * iterations
    for i in range(iterations):
        matrix = [["-"]*n for j in range(n)]
        game(0)
        results[i] = winner
    win_rate_zero[n-2] = mean(results)


win_rate_one = [0.5]*(max_n-1)
for n in range(2, max_n+1):
    results = [0.5] * iterations
    for i in range(iterations):
        matrix = [["-"]*n for j in range(n)]
        game(1)
        results[i] = winner
    win_rate_one[n-2] = mean(results)


xpoints = range(2, max_n+1)

plt.plot(xpoints, win_rate_zero, "r", label = "0 goes first")
plt.plot(xpoints, win_rate_one, "g", label = "1 goes first")
plt.xlabel("Grid size")
plt.ylabel("Average winrate")
plt.ylim(0, 1)

plt.legend()
plt.show()
    

