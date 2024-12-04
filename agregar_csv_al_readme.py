import pandas as pd

# Cargar el dataset
df = pd.read_csv('animia.csv', encoding='latin-1', delimiter=';')

# Ver los primeros registros del dataset
print(df.head())
print(df.columns)
print(df.info())