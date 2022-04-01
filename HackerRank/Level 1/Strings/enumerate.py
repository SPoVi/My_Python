vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
print("Introduce cadena: ")
s = input()
a = 0
b = 0

print("Cadena: {}".format(s))
for i, c in enumerate(s):  # crea lista de tuplas con (pos, valor) : [(0, hola), (1, mundo)]
    # i: counter
    # c: value
    print("\nCount = {};     Value = {}".format(i,c))

    # La cantidad de letras que hay despues de la posicion comprobada será la cantidad
    # de palabras que puede formar
    
    if c in vowels:
        b += len(s) - i #tamaño de la palbra - posicion del enumerate, la letra que se esta comprobando
    else:
        a += len(s) - i

    print("\nP1 (empieza por consonante): {}".format(a))
    print("P2 (empieza por vocal): {}".format(b))