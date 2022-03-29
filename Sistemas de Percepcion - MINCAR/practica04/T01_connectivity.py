# -*- coding: utf-8 -*-
__author__ = 106360

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import skimage
from skimage import data
from skimage.filters import threshold_otsu, threshold_local # New: local =adaptive
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
import skimage.morphology
from skimage.morphology import closing, square, disk , opening, dilation, erosion # New opening, dilation, erosion
from skimage.color import label2rgb
from practica00.T01_cargar_imagen import visualizar_imagenes,visualizar_imagen
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi    # Para el areal de los granos de arroz

from skimage.draw import ellipse
from skimage.measure import label, regionprops
from skimage.transform import rotate

#import matplotlib
#matplotlib.use('TkAgg')

file_garbanzos = '../data/conectividad/garbanzos.png'
file_rice = '../data/conectividad/rice.png'
image = data.coins()[50:-50, 50:-50]

def do_test_image_connectivity_coins():
    '''
    NOMBRE:
    TODO:
        Observa el código y el uso de la función label y regionprops.
        Lo utilizarás en los ejercicios siguientes.
    '''
    # apply threshold
    visualizar_imagen(image, 'monedas')

    thresh = threshold_otsu(image)
    bw = closing(image > thresh, square(3))
    visualizar_imagen(bw,'umbralizada')

    # remove artifacts connected to image border
    cleared = clear_border(bw)
    visualizar_imagen(cleared, 'umbralizada')

    # label image regions
    label_image = label(cleared)
    visualizar_imagen(label_image, 'labelled')
    image_label_overlay = label2rgb(label_image, image=image)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_label_overlay)

    for region in regionprops(label_image):
        # take regions with large enough areas
        if region.area >= 200:
            # draw rectangle around segmented coins
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(rect)

    ax.set_axis_off()
    plt.tight_layout()
    plt.show()

def do_test_image_connectivity_ellipse():
    '''
        NOMBRE:
        TODO:
            Observa el código y el uso de la función label y regionprops.
            Lo utilizarás en los ejercicios siguientes.
    '''
    image = np.zeros((600, 600))
    visualizar_imagen(image, 'zeros')

    rr, cc = ellipse(300, 350, 100, 220)
    image[rr, cc] = 1
    visualizar_imagen(image, 'ellipse')

    image = rotate(image, angle=15, order=0)
    visualizar_imagen(image, 'girada')

    label_img = label(image)
    regions = regionprops(label_img)

    fig, ax = plt.subplots()
    ax.imshow(image, cmap=plt.cm.gray)

    for props in regions:
        y0, x0 = props.centroid
        orientation = props.orientation
        x1 = x0 + math.cos(orientation) * 0.5 * props.minor_axis_length
        y1 = y0 - math.sin(orientation) * 0.5 * props.minor_axis_length
        x2 = x0 - math.sin(orientation) * 0.5 * props.major_axis_length
        y2 = y0 - math.cos(orientation) * 0.5 * props.major_axis_length

        ax.plot((x0, x1), (y0, y1), '-r', linewidth=2.5)
        ax.plot((x0, x2), (y0, y2), '-r', linewidth=2.5)
        ax.plot(x0, y0, '.g', markersize=15)

        minr, minc, maxr, maxc = props.bbox
        bx = (minc, maxc, maxc, minc, minc)
        by = (minr, minr, maxr, maxr, minr)
        ax.plot(bx, by, '-b', linewidth=2.5)

    ax.axis((0, 600, 600, 0))
    plt.show()

def do_test_image_granos_arroz():
    '''
    NOMBRE:
    TODO:
        Sobre la imagen rice.png realiza lo siguiente:
        - Segmenta la imagen para aislar todos los granos de arroz. (Blanco y Negro)
        - Mediante las técnicas de etiquetado estudiadas:
            - calcula el área y la longitud mayor del grano (eje mayor de la elipse equivalente) de cada uno de los granos de arroz.
            - Pinta el cajon capaz de cada objeto analizado.
        - Imaginad que estamos desarrollando un control de calidad de granos de arroz para una envasadora.
            Devuelve el valor medio y la desviación típica de la longitud y área de grano de arroz
        Almacena las imágenes obtenidas en ./data/out/image_granos_arroz_XXX.png
        Respuesta:

        # HOJA DE RUTA (Descripcion a groso modo del proceso)
        - La img tiene una escala de grises del 0 al 255 (8-unit).
         El objetivo consiste segmentar la img, dando valores distintos a los objetos.
         En este caso tenemos dos tipos de regiones, uno pertenece al arroz y otro al fondo vacio.
         Teniendo esto en cuenta se realizara una segmentacion binaria, convirtiendo la imagen de escala de grises a
         blanco o negro.
         Una vez realizado se contarán los granos de arroz.

        # SEGMENTADO Y AISLADO
         -- Eliminacion de bordes:
            -- Se ha realizado una erosion previa a la elimacion de bordes para separar aquellos granaos que estaban
            unidos a granos que estaban en contacto con el borde.
            -- Se ha aplicado la eliminacion de los granos en contacto con el borde.
            -- Posteriormente se ha dilatado (con el mismo valor al de la erosion anterior) para que vuelvan a su tamaño
            original.
            -- Se ha vuelto a pasar el filtro que elimina los granos en contacto con el borde (por si se da el caso de
            que al erosionar la img original se suprime el contacto del grano, como se da en este caso)

        # TECNICAS DE ETIQUETADO
         --

    '''
    # Visualizar imagen

    image = skimage.io.imread(file_rice) # imagen arroz
    #visualizar_imagen(image, 'Arroz')

    img_threshold = threshold_local(image, 255)
    # Función de scikit-image que aplica un umbral (threshold) para cada valor de la img
    image_binary_adaptive = image>img_threshold # si cambias signo a '<' los granos salen negros y el fondo blanco
    visualizar_imagenes([image,image_binary_adaptive],['Original','Imagen binaria'],2,1,
                        save_figure=True, figure_save_path='../data/out/practica04/T01/image_granos_arroz_001.png')

    bw = image_binary_adaptive
    # Eliminacion de elementos conectados al borde de la img
    cleared_original = clear_border(bw)             # Eliminacion del borde de la img original (para comparar despues)
    bw = erosion(image_binary_adaptive, disk(3))    # Erosion
    cleared_erosion = clear_border(bw)              # Eliminacion del borde de la img erosinada
    bw = dilation(cleared_erosion, disk(3))         # Dilatacion (vuelta a tamaño original)
    cleared_filtered = clear_border(bw)             # Eliminacion del borde tras la erosion y la dilatacion
    visualizar_imagenes([image_binary_adaptive, cleared_original, cleared_erosion, cleared_filtered],
                        ['original', 'sin bordes original', 'sin bordes tras erosion', 'sin bores tras erosion y dilatacion'],2,2,
                        save_figure=True, figure_save_path='../data/out/practica04/T01/image_granos_arroz_002.png')

    cleared_filtered = erosion(cleared_filtered, disk(2))
    # label image regions
    # Permite el etiquetado de las imagenes. Solo vale con grises.
    label_image = label(cleared_filtered)
    visualizar_imagen(label_image, 'Nivelada', save_figure= True,
                      figure_save_path='../data/out/practica04/T01/image_granos_arroz_003.png')
    image_label_overlay = label2rgb(label_image, image=image) # paso de grises a color
    visualizar_imagen(image_label_overlay, 'Nivelada a color', save_figure= True,
                      figure_save_path='../data/out/practica04/T01/image_granos_arroz_004.png')

    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(image_label_overlay)

    # Separacion de niveles
    # Mostrar garbanzos uno a uno
    for i in range(label_image.max()+1):
        if i == 0: # fondo
            continue
        bw_obj_i = label_image == i
        #visualizar_imagen(bw_obj_i)  # Visualizar garbanzo indiviudalmente
        # Lo hincho (dilate)
        bw_obj_i_hinchado = dilation(bw_obj_i, disk(2))
        #visualizar_imagen(bw_obj_i_hinchado)    # Visualizar garbanzo dilatado
        # Lo vuelve a pegar en el objeto i
        label_image[bw_obj_i_hinchado] = i
        #print(i)

    image_label_overlay = label2rgb(label_image, image = image)
    fig, ax = plt.subplots(figsize = (10,6))
    ax.imshow(image_label_overlay)

    # crea lista de valores vacia
    list_areas = []         # area del grano
    list_major_axis = []    # longitud eje mayor del grano
    list_minor_axis = []    # longitud eje menor del grano
    cantidad = label_image.max()

    # Inicio creacion tabla de resultados
    print('| ID Grano |  Eje mayor  |  Eje menor  |  Area  |')
    print('-------------------------------------------------')

    # Dibujar cuadricula, ejes, centroide
    id = 0  # Inicializar contador
    for region in regionprops(label_image):
        # take regions with large enough areas
        if region.area >= 100:
            id = id + 1;

            y0, x0 = region.centroid     # mediana. Centroide de la figura
            orientation = region.orientation
            # Calculo lineas de orientacion (vertical y horizontal) de la figura
            x1 = x0 + math.cos(orientation) * 0.5 * region.minor_axis_length
            y1 = y0 - math.sin(orientation) * 0.5 * region.minor_axis_length
            x2 = x0 - math.sin(orientation) * 0.5 * region.major_axis_length
            y2 = y0 - math.cos(orientation) * 0.5 * region.major_axis_length
            # Creacion y adicion de las lineas
            ax.plot((x0, x1), (y0, y1), '-b', linewidth=2.5)
            ax.plot((x0, x2), (y0, y2), '-b', linewidth=2.5)
            ax.plot(x0, y0, '.g', markersize=15)

            # Dibujar rectangulo alrededor de los granos de arroz
            minr, minc, maxr, maxc = region.bbox    # puntos que delimintan la region (cuadrada)
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,   # Dibujar rectacngulo
                                      fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(rect)  # anadir a la img el rectangulo

            # Anadir valores a la lista
            minor_axis = np.sqrt((x1-x0)**2+(y1-y0)**2)
            major_axis = np.sqrt((x2-x0)**2+(y2-y0)**2)
            area = pi*minor_axis*major_axis

            #print(major_axis/minor_axis) # Ver la relacion entre ambos ejes

            # Asegurar que siempre tiene un tamaño razonable
            if major_axis/minor_axis < 4.0:
                list_areas.append(area)

            # Asegurar que siempre se coje el eje mayor
            if major_axis > minor_axis:
                list_major_axis.append(major_axis)
            else:
                list_major_axis.append(minor_axis)

            # Asegurar que siempre se coje el eje menor
            if major_axis < minor_axis:
                list_minor_axis.append(major_axis)
            else:
                list_minor_axis.append(minor_axis)

            # Adicion de datos del grano a la tabla
            #print('Numero de Grano    Eje mayor    Eje menor    Area')
            '''print('|{id:3d}| |{ma:3f.2}| |{mi:3f.2}| |{a:3f.2}|'.format(id = id, ma = major_axis, mi=minor_axis,
                                                                                  a=area))'''
            print('{id:6d}         {ma:03.3f}         {mi:03.3f}     {a:03.3f}'.format(id = id, ma = major_axis,
                                                                                       mi = minor_axis, a = area))

            '''Analizando el código de la talba: 
            El indicador {3} se corresponde al carácter ‘|’ que forma las columnas.
            Los numeros 0, 1, 2 se corresponden al orden de los elementos dentro 
            de format (‘x’ para 0), (‘x*x’ para 1),(‘x*x*x’ para 3).
            Y finalmente luego de los dos puntos encontramos el 2d, 3d, 4d que corresponden a la cantidad de caracteres 
            para indicar la alineación de los elementos según la cantidad de cifras de los números. 
            La letra ‘d’ se utiliza para indicar que son datos enteros, en el caso de datos de texto (string) 
            se utiliza ‘s’'''


    # Medias y desviaciónes típica
    media_area = np.array(list_areas).mean()
    desviacion_area = np.array(list_areas).std()
    media_major_axis = np.array(list_major_axis).mean()
    desviacion_major_axis = np.array(list_major_axis).std()
    media_minor_axis = np.array(list_minor_axis).mean()
    desviacion_minor_axis = np.array(list_minor_axis).std()

    ax.set_axis_off()
    ax.set_title('Localizacion y diferenciacion de granos de arroz.')
    plt.tight_layout() # Automatically adjust subplot parameters to give specified padding.
    plt.show()

    fig.savefig('..\data\out\practica04\T01\image_granos_arroz_005.png')

    # Mostrar resultaddos por pantalla
    print('\n')
    print('----RESULTADOS: MEDIAS Y DESVIACIONES----------')
    print('Cantidad de granos de arroz:          {0}'.format(cantidad))
    print('Media longitud eje mayor:             {0:03.3f}'.format(media_major_axis))
    print('Desviacion típica longitud eje mayor: {0:03.3f}'.format(desviacion_major_axis))
    print('Media longitud eje menor:             {0:03.3f}'.format(media_minor_axis))
    print('Desviacion típica longitud eje menor: {0:03.3f}'.format(desviacion_minor_axis))
    print('Media area:                           {0:03.3f}'.format(media_area))
    print('Desvicacion típica del area:          {0:03.3f}'.format(desviacion_area))

    pass


def do_test_image_garbanzos():
    '''
    NOMBRE:
    TODO:
        Sobre la imagen garbanzos.bmp realiza lo siguiente:
        - Segmenta la imagen para aislar todos los garbanzos y fideos.
        - Mediante las técnicas de etiquetado estudiadas calcula el área de cada uno de los garbanzos.
        - Pinta el cajon capaz de cada garbanzo analizado.
        - Devuelve el valor medio y la desviación típica de la longitud y área de grano de garbanzo
        Ojo: Ten en cuenta que hay que eliminar los fideos de la imagen en algún momento del proceso.
        Almacena las imágenes obtenidas en ./data/out/image_garbanzos_XXX.png
        Respuesta:

        PROCEDIMIENTO ---------------------------------------------------------------------------------------
        1. UMBRALIZACIÓN Y TRATAMIENTO CON OPERACIONES MORFOLOGICAS
            1.1. Selección modelo de color
            1.2. Umbralizado Otsu
            1.3. Operaciones morfologicas
                1.3.1. Cierre para rellenar huecos en garbanzos
                1.3.2. Apertura para eliminar los fideos
                1.3.3. Eliminación de los garbanzos cortados por los limites de la imagen
        2. SEPARACIÓN GARBANZOS (LABELIZADO)
            2.1. Erosion para separar los garbanzos entre si
            2.2. Etiquetado de los diferentes grupos de pixeles que se corresponden a cada uno de los garbanzos
            2.3. Hinchado progresivo de los garbanzos para mantenerlos separados
        3. EXTRACCIÓN DE CARACTERISTICAS
            3.1. Generación lista areas y contador id
            3.2. Para cada garbanzo extracción de su area, colocación en la lista y muestra del valor en pantalla
            3.3. Calculo del area media y desviación
            3.4. Muestra de resultados

    '''

    # La imagen con la que trabajaremos va es cargada
    food_image = skimage.io.imread(file_garbanzos)
    # Recortamos el último canal para poder trabajar con ella
    food_image = food_image[:, :, 0:3]

    # En el modelo de color RGB nos quedamos con el canal azul para separar los garbanzos y fideos del fondo
    canal_B = food_image[:, :, 2]
    visualizar_imagen(food_image,'canal_B')

    # Se realiza un umbralizado automático con otsu y se consigue la imagen binaria
    th_value_otsu = threshold_otsu(canal_B)
    bw = canal_B < th_value_otsu
    visualizar_imagen(bw, 'Binarizada con th %.2f' % th_value_otsu,save_figure=True,
                      figure_save_path='../data/out/practica04/T01/image_garbanzos_001.png')

    # Con operaciones morfológicas se realiza un tratamiento de la imagen binaria.
    # Se rellenan los huecos de los garbanzos
    bw1 = skimage.morphology.binary.binary_closing(bw, np.ones((10,10)))
    visualizar_imagenes([bw, bw1], ['original', 'post closing'], 2, 1,save_figure=True,
                      figure_save_path='../data/out/practica04/T01/image_garbanzos_002.png')

    # Se eliminan los fideos con un open mayor de su tamaño
    bw2 = skimage.morphology.binary.binary_opening(bw1, disk(25))
    visualizar_imagenes([bw1, bw2], ['post closing', 'post opening'], 2, 1,save_figure=True,
                      figure_save_path='../data/out/practica04/T01/image_garbanzos_003.png')

    # Los objetos que se mantengan en contacto con el borde son eliminados con el objetivo final de no tomar
    # datos de areas no completas que modifiquen erroneamente el valor final
    bw3 = clear_border(bw2)
    visualizar_imagen(bw3, 'umbralizada',save_figure=True,
                      figure_save_path='../data/out/practica04/T01/image_garbanzos_004.png')

    # Para separar los garbanzos se erosionan
    bw4 = skimage.morphology.binary.binary_erosion(bw3, disk(25))
    visualizar_imagenes([bw3, bw4], ['post closing', 'post opening'], 2, 1,save_figure=True,
                      figure_save_path='../data/out/practica04/T01/image_garbanzos_005.png')

    # Una vez se tienen separados los garbanzos a cada grupo de pixeles se les da un valor de referencia
    label_image = label(bw4)
    visualizar_imagen(label_image, 'labelled')
    # Se muestra la imagen original con los garbanzos segmentados
    image_label_overlay = label2rgb(label_image, image=food_image)
    visualizar_imagen(image_label_overlay, 'labelled',save_figure=True,
                      figure_save_path='../data/out/practica04/T01/image_garbanzos_006.png')


    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_label_overlay)
    # Numero de garbanzos detectados
    cantidadg = label_image.max()

    '''
    Para la cantidad de garbanzos detectada se realizan las siguientes operaciones. 
    En primer lugar se muestra el garbanzo reducido. Sobre ese garbanzo se aplica una dilatación del mismo tamaño que 
    la erosion realizada previamente. Una vez dilatado se le etiqueta con su numero.
    '''
    for i in range(cantidadg+1):
        if i ==0:
            continue
        bw_obi = label_image == i
        visualizar_imagen(bw_obi, 'garbanzo %d' % i)
        bw_obi_hinch = skimage.morphology.binary.binary_dilation(bw_obi, disk(25))
        visualizar_imagen(bw_obi_hinch, 'garbanzo %d' % i)
        label_image[bw_obi_hinch] = i

    # Muestra de los resultados
    image_label_overlay = label2rgb(label_image, image=food_image)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_label_overlay)

    lista_areas = []    # Generación lista para areas de garbanzos

    '''
    Para cada uno de los garbanzos detectados en primer lugar se comprueba si su area en pixeles no es exageradamente 
    pequeña y por lo tanto se trata de ruido. Una vez descartado, se calcula el rectángulo que se colocará rodeando al 
    garbanzo y se añade el area a la lista de areas. 
    '''
    # Inicio creacion tabla de resultados
    print('| ID Garbanzo |  Area (pixels)  |')
    print('---------------------')

    id = 1
    for region in regionprops(label_image):

        # take regions with large enough areas
        if region.area >= 100:
            # draw rectangle around segmented coins
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(rect)

            id = id + 1
            lista_areas.append(region.area)

            print('{id:6d}           {a:03.3f}'.format(id=id, a=region.area))

    # Calculo media y desviación tipica del area
    mediaarea = np.array(lista_areas).mean()
    stdarea = np.array(lista_areas).std()

    # Imagen final
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig.savefig('..\data\out\practica04\T01\image_garbanzos_007.png')

    # Resultados
    print('\n')
    print('----RESULTADOS: MEDIAS Y DESVIACIONES----------')
    print('Cantidad de Garbanzos:                {0}'.format(cantidadg))
    print('Media area:                           {0:03.3f}'.format(mediaarea))
    print('Desvicacion típica del area:          {0:03.3f}'.format(stdarea))


if __name__ == "__main__":
    # do_test_image_connectivity_coins()
    # do_test_image_connectivity_ellipse()
    # do_test_image_granos_arroz()
    do_test_image_garbanzos()
