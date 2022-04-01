'''
Given five positive integers, find the minimum and maximum values that can be 
calculated by summing exactly four of the five integers. 

Then print the respective minimum and maximum values as a single line of two 
space-separated long integers.

EXAMPLE
    arr = [1,3,5,7,9]

    The minimum sum is 1 + 3 + 5 + 7 = 16
    The maximum sum is 9 + 7 + 5 + 3 = 24

    OUTPUT: 16 24
'''
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Reordenamos de menor a mayor el array
    arr.sort()
    # Copiamos a otra lista los cuatro ultimos (max) y los cuatro primero (min)
    max_list = arr[-4:].copy()
    min_list = arr[:4].copy()
    # Hacemos las sumas
    sum_max = sum(max_list)
    sum_min = sum(min_list)
    # Mostramos por pantall
    print("{} {}".format(sum_min, sum_max))




if __name__ == '__main__':

    print("Introduce el array de numeros: ")
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
