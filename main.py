import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file",type="csv" ) #En el tipo cual es el tipo de archivo que vas a subir (se puede poner muchos tipos)
#Si el usuario sube un archivo csv, el archivo de python va a volver a correrse
if uploaded_file is not None:
    #st.write("File uploaded...")
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head()) #Obtiene las primeras 5 filas del csv

    st.subheader("Data Summary")
    st.write(df.describe())

    #Filtrar los datos
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    #Tomamos todos los 'valores unicos' de la columna
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Selecciona un valor", unique_values)

    #Seleccionar los datos filtrados y colocarlos en la pantalla
    filtered_df = df[df[selected_column]== selected_value]
    st.write(filtered_df)

    st.subheader("Plot_Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    #Cuando apretas el boton genera un chart que usa los datos de la columna x e y
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
        st.write("Esperando el upload del archivo...")