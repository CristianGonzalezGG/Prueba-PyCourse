import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Llamando a los datos de un CSV 
df = pd.read_csv("archivos_problemas_graficos\\cofla_ingresos.csv")

#creando Grafico
sns.barplot(x="fuente",y="ingresos",data=df)

#OBTENIENDO EL TOTAL DE INGRESOS
total = df['ingresos'].sum()

#mostrando TOTAL ingresos
print(f"El todal de ingresos es de: {total}")


#creando el grafico
plt.show()