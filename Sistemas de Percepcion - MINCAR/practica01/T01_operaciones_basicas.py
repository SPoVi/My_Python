# -*- coding: utf-8 -*-
__author__ = "Grupo 9: Haritz, Pablo & Sergio"

import matplotlib.pyplot as plt
import numpy as np
import skimage,skimage.io
from practica00.T01_cargar_imagen import visualizar_imagen

'''
TODO: Elige una imagen para usar
'''
file_img_elegida_estudiante = '../data/color/Manzanas.jpg'
file_img_01 = '../data/underwater/Ancuti01.png'
file_img_02 = '../data/underwater/Ancuti03.png'
file_logo= '../data/mascaras/logo_ehu.png'
file_base = '../data/mascaras/orto.jpg'
#import cv2

def do_test01():
    '''
    NOMBRE: Sergio
    TODO:
        COMENTA LO QUE HACE EL CÓDIGO
        Respuesta:

        Primero hace una lectura de la imagen (la carga en el programa) y muestra sus dimensiones, tamaño en cantidad de
        pixeles y el tipo de dato.

            img.shape devuelve (Altura, Anchura, Nº de canales). En este caso tres, RGB (rojo, verde y azul)

            La cantidad de pixeles es el resultado de la multiplicacion de los tres valores que devuelve img.shape

        Hace una copia de imagen y muestra sus dimensiones, tamaño en cantidad de pixeles y el tipo de dato.
        Posteriormente realiza las mismas funciones descritas: dimensiones, tamaño y tipo de dato

    '''

    img_in =skimage.io.imread(file_img_01)                  # Lectura y escritura de imagen
    print('Dimensiones: ' + str(img_in.shape))              # Dimensiones. (Altura, Anchura, Nº de canales)
    print('Tamanio (numero pixeles): ' + str(img_in.size))  # Altura x Anchura x nº de canales
    print('Tipo de dato: ' + str(img_in.dtype))

    # copiar imagen
    img_out = img_in.copy()                                 # Copiar imagen
    print('Dimensiones: ' + str(img_out.shape))
    print('Tamanio (numero pixeles): ' + str(img_out.size))
    print('Tipo de dato: ' + str(img_out.dtype))


def do_test02():
    '''
    NOMBRE: Pablo
    TODO:
        COMENTA LO QUE HACE EL CÓDIGO
        Respuesta:

        Esta tarea realiza una representación de las diferentes imágenes que se encuentran dentro de la
        carpeta underwater.
        Para ello, en primer lugar se genera un bucle for dentro del cuál para cada valor se tratará una de las
        imágenes de la carpeta.
        1. Se genera una variable que actue como fichero (file_img) donde se guarda un string con la dirección
           y nombre de la imagen para esa iteración.
           La imagen con la que tratar será la que el nombre coincida con el indice del bucle y será obligada siempre
           a tener como mínimo dos cifras.
        2. Una vez se tiene el directorio se muestra en pantalla.
        3. Posteriormente acudimos a la librería importada para el tratamieno de imagenes y cargamos la imagen a partir
           de su directorio previamente generado.
        4. Finalmente se utiliza la función visualizar_imagen de la práctica 0 para representar la imagen importada y
           como titulo 'imagen numero' más el entero del índice del bucle for.

    '''
    for i in range(1, 11):
        file_img = '../data/underwater/Ancuti{0:02d}.png'.format(i)     # Generación de directorio
        print('Image: ' + file_img)
        img_in =skimage.io.imread(file_img)                             # Carga de imagen
        visualizar_imagen(img_in,'imagen número %d' % i,block=True)     # Representación de la imagen



def do_test03():
    '''
    NOMBRE: Haritz
    TODO:
        Sobre la imagen a color elegida por tí: Manzanas.jpg
        Cual es el tamaño de img_in, y de img_out?
        Modifica esta función para que en el título de las figuras aparezca también el tamaño de la imagen (ancho, alto, número de canales) y guardalo en ../data/out/practica1
        Respuesta:

            Esta tarea carga la imagen a color elegida por el alumno para empezar. A continuación realiza una conversión
            por el cual se obtiene una imagen en escala de grises. Por ultimo muestra ambas imágenes, el de color y el
            de la escala de grises, en los cuales en el titulo se indica el número total de pixel correspondiente a
            cada imagen.


    '''
    # Cargar una imagen a color, convertir a gris y guardar


    img_in = skimage.io.imread(file_img_elegida_estudiante)
    img_out = skimage.color.rgb2gray(img_in)



    visualizar_imagen(img_in,titulo='Imagen original. Tamaño de la imagen (número de píxeles): %d' % (img_in.size),save_figure=True,figure_save_path='../data/out/practica2/fig_test03_in.png')
    visualizar_imagen(img_out, titulo='Imagen gris. Tamaño de la imagen (número de píxeles): %d' % (img_out.size),save_figure=True,figure_save_path='../data/out/practica2/fig_test03_out.png')



def do_test04():
    '''
    NOMBRE: Sergio
    TODO:
        Sobre la imagen a color elegida por tí: Ancuti01.png
        Elige uno de los tres canales de img_in y ponlo a cero.
        Luego introduce ese canal en img_in.
        Para ello usa slicing, que también se puede utilizar para asignar.
        visualiza y comenta el resultado.
        Almacena la figura resultante
        Respuesta:

        Primero  se ha escogido una imagen de archivo y se ha cargado.
            La variable asignada a la imagen esta al principio del codgio.
        Posteriormente se visualiza la imagen seleccionada y se guarda la visualizacion.
        Despues muestra los canales (RGB) de la imagen (todos activos).
        Acto seguido visualiza y guarda las imágenes de cada canal.

        Se elimina un canal, en este caso el verde.
        Se le asigna el resultado a una nueva variable.
        Se visualiza la imagen y se guarda el resultado.
    '''

    img_in = skimage.io.imread(file_img_01)             # Carga la imagen asignada al princpio del programa

    # Funcion visualizar imagen original
    visualizar_imagen(img_in,titulo='imagen original',save_figure=True,figure_save_path='../data/out/practica2/fig_test04_in.png')

    # Con funciones de numpy. Canales.
    # Corregido nombre de variables
    np_r = img_in[:, :, 0]  # red
    np_g = img_in[:, :, 1]  # green
    np_b = img_in[:, :, 2]  # blue

    # Visualiza la imagen segun el canal escogido y guarda las imagenes
    visualizar_imagen(np_r, titulo='canal r',save_figure=True,figure_save_path='../data/out/practica2/fig_test04_r.png')
    visualizar_imagen(np_g, titulo='canal g',save_figure=True,figure_save_path='../data/out/practica2/fig_test04_g.png')
    visualizar_imagen(np_b, titulo='canal b',save_figure=True,figure_save_path='../data/out/practica2/fig_test04_b.png')


    # Eliminar un canal (en este caso el verde)
    img_in[:, :, 1] = 0                 # canal green a zero
    img_in_un_canal_a_cero = img_in     # asignacion en variable
    # Carga imagen modificada
    visualizar_imagen(img_in_un_canal_a_cero, titulo='imagen con un canal eliminado',save_figure=True,figure_save_path='../data/out/practica2/fig_test04_canal_eliminado.png')

def do_test05():
    '''
    NOMBRE: Pablo
    TODO:
        Repite el código sobre la imagen a color elegida por tí: Manzanas.jpg
        Almacena la figura resultante
        ¿Qué hace el código?
        Respuesta:

        En primer lugar se carga la imagen deseada, es decir la imagen a color escogida.
        Posteriormente se realiza un tratamiento sobre la imagen limitando sus dimensiones.
            Se seleccionan los pixels de las filas desde la 15 a la 350.
            Se realiza la misma selección de pixels pero de las columnas 180 a 480.
            Finalmente se seleccionan todas las capas y por lo tanto al tratarse de una imagen a color RGB se sigue
            manteniendo el color de la imagen.
        Para acabar se visualiza la imagen y se guarda en el directorio indicado para ello.
    '''
    # Asignacion de ROIs
    # Tiempo estimado -> 5 minutos (total = 40 min)

    img_in = skimage.io.imread(file_img_elegida_estudiante)
    img_roi = img_in[15:350, 180:480,:]
    visualizar_imagen(img_roi,titulo='imagen ROI',save_figure=True,figure_save_path='../data/out/practica2/fig_test05_roi.png')



def do_test06():
    '''

    NOMBRE: Haritz
    TODO:
        ¿Qué hace el código?
        Respuesta:

        Para comenzar carga la imagen file_img_01 y lo muestra. Seguidamente recorta una sección en los 3 canales de la
        imagen, para ser mas exactos del tamaño de 336x301 pixeles y empezando en (15, 180). Esta sección corresponde a
        la cara de la estatua submarina.

        A continuación, se calcula el valor medio de R, G y B para obtener la representación en escala de grises de la
        sección recortada.

        Seguidamente se carga la imagen de entrada en la imagen de salida, y a este ultimo se le inserta en cada canal
        de RGB la imagen en escala de grises obtenida anteriormente a partir de la posición (15,180).

        Por ultimo se muestra la imagen de salida, donde toda la imagen esta en color, excepto la sección que se ha
        escogido que se encuentra en escala de grises.

    '''

    img_in = skimage.io.imread(file_img_01)
    visualizar_imagen(img_in, titulo='imagen original')
    img_roi = img_in[15:350, 180:480,:]
    img_roi_gris = np.average(img_roi,axis=2) # Calculamos el gris como la media de R, G y B

    img_out = img_in.copy()
    img_out[15:350, 180:480, 0] = img_roi_gris
    img_out[15:350, 180:480, 1] = img_roi_gris
    img_out[15:350, 180:480, 2] = img_roi_gris

    visualizar_imagen(img_out, titulo='imagen reconstruida', save_figure=True,
                      figure_save_path='../data/out/practica2/fig_test06_recon.png')


def do_test07():
    '''
    NOMBRE: Sergio
    TODO:
        Basándote en el ejemplo anterior, cambia la estatua por la del buzo

    '''

    img_in = skimage.io.imread(file_img_01)                 # Carga de imagen
    visualizar_imagen(img_in, titulo='imagen original')     # Visualizar imagen

    #TODO: tu código aquí
    img_roi = img_in[10:320, 480:780, :]        # Dimensiones cuadrado (y posicion)
    img_roi_gris = np.average(img_roi, axis=2)  # Calculamos el gris como la media de R, G y B
                                                # La media es sobre los colores del recuadro seleccionado en img_roi

    img_out = img_in.copy()                     # Crea copia para no modificar la original
    img_out[10:320, 480:780, 0] = img_roi_gris  # Asigna a los canales (RGB) el mismo valor de gris
    img_out[10:320, 480:780, 1] = img_roi_gris
    img_out[10:320, 480:780, 2] = img_roi_gris

    visualizar_imagen(img_out, titulo='imagen reconstruida', save_figure=True,
                       figure_save_path='../data/out/practica2/fig_test07_recon.png')


def do_test08():
    '''
    NOMBRE: Pablo
    TODO: Revisa el código y analiza los resultados
        ¿Cuál es el tipo de dato de la imagen?
        Cuál es el valor máximo que puede alcanzar img_suma?
        Qué pasa si convierto las imágenes a números reales y repito el proceso?
        Respuesta:

        Las imagenes originales se tratan de imagenes de 778 filas, 1024 columnas y tres capas de pixels que
        representan el modelo de color RGB. A su vez cada uno de los pixels tiene un valor entero uint8 de 0 a 255 los
        cuales determinan la cantidad de color verde, azul y rojo existe en la imagen por cada una de las 3 capas.
        Es decir, en la primera capa (R) si un pixel tiene valor 255 indica que en esa posición la imagen es
        totalmente roja mientras que si es de 0 ese pixel no esta formado en ningún caso por el rojo.

        Al sumar ambas imagenes, los valores máximos de capa uno de los pixels se continuarán viendo limitados a 255.
        Los colores de la nueva imagen tenderán a ser más intensos.

        Al convetir las imagenes de uint8 a float ahora los tres canales estarán formados por pixeles de valor entre
        0 y 1. Si se vuelve a realizar la suma pero ahora con las nuevas imagenes, la suma no quedará saturada en 1
        y habrá pixeles que superen ese valor. Por ello, la imagen tenderá a tonalidades mucho más blancas. Lo
        contrario ocurrirá con la resta ya que de nuevo no existe límite en este caso en el cero y por lo tanto la
        imagen resultante tenderá a colores muy oscuros.
        En el caso del blending ahora si funcionará y se observará una nueva imagen compuesta por las dos previas.
    '''

    img_in1 = skimage.io.imread(file_img_01)
    img_in2 = skimage.io.imread(file_img_02)

    img_in1 = skimage.io.imread(file_img_01).astype(float)/255.0
    img_in2 = skimage.io.imread(file_img_02).astype(float)/255.0


    visualizar_imagen(img_in1, titulo='imagen 1')
    visualizar_imagen(img_in2, titulo='imagen 2')


    # suma imagenes
    img_suma = img_in1+img_in2
    visualizar_imagen(img_suma, titulo='imagen suma', save_figure=True,
                      figure_save_path='../data/out/practica2/fig_test08_suma.png')

    # resta imagenes
    img_resta = img_in1 - img_in2
    visualizar_imagen(img_resta, titulo='imagen resta', save_figure=True,
                      figure_save_path='../data/out/practica2/fig_test08_resta.png')

    # resta imagenes absoluta
    img_resta_abs = np.abs(img_in1 - img_in2)
    visualizar_imagen(img_resta_abs, titulo='imagen resta abs', save_figure=True,
                      figure_save_path='../data/out/practica2/fig_test08_resta_abs.png')

    # Blending
    img_blending = 0.30*img_in1 + 0.70*img_in2
    visualizar_imagen(img_blending, titulo='imagen blending', save_figure=True,
                      figure_save_path='../data/out/practica2/fig_test08_blending.png')



def do_test09():
    '''
        NOMBRE: Haritz
        TODO:
            Revisa el código y analiza los resultados presta atención a la máscara,
            la necesitarás para el trabajo con barrio sésamo.
            ¿Cómo afecta el valor threshold?
            Respuesta:

            El programa carga la imagen base y el logo y los visualiza. A continuación, se selecciona la zona donde ira
            el logo en la imagen base. Para ello se obtiene el numero de filas, columnas y canales de la imagen del logo
            y se extrae una zona del mismo tamaño en la imagen base a partir de (0,0). Con la función rgb2gray se
            convierte la imagen a escala de grises y hace que el rango este entre 0.0 y 1.0. A continuación, se genera
            una mascara para el cual se tienen en cuenta los pixeles correspondientes que tengan un valor mayor que el
            treshold (umbral) indicado. Se visualiza el resultado de esta operación.

            Se invierte la mascara y se muestra el resultado seguidamente. Se crea una mascara con tres canales para que
            soporten RGB y pode utilizarlo posteriormente. En la imagen del logo se pone a 0 aquellas zonas donde su
            valor no supera el treshold anteriormente citado y se visualiza el resultado. Igualmente, con la imagen
            base, se pone a 0 aquellas zonas donde ira el logo. Por ultimo se suman las 2 imágenes, y se visualiza.

            En cuanto al treshold, con la disminución de su valor, en este caso se “pierde” la información la nitidez
            de las letras, pero a su vez un incremento en el valor de treshold hace que el logotipo no este bien
            detallado. Por ello será crucial la correcta elección de dicho valor para cada problemática.

    '''
    # Operaciones logicas -> And / Not y mascaras
    # Tiempo estimado -> 20 minutos (total = 110 min)
    # cargar las imagenes del ejemplo

    img_logo = skimage.io.imread(file_logo)
    img_base = skimage.io.imread(file_base)


    visualizar_imagen(img_base, titulo='imagen base')
    visualizar_imagen(img_logo, titulo='imagen logo')

    # Comprobacion de cantidad de canales para que concuerden
    if len(img_logo.shape) == 3:
        img_logo = img_logo[:, :, 0:3]
    if len(img_base.shape) == 3:
        img_base = img_base[:, :, 0:3]
    # Seleccionar la zona de la imagen donde irá el logo
    rows, cols,channels = img_logo.shape
    roi = img_base[0:rows, 0:cols,:]

    # Ojo, rgb2gray convierte la imagen a float y la rerangea de cero a uno!
    img_logo_gris = skimage.color.rgb2gray(img_logo)

    # Mascara de la info del logo
    threshold = 0.2
    mask = img_logo_gris > threshold
    visualizar_imagen(mask, titulo='máscara logo')

    # mascara invertida
    mask_inv = np.logical_not(mask)
    visualizar_imagen(mask_inv, titulo='máscara invertida')

    #Crear las máscaras con tres canales para que soporten RGB y poder multiplicar
    mask_inv = np.stack((mask_inv,mask_inv,mask_inv),axis=-1)
    mask = np.stack((mask, mask, mask),axis=-1)

    # Poner a 0 la zona de la imagen del logo que no nos interesa
    img_logo_limpia = np.logical_and(mask,img_logo)*img_logo
    visualizar_imagen(img_logo_limpia, titulo='logo limpio')

    # Poner a 0 la zona de la imagen base que va a ir a cero
    img_roi_limpia = np.logical_and(mask_inv,roi) * roi
    visualizar_imagen(img_roi_limpia, titulo='logo limpio')

    # Sumar las 2 imagenes
    dst = img_roi_limpia + img_logo_limpia
    visualizar_imagen(dst, titulo='suma')

    img_base[0:rows, 0:cols] = dst
    visualizar_imagen(img_base, titulo='logo_output',save_figure=True,figure_save_path='../data/out/practica2/fig_test09_mascara.png')



if __name__ == "__main__":
    # do_test01()
    # do_test02()
    # do_test03()
    # do_test04()
    # do_test05()
    # do_test06()
    # do_test07()
    # do_test08()
    do_test09()



    input()