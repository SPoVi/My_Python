'''
In Python, a string of text can be aligned left, right and center.

.ljust(width)
    This method returns a left aligned string of length width.

.center(width)
    This method returns a centered string of length width.

.rjust(width)
    This metdho returns a right aligned string of length width.
'''

'''
TASK

You are given a partial code that is used for generating the HackerRank 
Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

'''

if __name__ == "__main__":
#Replace all ______ with rjust, ljust or center. 

    #thickness = int(input()) #This must be an odd number
    thickness = 5
    c = 'H'
    print("\nFigure:\n\n")

    #Top Cone
    for i in range(thickness):
        # Imprimir H de 0 a 4 veces a una distancia de la izquierda (justificado por la derecha) desde la posicion  'anchura'-1 
        # Imprimir H
        # Imprimir H de 0 a 4 veces a una distancia de la derecha (justificado por la izquieda) desde la posicion 'anchura'-1
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        # Imprimir H 'anchura' veces (5) centrado desde la posicion 'anchura'*2 (10) y otra igual desde la posicion 'anchura'*6
        # Hacer esto 'anchura' + 1  veces (0 a 5 = 6 veces)
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        # Cantidad de H a imprimir  desde la posicion X de forma centrada
        print((c*thickness*5).center(thickness*6))    

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))