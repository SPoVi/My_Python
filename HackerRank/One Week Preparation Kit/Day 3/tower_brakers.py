'''
Two players are playing a game of Tower Breakers! Player 1 always moves 
first, and both players always play optimally.

The rules of the game are as follows:

- Initially there are n towers.
- Each tower is of height m.
- The players move in alternating turns.
- In each turn, a player can choose a tower of height x and reduce its 
height to y, where 1 <= y < x and y evenly divides x.
    - evenly divides :  x % y == 0
-If the current player is unable to make a move, they lose the game. 

TASK
Given the values of and n, m determine which player will win. 
If the first player wins, return 1. Otherwise, return 2. 


'''


import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here   
    if m == 1: 
        return (2)
    else:
        if n % 2 == 1:
            return 1
        else:
            return 2

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print("\nIntroduce el numero de patidas: ")
    t = int(input().strip())

    for t_itr in range(t):
        print("\nIntroduce el numero de torres y de pisos por torre: ")
        first_multiple_input = input().rstrip().split()
        
        n = int(first_multiple_input[0])
        
        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        print(result)

        #fptr.write(str(result) + '\n')

    #fptr.close()
