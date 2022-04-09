'''
Given an integer,n , print the following values for each integer i from  1 to n:

    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary

'''

def print_formatted(number):
    # your code goes here
    for i in range(number):

        decimal = i
        octal = format(i,'o')
        hexadecimal = format(i, 'X')
        binario = format(i, 'b')
        print("{}\t{}\t{}\t{}\t".format(decimal, octal, hexadecimal, binario))

def print_formatted_v2(number):
    # Para imprimir con una distancia de separacion igual al numero 'n' en binario
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

if __name__ == '__main__':
    print("Introduce un numero entero: ")
    n = int(input())
    print_formatted(n)