'''
You are asked to ensure that the first and last names of people begin with
 a capital letter in their passports. For example, alison heck should be 
 capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(txt):

    txt = txt.split()
    lst = []
    for word in txt:
        lst.append(word.capitalize())
    txt = " ".join(lst)

    return txt

def solve_v2(s):
    words = s.split()
    capitalized_words = [w.capitalize() for w in words]
    s = " ".join(capitalized_words)

    return s

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    print("Introduce el nomber y apellido: ")
    s = input()

    print("\nMostrando resultado: ")
    result = solve(s)

    print(result)
    #fptr.write(result + '\n')
    #fptr.close()