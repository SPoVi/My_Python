# -*- coding: utf-8 -*-
import numpy
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder

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
file_geometrias_reescalada = '../data/color/geometrias_rescalada.png'
file_geometrias_circulo_cuadrado = '../data/color/geometrias_circulos_cuadrados.png'
file_geometrias_estrellas = '../data/color/geometrias_estrellas.png'

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


def do_test_knn():
    '''
    Nombre:
    TODO:
        En esta función se extraen las características geométricas de los diferentes blobs de dos imágenes.
        En la primera imagen tenemos circulos y cuadrados. --> Clase A
        En la segunda tenemos distintos tipos de estrellas. --> Clase B
        Vamos a crear un clasificador supervisado que separe en estos dos clases --> KNN
        Analizad el código porque será el punto de partida de los ejercicios siguientes.

    '''

    # --------------------------- OBTENCIÓN DE LOS DATOS -------------------------------------
    #IMAGEN COMPLETA
    # Se carga la imagen con todos los objetos, cuadrados, estrellas y circulos.
    image_rgb_geometria_completa = skimage.io.imread(file_geometrias)
    # Llamando a esta función se obtiene la imagen labelizada y las caracteristicas de cada objeto
    label_image_completa, pandas_dataframe_descriptores_completa = extract_geometrical_features(image_rgb_geometria_completa)
    visualizar_imagenes([image_rgb_geometria_completa, label_image_completa], ['Completa','Completa Labelizada'],2,1)
    blob_indexes_completa = pandas_dataframe_descriptores_completa.index
    # Se muestran todos los descriptores de cada objeto
    array_descriptores_completa_= numpy.array(pandas_dataframe_descriptores_completa)


    #IMAGEN CLASE A
    # Se carga una imagen igual pero que unicamente contiene los circulos y cuadrados
    print('\n::......CIRCULOS Y CUADRADOS......::')
    image_rgb_geometria_clase_a = skimage.io.imread(file_geometrias_circulo_cuadrado)
    label_image_clase_a, pandas_dataframe_descriptores_clase_a = extract_geometrical_features(image_rgb_geometria_clase_a)
    blob_indexes_clase_a = pandas_dataframe_descriptores_clase_a.index
    # Se muestran las carateristicas de este tipo de figuras
    array_descriptores_clase_a_= numpy.array(pandas_dataframe_descriptores_clase_a)

    #IMAGEN CLASE B
    # Se carga una imagen igual pero que unicamente contiene las estrellas
    print('\n::.......ESTRELLAS.......::')
    image_rgb_geometria_clase_b = skimage.io.imread(file_geometrias_estrellas)
    label_image_clase_b, pandas_dataframe_descriptores_clase_b = extract_geometrical_features(image_rgb_geometria_clase_b)
    blob_indexes_clase_b = pandas_dataframe_descriptores_clase_a.index
    # Se muestran las carateristicas de este tipo de figuras
    array_descriptores_clase_b_= numpy.array(pandas_dataframe_descriptores_clase_b)

    # -------------------------------- PREPARACIÓN DE LOS DATOS -----------------------------------------------

    # En clasificación supervisada necesitamos tener pares de datos X (descriptores),Y (clase a la que pertenece)
    # para 'enseñar al sistema'
    #X tiene tamaño (n_samples,n_features)
    #Y tiene el tamaño (n_samples,n_clases).
    # Normalmente la clase está codificada como un vector si tenemos dos clases, la cero es:
    # Clase 0 = [1,0], clase 1 = [0,1]
    #Si tuvieramos tres clases (perro, gato, oso) = [1,0,0] [0,1,0] [0,0,1]

    # Se declaran las clases
    Y_clase_a = numpy.zeros((array_descriptores_clase_a_.shape[0], 1))
    Y_clase_b = numpy.zeros((array_descriptores_clase_b_.shape[0], 1))
    # La clase a se rellena con ceros
    Y_clase_a[:] = 0
    # Mientras que la b con unos
    Y_clase_b[:] = 1
    # La clase estrellas tendra valores 1.0 y la clase circulos y cuadrados 0.1
    Y_train_n = numpy.vstack((Y_clase_a,Y_clase_b))
    print (Y_train_n)

    #Si en el problema tuvieramos más clases Y sería de tamño (n_samples,num_clases) ya que las clases se codifican con one_hot_encoder
    onehot_encoder = OneHotEncoder(sparse=False)
    Y_train_onehot_encoded = onehot_encoder.fit_transform(Y_train_n)
    print(Y_train_onehot_encoded)
    # No lo necesitamos ya que nuestro problema es binario (dos clases), pero es necesario para problemas con más de una clase

    X_train = numpy.vstack((array_descriptores_clase_a_,array_descriptores_clase_b_))
    Y_train = Y_train_onehot_encoded

    # --------------------------------- DISEÑO DEL CLASIFICADOR -------------------------------------
    # Clasificador por vecinos mas cercano
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=3)
    # -------------------------------------- ENTRENAMIENTO ------------------------------------------
    # Se entrena con los objetos y sus caracteristicas y Y train que es la clase a la que pertenece
    knn.fit(X_train, Y_train)
    # -------------------------------------- CLASIFICACIÓN -------------------------------------------
    # Se calcula y muestra la probabilidad de que sea de cada una de las clases
    Y_probabilidad = knn.predict_proba(array_descriptores_completa_)
    Y_prediccion_hotencoded = knn.predict(array_descriptores_completa_)
    # Nos quedamos con el indice del valor más alto
    Y_prediccion_label = numpy.argmax(Y_prediccion_hotencoded, axis=-1)
    # Y devuelve a que clase cree que pertenece cada objeto
    print(Y_prediccion_label)

    #Visualizar imagen
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_rgb_geometria_completa)

    # Corregimos los Labels
    predicted_label_image = label_image_completa.copy()

    # Entonces con la clasificacion se pintan cada clase de una forma
    for i in range(len(blob_indexes_completa)):
        blob_index = blob_indexes_completa[i]
        predicted_class = Y_prediccion_label[i] +1 #(añadimos uno para usar el fondo como clase 0)
        predicted_label_image[label_image_completa == blob_index] = predicted_class

    ax.imshow(predicted_label_image)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()

def do_test_knn_1():
    '''
    Nombre:
    TODO:
        En este código hemos sustituido el fichero de testing de geometrías por otra imagen que ha sido reescalada.
        Esto hace que el clasificador funcione sobre datos nunca vistos y en los que existe un cambio de dominio (los objetos son algo más grandes).
        Esto hace que, al ser el área la característica más dominante, sea la que influya en el KNN.
        Se pide:
            Corrige la preponderancia del área mediante la normalización de los descriptores.
                Se puede hacer manualmente o bien utilizando alguna de las funcionalidades de sklearn:
                    https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html
        Como siempre almacenar los resultados en /out/practica06/test_knn_1_xxx.png
    '''
    #IMAGEN COMPLETA
    image_rgb_geometria_completa = skimage.io.imread(file_geometrias_reescalada)
    label_image_completa, pandas_dataframe_descriptores_completa = extract_geometrical_features(image_rgb_geometria_completa)
    blob_indexes_completa = pandas_dataframe_descriptores_completa.index
    array_descriptores_completa_= numpy.array(pandas_dataframe_descriptores_completa)

    imax = len(array_descriptores_completa_)
    areamax = numpy.amax(array_descriptores_completa_)

    # for i in array_descriptores_clase_a_:
    for i in range(0, imax):
        array_descriptores_completa_[i, 0] = array_descriptores_completa_[i, 0] / areamax

    #IMAGEN CLASE A
    image_rgb_geometria_clase_a = skimage.io.imread(file_geometrias_circulo_cuadrado)
    label_image_clase_a, pandas_dataframe_descriptores_clase_a = extract_geometrical_features(image_rgb_geometria_clase_a)
    blob_indexes_clase_a = pandas_dataframe_descriptores_clase_a.index
    array_descriptores_clase_a_= numpy.array(pandas_dataframe_descriptores_clase_a)

    imax = len(array_descriptores_clase_a_)
    areamax = numpy.amax(array_descriptores_clase_a_)

    #for i in array_descriptores_clase_a_:
    for i in range (0,imax):
        array_descriptores_clase_a_[i,0] = array_descriptores_clase_a_[i,0]/areamax

    #IMAGEN CLASE B
    image_rgb_geometria_clase_b = skimage.io.imread(file_geometrias_estrellas)
    label_image_clase_b, pandas_dataframe_descriptores_clase_b = extract_geometrical_features(image_rgb_geometria_clase_b)
    blob_indexes_clase_b = pandas_dataframe_descriptores_clase_a.index
    array_descriptores_clase_b_= numpy.array(pandas_dataframe_descriptores_clase_b)
    numpy.argmax(array_descriptores_clase_b_, axis=-1)

    imax = len(array_descriptores_clase_b_)
    areamax = numpy.amax(array_descriptores_clase_b_)

    # for i in array_descriptores_clase_a_:
    for i in range(0, imax):
        array_descriptores_clase_b_[i, 0] = array_descriptores_clase_b_[i, 0] / areamax

    #Preparación de datos. En clasificación supervisada necesitamos tener pares de datos X (descriptores),Y (clase a la que pertenece)
    # para 'enseñar al sistema'
    #X tiene tamaño (n_samples,n_features)
    #Y tiene el tamaño (n_samples,n_clases). Normalmente la clase está codificada como un vector si tenemos dos clases, la cero es:
    # Clase 0 = [1,0], clase 1 = [0,1]
    #Si tuvieramos tres clases (perro, gato, oso) = [1,0,0] [0,1,0] [0,0,1]

    Y_clase_a = numpy.zeros((array_descriptores_clase_a_.shape[0],1))
    Y_clase_b = numpy.zeros((array_descriptores_clase_b_.shape[0], 1))
    Y_clase_a[:] = 0
    Y_clase_b[:] = 1
    Y_train_n = numpy.vstack((Y_clase_a,Y_clase_b))
    print (Y_train_n)

    #Si en el problema tuvieramos más clases Y sería de tamño (n_samples,num_clases) ya que las clases se codifican con one_hot_encoder
    onehot_encoder = OneHotEncoder(sparse=False)
    Y_train_onehot_encoded = onehot_encoder.fit_transform(Y_train_n)
    print(Y_train_onehot_encoded)
    # No lo necesitamos ya que nuestro problema es binario (dos clases), pero es necesario para problemas con más de una clase

    X_train = numpy.vstack((array_descriptores_clase_a_,array_descriptores_clase_b_))
    Y_train = Y_train_onehot_encoded

    # DISEÑO DEL CLASIFICADOR
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=3)
    # ENTRENAMIENTO
    knn.fit(X_train, Y_train)
    # CLASIFICACIÓN
    Y_probabilidad = knn.predict_proba(array_descriptores_completa_)
    Y_prediccion_hotencoded = knn.predict(array_descriptores_completa_)
    Y_prediccion_label = numpy.argmax(Y_prediccion_hotencoded, axis=-1)
    # o para recuperar el indice de las clases
    print(Y_prediccion_label)

    #Visualizar imagen
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_rgb_geometria_completa)

    # Corregimos los Labels
    predicted_label_image = label_image_completa.copy()

    for i in range(len(blob_indexes_completa)):
        blob_index = blob_indexes_completa[i]
        predicted_class = Y_prediccion_label[i] +1 #(añadimos uno para usar el fondo como clase 0)
        predicted_label_image[label_image_completa == blob_index] = predicted_class

    ax.set_title('Clasificación modelo KNN')
    ax.imshow(predicted_label_image)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig.savefig('..\data\out\practica05\T02\img_test_knn_1_001.png')


def do_test_knn_2():
    '''
    Nombre:
    TODO:
       SCIKIT-Learn permite cambiar el clasificador de forma muy sencilla.
       Esto se hace simplemente generando un clasificador distinto en la llamada al constructor.
       Repetid el ejercicio anterior utilizando un clasificador Naive Bayes (https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB)
       u otro que se os ocurra.
       Como siempre almacenar los resultados en /out/practica06/test_knn_2_xxx.png
    '''

    # --------------------------- OBTENCIÓN DE LOS DATOS -------------------------------------
    #IMAGEN COMPLETA
    # Se carga la imagen con todos los objetos, cuadrados, estrellas y circulos.
    image_rgb_geometria_completa = skimage.io.imread(file_geometrias)
    # Llamando a esta función se obtiene la imagen labelizada y las caracteristicas de cada objeto
    label_image_completa, pandas_dataframe_descriptores_completa = extract_geometrical_features(image_rgb_geometria_completa)
    visualizar_imagenes([image_rgb_geometria_completa, label_image_completa], ['Completa','Completa Labelizada'],2,1, save_figure=True,
                        figure_save_path='../data/out/practica05/T02/img_test_knn_2_001.png')
    blob_indexes_completa = pandas_dataframe_descriptores_completa.index
    # Se muestran todos los descriptores de cada objeto
    array_descriptores_completa_= numpy.array(pandas_dataframe_descriptores_completa)


    #IMAGEN CLASE A
    # Se carga una imagen igual pero que unicamente contiene los circulos y cuadrados
    print('\n::......CIRCULOS Y CUADRADOS......::')
    image_rgb_geometria_clase_a = skimage.io.imread(file_geometrias_circulo_cuadrado)
    label_image_clase_a, pandas_dataframe_descriptores_clase_a = extract_geometrical_features(image_rgb_geometria_clase_a)
    blob_indexes_clase_a = pandas_dataframe_descriptores_clase_a.index
    # Se muestran las carateristicas de este tipo de figuras
    array_descriptores_clase_a_= numpy.array(pandas_dataframe_descriptores_clase_a)

    #IMAGEN CLASE B
    # Se carga una imagen igual pero que unicamente contiene las estrellas
    print('\n::.......ESTRELLAS.......::')
    image_rgb_geometria_clase_b = skimage.io.imread(file_geometrias_estrellas)
    label_image_clase_b, pandas_dataframe_descriptores_clase_b = extract_geometrical_features(image_rgb_geometria_clase_b)
    blob_indexes_clase_b = pandas_dataframe_descriptores_clase_a.index
    # Se muestran las carateristicas de este tipo de figuras
    array_descriptores_clase_b_= numpy.array(pandas_dataframe_descriptores_clase_b)

    # -------------------------------- PREPARACIÓN DE LOS DATOS -----------------------------------------------

    # En clasificación supervisada necesitamos tener pares de datos X (descriptores),Y (clase a la que pertenece)
    # para 'enseñar al sistema'
    #X tiene tamaño (n_samples,n_features)
    #Y tiene el tamaño (n_samples,n_clases).
    # Normalmente la clase está codificada como un vector si tenemos dos clases, la cero es:
    # Clase 0 = [1,0], clase 1 = [0,1]
    #Si tuvieramos tres clases (perro, gato, oso) = [1,0,0] [0,1,0] [0,0,1]

    # Se declaran las clases
    Y_clase_a = numpy.zeros((array_descriptores_clase_a_.shape[0], 1))
    Y_clase_b = numpy.zeros((array_descriptores_clase_b_.shape[0], 1))
    # La clase a se rellena con ceros
    Y_clase_a[:] = 0
    # Mientras que la b con unos
    Y_clase_b[:] = 1
    # La clase estrellas tendra valores 1.0 y la clase circulos y cuadrados 0.1
    Y_train_n = numpy.vstack((Y_clase_a,Y_clase_b))
    print (Y_train_n)

    #Si en el problema tuvieramos más clases Y sería de tamño (n_samples,num_clases) ya que las clases se codifican con one_hot_encoder
    onehot_encoder = OneHotEncoder(sparse=False)
    Y_train_onehot_encoded = onehot_encoder.fit_transform(Y_train_n)
    print(Y_train_onehot_encoded)
    # No lo necesitamos ya que nuestro problema es binario (dos clases), pero es necesario para problemas con más de una clase

    X_train = numpy.vstack((array_descriptores_clase_a_,array_descriptores_clase_b_))
    Y_train = Y_train_onehot_encoded

    # --------------------------------- DISEÑO DEL CLASIFICADOR -------------------------------------
    # Clasificador por NaiveBayes Gaussian
    from sklearn.naive_bayes import GaussianNB
    knn = GaussianNB()
    # -------------------------------------- ENTRENAMIENTO ------------------------------------------
    # Se entrena con los objetos y sus caracteristicas y Y train que es la clase a la que pertenece
    knn.fit(X_train, Y_train[:,1])
    # -------------------------------------- CLASIFICACIÓN -------------------------------------------
    # Se calcula y muestra la probabilidad de que sea de cada una de las clases
    Y_probabilidad = knn.predict_proba(array_descriptores_completa_)
    Y_prediccion_hotencoded = knn.predict(array_descriptores_completa_)
    # Nos quedamos con el indice del valor más alto
    Y_prediccion_label = numpy.argmax(Y_prediccion_hotencoded, axis=-1)
    # Y devuelve a que clase cree que pertenece cada objeto
    print(Y_prediccion_label)

    #Visualizar imagen
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_rgb_geometria_completa)

    # Corregimos los Labels
    predicted_label_image = label_image_completa.copy()

    # Entonces con la clasificacion se pintan cada clase de una forma
    for i in range(len(blob_indexes_completa)):
        blob_index = blob_indexes_completa[i]
        predicted_class = Y_prediccion_hotencoded[i] +1 #(añadimos uno para usar el fondo como clase 0)
        predicted_label_image[label_image_completa == blob_index] = predicted_class

    # Img final
    ax.set_title('Clasificación modelo Naive Bayes-Gaussian')
    ax.imshow(predicted_label_image)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig.savefig('..\data\out\practica05\T02\img_test_knn_2_002.png')


if __name__ == "__main__":
    # do_test_knn()
    do_test_knn_1()
    # do_test_knn_2()