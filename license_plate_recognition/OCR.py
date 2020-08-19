# -*- coding: utf-8 -*-

def loadMNISTdataset():
    import tensorflow as tf
    
    # load MNIST dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    
    # reshape data so that it works with the Keras API
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    
    # normalise
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255

def createAndTrainKerasModel():
    from keras.models import Sequential
    from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
    
    # generate model
    model = Sequential()
    model.add(Conv2D(28, kernel_size=(3,3), input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation=tf.nn.relu))
    model.add(Dropout(0.2))
    model.add(Dense(10,activation=tf.nn.softmax))
    
    # complie and train model
    model.compile(optimizer='adam', 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['accuracy'])
    model.fit(x=x_train,y=y_train, epochs=10)
    model.save('MNISTmodel.h5') 

    # print accuracy of test data
    loss, accuracy = model.evaluate(x_test, y_test)
    print('Model accuracy of test data: {:5.2f}%'.format(100*accuracy))

def loadNumberplateImage():
    import numpy as np 
    import tensorflow as tf
    import matplotlib.pyplot as plt
    import cv2
    
    # read numberplate image
    image = cv2.imread('PrintedNumberplate.png')

    # only consider pixels from second top height section
    verticalCroppedImage = image[220:430, :]
    plt.figure()
    plt.imshow(verticalCroppedImage, cmap='Greys')

    # consider each number individually
    predictedNumberplate = ""
    lastPixels = np.array([220, 400, 580, 750, 925, 1115, 1260])
    for i in range(7):
        lastPixel = lastPixels[i]
        croppedImage = verticalCroppedImage[:, lastPixel-185:lastPixel]
        
        # convert to greyscale
        greyscaleImage = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2GRAY)
        
        # rescale to MNIST dimensions
        MNISTdimensions = (28,28)
        resizedGreyscaleImage = cv2.resize(greyscaleImage, MNISTdimensions, interpolation = cv2.INTER_AREA)
        
        # convert to black and white image
        (threshold, blackWhiteImage) = cv2.threshold(resizedGreyscaleImage, 120, 255, cv2.THRESH_BINARY)
        
        # invert black and white image
        invertedBlackWhiteImage = cv2.bitwise_not(blackWhiteImage)
        plt.figure()
        plt.imshow(invertedBlackWhiteImage, cmap='Greys')
        invertedBlackWhiteImage.resize(1,28,28,1)
        
        # predict number from model
        pred = model.predict(invertedBlackWhiteImage)
        predictedNumberplate = predictedNumberplate + str(pred.argmax()) + " "
    
    print(" ******************************")    
    print(" Numberplate is: " + predictedNumberplate) 
    print(" ******************************")

loadMNISTdataset()
createAndTrainKerasModel()
loadNumberplateImage()
