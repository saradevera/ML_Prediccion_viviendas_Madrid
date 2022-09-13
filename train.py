# MODELO DE REGRESION PARA PREDICCION DE PRECIOS DE VIVIENDAS EN MADRID

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

import pickle
import os
from datetime import datetime

# DATOS
current_dir = os.path.dirname(os.path.realpath(__file__)) 

# CARGAMOS LOS DATASETS DE TRAIN Y TEST YA PREPARADOS

path_train = os.path.join(current_dir, 'data//train.csv')
path_test = os.path.join(current_dir, 'data//test.csv') 
path_model_entrenado = os.path.join(current_dir, 'model//modelo_'+ datetime.now().strftime("%Y%m%d-%H%M%S"))

train = pd.read_csv(path_train)
test = pd.read_csv(path_test)


# ENTRENAMOS EL MODELO CON RANDOM FOREST REGRESSOR

X= train.drop(columns=(['buy_price']))
y= train['buy_price']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.10,random_state=42)

my_model = RandomForestRegressor(n_estimators = 1000)
my_model.fit(X_train, y_train)

## tarda unos 2 minutos en entrenarse, paciencia!


# EXPORTAMOS my_model A LA CARPETA model

with open(path_model_entrenado, 'wb') as archivo_salida:
    pickle.dump(my_model, archivo_salida)





