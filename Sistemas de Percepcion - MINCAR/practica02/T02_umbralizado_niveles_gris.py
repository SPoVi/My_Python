# -----------------------
#    Date = 17/07/2018
#  Author = 106376
# Project = code
# -----------------------

import matplotlib.pyplot as plt
import numpy as np
import skimage,skimage.io
from skimage.filters import threshold_otsu, threshold_local

from practica00.T01_cargar_imagen import visualizar_imagen


file_histo = '../data/histograma/cerebro_1.jpg'
file_thres = '../data/histograma/bookpage.jpg'
file_7seg = '../data/histograma/Segmentos7.jpg'

file_mariposa = '../data/morfologicos/mariposa.jpg'
file_mariposa_noisy = '../data/morfologicos/mariposa_noisy.jpg'

file_sudoku = '../data/morfologicos/sudoku.jpg'
file_windows = '../data/morfologicos/windows.jpg'

file_bodegon = '../data/color/bodegon.png'



def do_test05():
    '''
    NOMBRE:
    TODO:
        Comentar qué hace el código.
        Ver el efecto de variar el valor de threshold en la imagen
        Guardar la mejor imagen resultante en: /out/practica02/fig_test05_nombrexx.png
        Respuesta:

        El programa carga la imagen en escala de gris y lo muestra. Seguidamente se establece un umbral (threshold), por
        el cual cada valor de la escala de gris de cada uno de los pixeles se convierte en blanco o negro. Si el valor
        es mayor que el threshold se convierte en blanco y a su vez si es inferior se convierte en negro. Por último, se
        muestra esta imagen en blanco y negro.

        Un aumento del threshold implica que se convertirán a negro más pixeles claros en la imagen, a su vez una
        disminución hace que los pixeles más oscuros se conviertan en blancos.

    '''

    img_in = skimage.io.imread(file_7seg, as_gray=True)
    #Nos quedamos sólo con canal 0
    # img_in = img_in[:,:,0]
    visualizar_imagen(img_in, '7 segmentos')

    # 1. Manual
    th_value = 0.4
    binary_image = img_in>th_value
    visualizar_imagen(binary_image, '7 segmentos binarizada con threshold %.2f' % th_value,
                      save_figure=True,figure_save_path='../data/out/practica02/fig_test05_7seg.png')


def do_test06():
    '''
    NOMBRE:
    TODO:
        Comentar qué hace el código.
        Ver el efecto de variar el valor de threshold en la imagen
        Guardar la mejor imagen resultante en: /out/practica02/fig_test06_nombrexx.png
        Respuesta:

        El programa carga la misma imagen de la tarea anterior en escala de grises. Esta vez el threshold se calcula
        mediante el histograma de la imagen, más concretamente, mediante el método OTSU. Este método hace que el
        histograma de la imagen tenga una apariencia lo más homogénea posible. Una vez obtenido el threshold, al igual
        que antes, los valores en escala de grises de los pixeles que sean mayores que el threshold se convierten
        en blanco y los menores en negro.

        Se ha multiplicado el valor obtenido por threshold_otsu(img_in) por una constante de tipo float con el objetivo
        de mejorar la imagen resultante.

    '''

    img_in = skimage.io.imread(file_7seg, as_gray=True)
    #Nos quedamos sólo con canal 0
    #img_in = img_in[:,:,0]
    visualizar_imagen(img_in, '7 segmentos')

    # 2. Metodo Otsu:

    th_value_otsu =0.85* threshold_otsu(img_in)


    binary_image = img_in>th_value_otsu
    visualizar_imagen(binary_image, '7 segmentos binarizada con threshold otsu %.2f' % th_value_otsu,
                      save_figure=True,figure_save_path='../data/out/practica02/fig_test06_7seg.png')



def do_test07():
    '''
    NOMBRE:
    TODO:
        Comentar qué hace el código.
        Ver el efecto de variar el valor de threshold en la imagen
        Visualiza y guarda la imagen contenida en local_thres. ¿Qué representa esta imagen?
        Guardar la mejor imagen resultante en: /out/practica02/fig_test07_nombrexx.png
        Respuesta:

        En esta tarea también el programa carga la imagen en escala de grises. Esta vez se calcula el threshold mediante
        el método OTSU de forma local, por lo que cada pixel tendrá su threshold particular. Para la obtención del mejor
        resultado se calcula el histograma en un bloque de 41x41 pixeles y con un off-set de 0.05 pixeles.
    '''

    img_in = skimage.io.imread(file_7seg, as_gray=True)
    #Nos quedamos sólo con canal 0
    #img_in = img_in[:,:,0]
    visualizar_imagen(img_in, '7 segmentos')

    # # 3. Metodo Threshold local:
    local_thresh = threshold_local(img_in, block_size=41, offset=0.05)
    binary_local = img_in > local_thresh
    visualizar_imagen(binary_local, '7 segmentos binarizada con threshold local',
                      save_figure=True,figure_save_path='../data/out/practica02/fig_test07_7seg.png')


def do_test08():
    '''
    NOMBRE:
    TODO:
        Con la imagen sudoku.jpg y los métodos anteriores conseguir segmentar la imagen lo mejor posible para separar dígitos de fondo.
        Explicar las ventajas e inconvenientes de cada método.
        Guardar la mejor imagen resultante en: /out/practica02/fig_test08_nombrexx.png
        Respuesta:

        Se va a realizar en esta tarea el umbralizado en niveles de gris para la imagen de sudoku.jpg utilizando los 3
        métodos anteriores, es decir, el método manual, el método OTSU general y el método OTSU local.

        Método manual: Debido a que existe una zona de sombra en la parte inferior izquierda, la utilización de un
        threshold global no es buena idea ya que un valor bueno para las zonas más iluminadas es incorrecto para las
        zonas ensombrecidas y viceversa.

        Método OTSU general: Con este método pasa lo mismo que con el anterior. Debido al uso de un threshold global no
        se umbralizan bien las zonas mas iluminadas y oscuras a la vez.

        Metodo OTSU local: Con este método los resultados obtenidos son muy buenos. Se ha escogido un tamaño de bloque
        de 21x21 pixeles (Tras medir que cada cuadrado del sudoku es de aprox. 32x32) y se ha visto un off-set de 0.03
        es el mejor. Debido a que se aplica un threshold particularizado para cada pixel, aun a pesar de tener zonas
        iluminadas y otras ensombrecidas, el umbralizado se hace correctamente.

    '''

    img_in = skimage.io.imread(file_sudoku, as_gray=True)
    visualizar_imagen(img_in, '7 segmentos')

    # 1. Manual
    th_value = 0.18
    binary_image = img_in > th_value
    visualizar_imagen(binary_image, '7 segmentos binarizada con threshold %.2f' % th_value)

    # 2. Metodo Otsu:

    th_value_otsu =0.5* threshold_otsu(img_in)
    binary_image = img_in>th_value_otsu
    visualizar_imagen(binary_image, '7 segmentos binarizada con threshold otsu %.2f' % th_value_otsu)

    # 3. Metodo Threshold local:
    local_thresh = threshold_local(img_in, block_size=21, offset=0.03)
    binary_local = img_in > local_thresh
    visualizar_imagen(binary_local, '7 segmentos binarizada con threshold local',
                      save_figure=True, figure_save_path='../data/out/practica02/fig_test08_7seg.png')

if __name__ == "__main__":


    # do_test05()
    # do_test06()
    # do_test07()
    # do_test08()