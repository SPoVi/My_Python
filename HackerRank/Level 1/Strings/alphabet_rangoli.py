'''
You are given an integer, N. 

Your task is to print an alphabet rangoli of size . 
(Rangoli is a form of Indian folk art based on creation of patterns.)

#size 3

----c---- 8 +1
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

---------

#size 5  

------- -e- ------- 17
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''




def print_rangoli(n):
    from string import ascii_lowercase as chars

    # Para n = 3
        # Guion + char de i:n empezando del final al principio
            # - 3 - 2 - 1
            # - 3 - 2
            # - 3 
        # Añade un guion y encadena desde la posicion 1 desde i:n, es decir salta la posicion 0 correspondiente a la letra de en medio
            # - 2 - 3
            # - 3
            # - 
        # Lo centra todo desde la anchura, y el resto lo llena con guinoes

        # A la hora de imprimir lo hace empezando a la inversa, dado que la primera fila es la de en medio.
        # Utiliza puntero para acceder al valor, dado que es una matriz

    heap = [(('-'.join(chars[i:n])[::-1]+'-'.join(chars[i:n])[1:])).center(4*n-3, '-')for i in range(n)]
    #print(*(heap[::-1]+heap[1:]), sep="\n")

    print(*heap[::-1], sep='\n')
    print(*heap[1:], sep='\n')

if __name__ == '__main__':
    print("Introduce numero entero: (0-27)")
    n = int(input())
    print("Showing Rangoli Alphabet Matrix: \n")
    print_rangoli(n)