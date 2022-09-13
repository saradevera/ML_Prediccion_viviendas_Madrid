# ML_Prediccion_viviendas_Madrid

## TRABAJO DE MACHINE LEARNING DE PREDICCIÓN DE PRECIOS DE VIVIENDAS

##### Comenzamos cargando nuestro dataset 'houses_Madrid.csv'.

Estudiamos los datos obtenidos y empezamos a trabajar con ellos

1.- LIMPIEZA Y FEATURE ENGINEERING

En el notebook que se encuentra en el siguiente path: 'notebooks/project_limpieza_y_feat_engin.ipynb' se puede encontrar todo el código utilizado y todos los pasos que se han seguido, descritos.

    En resumen se han hecho los siguientes procesos:
        *Eliminación de duplicados
        *Estudio de missing values 
        *Eliminación de columnas innecesarias
        *Sustitución de los missing values según criterios acordes a cada caso
        *Tratamiento de las variables categóricas según cada caso
        *Sustitución de las variables booleanas por valores 0 y 1
        *Obtención de variables nuevas con el objetivo de tener más correlación con el target
        *Exportado del dataframe ya limpio y preparado para el estudio estadístico
        
        
##### Una vez los datos están limpios y convertidos al 100% en variables numéricas, procedemos al análisis estadístico
2.- EDA

En el notebook que se encuentra en el siguiente path: 'notebooks/project_eda.ipynb' se puede encontrar todo el código utilizado y todos los pasos que se han seguido, descritos.

    En resumen se han hecho los siguientes procesos:
        *Estudio completo estadístico de las variables
        *Histogramas de variables más importantes
        *Gráfico scatter bivariable para el estudio de la relación entre ellas y los outliers
        *Eliminación de outliers que afectarían al rendimiento del modelo
        *Pairplot completo de la relación entre todas las variables
        *Mapa de calor de la correlación entre las variables
        *Listado de variables ordenadas por su importancia con el target
        *Heatmap con las variables más correladas
        *Exportado del dataframe transformado en dos dataframes, uno completo y otro con las variables más importantes
        
        
##### Con los datos transformados según las decisiones tomadas en el EDA, procedemos al modelado
3.- Modelos

En el notebook que se encuentra en el siguiente path: 'notebooks/project_modelos.ipynb' se puede encontrar todo el código utilizado y todos los pasos que se han seguido, descritos.

    En este último notebook, se han probado distintos modelos con variación de parámetros, escalados, etc.
    
    De aquí ha salido el modelo definitivo que se puede entrenar a través del script 'train.py'
    
### importante!

##### PARA FACILITAR EL USO DEL MODELO DEFINITIVO, SE HAN PREPARADO DOS SCRIPTS .PY:

*El script llamado train.py, nos permite importar el modelo definitivo, entrenarlo y posteriormente exportarlo para su uso.

*El script llamado predict.py nos permite cargar el dataset de test, cargar el modelo creado anteriormente, sacar unas predicciones
y exportarlas en formato csv.
