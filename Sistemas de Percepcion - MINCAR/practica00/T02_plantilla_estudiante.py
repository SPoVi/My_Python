# -*- coding: utf-8 -*-
__author__ = "mi_nombre_aqui"

"""
Date = 17/07/2018
Author = xxxxxxx
Project = Práctica 0, principios de python
"""

from practica00.T01_cargar_imagen import cargar_imagen,visualizar_imagen



if __name__ == "__main__":
    '''
       TODO: Modifica el script para que cargue una imagen cualquiera y guarda la figura que se 
       visualiza incluyendo en el título el nombre de estudiante
        	Escribir por pantalla el valor del píxel fila=30, columna=50 de la imagen.
        	Pintar la imagen con el nombre del estudiante y el valor del pixel en el título y almacenar la figura generada en ../data/out/p0/figura_prueba.png
        	Sube el código y las imágenes generadas a tu repositorio de código.
    '''
    file_path = '../data/underwater/Ancuti01.png'
    imagen_rgb = cargar_imagen(file_path)
    visualizar_imagen(imagen_rgb,titulo='nombre_del_estudiante')



