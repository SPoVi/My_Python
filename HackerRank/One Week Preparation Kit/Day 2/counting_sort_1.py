'''
__Comparison Sorting__
Quicksort usually has a running time of 'n x log(n)', but is there an 
algorithm that can sort even faster? In general, this is not possible. 

Most sorting algorithms are comparison sorts, i.e. they sort a list just 
by comparing the elements to one another. 

A comparison sort algorithm cannot beat 'n x log(n)' (worst-case) 
running time, since 'n x log(n)' represents the minimum number of 
comparisons needed to know where to place each element. 
For more details, you can see these notes (PDF).

__Alternative Sorting__
Another sorting method, the counting sort, does not require comparison. 
Instead, you create an integer array whose index range covers the entire 
range of values in your array to sort. 

Each time a value occurs in the original array, you increment the counter
at that index. At the end, run through your counting array, printing the 
value of each non-zero valued index that number of times.
'''

'''
Given a list of integers, count and return the number of times each 
value appears as an array of integers.
'''

import math
import os
import random
import re
import sys


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    result = []

    # Compronar rango
    range_array = max(arr)
    # Crear lista de zeros
    result = [0]*(range_array+1) # contar el cero

    # Contar las veces que aparece un numero
    for i in arr:
        result[i] += 1 # incrementa la posicion
    
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    print("\nIntroduce el numero de elementos del array: ")
    n = int(input().strip())

    print("\nIntroduce {} enteros: ".format(n))
    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print("\nListado final: ")
    print(result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
