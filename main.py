import pandas as pd

print("Versión de pandas:", pd.__version__)

datos = pd.read_csv("datos/calidad_aire.csv")
print("Filas y columnas:", datos.shape)
print(datos["Name"].value_counts().head())
