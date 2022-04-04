'''
In this challenge, the task is to debug the existing code to successfully
 execute all provided test files.
---
Given an array of n distinct integers, transform the array into a zig zag
 sequence by permuting the array elements. 
 
 A sequence will be called a zig zag sequence if the first k elements in 
 the sequence are in increasing order and the last elements are in 
 decreasing order, where k = (n+1)/2. 
 
 You need to find the lexicographically smallest zig zag sequence of the 
 given array.
'''


def findZigZagSequence(a, n):
    #Odenar de menor a mayor
    a.sort()
    print("\nArray ordenado: {}".format(a))

    '''
    Tras hacer el sort, la parte de la izquieda del array queda ordenado
    de menos a mas.

    Ahora hay que hacer la parte de la derecha. Tiene que estar ordenada
    de mas a menos desde el elemento central.
    '''
    # Posicion medio del array
    mid = int((n + 1)/2)
    print("\nValor mid: {}".format(mid))
    # Intercambio de posiciones del lado derecho del array
    a[mid-1], a[n-1] = a[n-1], a[mid-1]  # n-1: ultima pos del array
                                     # mid: mitad + 1 pos del array
    '''
    Para n = 7 y a = [2, 3, 5, 4, 1, 7 , 6] 
    a[4], a[6] = a[6], a[4] : [1, 2, 7, 4, 5, 6]
    '''

    # Una posicion mas ala derecha del medio
    st = mid     # st : 4
    # Ultima posicion del array
    ed = n - 2      # ed : 7 - 2  = 5

    print("\nst: {}\ted: {}".format(st,ed))
    print("\nEntrando en el bucle while: ")
    # Mientras que la posicion a intercambiar no sea la ultima del array
    # hacer el cambio de posicion
    # Desplazamiento a la derecha del numero mas alto hasta llegar al 
    # centro del array.
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        # a[4], a[5] = a[5], a[4]
        st = st + 1
        ed = ed - 1
        print("\nst: {}\ted: {}".format(st,ed))
        print(a)

    print("\n\nSolucion:")
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

if __name__ == "__main__":
    print("\nIntroduce el numero de casos: ")
    #test_cases = int(input())
    test_cases = 1

    for cs in range (test_cases):
        print("\nIntroduce el numero de elementos del array: ")
        #n = int(input())
        n = 9

        print("\nIntroduce {} numeros enteros: ".format(n))
        #a = list(map(int, input().split()))
        a = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
        
        
        findZigZagSequence(a, n)