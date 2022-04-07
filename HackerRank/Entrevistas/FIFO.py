'''
    Metodo cargar() que añada un elemento a FIFO que es represnetado 
    por un array de enteros

    El FIFO solo acepta int >0

    El valor inicial del indice fifo es definido en el indice fifo ????

'''

# Inicializar pila
def initFIFO():
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
def cargar(pila, num, contador):

    # Comprobar el  estado pila
    state = checkFIFO(pila)

    if (state == 'vacia'):
        print("\nCargar op 1 - quedan huecos")
        pila.insert(0, num)
        pila.pop(fifo_size)
        contador += 1

    elif(state == 'llena'):
        print("\nCargar op 2 - llena")
        pila.pop(fifo_size-1) # Elimina el hueco vacio que estaría en la posicion ultima de la pila
        pila.insert(0,num)
    
    
    return contador

# Sacar elmento de la pila a partir de la posicion dada
def sacar(pila, contador):
    print("Sacando de {} la pos {}".format(pila, contador-1))
    # El primero que entro es el primero en salir
    pila.pop(contador-1)
    # Crea hueco en la primera posicion
    pila.insert(0,'')



# Mostrar estado acual de la pila
def mostrarFIFO(pila):
    print("\nMostrando pila: ")
    print(pila)

# Comprobar estado pila (si esta llena):
def checkFIFO(pila):
    estado = 'llena'
    for i in pila:
        if (i == ''):
            estado = 'vacia'
    
    return estado

# menu
def menu():

    print("\n----- MENU -----\n")
    print("1. Cargar numero\n")
    print("2. Sacar numero\n")
    print("3. Mostrar fifo\n")
    print("0. Salir\n")
    print("----------------\n")
    print("Introduce opcion: ")
    op = int(input())

    return op

# -------------------------------------- MAIN -------------------------------------
###################################################################################

if __name__ == '__main__':
    # Vars
    contador = 0
    
   
    #Init fifo
    fifo_size = initFIFO()
    fifo = ['']*fifo_size # Crear lista (pila) vacia
    print("\nMi pila fifo: {}".format(fifo)) 
    
    opcion = 100
    while(opcion != 0):

        opcion = menu()

        if opcion == 1:  # Cargar numero
            numero = pideNumero()

            contador = cargar(fifo, numero, contador)

        elif opcion == 2: 
            sacar(fifo, contador)
        
        elif opcion == 3:
            mostrarFIFO(fifo)

        elif opcion == 0:
            print("\nFinalizando programa...")
        
        else:
            print("ERROR.Opcion no valida\n")




