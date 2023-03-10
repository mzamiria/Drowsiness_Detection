# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:27:47 2023

@author: Mehrdad.Z
"""
import numpy as np
import os
import keras
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Input, Dropout,Flatten, Conv2D
from tensorflow.keras.layers import BatchNormalization, Activation, MaxPooling2D
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.utils import plot_model




    
#Generate Train and validation batches

img_size=86
batch_size=128

datagen_train=ImageDataGenerator(validation_split=0.2,
                                   preprocessing_function=preprocess_input)

datagen_validation=ImageDataGenerator(validation_split=0.2,
                                        preprocessing_function=preprocess_input)

train_generator=datagen_train.flow_from_directory('Images/',
                                                  target_size=(img_size,img_size),
                                                  batch_size=batch_size,
                                                  class_mode='categorical',
												  subset='training',
                                                  shuffle=True)

validation_generator=datagen_validation.flow_from_directory('Images/',
                                                  target_size=(img_size,img_size),
                                                  batch_size=batch_size,
                                                  class_mode='categorical',
												  subset='validation')
                                                  

#Create CNN
model=Sequential()
model.add(Conv2D(32,(3,3),padding='same',input_shape=(img_size,img_size,1)))
model.add(Activation('relu'))
model.add(MaxPooling2D(3,3))

model.add(Conv2D(64,(3,3),padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(3,3))

model.add(Conv2D(128,(3,3),padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(3,3))

model.add(Conv2D(128,(3,3),padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))

model.add(Dense(2, activation='softmax'))
opt=Adam(learning_rate=0.00001)
model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

epochs=100
steps_per_epoch=train_generator.n//train_generator.batch_size
validation_steps=validation_generator.n//validation_generator.batch_size

# saving the weights
checkpoint=ModelCheckpoint('model_weights.h5', monitor='val_accuracy',
                           save_weights_only=True, mode='max',verbose=1)


history=model.fit(train_generator, steps_per_epoch=steps_per_epoch, epochs=epochs,
                  validation_data=validation_generator,validation_steps=validation_steps)

# saving the model
model_json=model.to_json()
with open('model.json', 'w') as json_file:
    json_file.write(model_json)
