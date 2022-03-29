# -*- coding: utf-8 -*-
__author__ = 106360


# import cv2
import numpy as np
from matplotlib import pyplot as plt
import skimage.morphology
from practica00.T01_cargar_imagen import visualizar_imagenes,visualizar_imagen
import skimage

import matplotlib
matplotlib.use('TkAgg')

file_histo = '../data/histograma/cerebro_1.jpg'
file_thres = '../data/histograma/bookpage.jpg'
file_7seg = '../data/histograma/Segmentos7.jpg'

file_mariposa = '../data/morfologicos/mariposa.jpg'
file_mariposa_noisy = '../data/morfologicos/mariposa_noisy.jpg'

file_sudoku = '../data/morfologicos/sudoku.jpg'
file_windows = '../data/morfologicos/windows.jpg'




def do_test_binary_morphology_filter_1():
    image_gray = skimage.color.rgb2gray(skimage.io.imread(file_sudoku))
    img_threshold = skimage.filters.threshold_local(image_gray, 65, offset=0)
    image_binary_adaptive = image_gray<img_threshold
    visualizar_imagenes([image_gray,image_binary_adaptive],['orig','binary'],2,1)

    '''
    NOMBRE:
    TODO:
        Sobre la imagen binaria hacer lo siguiente:
        -  Aplicar un  filtro de erosión con tres tamaños de elemento estructural, incluyendo elementos rectangulares
        -  Aplicar un  filtro de dilatación con tres tamaños de elemento estructural, incluyendo elementos rectangulares
        -  Aplicar un  filtro de apertura con tres tamaños de elemento estructural, incluyendo elementos rectangulares
        -  Aplicar un  filtro de cierre con tres tamaños de elemento estructural, incluyendo elementos rectangulares
        - Guardar las imágenes en ./data/out/practica03/binary_morphology_filter_2_XXX.png    
        Respuesta:
        
        Tipo        Estructura
        Erosion:    - Cuadrado:        Elimina gran parte de los pixeles con valor 1, reduciendose la cantidad escogida
                    - R. Más filas:    [1; 1; 1] Aplica una erosion que afecta principalmente a lineas horizontales.
                    - R. Más columnas: [1 1 1] " " " que en este caso elimina lineas verticales del sudoku. 
        Dilatacion: - Cuadrado:        Es el caso contrario a la erosion, en este caso se aumenta el volumen de pixeles 
                                       de los objetos que se quieran seleccionar. 
                    - R. Más filas:    Aumenta el grosor de las lineas horizontales
                    - R. Más columnas: Aumenta el grosor de las lineas verticales
        Apertura:   - Cuadrado:        Open es una operacion morfologica que se utiliza eliminar pixeles sueltos como 
                                       puede ser el ruido no deseado en la imagen.
                    - R. Más filas:    Si se aplica sobre la horizontal consigue eliminar grupos de pixeles de mayor tamaño
                                       en la propia horizontal 
                    - R. Más columnas: En este caso ocurre lo mismo que añadiendo más filas pero afectando ahora a
                                       los grupos de pixeles con formas alargadas verticales no deseados. 
        Cierre:     - Cuadrado:        Mediante este tipo de operación morfologica se cierran agujeros en el interior de
                                       grupos de pixeles deseados que pueden conformar un objeto sobre el que desarrollamos 
                                       este tipo de operaciones. En este caso es apreciable su efecto la parte no deseada
                                       superior al sudoku.
                    - R. Más filas:    Mediante esta estructura se alargan las lineas horizontales deseadas, cerrando 
                                       con ello posibles huecos
                    - R. Más columnas: Lo mismo sobre lineas verticales
    '''

    # Filtro de Erosion
    eroded_image1 = skimage.morphology.binary.binary_erosion(image_binary_adaptive, np.ones((3, 3)))
    eroded_image2 = skimage.morphology.binary.binary_erosion(image_binary_adaptive, np.ones((3, 1)))
    eroded_image3 = skimage.morphology.binary.binary_erosion(image_binary_adaptive, np.ones((2, 4)))

    visualizar_imagenes([image_binary_adaptive, eroded_image1, eroded_image2, eroded_image3],
                        ['binary', 'eroded(3,3)', 'eroded(3,1)', 'eroded(2,4)'], 2, 2,
                        save_figure=True, figure_save_path='../data/out/practica03/T02/binary_morphology_filter_2_erosion.png')

    # Filtro de Dilatación
    dilated_image1 = skimage.morphology.binary.binary_dilation(image_binary_adaptive,np.ones((3, 3)))
    dilated_image2 = skimage.morphology.binary.binary_dilation(image_binary_adaptive, np.ones((3, 1)))
    dilated_image3 = skimage.morphology.binary.binary_dilation(image_binary_adaptive, np.ones((2, 4)))
    visualizar_imagenes([image_binary_adaptive, dilated_image1, dilated_image2, dilated_image3],
                        ['binary','dilated(3,3)', 'dilated(3,1)', 'dilated(2,4)'], 2, 2,
                        save_figure=True, figure_save_path='../data/out/practica03/T02/binary_morphology_filter_2_dilation.png')

    # Filtro de Apertura
    opened_image1 = skimage.morphology.binary.binary_opening(image_binary_adaptive,np.ones((3, 3)))
    opened_image2 = skimage.morphology.binary.binary_opening(image_binary_adaptive, np.ones((3, 1)))
    opened_image3 = skimage.morphology.binary.binary_opening(image_binary_adaptive, np.ones((2, 4)))
    visualizar_imagenes([image_binary_adaptive,opened_image1,opened_image2,opened_image3],
                        ['binary','opened(3,3)','opened(3,1)','opened(2,4)'], 2, 2,
                        save_figure=True, figure_save_path='../data/out/practica03/T02/binary_morphology_filter_2_opening.png')

    # Filtro de Cierre
    closed_image1 = skimage.morphology.binary.binary_closing(image_binary_adaptive, np.ones((3, 3)))
    closed_image2 = skimage.morphology.binary.binary_closing(image_binary_adaptive, np.ones((3, 1)))
    closed_image3 = skimage.morphology.binary.binary_closing(image_binary_adaptive, np.ones((2, 4)))
    visualizar_imagenes([image_binary_adaptive, closed_image1, closed_image2, closed_image3],
                        ['binary', 'closed(3,3)','closed(3,1)','closed(2,4)'], 2, 2,
                        save_figure=True, figure_save_path='../data/out/practica03/T02/binary_morphology_filter_2_closing.png')


def do_test_gray_morphology():
    '''
    NOMBRE:
    TODO:
        Una de las aplicaciones de las operaciones morfológicas que nos permiten aislar el valor del fondo, es decir la iluminación no homogenea de la imagen.
        Esta operación consiste en restarle a una imagen una operación morfológica de ella misma con un elemento estructural grande.
        Revisa el código y prueba sus efectos con distintos tipos de elemento esturctural (distinto tamaño y distinta forma (p.e tamaño 1,9 y tamaño 9,1))
        Respuesta:

        Para tamaño (1,9) se eliminan las lineas horizontales
        Para tamaño (9,1) se eliminan las lineas verticales
        Para tamaño (9,9) se realiza un aclarado homogenizado,
            si aumentamos sus valores (27,27) la img sale mas oscura (le restas menos a la original de hor y vert)
            si disminiyes sus valores (3,3) la img sale mas clara (le restas más a la original de hor y vert)
        A parte de la dilatación existen otras operaciones morfológicas que realizan otros cambios en la imagen:
        - Erosion: La imagen original suele ser más oscura que la original reduciendose los brillos orignales
        - Apertura: Borra pequeños detalles claros en comparación con el elemento principal
        - Cierre: Al contrario que la apertura esta operacion morfológica es usada para eliminar detalles oscuros de la
          imagen. Se diferencia con la dilatación en que no aclara el conjunto de la imagen.
    '''

    image_gray = skimage.color.rgb2gray(skimage.io.imread(file_sudoku))
    imagen_opening = skimage.morphology.dilation(image_gray,np.ones((9,9)))
    imagen_removal = image_gray / (imagen_opening+0.001)                        # Operacion de resta

    # Matriz horizontal (fila)
    imagen_opening_2 = skimage.morphology.dilation(image_gray,np.ones((1,9)))
    imagen_removal_2 = image_gray / (imagen_opening_2+0.001)
    # Matriz verical (columna)
    imagen_opening_3 = skimage.morphology.dilation(image_gray,np.ones((9,1)))
    imagen_removal_3 = image_gray / (imagen_opening_3+0.001)
    # Matriz cuadrada de mayor dimension
    imagen_opening_4 = skimage.morphology.dilation(image_gray,np.ones((27,27)))
    imagen_removal_4 = image_gray / (imagen_opening_4+0.001)
    # Matriz cuadrad de menor dimension
    imagen_opening_5 = skimage.morphology.dilation(image_gray,np.ones((3,3)))
    imagen_removal_5 = image_gray / (imagen_opening_5+0.001)

    visualizar_imagenes([image_gray, imagen_removal, imagen_removal_2, imagen_removal_3, imagen_removal_4, imagen_removal_5],
                        ['orig','Elmnto struc 9x9', 'Elmnto estruc 1x9', 'Elmnto struc 9x1','Elmnto struc 27x27',
                         'Elmnto struc 3x3'], 2, 3, save_figure=True, figure_save_path='../data/out/practica03/T02/fig_gray_morphology.png')

    visualizar_imagenes([imagen_opening, imagen_opening_2, imagen_opening_3, imagen_opening_4,imagen_opening_5],
                        ['op 9x9', 'op 1x9', 'op 9x1', 'op 27x27', 'op 3x3'], 2, 3,
                        save_figure=True, figure_save_path='../data/out/practica03/T02/fig_gray_morphology_openings.png')


def do_test_binary_morphology_filter_2():

    '''
    NOMBRE:
    TODO:
        Sobre la imagen binaria diseñar la cadena de filtros más adecuada que permita quedarnos sólamente con los números del sudoku y la retícula
        Recodrad que podéis aplicar operaciones lógicas a los resultados de distintos filtros para combinarlos.
        - Explicar el proceso
        - Guardar las imágenes en ./data/out/practica03/binary_morphology_filter_2_XXX.png
        - Si queréis podéis también trabajar sobre la imagen en gris original antes de realizar el threshold.
        ¿Podría ayudar el aplicar filtros morfológicos en niveles de gris antes de aplicar el threshold?
        Respuesta:

        Durante esta tarea se ha desarrollado un algoritmo en tres fases diferenciadas:
        1. Obtención lineas verticales
        2. Obtención lineas horizontales
        3. Obtención numeros a partir de la imagen original y la capa conseguida en los dos anteriores pasos.

        Al aplicar filtros morfologicos sobre la imagen en nivel de gris somos capaces de mejorar la iluminacion
        del fondo así como reducir la influencia de las lineas verticales y ruido cuando se quieran extraer las
        horizontales y viceversa.


    '''

    # ----------------------------------------------------------------------------------------------------------------
    # En primer lugar se realiza la extracción de las lineas verticales
    image_gray = skimage.color.rgb2gray(skimage.io.imread(file_sudoku))
    # Se realiza una dilatación en niveles de grises de modo que se vean reducidas las lineas horizontales
    imagen_dilatedV = skimage.morphology.dilation(image_gray, np.ones((1, 20)))
    visualizar_imagen(imagen_dilatedV, 'Gray dilation')
    # La resultante se sustrae de la imagen en niveles de grises para eliminar el brillo del fondo
    imagen_removalV = image_gray / (imagen_dilatedV + 0.001)
    visualizar_imagen(imagen_removalV, 'Gray dilation')

    # A continuacion se aplica un umbral y se consigue la imagen binaria con la que trabajaremos
    img_threshold_oriV = skimage.filters.threshold_local(imagen_removalV, 65, offset=0)
    image_binary_adaptive_oriV = imagen_removalV < img_threshold_oriV
    visualizar_imagen(image_binary_adaptive_oriV, 'Gray dilation')

    # Una vez se tiene la imagen se aplican operaciones morfologicas sobre ella tratando de quedarnos unicamente con
    # las lineas verticales aplicando la experiencia adquirida en el primer apartado
    imageV1 = skimage.morphology.binary.binary_erosion(image_binary_adaptive_oriV, np.ones((7,1)))
    visualizar_imagenes([image_binary_adaptive_oriV, imageV1], ['orig', 'numbers'], 2, 1)
    imageV2 = skimage.morphology.binary.binary_opening(imageV1, np.ones((7, 1)))
    visualizar_imagenes([imageV1, imageV2], ['orig', 'numbers'], 2, 1)
    imageV3 = skimage.morphology.binary.binary_dilation(imageV2, np.ones((7, 1)))
    visualizar_imagenes([imageV2, imageV3], ['orig', 'numbers'], 2, 1)
    finalV = skimage.morphology.binary.binary_opening(imageV3, np.ones((25, 1)))
    visualizar_imagenes([imageV3, finalV], ['orig', 'numbers'], 2, 1)

    # ----------------------------------------------------------------------------------------------------------------
    # En segundo lugar se realiza la extracción de las lineas horizontales mediante el mismo proceso solo que se cambian
    # los parametros de las filas por los de las columnas

    image_grayH = skimage.color.rgb2gray(skimage.io.imread(file_sudoku))
    imagen_DilatedH = skimage.morphology.dilation(image_grayH, np.ones((20, 1)))
    imagen_removalH = image_grayH / (imagen_DilatedH + 0.001)
    visualizar_imagen(imagen_removalH, 'Gray dilation')

    img_threshold_oriH = skimage.filters.threshold_local(imagen_removalH, 65, offset=0)
    image_binary_adaptive_oriH = imagen_removalH < img_threshold_oriH
    visualizar_imagen(image_binary_adaptive_oriH, 'Gray dilation')

    imageH1 = skimage.morphology.binary.binary_erosion(image_binary_adaptive_oriH, np.ones((1, 7)))
    visualizar_imagenes([image_binary_adaptive_oriH, imageH1], ['orig', 'numbers'], 2, 1)
    imageH2 = skimage.morphology.binary.binary_opening(imageH1, np.ones((1, 7)))
    visualizar_imagenes([imageH1, imageH2], ['orig', 'numbers'], 2, 1)
    imageH3 = skimage.morphology.binary.binary_dilation(imageH2, np.ones((1, 10)))
    visualizar_imagenes([imageH2, imageH3], ['orig', 'numbers'], 2, 1)
    finalH = skimage.morphology.binary.binary_opening(imageH3, np.ones((1, 20)))
    visualizar_imagenes([imageH3, finalH], ['orig', 'numbers'], 2, 1)

    # -------------------------------------------------------------------------------------------------------
    # Una vez se tienen ambas, se forma la cuadricula con la union de ambas
    Cuadricula = np.logical_or(finalV, finalH)
    visualizar_imagen(Cuadricula, 'Gray dilation')
    # Y se aplica una operacion morfologica que elimina aquellos grupos de pixeles menores del tamaño deseado
    CuadriculaLimpia = skimage.morphology.remove_small_objects(Cuadricula, min_size=2000, connectivity=8)
    visualizar_imagen(CuadriculaLimpia, 'Gray dilation')

    # ---------------------------------------------------------------------------------------------------------
    # Finalmente se obtienen los diferentes números
    image_num_gray = skimage.color.rgb2gray(skimage.io.imread(file_sudoku))
    # Se realiza una dilatación en niveles de grises pero en este caso aplicando un filtro cuadrado lo suficientemente
    imagen_closedN = skimage.morphology.dilation(image_num_gray, np.ones((6,6)))
    imagen_removalN = image_num_gray / (imagen_closedN + 0.001)
    visualizar_imagen(imagen_removalN, 'Gray dilation')

    # De nueco se aplica un umbral
    img_threshold_oriN = skimage.filters.threshold_local(imagen_removalN, 65, offset=0)
    image_binary_adaptive_oriN = imagen_removalN < img_threshold_oriN
    visualizar_imagen(image_binary_adaptive_oriN, 'Gray dilation')

    # --------------------------------------------------------------------------------------------------------
    # Para finalizar se genera una imagen binaria con todos los valores 0 del mismo tamaño que la imagen.
    negra = image_num_gray.copy()
    negra = negra < 1
    negra = np.logical_not(negra)

    # Con la imagen de la cuadricula se podrian aplicar diferentes bucles de modo que se detectase el valor de los
    # pixeles los cuales forman los extremos de las cuadriculas detectando con iteraciones cuando se cambia de false a
    # true y después al contrario.

    # Con esos valores se genera un recorte de la imagen principal con el cual restandole a el mismo con una puerta
    # logica xor la imagen de la cuadricula conseguirmos una imagen con los numeros y ruido del fondo
    roiN = image_binary_adaptive_oriN[90:396,25:380]
    roiC = Cuadricula[90:396,25:380]
    num = np.logical_xor(roiN, roiC)
    visualizar_imagen(num, 'Gray dilation')
    negra[90:396,25:380] = num
    visualizar_imagen(negra, 'Gray dilation')

    # Para finalizar se volverá a realizar la misma limpieza que con la imagen de la cuadricula y se obtiene el resultado
    imageFinal = np.logical_or(CuadriculaLimpia, negra)
    visualizar_imagen(imageFinal, 'Gray dilation')
    FinalLimpia = skimage.morphology.remove_small_objects(imageFinal, min_size=50, connectivity=8)
    visualizar_imagen(FinalLimpia, 'Gray dilation',save_figure=True, figure_save_path='../data/out/practica03/T02/fig_gray_morphology_openings_2.png')



if __name__ == "__main__":
    # do_test_binary_morphology_filter_1()
    # do_test_gray_morphology()
    do_test_binary_morphology_filter_2()