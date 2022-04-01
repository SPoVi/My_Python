'''
Game Rules

Both players are given the same string,S.

Both players have to make substrings using the letters of the string S.

Player 1 has to make words starting with consonants.
Player 2 has to make words starting with vowels.

The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

'''

def minion_game(string):
    # your code goes here
    vowels = ['a','e','i','o', 'u', 'A','E', 'I', 'O', 'U'] # in / not in .tolower()

    my_list = []
    len_string = len(string)

    # Crear lista con todas las soluciones, del P1 y P2
    for n in range(len_string):
        for i in range(len_string):
            output = string[n:i+1]          # Desde el principio hasta
            if output != '':               # Si no es un espacio en blanco
                my_list.append(output)
    
    # Contadores de los jugadores
    counter_p1 = 0  # consonantes
    counter_p2 = 0  # vocales
    for i in my_list:
        if i[0] not in vowels:
            counter_p1 += 1
        else:
            counter_p2 += 1

    
    
    print("\n--MY LISTA DE RESPUESTAS--\n")
    print(my_list)

    print("\n--Puntuaciones--\n")
    print("Player 1: "+str(counter_p1))
    print("Player 2: "+str(counter_p2))


    # Seleccionar ganador
    print("\n--RESULT--\n")
    if counter_p1 > counter_p2:
        print("P1 wins")
    elif counter_p1 < counter_p2:
        print("P2 wins")
    else:
        print("draws")
      

if __name__ == '__main__':
    s = input()
    minion_game(s)


'''
OTRA SOLUCION

# Enter your code here. Read input from STDIN. Print output to STDOUT
vowels = ['A', 'E', 'I', 'O', 'U']
s = raw_input()
a = 0
b = 0
for i, c in enumerate(s):  # crea lista de tuplas con (pos, valor) : [(0, hola), (1, mundo)]
    if c in vowels:
        b += len(s) - i
    else:
        a += len(s) - i
        
if a == b:
    print "Draw"
elif a > b:
    print 'Stuart {}'.format(a)
else:
    print 'Kevin {}'.format(b)
'''