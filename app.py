import streamlit as st
import pandas as pd
import plotly.express as px

car_data=pd.read_csv('vehicles_us.csv')
# print(car_data.head())
# Encabezado
st.header("Aplicación de Visualización con Streamlit y Plotly")

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
            
hist_checkbox = st.checkbox('Mostrar histograma')  # casilla de verificación

if hist_checkbox:  # Si la casilla está marcada
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)            
