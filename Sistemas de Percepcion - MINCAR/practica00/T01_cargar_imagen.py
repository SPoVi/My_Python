# -*- coding: utf-8 -*-
__author__ = "Grupo 9: Haritz, Pablo & Sergio"

"""
Date = 20/04/2020
Author = Grupo 9: Haritz, Pablo & Sergio
Project = Práctica 0, principios de python
"""

'''
   En este código proporcionamos herramientas que nos van a permitir cargar, guardar y visualizar 
   imágenes. Lo usaremos durante todas las prácticas.
   
   TODO: Entiende este código y haz que funcione asegurándote de que tienes bien elegido el intérprete    
'''

#Aquí importo las librerías que me resultan útiles
import skimage, sklearn, skimage.io
import numpy, scipy
#Para escribir menos puedo poner alias a lo que importo:
import numpy as np
import matplotlib.pyplot as plt
import os

#Las funciones de python se definen con def. El contenido se escribe indentado:
def cargar_imagen(nombre_fichero):   # def nombre_funcion(variable)
    '''
    Carga una imagen a partir de un fichero
    :param nombre_fichero: Nombre del fichero
    :return:
    '''
    imagen_rgb = skimage.io.imread(nombre_fichero)
    return imagen_rgb

def guardar_imagen(nombre_fichero, imagen_rgb):
    '''
    Guarda una imagen y crea el subdirectorio si no existe.
    :param nombre_fichero: Nombre del fichero
    :param imagen_rgb: imagen numpy array para guardar
    :return:
    '''
    # Crea el directorio si no existe
    folder, filename = os.path.split(nombre_fichero)
    try:
        os.makedirs(folder)
    except:
        pass
    #Guarda la imagen
    skimage.io.imwrite(nombre_fichero, imagen_rgb)

def visualizar_imagen(imagen,titulo = 'nombre_del_estudiante',block = True,save_figure=False,figure_save_path='../data/out/fig_sample.png',rescale_colors=True):
    '''
    Esta función visualiza y almacena una imagen y salva la figura si se indica
    :param imagen_rgb: imagen RGB de tipo numpy array
    :param titulo: Indica el nombre del estudiante más la información adicional requerida
    :param block: Permite que al visualizar la imagen en programa pare hasta cerrar la ventana
    :return:
    '''

    fig,ax = plt.subplots(1,1,sharex=True,sharey=True)
    if len(imagen.shape)==2:
        if rescale_colors:
            ax.imshow(imagen,cmap=plt.get_cmap('gray'))
        else:
            ax.imshow(imagen)

    else:
        ax.imshow(imagen)
    ax.set_title(titulo)
    if save_figure:
        folder, filename = os.path.split(figure_save_path)
        try:
            os.makedirs(folder)
        except:
            pass
        plt.savefig(figure_save_path, dpi=600)
    plt.show(block=block)

def visualizar_imagenes(lista_imagen,lista_titulos,n_row,n_col,block = True,save_figure=False,figure_save_path='../data/out/fig_sample.png',rescale_colors=True):
    '''
    Esta función visualiza y almacena una imagen y salva la figura si se indica
    :param imagen_rgb: imagen RGB de tipo numpy array
    :param titulo: Indica el nombre del estudiante más la información adicional requerida
    :param block: Permite que al visualizar la imagen en programa pare hasta cerrar la ventana
    :return:
    '''
    if n_row<2:
        raise Exception('n_row tiene que ser mayor que 2')
    fig,ax = plt.subplots(n_row,n_col,sharex=True,sharey=True)

    nc=0
    nr=0
    if n_col > 1:
        for i,(imagen,titulo) in enumerate(zip(lista_imagen,lista_titulos)):
            try:
                if len(imagen.shape)==2:
                    if rescale_colors:
                        ax[nr,nc].imshow(imagen,cmap=plt.get_cmap('gray'))
                    else:
                        ax[nr, nc].imshow(imagen, cmap=plt.get_cmap('gray'))
                else:
                    ax[nr,nc].imshow(imagen)
                ax[nr,nc].set_title(titulo)
            except:
                pass
            nr += 1
            if nr == n_row:
                nr = 0
                nc += 1
    else:
        for i, (imagen, titulo) in enumerate(zip(lista_imagen, lista_titulos)):
            try:
                if len(imagen.shape) == 2:
                    ax[nr].imshow(imagen, cmap=plt.get_cmap('gray'))
                else:
                    ax[nr].imshow(imagen)
                ax[nr].set_title(titulo)
            except:
                pass
            nr += 1
            if nr == n_row:
                nr = 0
                nc += 1


    if save_figure:
        folder, filename = os.path.split(figure_save_path)
        try:
            os.makedirs(folder)
        except:
            pass
        plt.savefig(figure_save_path, dpi=600)
    plt.show(block=block)

#Es buena costumbre meter este if al final para evitar que se ejecute código al importar este script desde otro.
if __name__ == "__main__":

    file_path = '../data/underwater/Ancuti01.png'
    imagen_rgb = cargar_imagen(file_path)
    pixel_info = imagen_rgb[20,30,:]
    visualizar_imagen(imagen_rgb,titulo='Grupo 9, El valor RGB del pixel (20,30) es %d,%d,%d' % (pixel_info[0],pixel_info[1],pixel_info[2]),save_figure=True,figure_save_path='../data/out/practica0/fig_sample.png')



