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
    # ----- NO VALE: Son punteros ¡¡, modificas una y modificas todo
    # my_list_max = arr     
    # my_list_min = arr
    # ----- SOLUCION: strcopy()
    my_list_max = arr.copy()     
    my_list_min = arr.copy()

    # haremos un pop posicion i 
    max_sum_list = []
    min_sum_list = []
    for _ in range(4):
        maximum = 0
        minimum = 1000000000
        for i in my_list_max:
            if i > maximum: maximum = i
        for i in my_list_min:    
            if i < minimum: minimum = i
        
        #agregamos valoresa las listas de sumas
        max_sum_list.append(maximum)
        min_sum_list.append(minimum)

        #eliminamos valores de las listas
        my_list_max.remove(maximum)
        my_list_min.remove(minimum)

    #print(max_sum_list)
    #print(min_sum_list)
    # Sumar valores listas
    sum_max = sum(max_sum_list)
    sum_min = sum(min_sum_list)

    print("{} {}".format(sum_min, sum_max))
                




if __name__ == '__main__':

    print("Introduce el array de numeros: ")
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
