import pandas as pd
import streamlit as st

areas =  pd.read_csv('area_protegida.csv')
st.title("Parte 1")
st.header("Datos que encontraron")
filas, columnas = areas.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = areas.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')
    
    
filtr2 = areas["jap"].value_counts()


with st.expander("1.calculo: de todas las areas de jurisdiccion jap, cual es su subtipo mas frecuente?"):
    st.write(filtr2)

filtr1 = areas["lat"].max()
filtr2 = areas["lng"].max()
with st.expander("2.calculo: ¿cual es el valor maximo total de las longitudes y latitudes?"):
    st.write(filtr1, filtr2)


a = areas["lat"].min()
print(a)
with st.expander("1.filtr¿Cuál es el Parques Nacional ubicado más hacia el sur? (tap == 1 y jap == 2)? ¿Y de las Reservas Provinciales (tap == 2 y jap == 3)?"):
   st.write(a)

filtr = areas[areas["tap"] == 2]
filtr2W = filtr["lat"].mean()

filtr1 = areas[areas["lat"] < -35]
filtr2 = filtr1[filtr1["tap"] == 2]
with st.expander("2.filtro: filtrar todas las areas nacionales (tap == 2) que sean menores a la latitud -34"):
    st.write(filtr2W)
    st.write(filtr2.value_counts())

filtr1 = areas[areas["gid"] == 262]
filtr2 = filtr1["nam"]
with st.expander("3.filtro: ¿cual es la area protegida cuyo codigo gid es 262?"):
    st.write(filtr2)

