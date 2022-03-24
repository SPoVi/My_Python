# -*- coding: utf-8 -*-
__author__ = 106360

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
import math
import matplotlib.pyplot as plt
import numpy as np

from skimage.draw import ellipse
from skimage.measure import label, regionprops
from skimage.transform import rotate

image = data.coins()[50:-50, 50:-50]

def do_test_image_connectivity_coins():
    '''
    NOMBRE:
    TODO:
        Observa el código y el uso de la función label y regionprops.
        Lo utilizarás en los ejercicios siguientes.
    '''
    # apply threshold
    thresh = threshold_otsu(image)
    bw = closing(image > thresh, square(3))

    # remove artifacts connected to image border
    cleared = clear_border(bw)

    # label image regions
    label_image = label(cleared)
    image_label_overlay = label2rgb(label_image, image=image)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_label_overlay)

    for region in regionprops(label_image):
        # take regions with large enough areas
        if region.area >= 100:
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

    rr, cc = ellipse(300, 350, 100, 220)
    image[rr, cc] = 1

    image = rotate(image, angle=15, order=0)

    label_img = label(image)
    regions = regionprops(label_img)

    fig, ax = plt.subplots()
    ax.imshow(image, cmap=plt.cm.gray)

    for props in regions:
        y0, x0 = props.centroid
        orientation = props.orientation
        x1 = x0 + math.cos(orientation) * 0.5 * props.major_axis_length
        y1 = y0 - math.sin(orientation) * 0.5 * props.major_axis_length
        x2 = x0 - math.sin(orientation) * 0.5 * props.minor_axis_length
        y2 = y0 - math.cos(orientation) * 0.5 * props.minor_axis_length

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
        - Segmenta la imagen para aislar todos los granos de arroz.
        - Mediante las técnicas de etiquetado estudiadas:
            - calcula el área y la longitud mayor del grano (eje mayor de la elipse equivalente) de cada uno de los granos de arroz.
            - Pinta el cajon capaz de cada objeto analizado.
        - Imaginad que estamos desarrollando un control de calidad de granos de arroz para una envasadora.
            Devuelve el valor medio y la desviación típica de la longitud y área de grano de arroz
        Almacena las imágenes obtenidas en ./data/out/image_granos_arroz_XXX.png
        Respuesta:
    '''


    pass


def do_test_image_garbanzos():
    '''
    NOMBRE:
    TODO:
        Sobre la imagen garbanzos.bmp realiza lo siguiente:
        - Segmenta la imagen para aislar todos los garbanzos y fideos.
        - Mediante las técnicas de etiquetado estudiadas calcula el área de cada uno de los garbanzos.
        - Pinta el cajon capaz de cada garbanzo analizado.
        - Devuelve el valor medio y la desviación típica de la longitud y área de grano de arroz
        Ojo: Ten en cuenta que hay que eliminar los fideos de la imagen en algún momento del proceso.
        Almacena las imágenes obtenidas en ./data/out/image_garbanzos_XXX.png
        Respuesta:
    '''

    pass


if __name__ == "__main__":
    # do_test_image_connectivity_coins()
    do_test_image_connectivity_ellipse()