# -----------------------
# Date = 20/04/2020
# Author = G9_PG_SP_HO
# Project = code
# -----------------------

import matplotlib.pyplot as plt
import numpy as np
import skimage,skimage.io,skimage.exposure
from practica00.T01_cargar_imagen import visualizar_imagen, visualizar_imagenes


file_histo = '../data/histograma/cerebro_1.jpg'
file_thres = '../data/histograma/bookpage.jpg'
file_7seg = '../data/histograma/Segmentos7.jpg'

file_mariposa = '../data/morfologicos/mariposa.jpg'
file_mariposa_noisy = '../data/morfologicos/mariposa_noisy.jpg'

file_sudoku = '../data/morfologicos/sudoku.jpg'
file_windows = '../data/morfologicos/windows.jpg'

file_hand = '../data/histograma/radiografiaMano.png'  # Imagen medica de mi eleccion

def do_test01():
    # Calcular un histograma
    '''
    NOMBRE:
    TODO:
        Comentar qué se observa en la distribución de histograma.

        Un histograma muestra para cada posible valor de intensidad de un pixel en una imagen, el número de píxeles
        que presentan esa intensidad dentro de la imgagen.

        En el historgama de numpy:
            El eje de ordenadas (eje y) muestra la repitividad del pixel con un valor determinado en la escala de grises.
            El eje de abcisas (eje x) muestra la escala de grises ordenada de 0 a 256 (aunque se utilicen 255).
            En este caso, los valores del eje x se encuentran entre 100 y 150  y llegan a superar los 6000 en el eje y.

            La variable hist, es un vector de 256. El índice corresponde al valor del pixel (0-255) y el valor hist[i]
             corresponde al número de pixeles encontrados en la imagen.

            En este caso, hist[0] y hist[255] corresponden a negro y blanco respectivamente, que son los valores más
             altos en el vector.

            Solo pinta el valor (no pinta el area bajo la curva)

        El histograma de matplotlib:
             Este tipo de histograma es útil para un grafico RGB.
             A diferencia dle caso anteiro, te pinta el area bajo la curva (o lineas hasta el punto del valor)

    '''
    # Carga de la imagen y visualización
    img_in = skimage.io.imread(file_histo, as_gray=True) # as_gray  es para que te lo convierta a niveles de gris
        # se ha devuelto un array de (274 filas y 258 collumnas)
        # Al poner as_gray = TRUE devuelve valores de 0 a 1.
        # el valor min es 0.39... y el max 0.58...
    visualizar_imagen(img_in,'Cerebro') # Visualizar img


    # Con numpy
    hist, bins = np.histogram(img_in.ravel(), 256, [0.0, 1.0]) # Que te divida la img en 256 trozos; rango de valores de la img
        # ravel() : pasa una matriz 2D a una 1D, poniendolas unas detras de otras
        # 256 hace referencia a los bins, es decir, los trozos en los que divide niveles de intensidades
        # por ultimo indica que los valores que se clasifican van desde 0.0 a 1.0
    plt.plot(hist)
    plt.show()
        # Los valores del histograma estan ente el 100 y el 150

    # Con matplotlib
    plt.hist(img_in.ravel(), 256, [0.0, 1.0], color='r') # por defecto el color es azul 'b'
    plt.xlim([0, 1.0])
    plt.show()
    # Los valores del histograma estan ente el 100 y el 150. En este caso el area bajo la curva tiene color.

def do_test02():
    '''
    NOMBRE:
    TODO:
        Comentar qué se observa en la distribución de histograma en cada uno de los pasos.

        Stretching (Estirado)
            Io = (Ii-Mini)*(((Maxo-Mino)/(Maxi-Mini))+Mino)
            Mediante una regla de tres se cambian los valores del eje x para expandir el grafico.

            "El estirado de histograma permite aplicar una transformacion lineal a cada valor de intensidad
            existente en la imagen.
            Permite relacionar el valor max y min presente en el histograma (o valores porcentuales a ellos) a
            los valores max y min soportados por el tipo de imagen presente.
            Esto produce una mayor gama de rangos de intensidad en la imagen y una mejor visualización." (A.Picon)

            Al pixel con valor mas pequeño le asignas el cero y al mas grande le asigna 255.

        Stretching using skimage (Estirado)
            La funcion skimage.exposure.rescale_intensity() cambio los valores del eje x para expandir el grafico.

        Ecualizacion de histograma
            Modificación de la curva del histograma haciendo que probabilidad de los niveles de intensidad más
              constante.

            "Esto permite que la distribucion de los niveles de intensidad sea homogenea y sea mas sencillo
            discriminar informacion visual" (A.Picon)

        Ecualizacion de histograma adaptativa
            El ecualizado se realiza el ecualizado mediante la tecnica CLAHE (Contrast Limited Adaptative Histogram
                Equalizacion).
            "Se realiza la ecualizacion por regiones de la img y luego el resultado final se interpola." (A. Picon)
            Es más eficiente que el ecualizado normal.
    '''

    # Estirar / ecualizar un histograma
    # Tiempo estimado -> 10 minutos (total = 15 min)
    img_in = skimage.io.imread(file_histo) #.astype(float)/255
        # Los valores de la img van de 0 a 256.
        # al poner astype(float)/255 pasamos a tener valores entre 0 y 1.
        # min 100.333 y max 148.0
    if len(img_in.shape) == 3:
        # Convertir a gris haciendo la media de RGB
        img_in = np.average(img_in, axis=-1)

    # Stretching
    # Io = (Ii-Mini)*(((Maxo-Mino)/(Maxi-Mini))+Mino)
    min_in = img_in.min()
    max_in = img_in.max()
    min_out = 0
    max_out = 255
    img_strecthed = (img_in - min_in) * (((max_out - min_out) / (max_in - min_in)) + min_out)
        # Regla de 3

    # Stretching using skimage
    img_strecthed2 = skimage.exposure.rescale_intensity(img_in, out_range=(0, 255))

    # Ecualizacion de histograma

    img_equ = (skimage.exposure.equalize_hist(img_in) * 255).astype('uint8')

    # Ecualizacion de histograma adaptativa
    img_adapt_equ = skimage.exposure.equalize_adapthist(img_in.astype(float) / 255, kernel_size=None, clip_limit=0.01,
                                                        nbins=256)

    plt.subplot(131)
    plt.hist(img_in.ravel(), 256, [0, 256], color='b')          # Histograma original
    plt.subplot(132)
    plt.hist(img_strecthed2.ravel(), 256, [0, 256], color='r')  # Streching con skimage
        # El valor minimo de la imagen a pasado a ser 0 y el maximo a ser 255.
    plt.subplot(133)
    plt.hist(img_equ.ravel(), 256, [0, 256], color='g')         # Ecualizado
    plt.show(block=True)

    plt.figure()
    plt.subplot(141)
    plt.imshow(img_in, cmap=plt.get_cmap('gray'))           # Img original
        # Es la que tiene menos contraste
    plt.subplot(142)
    plt.imshow(img_strecthed2, cmap=plt.get_cmap('gray'))   # Img con histograma estirado
        # Al no haberse estirado mucho la variacion es minima con respepcto a la original
    plt.subplot(143)
    plt.imshow(img_equ, cmap=plt.get_cmap('gray'))          # Img Ecualizada
        # Hay un mayor contraste, pero algunas zonas quedan quemadas y otras zonas quedan muy oscuras.
    plt.subplot(144)
    plt.imshow(img_adapt_equ, cmap=plt.get_cmap('gray'))    # Img con ecualizacion CHLAE
        # Es la que mayor calidad tiene.
        # Hay mayor contraste ne la zona del cerebro sin embargo otras zonas no las satura.
    plt.show(block=True)


def do_test03():
    '''
    NOMBRE:
    TODO:
        Repetir el ejercicio do_test02 con la imagen sudoku.jpg :
        Extraer y visualizar los histogramas de la imagen original
        de la imagen con el histograma estirado y de la imagen ecualizada.
        Analizar el uso de CLAHE (imadapthist) en estas imágenes.
        Comentar resultados
        Almacenar las figuras resultantes en el directorio /out/practica02/fig_test03_nombrexx.png
        Respuesta:

        En los histogramas se han observado que:
            En el normal orignal el pico se situa  en el centro.
            Mediante skimage se ha estirado.
            En la equilizacion se han redistribuido los valores lo mas homogeneamente posible
            Mediante el equalizado adptativo (CLAHE) el pico se ha desplazado a la derecha.

        En las imagenes se observa que:
            La original tiene una zona mas oscura en la parte inf izq y mas ilumianda en la der sup
            Tras el estirado no se aprecima muhca mejoria
            Mediante el ecualizado las zonas oscuras son mas oscuras y las iluminadas mas iluminadas
            El mejor resultado se ha obtenido en el ecualizado adptativo (CALHE), la iluminacion de la
            imagen es mas homogenea. Se aprecia mejor calidad de imagen respecto a todas las anteriores.

    '''

    # Estirar / ecualizar un histograma
    # Tiempo estimado -> 10 minutos (total = 15 min)
    img_in = skimage.io.imread(file_sudoku)  # .astype(float)/255
    # Los valores de la img van de 0 a 256.
    # si se pone astype(float)/255 pasamos a tener valores entre 0 y 1.
    # min 4.0 y max 219.3333334
    if len(img_in.shape) == 3:
        # Convertir a gris haciendo la media de RGB
        img_in = np.average(img_in, axis=-1)

    # Stretching
    # Io = (Ii-Mini)*(((Maxo-Mino)/(Maxi-Mini))+Mino)
    min_in = img_in.min()
    max_in = img_in.max()
    min_out = 0
    max_out = 255
    img_strecthed = (img_in - min_in) * (((max_out - min_out) / (max_in - min_in)) + min_out)
    # Regla de 3

    # Stretching using skimage
    img_strecthed2 = skimage.exposure.rescale_intensity(img_in, out_range=(0, 255))
        # Expansion del grafico.
        # Los valores min y max de la imagen pasan a ser 0 y 255 respectivamente.

    # Ecualizacion de histograma

    img_equ = (skimage.exposure.equalize_hist(img_in) * 255).astype('uint8')
        #  Modificacion de la curva del histograma para que la probabilidad de los niveles de intensidad sea
    #   mas constante.

    # Ecualizacion de histograma adaptativa
    img_adapt_equ = skimage.exposure.equalize_adapthist(img_in.astype(float) / 255, kernel_size=None, clip_limit=0.01,
                                                        nbins=256)

    # Ecualizado mediante la tecnica CLAHE.
    # Consiste segmentar la imagen, realizar el histograma y ecualizacion de cada segmento  para posteiormente
    # ponderar todo.
    # Mas eficiente que el ecualizado normal.

    plt.figure()        # Crear nueva  figura para poder guardarla luego
    plt.subplot(141)
    plt.hist(img_in.ravel(), 256, [0, 256], color='b')  # Histograma original
    plt.subplot(142)
    plt.hist(img_strecthed2.ravel(), 256, [0, 256], color='r')  # Streching con skimage
    # El valor minimo de la imagen a pasado a ser 0 y el maximo a ser 255.
    plt.subplot(143)
    plt.hist(img_equ.ravel(), 256, [0, 256], color='g')  # Ecualizado
    plt.subplot(144)
    plt.hist(img_adapt_equ.ravel(), 256, [0.0, 1.0], color='m')             # Rango de valores de 0.0 a 1.0
    plt.savefig('../data/out/practica02/T01/fig_test03_sudoku_hist.png')
    plt.show(block=True)

    plt.figure()
    plt.subplot(141)
    plt.imshow(img_in, cmap=plt.get_cmap('gray'))  # Img original
    # Es la que tiene menos contraste
    plt.subplot(142)
    plt.imshow(img_strecthed2, cmap=plt.get_cmap('gray'))  # Img con histograma estirado
    # Al no haberse estirado mucho la variacion es minima con respepcto a la original
    plt.subplot(143)
    plt.imshow(img_equ, cmap=plt.get_cmap('gray'))  # Img Ecualizada
    # Hay un mayor contraste, pero algunas zonas quedan quemadas y otras zonas quedan muy oscuras.
    plt.subplot(144)
    plt.imshow(img_adapt_equ, cmap=plt.get_cmap('gray'))  # Img con ecualizacion CHLAE
    # Es la que mayor calidad tiene.
    # Las zonas oscuras y muy ilimunadas de la imagen original han quedado equilibradas.
    plt.show(block=True)

    img_t3_sudoku = [img_in, img_strecthed2, img_equ, img_adapt_equ]          # Lista con las imanenes
    titulos_t3_2 = ['Original', 'Expandida', 'Ecualizada', 'EC_Adaptativa']   # Lista con los nombres de las imagenes
    visualizar_imagenes(img_t3_sudoku, titulos_t3_2, 2, 2, block=True, save_figure=True,
                        figure_save_path='../data/out/practica02/T01/fig_test03_sudoku.png')  # Guardar Imagen

def do_test04():
    '''
    NOMBRE:
    TODO:
        Completar el ejercicio do_test02 con la imagen médica de vuestra elección :
        Extraer y visualizar los histogramas de la imagen original
        de la imagen con el histograma estirado y de la imagen ecualizada.
        Analizar el uso de CLAHE (imadapthist) en estas imágenes.
        Comentar resultados
        Almacenar las figuras resultantes en el directorio /out/practica02/fig_test04_nombrexx.png
        Respuesta:


        En las imagenes se observa que:
            La original tiene una zona mas oscura en la parte inf izq y mas ilumianda en la der sup
            Tras el estirado no se aprecima muhca mejoria
            Mediante el ecualizado la imagen se ha quemado y sobreexpuesto, esto se debe a que la orignial no era
            homogenea
            El mejor resultado se ha obtenido en el ecualizado adptativo (CALHE), la iluminacion de la
            imagen es mas homogenea. Se aprecia mejor calidad de imagen respecto a todas las anteriores.
    '''
 # Estirar / ecualizar un histograma
    # Tiempo estimado -> 10 minutos (total = 15 min)
    img_in = skimage.io.imread(file_hand)  # .astype(float)/255
    # Los valores de la img van de 0 a 256.
    # si se pone astype(float)/255 pasamos a tener valores entre 0 y 1.
    # min 4.0 y max 219.3333334
    if len(img_in.shape) == 3:
        # Convertir a gris haciendo la media de RGB
        img_in = np.average(img_in, axis=-1)

    # Stretching
    # Io = (Ii-Mini)*(((Maxo-Mino)/(Maxi-Mini))+Mino)
    min_in = img_in.min()
    max_in = img_in.max()
    min_out = 0
    max_out = 255
    img_strecthed = (img_in - min_in) * (((max_out - min_out) / (max_in - min_in)) + min_out)
    # Regla de 3

    # Stretching using skimage
    img_strecthed2 = skimage.exposure.rescale_intensity(img_in, out_range=(0, 255))
        # Expansion del grafico.
        # Los valores min y max de la imagen pasan a ser 0 y 255 respectivamente.

    # Ecualizacion de histograma

    img_equ = (skimage.exposure.equalize_hist(img_in) * 255).astype('uint8')
        #  Modificacion de la curva del histograma para que la probabilidad de los niveles de intensidad sea
    #   mas constante.

    # Ecualizacion de histograma adaptativa
    img_adapt_equ = skimage.exposure.equalize_adapthist(img_in.astype(float) / 255, kernel_size=None, clip_limit=0.01,
                                                        nbins=256)

    # Ecualizado mediante la tecnica CLAHE.
    # Consiste segmentar la imagen, realizar el histograma y ecualizacion de cada segmento  para posteiormente
    # ponderar todo.
    # Mas eficiente que el ecualizado normal.

    plt.figure()        # Crear nueva  figura para poder guardarla luego
    plt.subplot(141)
    plt.hist(img_in.ravel(), 256, [0, 256], color='b')  # Histograma original
    plt.subplot(142)
    plt.hist(img_strecthed2.ravel(), 256, [0, 256], color='r')  # Streching con skimage
    # El valor minimo de la imagen a pasado a ser 0 y el maximo a ser 255.
    plt.subplot(143)
    plt.hist(img_equ.ravel(), 256, [0, 256], color='g')  # Ecualizado
    plt.subplot(144)
    plt.hist(img_adapt_equ.ravel(), 256, [0.0, 1.0], color='m')             # Rango de valores de 0.0 a 1.0
    plt.savefig('../data/out/practica02/T01/fig_test04_hand_hist.png')
    plt.show(block=True)

    plt.figure()
    plt.subplot(141)
    plt.imshow(img_in, cmap=plt.get_cmap('gray'))  # Img original
    # Es la que tiene menos contraste
    plt.subplot(142)
    plt.imshow(img_strecthed2, cmap=plt.get_cmap('gray'))  # Img con histograma estirado
    # Al no haberse estirado mucho la variacion es minima con respepcto a la original
    plt.subplot(143)
    plt.imshow(img_equ, cmap=plt.get_cmap('gray'))  # Img Ecualizada
    # Hay un mayor contraste, pero algunas zonas quedan quemadas y otras zonas quedan muy oscuras.
    plt.subplot(144)
    plt.imshow(img_adapt_equ, cmap=plt.get_cmap('gray'))  # Img con ecualizacion CHLAE
    # Es la que mayor calidad tiene.
    # Las zonas oscuras y muy ilimunadas de la imagen original han quedado equilibradas.
    plt.show(block=True)

    img_t3_sudoku = [img_in, img_strecthed2, img_equ, img_adapt_equ]          # Lista con las imanenes
    titulos_t3_2 = ['Original', 'Expandida', 'Ecualizada', 'EC_Adaptativa']   # Lista con los nombres de las imagenes
    visualizar_imagenes(img_t3_sudoku, titulos_t3_2, 2, 2, block=True, save_figure=True,
                        figure_save_path='../data/out/practica02/T01/fig_test04_hand.png')  # Guardar Imagen

    null;
if __name__ == "__main__":
    #do_test01()
    #do_test02()
    #do_test03()
    do_test04()


    input()