#importando la libreria panda para trabajaar con archivos CSV
import pandas as pd

#definiendo la variable que va a acceder a el archivo por medio de la ruta leyendolo por read_csv
pf = pd.read_csv("archivos\\datos.csv")
pf2 = pd.read_csv("archivos\\datos.csv")
#obteniendo los datos de la colmna nombre 
print(pf["nombre"]) 

#SLICING para tomar un rango de valore en una cadena
#cadena = "0123456"
#print(cadena[0:4])

#ordenando el DF por edad de forma desendente, si es asendente quitamos ascending
df_ordenao = pf.sort_values("edad",ascending=False)  
#print(df_ordenao)

#concatenando 2 dataframes
df_concat = pd.concat([pf,pf2])
#print(df_concat)

#mostrar las 3 primeras filas con head()
primeras = pf.head(3)

#mostrar las 3 ultimas filas con tail()
ultimas = pf.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = pf.shape

#obteniendo data estadística del dataframe:
df_info = pf.describe()

#accediendo a la edad de la fila 2
elemento_especifico_loc = pf.loc[2,"edad"]

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = pf.iloc[2,2]      

#accediendo a todos los apellidos con loc
apellidos_loc = pf.loc[:,"apellido"]

#accediendo a todos los apellidos con iloc
apellidos = pf.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = pf.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = pf.iloc[2,:]

#accediendo a filas con edad mayor que 30 con loc
mayor_que_30 = pf.loc[pf["edad"]>30,:]
