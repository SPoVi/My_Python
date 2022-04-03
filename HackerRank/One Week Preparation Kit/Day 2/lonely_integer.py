'''
Given an array of integers, where all elements but one occur twice, 
find the unique element. 
'''

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here

    for i in a:
        c = a.count(i)
        if c < 2:
            lonely_int = i
    
    return lonely_int

if __name__ == '__main__':
    
    # Abrir arrchivo. File pointer
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    print("\nIntroduce numero de elementos: ")
    n = int(input().strip())
    print("\nIntroduce {} numeros: ".format(n))
    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print("\nEntero unico: ")
    print(result)

    # Escribir en archivo
    #fptr.write(str(result) + '\n')
    # Cerrar archivo
    #fptr.close()