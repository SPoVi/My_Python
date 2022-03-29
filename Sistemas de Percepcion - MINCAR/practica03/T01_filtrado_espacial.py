# -*- coding: utf-8 -*-
import skimage

from practica00.T01_cargar_imagen import visualizar_imagenes, visualizar_imagen
import scipy.ndimage
import skimage.filters
__author__ = 106360


# import cv2
import numpy as np
from matplotlib import pyplot as plt
import scipy

import matplotlib
import skimage
import skimage.filters
from skimage.filters import gaussian
from skimage.filters import median

from skimage import feature     # Para Canny
from skimage import viewer      # Para plugin en Canny

matplotlib.use('TkAgg')

file_histo = '../data/histograma/cerebro_1.jpg'
file_thres = '../data/histograma/bookpage.jpg'
file_7seg = '../data/histograma/Segmentos7.jpg'

file_mariposa = '../data/morfologicos/mariposa.jpg'
file_mariposa_noisy = '../data/morfologicos/mariposa_noisy.jpg'

file_sudoku = '../data/morfologicos/sudoku.jpg'
file_windows = '../data/morfologicos/windows.jpg'

# Frangi
file_vessels = '../data/mis_imagenes/vessels.jpg'


def add_noise_to_image(noise_typ, image):
    if noise_typ == "gauss":
        row, col, ch= image.shape
        mean = 0
        var = 0.1
        sigma = var**0.5
        gauss = np.random.normal(mean,sigma,(row,col,ch))
        gauss = gauss.reshape(row,col,ch)
        noisy = image + gauss
        return noisy

    elif noise_typ == "s&p":
        row, col, ch = image.shape
        s_vs_p = 0.5
        amount = 0.01
        out = np.copy(image)

        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
        out[coords] = 0
        return out

    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy

    elif noise_typ =="speckle":
        row,col,ch = image.shape
        gauss = np.random.randn(row,col,ch)
        gauss = gauss.reshape(row,col,ch)
        noisy = image + image * gauss
        return noisy



def do_test_efectos_filtros_lineales():

    #Cargamos la imagen
    img_in = skimage.io.imread(file_mariposa_noisy)
    #Pasamos a nivel de gris (se puede aplicar también en color o en el canal L)
    img_gray = skimage.color.rgb2gray(img_in)

    #Filtrado de ruido de media cuadrado
    filtro_A = np.array([[1.0,1.0,1.0],[1.0,1.0,1.],[1.0,1.0,1.0]])
    filtro_A = filtro_A / (filtro_A[:]).sum()
    #Filtrado de ruio de media de disco
    filtro_B = np.array([[0.0, 1.0, 0.0], [1.0, 1.0, 1.0], [0.0, 1.0, 0.0]])
    filtro_B = filtro_B / (filtro_B[:]).sum()

    #Filtro de extracción de borde vertical (Gy)
    filtro_C = np.array([[1.0, 1.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -1.0, -1.0]])

    visualizar_imagenes([filtro_A,filtro_B,filtro_C],('filtro A', 'Filtro B', 'Filtro C'),3,1,rescale_colors=False)

    image_fA = scipy.ndimage.correlate(img_gray,filtro_A)
    image_fB = scipy.ndimage.correlate(img_gray, filtro_B)
    image_fC = scipy.ndimage.correlate(img_gray, filtro_C)

    visualizar_imagenes([img_gray,image_fA,image_fB,image_fC],('Original','filtro A', 'Filtro B', 'Filtro C'),4,1,rescale_colors=False)

def do_test_restauracion_imagen():
    '''
    Skimage dispone de funciones de filtrado que directamente permiten aplicar lso filtros deseados a las imágenes
    http://scikit-image.org/docs/dev/api/skimage.filters.html
    NOMBRE:
    TODO:
        Aplicar a la imagen de la mariposa con ruido distintos filtros.
        Aplicad a la imagen anterior filtros gausianos y de mediana, visualizad el resultado
        y elegid aquellos filtros que mejoren la imagen.
        Probad diferentes tamaños de filtros y analizad los resultados.
        ¿Qué filtros de imagen funcionan mejor? , ¿Cuál es la causa?
        Visualizar y guardar la imagen en /data/out/practica03/fig_restauracion_imagen_XXX.png
        Respuesta:

        Se han aplicado el filtro gaussiano y de mediana a la imagen de la mariposa. Se ha observado que el filtro
        gaussiano no obtiene resultados para nada buenos. Al contrario, el filtro de la mediana obtiene unos resultados
        bastante buenos, sobre todo comparados con el del gaussiano. Esto se debe a que el ruido de la imagen de la
        mariposa es de tipo impulsional, por lo que el filtro de la mediana desprecia los valores de los extremos en la
        escala de grises obteniendo así un mejor resultado, mientras que el filtro gaussiano no logra despreciar estos
        valores extremos tan bien.


    '''
    img_in = skimage.io.imread(file_mariposa_noisy)
    img_gray = skimage.color.rgb2gray(img_in)
    visualizar_imagen(img_gray,'Imagen con ruido')


    img_gauss = gaussian(img_gray,sigma=1,multichannel=True,mode='wrap')
    visualizar_imagen(img_gauss,'Filtro gausiano')


    img_mediana = median(img_gray)
    visualizar_imagen(img_mediana, 'Filtro mediana', save_figure=True, figure_save_path='../data/out/practica03/T01/fig_restauracion_imagen_mediana.png')



def do_test_afilado_imagen():
    '''
        Combinando filtros gausianos a diferentes frecuencias se pueden realizar tareas de enfatizado.
        Este enfatizado se realiza extrayendo las altas frecuencias de la imagen y añadiendo estas altas frecuencias (bordes)
        a la imagen original.
        Revisa el cuaderno de prácticas o las presentaciones de teoría y:

        NOMBRE:
        TODO:
            Selecciona una imagen que se encuentre un poco borrosa.
            Realiza las combinaciones de filtros necesarias para realizar un afilado.
            Explica el proceso.
            Visualizar y guardar la imagen en /data/out/practica03/fig_afilado_imagen_XXX.png
            Respuesta:

            Se ha seleccionado como imagen borrosa el resultado obtenido en subprograma anterior, es decir el filtrado
            mediana de la imagen con ruido de la mariposa. Se ha creado una mascara de 20x20 pixeles normalizado. Se ha
            realizado la correlación de esta mascara con la imagen borrosa.

            El detalle de la imagen se define como la resta de la imagen borrosa original y la imagen obtenida mediante
            la aplicación de la máscara. Por ultimo se le suma al imagen borrosa el detalle multiplicado por un valor
            de 0.5 en este caso para obtener una imagen afilada.

    '''

    img_in = skimage.io.imread(file_mariposa_noisy)
    img_gray = skimage.color.rgb2gray(img_in)
    img_mediana = median(img_gray)
    visualizar_imagen(img_mediana, 'Imagen borrosa')

    filtro_A = np.ones([20,20])
    filtro_A = filtro_A / (filtro_A[:]).sum()
    image_fA = scipy.ndimage.correlate(img_mediana, filtro_A)

    detalle = img_mediana - image_fA
    visualizar_imagen(detalle,'Detalle de la imagen')

    afilado = img_mediana + 0.5*detalle
    visualizar_imagen(afilado, 'Imagen afilado', save_figure=True, figure_save_path ='../data/out/practica03/T01/fig_afilado_imagen.png')


def do_test_gradiente_imagen():
    '''
        Otra topología de filtros sirven para la detección de bordes.
        Uno de los filtros más conocidos es el filtro de sobel.
        NOMBRE:
        TODO:
            Para la imagen sudoku
            Calcula y visualiza el gradiente horizontal y vertical de la imagen mediante el filtro de sobel.
            Calcula y visualiza el módulo del gradiente y el argumento del gradiente de la imagen.
            Utilizad la función: scipy.ndimage.convolve()
            Almacena las imágenes generadas en:
            /data/out/practica03/fig_gradiante_imagen_XXX.png
            Respuesta:

            En este ejercicio se ha utilizado unas mascaras de 3x3 pixeles para la generación de la gradiente en
            horizontal y la vertical. Para el gradiente horizontal se ha utilizado una máscara de tipo Robinson II Este
            y para el gradiente vertical uno de tipo Robinson II Sur.

            Se ha convolucionado la imagen con cada una de los gradientes. De los resultados obtenidos se ha procedido
            a calcular tanto el modulo de la gradiente como el argumento del mismo.

            También se ha realizado la operación de gradiente mediante el filtro Sobel de SKIMAGE. En este caso también
            se han calculado las gradientes horizontales y verticales de la imagen y se han obtenido el modulo y el
            argumento del gradiente.

    '''

    # Cargamos la imagen
    img_in = skimage.io.imread(file_sudoku, as_gray=True)     # Cambiar a sudoku
    # visualizar_imagen(img_in,"Imagen Original")


    '''HSOBEL_WEIGHTS = skimage.filters.sobel_h(img_in)
    VSOBEL_WEIGHTS = skimage.filters.sobel_v(img_in)
    print(HSOBEL_WEIGHTS)
    print(VSOBEL_WEIGHTS)'''

    #print(skimage.filters.HSOBEL_WEIGHTS)
    #print(skimage.filters.VSOBEL_WEIGHTS)

    # Filtro Gaussiano a Mano

    '''Ax = np.array([[0.0, 0.0, 0.0], [-1.0, 0.0, 1.0], [0.0, 0.0, 0.0]])
    Ay = np.array([[0.0, -1.0, 0.0],[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]])

    visualizar_imagenes([Ax, Ay],['Ax',['Ay']],2,1)'''

    grad_h = np.array([[-1.0, 0.0, 1.0], [-2.0, 0.0, 2.0], [-1.0, 0.0, 1.0]])
    grad_v = np.array([[-1.0, -2.0, -1.0], [0.0, 0.0, 0.0], [1.0, 2.0, 1.0]])

    g_x = scipy.ndimage.convolve(img_in, grad_h)
    g_y = scipy.ndimage.convolve(img_in, grad_v)

    g_module = np.sqrt(g_x*g_x + g_y*g_y)          # Modulo del gradiente
    #visualizar_imagen(g_module, 'Modulo del gradiente')
    g_angle = np.arctan2(g_y, g_x)
    #visualizar_imagen(g_angle, 'Argumento del gradiente')

    visualizar_imagenes([g_x, g_y, g_module, g_angle], ['Gx', 'Gy', 'Modulo del gradiente', 'Argumento del gradiente'],
                        2,2, save_figure=True, figure_save_path='../data/out/practica03/T01/figure_Sovel_filter_calculado.png')

    # Filtro Sobel de SKIMAGE

    image_f_sobel_h = skimage.filters.sobel_h(img_in)
    image_f_sobel_v = skimage.filters.sobel_v(img_in)
    image_f_sobel = skimage.filters.sobel(img_in)

    image_f_module_grad = np.sqrt(image_f_sobel_h*image_f_sobel_h + image_f_sobel_v*image_f_sobel_v)
    image_f_arg_grad = np.arctan2(image_f_sobel_v, image_f_sobel_h)

    visualizar_imagenes([image_f_sobel_h, image_f_sobel_v, image_f_module_grad,image_f_arg_grad],
                        ['Gx', 'Gy', 'Modulo del gradiente', 'Argumento del gradiente'], 2,2,
                        save_figure=True, figure_save_path='../data/out/practica03/T01/figure_Sovel_filter_skimage.png')

    visualizar_imagenes([image_f_sobel, image_f_module_grad], ['Modulo directo con Skimage', 'Modulo con Gx y Gy de Skimage'],
                        2,1)


    pass


def do_test_canny():
    '''
        Existen métodos más avanzados para la obtención de bordes.
        Por ejemplo el filtro de canny, ampliamente utilizado en
        visión artificial para la localización de bordes.
        NOMBRE:
        TODO:
            Para la imagen sudoku aplicar el filtro de skimage canny
            Analizar el efecto aplicando varios parámetros.
            Obtener la imagen que mejor aísle los bordes de la imagen y almacenarla en:
            /data/out/practica03/fig_canny_XXX.png
            Respuesta:

            Parametros de la función CANNY:
            def canny(image, sigma=1., low_threshold=None, high_threshold=None, mask=None, use_quantiles=False)
                sigma: Desviación estandar del filtro de Gauss. por defecto 1
                low_threshold: Lim inf umbral de histéresis (bordes de union) 10% por defecto
                high_threshold: Lim sup umbral de histéresis (bordes de union) 20% por defecto
                mask: Máscara para limitar la aplicación de Canny a una cierta área.
                use_quantiles:Si es True, entonces trata el umbral bajo y el umbral alto como cuantiles de la imagen de
                                la magnitud del borde, en lugar de los valores absolutos de la magnitud del borde.
                                Si es True entonces los umbrales deben estar en el rango [0, 1].

            Funcionamiento según la descripción de la función:
            Suavizar la imagen usando un Gaussiano con un ancho de "Sigma".
            Aplicar los operadores Sobel horizontal y vertical para obtener los gradientes dentro de la imagen.
                La fuerza del borde es la norma del gradiente.
            Estrechar bordes potenciales a curvas de un píxel de ancho.
                Primero, encontrar la normal hasta el borde en cada punto. Esto se hace mirando los signos y la magnitud
                relativa de X-Sobel e Y-Sobel para clasificar los puntos en 4 categorías: horizontal, vertical, diagonal
                 y antidiagonal. Entonces se mira en la normal y se invierten las direcciones para ver si los valores en
                cualquiera de esas direcciones son más grandes que el punto en cuestión. Usa la interpolación para
                obtener una mezcla de en lugar de elegir el que está más cerca de lo normal.

            Realizar un umbral de histéresis: primero etiquetar todos los puntos por encima del umbral alto como bordes.
                Luego, recursivamente etiquetar cualquier punto por encima del umbral bajo que está 8-conectado a un
                punto etiquetado como un borde.

            Explicación propia:
            Sigma: Mediante este parámetro se suaviza la imagen. Los filtros más pequeños causan menos desenfoque, y
                permiten la detección de líneas pequeñas y afiladas. Un filtro más grande causa más desenfoque,
                difuminando el valor de un píxel dado en un área más grande de la imagen.
            Histéresis  de  umbral:   con este proceso se pretende reducir la posibilidad de aparición de contornos
                falsos.el uso de dos umbrales con histéresis permite más flexibilidad que en el enfoque de un solo
                umbral, pero siguen existiendo problemas generales de los enfoques de umbral.
                Un umbral demasiado alto puede hacer que se pierda información importante. Por otra parte,
                un umbral demasiado bajo identificará falsamente la información irrelevante (como el ruido) como
                importante.

            Mejor imagen:
                De los resultados de las pruebas se ha obersvar que el sigma tiene que ser inferior a 3, puesto que
                para ese valor ya se pierde informacion (hay numeros que dejan de verse)
                Asi que enun principio se elegio sigma = 2, pero posteriormente al variar los valores de los thresholds
                se comprobo que se obtenia un mejor resultado con un sigma de 1.

            V17 de SCI-KIT IMAGE
                Instalando la version dev de este paquete se peude implementar unas barras de deslizamiento para
                realizar las variaciones de los paramentros y ver los efectos de dichas variaciones en la imagen.

    '''

    #SCI_KIT SKIMAGE
    img_in = skimage.io.imread(file_sudoku, as_gray =True)
    #visualizar_imagen(img_in, 'Original')

    # viewer = skimage.viewer.ImageViewer(img_in)         # Necesario import viewer  y version v17 de skimage

    # Filtro Canny
    edges = skimage.feature.canny(img_in)
    #visualizar_imagen(edges, 'Canny')


    # Moficiacion de sigma (suavizado)
    edges_sigma_1 = skimage.feature.canny(img_in, sigma=2.0, low_threshold=0.1,
                                          high_threshold=0.2)
    edges_sigma_2 = skimage.feature.canny(img_in, sigma=3.0, low_threshold=0.1,
                                          high_threshold=0.2)
    edges_sigma_3 = skimage.feature.canny(img_in, sigma=4.0, low_threshold=0.1,
                                          high_threshold=0.2)

    # Visualizacion sigma = 1.0 y distntos thresholds
    visualizar_imagenes([edges, edges_sigma_1, edges_sigma_2, edges_sigma_3],
                        ['Por defecto, Sigma = 1', 'Sigma = 2', 'Sigma = 3', 'Sigma = 4'],2,2,
                        save_figure=True, figure_save_path='../data/out/practica03/T01/fig_Canny_comparacion_sigmas.png')

    # Moficiacion de valores de low_threshold para sigma 1
    edges_sigma2_low_1 = skimage.feature.canny(img_in, sigma=1.0, low_threshold=0.1,
                                               high_threshold=0.2)
    edges_sigma2_low_2 = skimage.feature.canny(img_in, sigma=1.0, low_threshold=0.3,
                                               high_threshold=0.2)
    edges_sigma2_low_3 = skimage.feature.canny(img_in, sigma=1.0, low_threshold=0.1,
                                               high_threshold=0.4)
    edges_sigma2_low_4 = skimage.feature.canny(img_in, sigma=1.0, low_threshold=0.3,
                                               high_threshold=0.4)
    # Visualizacion sigma = 1.0 y distntos thresholds
    visualizar_imagenes([edges_sigma2_low_1, edges_sigma2_low_2, edges_sigma2_low_3,edges_sigma2_low_4],
                        ['Sigma=1 low=0.1 high=0.2', 'Sigma=1 low=0.3 high = 0.2', 'Sigma=1 low=0.1 high=0.4',
                         'Sigma=1 low=0.3 high=0.4'],2,2, save_figure=True,
                        figure_save_path='../data/out/practica03/T01/fig_Canny_comparacion_low_thresholds.png')

    # Mejor imagen
    # Moficiacion de sigma (suavizado)
    image_f_canny = skimage.feature.canny(img_in, sigma=1.0, low_threshold=0.35,
                                          high_threshold=0.45)
    visualizar_imagen(image_f_canny, 'Mejor resultado con filtro Canny (sigma=1, low=0.35, high=0.45)', save_figure=True,
                      figure_save_path='../data/out/practica03/T01/fig_Canny_mejor.png')


    # PARA LA VERSION SCIKIT-IMAGE V17
    # https://github.com/scikit-image/scikit-image/blob/master/INSTALL.rst
    '''# Creacion del plugin
    canny_plugin = skimage.viewer.plugings.Plugin(image_filter = skimage.feature.canny)   # Clase para manipular imagenes
    canny_plugin.name= "Canny Filter Plugin"

    # Añadir deslizadores en el plugin
    canny_plugin += skimage.viewer.widgets.Slider(
        name= "sigma", low = 0.0, high=7.0, value=2.0
    )
    canny_plugin += skimage.viewer.widgets.Slider(
        name= "low_threshold", low = 0.0, high = 1.0, value = 0.1
    )
    canny_plugin += skimage.viewer.widgets.Slider(
        name = "high:threshold", low = 0.0, high = 1.0, value = 0.2
    )

    # Añadir el plugin a la imagen y mostrar la ventana
    viewer += canny_plugin
    viewer.show()'''




    # Con openCV
    '''img = cv2.imread(file_sudoku)
    edges = cv2.Canny(img,100,200)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()'''


def do_test_frangi():
    '''
        Existen otros métodos más avanzados para la obtención de bordes.
        Por ejemplo el filtro de frangi, ampliamente utilizado en imagen médica.

        NOMBRE:
        TODO:
            Para la imagen de color deseada aplicar el filtro de skimage frangi
            Analizar el efecto aplicando varios parámetros.
            Obtener la imagen que mejor aísle los bordes de la imagen y almacenarla en:
            /data/out/practica03/fig_frangi_XXX.png
            Respuesta:

            Parametros de la funcion Frangi
            def frangi(image, sigmas=range(1, 10, 2), scale_range=None, scale_step=None,
                beta1=None, beta2=None, alpha=0.5, beta=0.5, gamma=15, black_ridges=True):
                sigmas : (float) escalas de filtro
                         np.arange(scale_range[0], scale_range[1], scale_step)
                beta : Constante de corrección de Frangi que ajusta la sensibilidad del filtro a la desviación de una
                        estructura similar a una mancha.
                gamma: Constante de corrección de Frangi que ajusta la sensibilidad del filtro a las áreas de alta
                        varianza/textura/estructura.

            DESCRIPCIÓN:
            Este filtro puede ser usado para detectar crestas continuas, por ejemplo, vasos, arrugas, ríos.
            Puede usarse para calcular la fracción de la imagen completa que contiene tales objetos.
            Definido sólo para imágenes 2-D y 3-D.

    '''

    # Cargamos la imagen
    img_in = skimage.io.imread(file_vessels, as_gray=True)     # Imagen vessels
    visualizar_imagen(img_in, "Imagen Original")

    image_f_frangi = skimage.filters.frangi(img_in)
    visualizar_imagen(image_f_frangi, 'Frangi')

    # Parámetros modificados
    f1 = skimage.filters.frangi(img_in, sigmas=range(0, 20, 2))
    f2 = skimage.filters.frangi(img_in, beta=0.5)
    f3 = skimage.filters.frangi(img_in, gamma=0.5)
    f4 = skimage.filters.frangi(img_in, alpha=5.0)

    visualizar_imagenes([img_in, image_f_frangi, f1, f2, f3, f4],
                        ['Original', 'Frangi por defecto','Sigmas=range(10,20,2)', 'beta=0.5', 'gamma=0.5',
                         'alpha=0.5'],2,3, save_figure=True, figure_save_path='../data/out/practica03/T01/fig_frangi_comparacion.png')

    pass



if __name__ == "__main__":

    # do_test_efectos_filtros_lineales()
    # do_test_restauracion_imagen()
    # do_test_afilado_imagen()
    # do_test_gradiente_imagen()
    # do_test_canny()
    # do_test_frangi()