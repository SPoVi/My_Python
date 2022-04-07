'''
    Metodo cargar() que añada un elemento a FIFO que es represnetado 
    por un array de enteros

    El FIFO solo acepta int >0

    El valor inicial del indice fifo es definido en el indice fifo ????

'''

# Inicializar pila
def initLIFO():
    tam = 0
    while(tam <= 0):
        print("\nIntroduce el tamaño de la pila: ")
        tam = int(input())

        if (tam <= 0):
            print("\nERROR. Debe ser un numero real.")

    return tam
       
    
# Pedir numero
def pideNumero():
    num = 0
    while(num <= 0):
        print("\nIntroduce un numero del entero (>0): ")
        num = int(input())

        if (num <= 0):
            print("\nNumero no valido.")
        else:
            return num

    iPos = 0

    print("\nIntroduce el valor de la posicion (0 - {}): ".format(fifo_size-1))
    iPos = int(input())

    return iPos

    
# Cargar numero a la pila
def cargar(pila, num, pos=0):

    # Comprobar el  estado pila
    state = checkLIFO(pila)

    if (state == 'vacia'):
        print("\nCargar op 1 - quedan huecos")
        pila.insert(pos,num)
        pila.pop(-1)

    elif(state == 'llena'):
        print("\nCargar op 2 - llena")
        pila.pop(pos) # Elimina el hueco vacio que estaría en la posicion ultima de la pila
        pila.insert(pos,num)

# Sacar elmento de la pila a partir de la posicion dada
def sacar(pila, pos=0):
  
    pila.pop(pos)
    pila.insert(fifo_size-1,'')


# Mostrar estado acual de la pila
def mostrarLIFO(pila):
    print("\nMostrando pila: ")
    print(pila)

# Comprobar estado pila (si esta llena):
def checkLIFO(pila):
    estado = 'llena'
    for i in pila:
        if (i == ''):
            estado = 'vacia'
    
    return estado



    


if __name__ == '__main__':

    sacarNumero = 'n'
    continuar = 'y'
   
    #Init fifo
    fifo_size = initLIFO()
    fifo = ['']*fifo_size # Crear lista (pila) vacia
    print("\nMi pila fifo: {}".format(fifo)) 

    while(continuar == 'y'):

        
        numero = pideNumero()

        # Cargar numero
        cargar(fifo, numero)
        mostrarLIFO(fifo)

        # Sacar numero
        print('\nSacar numero? (y/n)')
        sacarNumero = input()

        if (sacarNumero == 'y'):
            sacar(fifo)
            mostrarLIFO(fifo)

        # Continuar ?
        print('\nDesa continuar? (y/n)')
        continuar = input()
        if (continuar == 'n'):
            print("\nFinalizando programa...")
            mostrarLIFO(fifo)





