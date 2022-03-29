# -*- coding: utf-8 -*-
__author__ = "Grupo 9: Haritz, Pablo & Sergio"

'''
   TODO: Entiende este código y haz que funcione asegurándote de que tienes bien elegido el intérprete 
'''

#Aquí importo las librerías que me resultan útiles
import skimage,sklearn
import numpy,scipy
#Para escribir menos puedo poner alias a lo que importo:
import numpy as np
import matplotlib.pyplot as plt

# Operaciones basicas de Python

# un comentario se hace con almohadilla

# 1 - Visualizar textos
print('Esto es un texto de python') # comilla simple
print("Esto tambien es un texto de python") # doble comilla
num1 = 1
num2 = 0.5
print("Esto tambien es un texto de python con el número entero %d y el número real  %f metido en la cadena" % (num1,num2)) # doble comilla

#Numpy nos permite trabajar con arrays y matrices, de forma muy parecida a Matlab
A = np.uint8(np.ones((8, 8)))
print(A)
B = np.uint8(np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]))
print(B)

#Podemos acceder a todas las filas o columnas de una matriz mediante el operador :
A[0, :] = 0
A[:, 0] = 0
A[:, 7] = 0
A[7, :] = 0
print(A)

#Podemos acceder a subregiones de la matriz accediendo mediante el operador corchete
A[2:5, 3:6] = 2
print(A)

#Tambien podemos crear matrices 3D, perfectas para guardar imágenes
ancho_imagen = 100
alto_imagen = 100
imagen = np.zeros((alto_imagen,ancho_imagen,3))
print(imagen.shape)

#Python es muy limpio, para indicar el alcance de una función no se usan ni begin-end ni llaves, todo se indenta de forma ordenada

if imagen.shape[0]>10:
    print('La imagen es suficientemente grande')
    print('esto está dentro del if')
else:
    print('La imagen es pequeña')
print('esto no está dentro del else porque no está indentado')

#Este for cuenta de cero al nueve
for i in range(10):
    print(i)

#prueba