#!/usr/bin/env python3

'''You are given three integers 'x,y,z' and representing the dimensions of a cuboid along with an integer 'n' . 
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of 'i+j+k'is not equal to 'n'.
'''
print("Introduce x: ")
x = int(input())
print("Introduce y: ")
y = int(input())
print("Introduce z: ")
z = int(input())
print("Introduce n: ")
n = int(input())

matrix = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]

print("-- SOLUTION --")
matrix2 = [line for line in matrix if sum(line) != n]
print(matrix2)