'''
Sean invented a game involvinf a 2n x 2n matrix where each cell of the matrix
contains an integer.

He can reverse any of its rows or columns any number of times.

The goal of the game is to maximize the sum of the elements in the nxn 
submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations fow 'q' matrices, help sean reverse the
rows and columns of each matrix in the bes possible way sso that the sum
of the elements in the matrix's upper-left quadran is maximal.

Example: matrix = [[1,2],[3,4]]
1 2
3 4

1 2
4 3

Solution: The maximal sum is 4.
4 2
1 3

'''

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix): # returns an int, the maximum sum possible
    # matrix is an int matrix[2n][2n]: a 2-dimensional array of integers

    

if __name__ == '__main__':

    print("\nIntroduce el numero de preguntas: ")
    q = int(input().strip())

    for q_itr in range(q):
        print("\nTamaño de la matriz: ")
        n = int(input().strip())

        matrix = []

        # Creamos matriz 2n x 2n
        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print("\nMatrix:")
        print(matrix)
        print("\nFlipped matrix:")
        print(result)


'''
v = 0
    for i in range(n):
        for j in range(n):
            l = []
            l.append(a[i][j]) # current matrix
            l.append(a[2 * n - 1 - i][j])  # bottom left
            l.append(a[i][2 * n - 1- j]) # top right
            l.append(a[2* n - 1 - i][2 * n - 1- j]) # bottom right
    
            maxv = max(l)
            #print(l)
            #print(max(l))
            
            v += maxv

'''