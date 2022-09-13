import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 
  
pickle_in = open('modelos/Modelo_STREAMLITE', 'rb') 
modelo_rf = pickle.load(pickle_in) 

## VARIABLES PREDICTORAS ÚTILES
                        # 'latitude',
                        # 'longitude',
                        # 'accommodates',
                        # 'bedrooms',
                        # 'room_type_code',
                        # 'eur_distrito',
                        # 'bathrooms_num',
                        # 'bathrooms_priv_or_shar',
                        # 'air_cond',
                        # 'elevator',
                        # 'total_viviendas_host',



def welcome(): 
    return 'welcome all'
  
def prediction(latitude,
                longitude,
                accommodates,
                bedrooms,
                room_type_code,
                # eur_distrito,
                bathrooms_num,
                bathrooms_priv_or_shar,
                air_cond,
                elevator,
                total_viviendas_host
                ):   
   
    prediction = modelo_rf.predict( 
                [[latitude,
                longitude,
                accommodates,
                bedrooms,
                room_type_code,
                # eur_distrito,
                bathrooms_num,
                bathrooms_priv_or_shar,
                air_cond,
                elevator,
                total_viviendas_host]]) 
    print(prediction) 
    return prediction 
      
  
def main(): 
      
    st.title("Prediction AirBnb Price") 
      
    
    
    html_temp = 'http://localhost:8501/'
    
    
    
    
      
    
    
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    
    latitude= st.text_input('Escribe aquí la latitud, tipo: 40.45724')
    longitude= st.text_input('Escribe aquí la longitud, tipo: -3.67688')
    accommodates= st.text_input('Escribe aquí el número de personas(entre el 1 y el 100) que caben en tu casa')
    bedrooms= st.text_input('Escribe aquí el número de habitaciones (entre el 1 y el 100) que hay en tu casa')
    room_type_code= st.text_input('Escribe aquí que tipo de casa alquilas: 100 para "Apartamento Entero", 50 para "Habitación privada"')
    # eur_distrito= st.text_input('Escribe aquí el nombre de tu distrito')
    bathrooms_num= st.text_input('Escribe aquí el número de baños (entre el 1 y el 100) que hay en tu casa')
    bathrooms_priv_or_shar= st.text_input('Escribe aquí un 1 si el baño es privado, 0 si es compartido')
    air_cond= st.text_input('Escribe aquí un 1 si tienes Aire Acondicionado, 0 si no')
    elevator= st.text_input('Escribe aquí un 1 si tienes Ascensor, 0 si no')
    total_viviendas_host= st.text_input('Escribe aquí el total de viviendas que alquilas')

    result ="" 
      
    
    
    
    if st.button("Predict"): 
        result = prediction(latitude,
                longitude,
                accommodates,
                bedrooms,
                room_type_code,
                # eur_distrito,
                bathrooms_num,
                bathrooms_priv_or_shar,
                air_cond,
                elevator,
                total_viviendas_host) 
    st.success('The output is {}'.format(result/12/15)) 
     
if __name__=='__main__': 
    main() 