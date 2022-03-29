# -*- coding: utf-8 -*-
__author__ = "Grupo 9: Haritz, Pablo & Sergio"

import matplotlib.pyplot as plt
import numpy as np
import skimage,skimage.io
from practica00.T01_cargar_imagen import visualizar_imagen
from practica00.T01_cargar_imagen import visualizar_imagenes

file_img_01 = '../data/color/barrio_sesamo.jpg'
file_img_02 = '../data/color/espinete.jpg'


def integrar_a_espinete():

    img_grupo = skimage.io.imread(file_img_01)          # Lectura de img grupo
    img_espinete= skimage.io.imread(file_img_02)        # Lectura de img espinete

    visualizar_imagen(img_grupo, titulo='imagen grupo')         # Visualizar img
    visualizar_imagen(img_espinete, titulo='imagen espinete')

    '''
        NOMBRE: 
        TODO:        
            Sobre la imagen de grupo
            Extraer los tres canales de color y pintarles por separado. 
            Guarda los tres canales de color por separado
    '''
    canal_R = img_grupo[:, :, 0]  # blue
    canal_G = img_grupo[:, :, 1]  # green
    canal_B = img_grupo[:, :, 2]  # red

    visualizar_imagen(canal_R, titulo='Grupo color Rojo', save_figure = True, figure_save_path ='../data/out/practica1/fig_espinete_r.png')
    visualizar_imagen(canal_G, titulo='Grupo color Verde', save_figure = True, figure_save_path ='../data/out/practica1/fig_espinete_g.png')
    visualizar_imagen(canal_B, titulo='Grupo color Azul', save_figure = True, figure_save_path ='../data/out/practica1/fig_espinete_b.png')

    '''
        NOMBRE:
        TODO:
            Sobre la imagen de grupo
            Pon a cero todos los canales menos uno y pinta la imagen resultante.
            Repite con las tres combinaciones posibles. 
    '''

    img_for_r = img_grupo.copy()
    img_for_r[:, :, 1] = 0                  # canal verde a zero
    img_for_r[:, :, 2] = 0                  # canal azul a zero


    visualizar_imagen(img_for_r, titulo='Imagen solo con tonos rojos', save_figure = True,
                      figure_save_path ='../data/out/practica1/fig_espinete_r2.png')

    img_for_g = img_grupo.copy()
    img_for_g[:, :, 0] = 0                  # canal rojo a zero
    img_for_g[:, :, 2] = 0                  # canal azul a zero

    visualizar_imagen(img_for_g, titulo='Imagen solo con tonos verdes', save_figure = True,
                      figure_save_path ='../data/out/practica1/fig_espinete_g2.png')

    img_for_b = img_grupo.copy()
    img_for_b[:, :, 0] = 0  # canal rojo a zero
    img_for_b[:, :, 1] = 0  # canal verde a zero

    visualizar_imagen(img_for_b, titulo='Imagen solo con tonos azules', save_figure = True,
                      figure_save_path ='../data/out/practica1/fig_espinete_b2.png')
    '''
        NOMBRE: Sergio
        TODO:
            Mediante slicing, extraer las caras de coco, epi, blas y triki y visualizar cada cara en un subplot.
            Graba las figuras resultantes
    '''
    img_in = skimage.io.imread(file_img_01)
    # Cara de coco
    img_roi_coco = img_in[40:140, 320:410, :] #Vertical, Horizontal
    visualizar_imagen(img_roi_coco, titulo='Coco', save_figure=True,
                      figure_save_path='../data/out/practica1/fig_cara_coco.png')
    # Cara de epi
    img_roi_epi = img_in[120:220, 90:210, :]
    visualizar_imagen(img_roi_epi, titulo='Epi', save_figure=True,
                      figure_save_path='../data/out/practica1/fig_cara_epi.png')
    # Cara de blas
    img_roi_blas = img_in[200:340, 120:230, :]
    visualizar_imagen(img_roi_blas, titulo='Blas', save_figure=True,
                      figure_save_path='../data/out/practica1/fig_cara_blas.png')
    # Cara de triki (monstruo de las galletas)
    img_roi_triki = img_in[30:120, 110:230, :]
    visualizar_imagen(img_roi_triki, titulo='Triki', save_figure=True,
                      figure_save_path='../data/out/practica1/fig_cara_triki.png')


    # Creacion subplot
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Caras teleñecos')

    axs[0, 0].imshow(img_roi_coco)
    axs[0, 0].set_title('Coco')
    axs[0, 1].imshow(img_roi_epi)
    axs[0, 1].set_title('Epi')
    axs[1, 0].imshow(img_roi_blas)
    axs[1, 0].set_title('Blas')
    axs[1, 1].imshow(img_roi_triki)
    axs[1, 1].set_title('Triki')

    # Guadar la imagen. Metodo 1
    fig.savefig('../data/out/practica1/fig_caras_teleñecos_metodo1.png')

    # Metodo 2
    # Para guardar la igamen se ha creado una lista de imagenes y de titulos y ha sido necesario
    # importar otra funcion 'visiualizar_imagenes'
    f1 = img_roi_coco.copy()
    t1 = 'Coco'
    f2 = img_roi_epi.copy()
    t2 = 'Epi'
    f3 = img_roi_blas.copy()
    t3 = 'Blas'
    f4 = img_roi_triki.copy()
    t4 = 'Triki'

    lista_imagenes = [f1, f2, f3, f4]
    lista_titulos = [t1, t2, t3, t4]

    '''visualizar_imagenes(lista_imagen, lista_titulos, n_row, n_col, block=True, save_figure=False,
                            figure_save_path='../data/out/fig_sample.png', rescale_colors=True):'''
    visualizar_imagenes(lista_imagenes,lista_titulos,2,2, block=True, save_figure=True,
                      figure_save_path='../data/out/practica1/fig_caras_teleñecos_metodo2.png')

    '''
        NOMBRE:
        TODO:
            Espinete (al que no conocéis igual), no se encuentra en la foto de grupo, tratad de incluirle mediante slicing y visualizar la foto
            Bonus: Pega a Espinete de forma elegante mediante el uso de las máscaras que hemos usado en el otro script.
            Graba las figuras resultantes
            Explica el algoritmo desarrollado
            Respuesta:
            
            Para la resolución del siguente apartado donde se realiza a inclusión de una imagen dentro de otra se lleva
            a cabo una operación sencilla mediante el uso de máscaras. 
            Para ello se debe realizar una máscara de la nueva imagen que será incluida en la base. Esta máscara y 
            su inversa serán utilizadas para diferenciar las partes usadas de las inservibles de cada imagen. Por lo 
            tanto se conseguira una imagen donde espinete este separado de su fondo y otra donde la imagen base tenga 
            representado con ceros la silueta de espinete para posteriormente sumar ambas dos y conseguir la imagen 
            final sin ningun tipo de alteración de color. 
    '''
    # Se generan copias de las imagenes a tratar para proteger las originales
    img_barrio = img_grupo.copy()
    img_espi = img_espinete.copy()

    # Seleccionar la zona de la imagen grupal donde va a ir colocado espinete teniendo en cuanta sus dimensiones
    rows, cols,channels = img_espi.shape
    roi = img_barrio[170:170+rows, 430:430+cols,:]

    # Se transforma la imagen de espinete a niveles de gris, esto convierte sus valores al rango [0,1]
    img_espi_gris = skimage.color.rgb2gray(img_espi)

    # Se genera una máscara con la forma de espinete.
    threshold = 0.9                                         # Para ello se determina un umbral de grises
    mask = img_espi_gris < threshold                        # los niveles de gris inferiores serán seleccionados
                                                            # y formarán la máscara.
    visualizar_imagen(mask, titulo='máscara espinete')

    # mascara invertida
    mask_inv = np.logical_not(mask)
    visualizar_imagen(mask_inv, titulo='máscara invertida')

    #Crear las máscaras con tres canales para que soporten RGB y poder multiplicar
    mask_inv = np.stack((mask_inv,mask_inv,mask_inv),axis=-1)
    mask = np.stack((mask, mask, mask),axis=-1)

    # La zona que no es necesaria de la imagen de espinete es eliminada con su máscara y posteriormente la imagen
    # resultante multiplicada por la imagen original para conseguir una mayor nitidez en la respuesta
    img_espi_limpia = np.logical_and(mask,img_espi)*img_espi
    visualizar_imagen(img_espi_limpia, titulo='espinete limpio')

    # Se hace lo mismo en la zona de la imagen original donde iba a ir espinete, dejando ahora su figura a 0 para que
    # no se vean modificados los colores a la hora de hacer la suma de ambas imagenes
    img_roi_limpia = np.logical_and(mask_inv,roi) * roi
    visualizar_imagen(img_roi_limpia, titulo='base con 0 en espinete')

    # Se termina por integrar ambas imagenes
    dst = img_roi_limpia + img_espi_limpia
    visualizar_imagen(dst, titulo='suma')

    # La imagen final se coloca en su respectiva posicion de la imagen grupal
    img_barrio[170:170+rows, 430:430+cols] = dst
    # Se visualizan los resultados y se guardan
    visualizar_imagen(img_barrio, titulo='Espinete con sus amigos', save_figure=True,
                      figure_save_path='../data/out/practica1/fig_espiyfriend_mascara.png')


if __name__ == "__main__":
    integrar_a_espinete()
    input()