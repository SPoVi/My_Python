# -*- coding: utf-8 -*-
__author__ = 106360

'''
Leed el documento asociado sobre deep learning (o la charla de Aitor Álvarez) y haced lo siguiente:
- Entrenar un modelo cifar10 con el script que os hemos dado (script T01_train_CNN.py)
- Crear un programita que cargue ese modelo y prediga si en una imagen hay cierta clase:
    Para ello debéis:
        - Cargar el fichero H5 proporcionado por el otro script.
        - Poner la imagen al tamaño (el mismo en el que se entrena la red) y escala (rango de los canales RGB) requerido.
        - Llamar a la función predict del modelo de keras para predecir.
        
        
        COMENTARIOS:
        
        Se han probado con multiples imagenes, y en la mayoria de ellas se ha dado con la solucion correcta.
        
        Por otra parte, nosiempre han sido acertados, como en el caso del gato. Para los archivos cat y cat2 no los ha 
        identificado correctamente, siendo la opcion correcta la segunda opcion de la red,  pero para el archivocat3 si 
        que ha acertado.
        
        Por otra parte, a modo de chiste, se ha cargado una imagen de superman esperando que lo identificara como un avión,
        resultado que se ha produido.

'''
import tensorflow as tf
import skimage,skimage.io,skimage.transform
import numpy

if __name__ == "__main__":

    # Lista de clases
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                   'dog', 'frog', 'horse', 'ship', 'truck']

    # Prueba 1: Avion
    mi_image_file = '../data/Tensorflow/avion.png' #buscad un fichero de imagen de alguna de las clases que existen
    model = tf.keras.models.load_model('mi_modelo.h5')
    #Lo cargamos
    image_rgb = skimage.io.imread(mi_image_file).astype(float)/255.0
    #Lo recortamos a 32x32
    image_rgb_32x32 = skimage.transform.resize(image_rgb,(32,32),preserve_range=True)
    imagen_extendida = numpy.expand_dims(image_rgb_32x32,axis=0)

    print(imagen_extendida.shape)
    prediction = model.predict(imagen_extendida)
    print('\n::...RESULTADOS PRUEBA 1.::')
    print('\nPrediccion: {0}'.format(prediction))

    # Identificacion de la clase
    posicion_clase = prediction.argmax()
    print('\nLa clase seleccionada ha sido : airplane')
    print('\nLa clase  identificada es: {0}'.format(class_names[posicion_clase]))


    # Prueba 2: Gato
    mi_image_file = '../data/Tensorflow/cat.jpg' #buscad un fichero de imagen de alguna de las clases que existen
    model = tf.keras.models.load_model('mi_modelo.h5')
    #Lo cargamos
    image_rgb = skimage.io.imread(mi_image_file).astype(float)/255.0
    #Lo recortamos a 32x32
    image_rgb_32x32 = skimage.transform.resize(image_rgb,(32,32),preserve_range=True)
    imagen_extendida = numpy.expand_dims(image_rgb_32x32,axis=0)

    print(imagen_extendida.shape)
    prediction = model.predict(imagen_extendida)
    print('\n::...RESULTADOS PRUEBA 2..::')
    print('\nPrediccion: {0}'.format(prediction))

    # Identificacion de la clase
    posicion_clase = prediction.argmax()
    print('\nLa clase seleccionada ha sido : cat')
    print('\nLa clase  identificada es: {0}'.format(class_names[posicion_clase]))

    # Prueba 3: Gato 3
    mi_image_file = '../data/Tensorflow/cat3.jpg' #buscad un fichero de imagen de alguna de las clases que existen
    model = tf.keras.models.load_model('mi_modelo.h5')
    #Lo cargamos
    image_rgb = skimage.io.imread(mi_image_file).astype(float)/255.0
    #Lo recortamos a 32x32
    image_rgb_32x32 = skimage.transform.resize(image_rgb,(32,32),preserve_range=True)
    imagen_extendida = numpy.expand_dims(image_rgb_32x32,axis=0)

    print(imagen_extendida.shape)
    prediction = model.predict(imagen_extendida)
    print('\n::...RESULTADOS PRUEBA 3..::')
    print('\nPrediccion: {0}'.format(prediction))

    # Identificacion de la clase
    posicion_clase = prediction.argmax()
    print('\nLa clase seleccionada ha sido : cat')
    print('\nLa clase  identificada es: {0}'.format(class_names[posicion_clase]))

    # Prueba 4: Superman
    mi_image_file = '../data/Tensorflow/superman.jpg' #buscad un fichero de imagen de alguna de las clases que existen
    model = tf.keras.models.load_model('mi_modelo.h5')
    #Lo cargamos
    image_rgb = skimage.io.imread(mi_image_file).astype(float)/255.0
    #Lo recortamos a 32x32
    image_rgb_32x32 = skimage.transform.resize(image_rgb,(32,32),preserve_range=True)
    imagen_extendida = numpy.expand_dims(image_rgb_32x32,axis=0)

    print(imagen_extendida.shape)
    prediction = model.predict(imagen_extendida)
    print('\n::...RESULTADOS PRUEBA 4..::')
    print('\nPrediccion: {0}'.format(prediction))

    # Identificacion de la clase
    posicion_clase = prediction.argmax()
    print('\nLa clase seleccionada ha sido : superman')
    print('\nLa clase  identificada es: {0}'.format(class_names[posicion_clase]))