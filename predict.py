# PREDICCIONES DEL MODELO DE REGRESION PARA PREDICCION DE PRECIOS DE VIVIENDAS EN MADRID

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn import metrics
import pickle
import os
from datetime import datetime

# DATOS
current_dir = os.path.dirname(os.path.realpath(__file__)) 


# CARGAMOS EL DATASET DE TEST

path_test = os.path.join(current_dir, 'data//test.csv') 
path_my_model = os.path.join(current_dir, 'model//my_model')
path_predicciones = os.path.join(current_dir, 'data//predicciones' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.csv')

test = pd.read_csv(path_test, index_col=[0])


# IMPORTAMOS my_model PARA PODER SACAR PREDICCIONES DEL ARCHIVO TEST.CSV

with open(path_my_model, 'rb') as archivo_entrada:
    my_model = pickle.load(archivo_entrada)


# PREDECIMOS CON LOS DATOS DE TEST

predicciones = my_model.predict(test)

predicciones_test = pd.DataFrame(test.index)
predicciones_test['preds'] = predicciones


predicciones_test.to_csv(path_predicciones, index = False)

# EXPORTAMOS LOS DATOS DE LAS PREDICCIONES
