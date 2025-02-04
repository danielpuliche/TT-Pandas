import pandas as pd

# Ruta del archivo Excel
# file_path = './animeflv.xlsx'
file_path = './Analisis de datos integrador.xlsx'

# Cargar el archivo Excel en un DataFrame de pandas
df = pd.read_excel(file_path)

# Mostrar las primeras filas del DataFrame
print(df.head())