'''
Given an integer, n , and n space-separated integers as input, create a tuple,t
, of those n integers. Then compute and print the result of hash(t)

.

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported. 
'''

from builtins import hash

print("Introduce la cantidad de elementos en la tupla: ")
n = int(input())

n_list= []
print("Introduce "+str(n)+" numeros: ")
for _ in range(n):
    n_list.append(int(input()))

# Tupla
tup = ()
for number in n_list:
    tup+=(number,)


print(hash(tup))
