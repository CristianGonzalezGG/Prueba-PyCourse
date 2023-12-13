#cambiar tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas.py\\datos.csv")

#conviertiendo a string los datos de una columna edad
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
print(df['edad'][0])

#remplazar datos en una columna y elemento especifico

df['nombre'].replace("cristian","Cristancho",inplace=True)
print(df['nombre'])

#eliminando filas con datos faltantes 
df = df.dropna()
print(df)

#eliminandoo filas repetidas
df = df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas.py\\datos_limpios.csv")
