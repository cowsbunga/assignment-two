#this program lets you play the matrix game against a computer that plays completely randomly

import numpy as np

rng = np.random.default_rng()

n = int(input("Enter the grid size you'd like to play on:"))

matrix = [["-"] * n for i in range(n)]

#prints the matrix thats being worked on
def print_matrix():
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print("\n", end = "")

#finds the winner at the end of the game
def countup():
    print_matrix()
    if np.linalg.det(matrix) == 0:
        print("Congratulations you win")
    else:
        print("You lose")

#plays the game
def game(myturn):
    if myturn == 1:
        print_matrix()

        #player puts a 0 in the matrix somewhere
        while True:
            x = int(input("Enter row number of target: "))
            if x>0 and x < n+1:
                break
            print("invalid point - enter a number between 1 and ", n)

        while True:
            y = int(input("Enter column number of target: "))
            if y>0 and y < n+1:
                break
            print("invalid point - enter a number between 1 and ", n)

        if matrix[x-1][y-1] != "-":
            print("That space is not empty, try again")
            game(1)
        else:
            matrix[x-1][y-1] = 0
            if not any('-' in sublist for sublist in matrix):
                countup()
                return 0
            game(0)
        

    else:
        #takes computers turn
        print_matrix()
        print("Computer turn: ")
        
        while True:
            x = rng.integers(0, n)
            y = rng.integers(0, n)
            if matrix[x][y] == "-":
                matrix[x][y] = 1
                break
        
        if not any('-' in sublist for sublist in matrix):
            countup()
            return 0
        game(1)

myturn = 1 # 1 = player starts first, 0 = bot starts first
#I assume that the player goes first and that the player chooses the 0s

game(myturn)
