'''
Given a square matrix, calculate the absolute difference between the sums
 of its diagonals. 
'''

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d1 = []
    d2 = []
    for i in range(n):
        d1.append(arr[i][i])
        d2.append(arr[i][n-1-i])

    # Mostrar diagonales
    print("\nDiagonales:")
    print("d1 = {}\td2 = {}".format(d1,d2))

    # Sumar diagonales
    sum_d1 = sum(d1)
    sum_d2 = sum(d2)

    # Diferencia absoluta de diagonales
    result = abs(sum_d1 - sum_d2)

    return result


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    print("\nIntroduce el tamaño de la matriz cuadrada: ")
    n = int(input().strip())

    arr = []
    
    print("\nIntroduce los valores de la matriz: ")
    for i in range(n):
        print("\nFila {}".format(i+1))
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    
    print("\nResultado de la diferencia absoluta de las diagonales: {}".format(result))

    #fptr.write(str(result) + '\n')

    #fptr.close()