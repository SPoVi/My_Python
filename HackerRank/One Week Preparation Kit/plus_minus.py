'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with

places after the decimal.

Note: This challenge introduces precision problems. The test cases are 
scaled to six decimal places, though answers with absolute error of up 
to are acceptable.

Example:
    arr = [1,1,0,-1,-1]

    There are n = 5 alements, 2 pos, 2 neg and 1 zero. Their ratios are 2/5, 2/5 adn 1/5.
    Results printed: (6 digits after decimal)
        0.400000
        0.200000
        0.200000

'''


import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    counter_pos = 0
    counter_neg = 0
    counter_zero = 0
    # Write your code here
    for i in arr:
        if i < 0:
            counter_neg += 1
        elif i > 0:
            counter_pos += 1
        elif i == 0:
            counter_zero += 1

    # Mostrar resultados
    print("%.6f"%(counter_pos/n))
    print("%.6f"%(counter_neg/n))
    print("%.6f"%(counter_zero/n))


if __name__ == '__main__':
    # number of integers

    print("\nIntroduce el numero de enteros: ")
    n = int(input().strip())

    # array of integers
    print("\nIntroduce ")
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)