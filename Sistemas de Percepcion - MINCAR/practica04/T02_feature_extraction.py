# -*- coding: utf-8 -*-
__author__ = 106360

import matplotlib.patches as mpatches
from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.morphology import closing, square
from skimage.color import label2rgb
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from practica00.T01_cargar_imagen import visualizar_imagenes,visualizar_imagen
import skimage, skimage.io
import pandas as pd

file_geometrias = '../data/color/geometrias.png'

# Codigo para pintar las img en una nueva ventana
import matplotlib
matplotlib.use('TkAgg')

def do_test_image_figuras():
    '''
    NOMBRE:
    TODO:
        Ejecuta el script y analiza el listado de descriptores que se obtienen.

    '''


    image_rgb = skimage.io.imread(file_geometrias)  # Carga imagen rgb

    visualizar_imagen(image_rgb,'Imagen_Original')

    image_gray = skimage.color.rgb2gray(image_rgb)  # Convierte a escala grises
    image_binary = image_gray>0.1
    image_binary_filtered = skimage.morphology.binary_closing(image_binary)  # filtro closing binario
    visualizar_imagen(image_binary_filtered, 'Imagen binaria')

    # label image regions
    # Etiquetado de las regiones en la imagen
    label_image = label(image_binary_filtered)
    visualizar_imagen(label_image, 'Etiquetada')
    image_label_overlay = label2rgb(label_image, image=image_rgb) # paso a color


    # Creacion de img compuesta por multiples img
    fig, ax = plt.subplots(figsize=(10, 6)) # tamaño 1000x600
    ax.imshow(image_label_overlay)

    lista_descriptores=[]       # crea lista vacia para usar luego
    for region in regionprops(label_image):

        if region.area >= 10:

            # Dibuja rectangulo alrededor de las estrellas y circulos
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(rect)

            # guarda datos en la lista de cada etiqueta
            lista_descriptores.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])

    ax.set_axis_off()
    plt.tight_layout()
    plt.show()

    #Pandas es una librería para manejo de datos.
    pandas_dataframe_descriptores = pd.DataFrame.from_records(lista_descriptores, columns=['Label','Area','Extent','Solidity','Eccentricity'],index='Label')

    print(pandas_dataframe_descriptores)

def do_test_image_figuras_2():
    '''
    NOMBRE:
    TODO:
        Modifica el script anterior de tal forma que:
        - Las estrellas les pinte un recuadro rojo
        - Los círculos y cuadrados les pinte un recuadro verde.
        Almacena las imágenes en /data/out/practica05/fig_feature_extraction_xxx.png
        Comenta el método empleado:
        Respuesta:
    '''

    image_rgb = skimage.io.imread(file_geometrias)  # Carga imagen rgb

    visualizar_imagen(image_rgb,'Imagen Original', save_figure=True,
                      figure_save_path='../data/out/practica04/T02/fig_feature_extraction_001.png')

    image_gray = skimage.color.rgb2gray(image_rgb)  # Convierte a escala grises
    image_binary = image_gray>0.1
    image_binary_filtered = skimage.morphology.binary_closing(image_binary)  # filtro closing binario
    visualizar_imagen(image_binary_filtered, 'Imagen binaria', save_figure=True,
                      figure_save_path='../data/out/practica04/T02/fig_feature_extraction_002.png')

    # label image regions
    # Etiquetado de las regiones en la imagen
    label_image = label(image_binary_filtered)
    image_label_overlay = label2rgb(label_image, image=image_rgb) # paso a color
    visualizar_imagen(image_label_overlay, 'Etiquetada a color', save_figure=True,
                      figure_save_path='../data/out/practica04/T02/fig_feature_extraction_003.png')

    # Creacion de img compuesta por multiples img
    fig, ax = plt.subplots(figsize=(10, 6)) # tamaño 1000x600
    ax.imshow(image_label_overlay)

    lista_descriptores=[]       # crea lista vacia para usar luego
    lista_circulos_cuadrados=[]
    lista_estrellas=[]
    for region in regionprops(label_image):

        if region.area >= 10 and region.solidity >= 0.9:
            # Dibuja rectangulo verde (circulos y cuadrados)
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='green', linewidth=2)
            ax.add_patch(rect)


            # guarda datos en la lista global de cada etiqueta
            lista_descriptores.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])
            # guarda datos en la lista de cuadrados y circulos
            lista_circulos_cuadrados.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])

        elif region.area >=10 and region.solidity <0.9:
            # Dibuja rectangulo verde (circulos y cuadrados)
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(rect)

            # guarda datos en la lista global de cada etiqueta
            lista_descriptores.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])
            # guarda datos en la lista de estrellas
            lista_estrellas.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])

    ax.set_title('Diferenciacion de figuras: Estrllas(r), Círculos-Cuadrados(g)')
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig.savefig('../data/out/practica04/T02/fig_feature_extraction_004.png')


    #Pandas es una librería para manejo de datos.
    pandas_dataframe_descriptores = pd.DataFrame.from_records(lista_descriptores, columns=['Label','Area','Extent','Solidity','Eccentricity'],index='Label')
    panda_dataframe_circulos_cuadrados = pd.DataFrame.from_records(lista_circulos_cuadrados,columns=['Label','Area','Extent','Solidity','Eccentricity'],index='Label')
    panda_dataframe_estrellas = pd.DataFrame.from_records(lista_estrellas,columns=['Label','Area','Extent','Solidity','Eccentricity'],index='Label')

    print('             ---LISTA GLOBAL---')
    print(pandas_dataframe_descriptores)
    print('\n')
    print('      ---LISTA CUADRADOS Y CRICULOS---')
    print(panda_dataframe_circulos_cuadrados)
    print('\n')
    print('            ---LISTA ESTRELLAS---')
    print(panda_dataframe_estrellas)

    pass

def do_test_image_figuras_3():
    '''
    NOMBRE:
    TODO:
        Modifica el script anterior de tal forma que:
        - Las estrellas 4 puntas les pinte un recuadro rojo
        - las estrllas de 5 puntas les pinte un recuadro amarillo
        - Los círculos los pinte un recuadro verde.
        - Los cuadrados los pinte un recuadro azul.
        Almacena las imágenes en /data/out/practica05/fig_feature_extraction_xxx.png
        Comenta el método empleado:
        Respuesta:

        - Primero se ha diferenciado enter las estrellas y los rectangulos-cuadrados. Para ello se ha usado como elemtento
          diferencial su propiedad 'solidity'. Los valores muy proximos al 1 indica que es un cuadrado o un circulo.
        - Para diferenciar entre cuadrados y circulos se ha usado como elemento diferencial su propiedad 'extent'.
          Valores muy proximos al 1 indican que es un cuadrado.
        - Para diferenciar las estrellas de 4 puntdas de las de 5 puntas se ha usado como elemento diferencial su
          propiedad 'eccentricity'. Valores por debajo de 0.3 indican que tiene 5 puntas.
    '''

    image_rgb = skimage.io.imread(file_geometrias)  # Carga imagen rgb

    visualizar_imagen(image_rgb,'Imagen Original')

    image_gray = skimage.color.rgb2gray(image_rgb)  # Convierte a escala grises
    image_binary = image_gray>0.1
    image_binary_filtered = skimage.morphology.binary_closing(image_binary)  # filtro closing binario
    visualizar_imagen(image_binary_filtered, 'Imagen binaria')

    # label image regions
    # Etiquetado de las regiones en la imagen
    label_image = label(image_binary_filtered)
    visualizar_imagen(label_image, 'Etiquedata')
    image_label_overlay = label2rgb(label_image, image=image_rgb) # paso a color
    visualizar_imagen(image_label_overlay, 'Etiquetada a color')

    # Creacion de img compuesta por multiples img
    fig, ax = plt.subplots(figsize=(10, 6)) # tamaño 1000x600
    ax.imshow(image_label_overlay)

    lista_descriptores=[]       # crea lista vacia para usar luego
    lista_circulos=[]
    lista_cuadrados=[]
    lista_estrellas_4puntas=[]
    lista_estrellas_5puntas=[]
    for region in regionprops(label_image):

        if region.area >= 10 and region.solidity >= 0.9: # es un cuadrado o un círculo

            if region.extent >0.95: # es un cuadrado

                # Dibuja rectangulo azul (cuadrado)
                minr, minc, maxr, maxc = region.bbox
                rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                          fill=False, edgecolor='blue', linewidth=2)
                ax.add_patch(rect)
                # guarda datos en la lista de cuadrados
                lista_cuadrados.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])
            else:
                # Dibuja rectangulo verde (circulos)
                minr, minc, maxr, maxc = region.bbox
                rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                          fill=False, edgecolor='green', linewidth=2)
                ax.add_patch(rect)
                # guarda datos en la lista circulos
                lista_circulos.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])


            # guarda datos en la lista global de cada etiqueta
            lista_descriptores.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])


        elif region.area >=10 and region.solidity <0.9: # Son estrellas

            if region.eccentricity < 0.3:
                # Dibuja rectangulo amarillo estrella 5 puntas
                minr, minc, maxr, maxc = region.bbox
                rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='yellow', linewidth=2)
                ax.add_patch(rect)

                # guarda datos en la lista global de cada etiqueta
                lista_descriptores.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])
                # guarda datos en la lista de estrellas
                lista_estrellas_5puntas.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])

            else:
                # Dibuja rectangulo rojo (estrella 4 puntas)
                minr, minc, maxr, maxc = region.bbox
                rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                          fill=False, edgecolor='red', linewidth=2)
                ax.add_patch(rect)

                # guarda datos en la lista global de cada etiqueta
                lista_descriptores.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])
                # guarda datos en la lista de estrellas
                lista_estrellas_4puntas.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])

    ax.set_title('Diferenciacion de figuras: Estrellas 4 Puntas(r), Estrellas 5 Puntas(y), Círculos(g) y Cuadrados(b)')
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig.savefig('../data/out/practica04/T02/fig_feature_extraction_005.png')


    #Pandas es una librería para manejo de datos.
    pandas_dataframe_descriptores = pd.DataFrame.from_records(lista_descriptores, columns=['Label','Area','Extent','Solidity','Eccentricity'],index='Label')
    panda_dataframe_cuadrados = pd.DataFrame.from_records(lista_cuadrados,columns=['Label','Area','Extent','Solidity','Eccentricity'],index='Label')
    panda_dataframe_circulos = pd.DataFrame.from_records(lista_circulos,columns=['Label','Area','Extent','Solidity','Eccentricity'],index='Label')
    panda_dataframe_estrellas_4puntas = pd.DataFrame.from_records(lista_estrellas_4puntas,columns=['Label','Area','Extent','Solidity','Eccentricity'],index='Label')
    panda_dataframe_estrellas_5puntas = pd.DataFrame.from_records(lista_estrellas_5puntas,columns=['Label','Area','Extent','Solidity','Eccentricity'],index='Label')

    print('             ---LISTA GLOBAL---')
    print(pandas_dataframe_descriptores)
    print('\n')
    print('             ---LISTA CUADRADOS---')
    print(panda_dataframe_cuadrados)
    print('\n')
    print('             ---LISTA CRICULOS---')
    print(panda_dataframe_circulos)
    print('\n')
    print('     ---LISTA ESTRELLAS 4 PUNTAS---')
    print(panda_dataframe_estrellas_4puntas)
    print('\n')
    print('     ---LISTA ESTRELLAS 5 PUNTAS---')
    print(panda_dataframe_estrellas_5puntas)

    pass
if __name__ == "__main__":
    # do_test_image_figuras()
    # do_test_image_figuras_2()
    do_test_image_figuras_3()