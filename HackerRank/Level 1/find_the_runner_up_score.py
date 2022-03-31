'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given scores. 

Store them in a list and find the score of the runner-up. 
'''

print("Introduce la cantidad de numeros: ")
n = int(input())
arr = []
print("Introduce los numeros: ")
for i in range(n):
    arr.append(int(input()))

print(arr)

print("\nPuntuacion del segundo clasificado: ")
score = sorted(set(arr))[-2]
print(score)