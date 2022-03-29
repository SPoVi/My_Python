# -----------------------
#    Date = 17/07/2018
#  Author = 106376
# Project = code
# -----------------------

import matplotlib.pyplot as plt
import numpy as np
import skimage,skimage.io
from skimage.filters import threshold_otsu, threshold_local

from practica00.T01_cargar_imagen import visualizar_imagen, visualizar_imagenes

file_bodegon = '../data/color/bodegon.jpg'
file_manzanas = '../data/color/Manzanas.jpg'



def do_test09():
    '''
    NOMBRE:
    TODO:
        Comentar qué hace el código.
        Guardar la mejor imagen resultante en: /out/practica02/fig_test09_nombrexx.png
        Respuesta:

        Durante este test se realiza la misma operación realizada en la práctica anterior con la imagen grupal de
        barrio sesamo.
        El objetivo de esta es realizar una separación por canales de la imagen inicial y hacer cero el resto de canales
        para cada una de ellas. Es decir, para imagen donde se quiera representar unicamente el canal rojo se hacen
        cero tanto el verde como el azul realizando la misma operación con el resto de los canales
    '''

    img_in = skimage.io.imread(file_manzanas)               # Se carga la imagen
    visualizar_imagen(img_in, 'manzanas' )                  # La imagen cargada es visualizada
    canal_R = img_in[:,:,0]                                 # Los tres canales R,G y B son separados y visualizados en
    canal_G = img_in[:, :, 1]                               # un subplot
    canal_B = img_in[:, :, 2]
    visualizar_imagenes([img_in,None,None,canal_R,canal_G,canal_B],['Orig','None','None','R','G','B'],3,2)

    img_in = skimage.io.imread(file_manzanas)               # Se lee de nuevo la misma imagen
    visualizar_imagen(img_in, 'manzanas' )
    imagen_R = img_in.copy()                                # Esta vez se generan tres copias distintas para
    imagen_G = img_in.copy()                                # proteger la immagen principal de las nuevas modificaciones
    imagen_B = img_in.copy()

    imagen_R[:, :, 1] = 0                                   # Para cada imagen se hacen cero el resto de los canales
    imagen_R[:, :, 2] = 0
    imagen_G[:, :, 0] = 0
    imagen_G[:, :, 2] = 0
    imagen_B[:, :, 0] = 0
    imagen_B[:, :, 1] = 0
    visualizar_imagenes([img_in,None,None,imagen_R,imagen_G,imagen_B],['Orig','None','None','R','G','B'],3,2,
                        save_figure=True,figure_save_path='../data/out/practica02/fig_test09_SubApple.png')


def do_test10():
    '''
    NOMBRE:
    TODO:
        ¿Qué ocurre en la imagen de tono en la manzana roja, por qué?
        Guardar la mejor imagen resultante en: /out/practica02/fig_test10_nombrexx.png
        Respuesta:

        En este caso es esta realizando una iniciación en el modelo de color HSV.
        Analizando los resultados obtenidos en cada canal.
        - Hue: el color rojo corresponde a 0 grados y en su correspondiente valor en la imagen de tipo float es un 1.
               esto le hace distinguirse de otros colores como amarillo o verde entre los cuales no existe tanta diferencia
               como con respecto del rojo.
        - Saturation: Aqui la mayor diferencia es evidente con respecto del fondo. Pero entre zonas de la manzana tambien
                      es evidente esa diferencia debido a que en aquellas zonas donde los colores son más vivos y menos
                      grisaceos el valor del canal el mayor.
        - Value: Se corresponde con la luminosidad, en la manzana es perfectamente observable aquellas zonas donde
                 la luz esta reflejando directamente de las que se encuentran ensombrecidas ya que en las primeras el valor
                 del canal es más cercano a 1.0 que en las otras.
    '''

    img_in = skimage.io.imread(file_manzanas)       # Al igual que en el anterior test se realiza la separación de la
                                                    # imagen en los tres canales del modelo RGB
    visualizar_imagen(img_in, 'manzanas' )
    canal_R = img_in[:, :, 0]
    canal_G = img_in[:, :, 1]
    canal_B = img_in[:, :, 2]
    visualizar_imagenes([img_in,None,None,canal_R,canal_G,canal_B],['Orig','None','None','R','G','B'],3,2)

    img_HSV = skimage.color.rgb2hsv(img_in)         # En este caso se obtiene a partir del modelo RGB el HSV de la imagen
    canal_H = img_HSV[:, :, 0]                      # Se crean nuevas imagenes punteros de la inicial que contienen
    canal_S = img_HSV[:, :, 1]                      # los parametros Hue, Saturation y Value del modelo HSV
    canal_V = img_HSV[:, :, 2]
    visualizar_imagenes([img_in, img_HSV, None, canal_H, canal_S, canal_V], ['Orig', 'HSV', 'None', 'H', 'S', 'V'], 3, 2,
                        save_figure=True,figure_save_path='../data/out/practica02/fig_test10_AppleHSV.png')

def do_test11():
    '''
    NOMBRE:
    TODO:
        Explica lo que aparece en los canales L a y b y por qué
        Guardar la mejor imagen resultante en: /out/practica02/fig_test11_nombrexx.png
        Respuesta:

        En este caso se esta testeando el modelo de color Lab:
        L: Luminosidad del color. 0 serían rendimientos negros y 100 luz blanca.
        a: Se trata de la posición entre el rojo y el verde. Los valores negativos indican verde, mientras que los
           positivos indican rojo. Por este motivo la manzana verde (valores sobre [-20,-40]) se encuentra representada
           con negro y la roja (valores sobre [40,60]) en blanco. Por otro lado la manzana amarilla se encuentra a medio
           camino.
        b: Es la posición de un pixel entre el amarillo y el azul. Correspondiendo los valores negativos a azul y
           positivos a amarillo. En este caso no existen tonalidades claramente azules en la imagen pero si se puede
           apreciar como el nivel de amarillo de la manzana de ese mismo color es mayor que es del resto de elementos
           de la imagen
    '''

    img_in = skimage.io.imread(file_manzanas)
    visualizar_imagen(img_in, 'manzanas' )
    canal_R = img_in[:,:,0]
    canal_G = img_in[:, :, 1]
    canal_B = img_in[:, :, 2]
    visualizar_imagenes([img_in,None,None,canal_R,canal_G,canal_B],['Orig','None','None','R','G','B'],3,2)

    img_Lab = skimage.color.rgb2lab(img_in)
    canal_L = img_Lab[:,:,0]
    canal_a = img_Lab[:, :, 1]
    canal_b = img_Lab[:, :, 2]
    visualizar_imagenes([img_in, img_Lab, None, canal_L, canal_a, canal_b], ['Orig', 'Lab', 'None', 'L', 'a', 'b'], 3, 2,
                        save_figure=True,figure_save_path='../data/out/practica02/fig_test11_AppleLab.png')



def do_test12():
    '''
    NOMBRE:
    TODO:
        Ajustar los valores de threshold para segmentar la manzana roja.
        Prestad atención al uso de operaciones lógicas en la segmentación con varios thresholds.
        Guardar la mejor imagen resultante en: /out/practica02/fig_test12_nombrexx.png
        Respuesta:

        Al igual que en la anterior caso a continuación se va a tratar con el modelo de color Lab solo que en este
        caso no solo se estudiarán los diferentes canales sino que se llevará a cabo una segmentación en este caso
        de la manzana roja.

        Como conclusión se llega a que para este tipo de modelo sería posible realizar entre los canales a y b una
        conexión con puerta or pero para este caso se debe ser excesivamente restrictivo y por lo tanto se decide
        mantener la puerta lógica and
    '''

    img_in = skimage.io.imread(file_manzanas)       # Imagen con la que tratar

    img_Lab = skimage.color.rgb2lab(img_in)         # División en modelo de color Lab
    canal_L = img_Lab[:,:,0]
    canal_a = img_Lab[:, :, 1]
    canal_b = img_Lab[:, :, 2]

    th_L_max = 80                                # Generación de diferentes thresholds para cada uno de los canales
    th_L_min = 10
    th_a_max = 80
    th_a_min = 20
    th_b_max = 70
    th_b_min = 10


    seg_L = np.logical_and(canal_L < th_L_max,canal_L  > th_L_min)      # Segmentación de los canales para la obtención
    seg_a = np.logical_and(canal_a < th_a_max, canal_a > th_a_min)      # de cada manzana por separado
    seg_b = np.logical_and(canal_b < th_b_max, canal_b > th_b_min)
    imagen_segmentada = np.logical_and(np.logical_and(seg_a,seg_b),seg_L)
    visualizar_imagenes([img_in, img_Lab, imagen_segmentada, canal_L, canal_a, canal_b],
                        ['Orig', 'Lab', 'Segmentada', 'L', 'a', 'b'], 3, 2,
                        save_figure=True,figure_save_path='../data/out/practica02/fig_test12_AppleSeg.png')


def do_test13():
    '''
    NOMBRE:
    TODO:
        Seleccionando la imagen bodegon, selecciona una fruta y segmentala en al menos dos modelos de color.
        ¿Con qué modelo de color se segmenta mejor?
        Guarda la imagen en/out/practica02/fig_test13_nombrexx.png
        Respuesta:

        Para la realización de esta tarea se ha seleccionado como primer objetivo los albaricoques de la imagen, los
        cuales han sido segmentados mediante el uso de los tres modelo de color utilizados en las pruebas anteriores.
        Observando los resultados y el proceso intermedio de ajuste de los umbrales para cada uno de los canales de los
        modelos de color se ha llegado a la conclusión que el modelo que mejor logra una separación de las distintas
        piezas de fruta es el Lab debido a que modificando en pasos cada uno de los canales indivialmente se pueden
        dejar fuera de la zona seleccionada en este caso piezas de fruta progresivamente y no verse afectadas
        posteriormente al modificar el resto de los canales.

        Por eso se llega a la conclusión de que aun no siendo la mejor segmentación de los albaricoques posible
        si ha sido la más sencilla de realizar de forma que se excluya lo máximo posible al resto de las piezas de
        fruta con tonalidades similares que al fin y al cabo son las más dificiles de extraer individualmente.

    '''

    img_13 = skimage.io.imread(file_bodegon)
    visualizar_imagen(img_13, 'Bodegon')

    img_rgb = img_13.copy()
    imagen_for_hsv = img_13.copy()
    imagen_for_lab = img_13.copy()

    img_hsv = skimage.color.rgb2hsv(imagen_for_hsv)
    img_lab = skimage.color.rgb2lab(imagen_for_lab)

    # TODO: Segmentación por el modelo de color RGB ----------------------------------------------------------------
    canal_R = img_rgb[:, :, 0]
    canal_G = img_rgb[:, :, 1]
    canal_B = img_rgb[:, :, 2]

    th_R_max = 255
    th_R_min = 150
    th_G_max = 180
    th_G_min = 100
    th_B_max = 45
    th_B_min = 15

    seg_R = np.logical_and(canal_R < th_R_max, canal_R > th_R_min)  # Segmentación de los canales para la obtención
    seg_G = np.logical_and(canal_G < th_G_max, canal_G > th_G_min)  # de cada manzana por separado
    seg_B = np.logical_and(canal_B < th_B_max, canal_B > th_B_min)
    imagen_segmentadaRGB = np.logical_and(np.logical_and(seg_R, seg_G), seg_B)
    visualizar_imagenes([img_13, img_rgb, imagen_segmentadaRGB, canal_R, canal_G, canal_B],
                        ['Orig', 'Lab', 'Segmentada', 'R', 'G', 'B'], 3, 2)

    # TODO: Segmentación por el modelo de color HSV ----------------------------------------------------------------
    canal_H = img_hsv[:, :, 0]
    canal_S = img_hsv[:, :, 1]
    canal_V = img_hsv[:, :, 2]

    th_H_max = 40.0/360.0
    th_H_min = 20.0/360.0
    th_S_max = 1.0
    th_S_min = 0.80
    th_V_max = 1.0
    th_V_min = 0.70

    seg_H = np.logical_and(canal_H < th_H_max, canal_H > th_H_min)  # Segmentación de los canales para la obtención
    seg_S = np.logical_and(canal_S < th_S_max, canal_S > th_S_min)  # de cada manzana por separado
    seg_V = np.logical_and(canal_V < th_V_max, canal_V > th_V_min)
    imagen_segmentadaHSV = np.logical_and(np.logical_and(seg_H, seg_S), seg_V)
    visualizar_imagenes([img_13, img_hsv, imagen_segmentadaHSV, canal_H, canal_S, canal_V],
                        ['Orig', 'Lab', 'Segmentada', 'H', 'S', 'V'], 3, 2)

    # TODO: Segmentación por el modelo de color Lab ----------------------------------------------------------------
    canal_L = img_lab[:, :, 0]
    canal_a = img_lab[:, :, 1]
    canal_b = img_lab[:, :, 2]

    th_L_max = 75  # Generación de diferentes thresholds para cada uno de los canales
    th_L_min = 55
    th_a_max = 48
    th_a_min = 18
    th_b_max = 73
    th_b_min = 58

    seg_L = np.logical_and(canal_L < th_L_max, canal_L > th_L_min)  # Segmentación de los canales para la obtención
    seg_a = np.logical_and(canal_a < th_a_max, canal_a > th_a_min)  # de cada manzana por separado
    seg_b = np.logical_and(canal_b < th_b_max, canal_b > th_b_min)
    imagen_segmentada = np.logical_and(np.logical_and(seg_a, seg_b), seg_L)
    visualizar_imagenes([img_13, img_lab, imagen_segmentada, canal_L, canal_a, canal_b],
                        ['Orig', 'Lab', 'Segmentada', 'L', 'a', 'b'], 3, 2, save_figure=True,
                        figure_save_path='../data/out/practica02/fig_test13_AlbariSegm.png')

    img_13gris = img_13.copy()
    img_bode_gris = skimage.color.rgb2gray(img_13gris)

    visualizar_imagen(img_bode_gris, titulo='espinete limpio')
    img_bode_gris = np.stack((img_bode_gris, img_bode_gris, img_bode_gris), axis=-1)

    mask = imagen_segmentada.copy()
    mask_inv = np.logical_not(mask)
    mask = np.stack((mask, mask, mask), axis=-1)
    mask_inv = np.stack((mask_inv, mask_inv, mask_inv), axis=-1)

    img_color = np.logical_and(mask, img_13) * img_13
    visualizar_imagen(img_color, titulo='espinete limpio')

    img_gris = np.logical_and(mask_inv, img_bode_gris) * img_bode_gris
    visualizar_imagen(img_gris, titulo='espinete limpio')
    img_color = img_color.astype(float) / 255.0


    final = img_gris + img_color

    visualizar_imagen(final,titulo = 'seleccionada con escala de grises', save_figure=True,
                      figure_save_path='../data/out/practica02/fig_test13_AlbariGray.png')

if __name__ == "__main__":


    # do_test09()
    # do_test10()
    # do_test11()
    # do_test12()
    do_test13()

