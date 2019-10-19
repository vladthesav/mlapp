import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import cv2
import h5py
from keras.models import Sequential
from keras.layers import Flatten, Dense, Dropout, BatchNormalization, AveragePooling2D
from keras.applications.mobilenet import MobileNet

labels = ['Atelectasis','Cardiomegaly','Consolidation','Edema','Effusion','Emphysema','Fibrosis',
 'Hernia','Infiltration','Mass','Nodule','Pleural_Thickening','Pneumonia','Pneumothorax']


def get_model(path = "best_model.hdf5"):
	raw_model = MobileNet(input_shape=(None, None, 1), include_top = False, weights = None)
	full_model = Sequential()
	full_model.add(AveragePooling2D((2,2), input_shape = (128,128,1)))
	full_model.add(BatchNormalization())
	full_model.add(raw_model)
	full_model.add(Flatten())
	full_model.add(Dropout(0.5))
	full_model.add(Dense(64))
	full_model.add(Dense(len(labels), activation = 'sigmoid'))
	full_model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['acc'])
	full_model.load_weights(path)
	return model

