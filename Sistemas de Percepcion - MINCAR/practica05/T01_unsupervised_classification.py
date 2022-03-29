# -*- coding: utf-8 -*-
import numpy
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

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


def extract_geometrical_features(image_rgb):

    #SEGMENTAMOS LA IMAGEN
    # visualizar_imagen(image_rgb,'Imagen_Original')

    image_gray = skimage.color.rgb2gray(image_rgb)
    image_binary = image_gray>0.1
    image_binary_filtered = skimage.morphology.binary_closing(image_binary)
    # visualizar_imagen(image_binary_filtered, 'Imagen binaria')

    # label image regions
    label_image = label(image_binary_filtered)
    image_label_overlay = label2rgb(label_image, image=image_rgb)

    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.imshow(image_label_overlay)

    # EXTRAEMOS DESCRIPTORES
    lista_descriptores=[]
    for region in regionprops(label_image):

        if region.area >= 10:
            # draw rectangle around segmented coins
            # minr, minc, maxr, maxc = region.bbox
            # rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
            #                           fill=False, edgecolor='red', linewidth=2)
            # ax.add_patch(rect)

            lista_descriptores.append([region.label,region.area,region.extent,region.solidity,region.eccentricity])

    # ax.set_axis_off()
    # plt.tight_layout()
    # plt.show()

    #Pandas es una librería para manejo de datos.
    pandas_dataframe_descriptores = pd.DataFrame.from_records(lista_descriptores, columns=['Label','Area','Extent','Solidity','Eccentricity'],index='Label')
    print(pandas_dataframe_descriptores)

    #,LA IMAGEN LABEL Y LOS DESCRIPTORES

    return label_image,pandas_dataframe_descriptores


def do_test_kmeans():
    '''
    Nombre:
    TODO:
        En esta función se extrae un descriptor que contiene las geométricas de los diferentes blobs.
        Estas características se pueden seleccionar para generar un algoritmo KMeans que precalcule clústeres apropiados.
        En función de las características que preseleccionemos la función de similitud que definimos generará clústeres diferentes según las distancias entre ellos.
        Analizad el código porque será el punto de partida de los ejercicios siguientes.

    '''
    image_rgb_geometria = skimage.io.imread(file_geometrias)
    label_image, pandas_dataframe_descriptores = extract_geometrical_features(image_rgb_geometria)

    blob_indexes = pandas_dataframe_descriptores.index

    #Todos los descriptores posibles
    available_descriptors = ['Area','Extent','Solidity','Eccentricity']
    # Selecciona sólo tres descriptores:
    used_descriptors =  ['Area','Extent','Solidity']
    used_descriptors = ['Area', 'Extent', 'Solidity']
    used_descriptors = ['Extent', 'Solidity', 'Eccentricity']
    # used_descriptors = ['Area', 'Area', 'Area']

    array_descriptores= numpy.array([pandas_dataframe_descriptores[used_descriptors[0]],pandas_dataframe_descriptores[used_descriptors[1]],pandas_dataframe_descriptores[used_descriptors[2]]])
    array_descriptores=array_descriptores.transpose()

    '''
        Nombre:
        TODO:
           Verificar numero de clusters. ¿Cómo varía el resultado del algoritmo?
        Respuesta:  

        Si ponemos disminuimos el número de clústeres a 3 por ejemplo, el programa deja de diferenciar entre círculos y 
        cuadrados. A su vez, si disminuimos el número de clústeres a 2, los cuadrados y círculos se muestran como mismos 
        elementos y las estrellas de 5 puntas y 4 puntas son identificados como elementos iguales. 

        El aumento del numero de clústeres no lleva consigo ningún error de identificación, pues solo existen 4 tipos 
        distintos de geometría en la imagen.

    '''


    number_of_clusters = 6
    kmeans = KMeans(n_clusters=number_of_clusters, random_state=0).fit(array_descriptores)

    #Visualizar espacio de características
    fig = plt.figure(figsize=(4, 3))
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

    clusters = kmeans.labels_ + 1 # añadimos uno para que el cero sea el fondo

    ax.scatter(array_descriptores[:, 0], array_descriptores[:, 1], array_descriptores[:, 2],
               c=clusters.astype(numpy.float), edgecolor='k')

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel(used_descriptors[0])
    ax.set_ylabel(used_descriptors[1])
    ax.set_zlabel(used_descriptors[2])
    ax.set_title('Kmeans with %d clusters using %s features' % (number_of_clusters,used_descriptors))
    ax.dist = 12

    plt.show(block=True)

    #Visualizar imagen
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_rgb_geometria)

    # Corregimos los Labels
    clustered_label_image = label_image.copy()
    lista_descriptores = []
    for label_val,cluster_val in zip(blob_indexes,clusters):
        clustered_label_image[label_image == label_val] = cluster_val

    ax.imshow(clustered_label_image)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()

def do_test_kmeans_1():
    '''
    Nombre:
    TODO:
        Se pide:
            - Elegir una combinación de descriptores que me permita separar las siguientes dos clases:
                - Cuadrados y círculos
                - Estrellas
            - Partid de la función do_test_kmeans
            - Almacedad las figuras en ./out/practica05/test_kmeans_1_fig_xxx
            - Explicad la motivación del código en los comentarios.
            Respuesta:

            Como se ha mencionado antes, con la combinación de descriptores utilizados posteriormente, escogiendo un
            clúster de 3 el programa separa por un lado los círculos y los cuadrados, y por otro lado los dos tipos de
            estrellas. Por lo tanto, no es necesario la modificación de la combinación de descriptores utilizados, sino
            un adecuado clúster para este caso.

    '''

    image_rgb_geometria = skimage.io.imread(file_geometrias)
    label_image, pandas_dataframe_descriptores = extract_geometrical_features(image_rgb_geometria)

    blob_indexes = pandas_dataframe_descriptores.index

    # Todos los descriptores posibles
    available_descriptors = ['Area', 'Extent', 'Solidity', 'Eccentricity']
    # Selecciona sólo tres descriptores:
    used_descriptors = ['Area', 'Extent', 'Solidity']
    used_descriptors = ['Area', 'Extent', 'Solidity']
    used_descriptors = ['Extent', 'Solidity', 'Eccentricity']
    # used_descriptors = ['Area', 'Area', 'Area']

    array_descriptores = numpy.array(
        [pandas_dataframe_descriptores[used_descriptors[0]], pandas_dataframe_descriptores[used_descriptors[1]],
         pandas_dataframe_descriptores[used_descriptors[2]]])
    array_descriptores = array_descriptores.transpose()

    number_of_clusters = 2
    kmeans = KMeans(n_clusters=number_of_clusters, random_state=0).fit(array_descriptores)

    # Visualizar espacio de características
    fig = plt.figure(figsize=(4, 3))
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

    clusters = kmeans.labels_ + 1  # añadimos uno para que el cero sea el fondo

    ax.scatter(array_descriptores[:, 0], array_descriptores[:, 1], array_descriptores[:, 2],
               c=clusters.astype(numpy.float), edgecolor='k')

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel(used_descriptors[0])
    ax.set_ylabel(used_descriptors[1])
    ax.set_zlabel(used_descriptors[2])
    ax.set_title('Kmeans with %d clusters using %s features' % (number_of_clusters, used_descriptors))
    ax.dist = 12

    plt.show(block=True)

    # Visualizar imagen
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_rgb_geometria)

    # Corregimos los Labels
    clustered_label_image = label_image.copy()
    lista_descriptores = []
    for label_val, cluster_val in zip(blob_indexes, clusters):
        clustered_label_image[label_image == label_val] = cluster_val

    ax.imshow(clustered_label_image)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig.savefig('..\data\out\practica05\T01\img_test_kmeans_1_fig_001.png')

    pass


def do_test_kmeans_2():
    '''
    Nombre:
    TODO:
        El algoritmo de KMeans se ve afectado por la escala de las variables descriptoras.
        Si una variable tiene un rango entre 0 y 1 (p.e. excentricidad) y otra variable tiene un rango entre 0-10^6 (p.e. área)
        esta última tendrá una ponderación mucho mayor en el cálculo de las distancias haciendo que los clústeres dependan sólo del área.
        Es por eso importante normalizar el vector de descriptores.
        Se pide:
            - Normalizar el vector de descriptores dividiendo cada descriptor por su valor máximo
            - Elegid un triplete de tres desciptores en el que se encuentre el área.
            - Realizad un análisis de los resultados de clustering con el descriptor normalizado y sin normalizar.
            - Almacedad las figuras en ./out/practica05/test_kmeans_2_fig_xxx
            - Explicad la motivación del código en los comentarios.
        Respuesta:
    '''

    image_rgb_geometria = skimage.io.imread(file_geometrias)
    label_image, pandas_dataframe_descriptores = extract_geometrical_features(image_rgb_geometria)

    blob_indexes = pandas_dataframe_descriptores.index

    # Todos los descriptores posibles
    available_descriptors = ['Area', 'Extent', 'Solidity', 'Eccentricity']
    # Selecciona sólo tres descriptores:
    used_descriptors = ['Area', 'Extent', 'Solidity']
    #used_descriptors = ['Area', 'Extent', 'Solidity']
    #used_descriptors = ['Extent', 'Solidity', 'Eccentricity']
    # used_descriptors = ['Area', 'Area', 'Area']

    area = pandas_dataframe_descriptores[used_descriptors[0]]
    extent = pandas_dataframe_descriptores[used_descriptors[1]]
    solidity = pandas_dataframe_descriptores[used_descriptors[2]]

    area_norm = area / area.max()
    extent_norm = extent / extent.max()
    solidity_norm = solidity / solidity.max()

    array_descriptores_norm = numpy.array(
        [area_norm,extent_norm,solidity_norm])
    array_descriptores_norm = array_descriptores_norm.transpose()

    array_descriptores = numpy.array(
        [pandas_dataframe_descriptores[used_descriptors[0]], pandas_dataframe_descriptores[used_descriptors[1]],
         pandas_dataframe_descriptores[used_descriptors[2]]])
    array_descriptores = array_descriptores.transpose()


    number_of_clusters = 4
    kmeans = KMeans(n_clusters=number_of_clusters, random_state=0).fit(array_descriptores)

    kmeans_norm = KMeans(n_clusters=number_of_clusters, random_state=0).fit(array_descriptores_norm)



    # Visualizar espacio de características
    fig = plt.figure(figsize=(4, 3))
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

    clusters = kmeans.labels_ + 1  # añadimos uno para que el cero sea el fondo

    clusters_norm = kmeans.labels_ + 1

    #SIN NORMALIZAR

    ax.scatter(array_descriptores[:, 0], array_descriptores[:, 1], array_descriptores[:, 2],
               c=clusters.astype(numpy.float), edgecolor='k')

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel(used_descriptors[0])
    ax.set_ylabel(used_descriptors[1])
    ax.set_zlabel(used_descriptors[2])
    ax.set_title('Kmeans with %d clusters using %s features' % (number_of_clusters, used_descriptors))
    ax.dist = 12

    plt.show(block=True)

    # Visualizar imagen
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_rgb_geometria)

    # Corregimos los Labels
    clustered_label_image = label_image.copy()
    lista_descriptores = []
    for label_val, cluster_val in zip(blob_indexes, clusters):
        clustered_label_image[label_image == label_val] = cluster_val

    ax.imshow(clustered_label_image)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig.savefig('..\data\out\practica05\T01\img_test_kmeans_2_fig_001.png')


    #NORMALIZADO
    fig = plt.figure(figsize=(4, 3))
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

    ax.scatter(array_descriptores_norm[:, 0], array_descriptores_norm[:, 1], array_descriptores_norm[:, 2],
               c=clusters_norm.astype(numpy.float), edgecolor='k')

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel(used_descriptors[0])
    ax.set_ylabel(used_descriptors[1])
    ax.set_zlabel(used_descriptors[2])
    ax.set_title('Kmeans with %d clusters using %s features and applying normalization' % (number_of_clusters, used_descriptors))
    ax.dist = 12

    plt.show(block=True)

    # Visualizar imagen
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_rgb_geometria)

    # Corregimos los Labels
    clustered_label_image = label_image.copy()
    lista_descriptores = []
    for label_val, cluster_val in zip(blob_indexes, clusters):
        clustered_label_image[label_image == label_val] = cluster_val

    ax.imshow(clustered_label_image)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig.savefig('..\data\out\practica05\T01\img_test_kmeans_2_fig_001_norm.png')

    pass

if __name__ == "__main__":
    #do_test_kmeans()
    #do_test_kmeans_1()
    do_test_kmeans_2()