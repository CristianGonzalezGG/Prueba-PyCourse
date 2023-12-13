import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Llamando a los datos de un CSV 
df = pd.read_csv("archivos_problemas_graficos\\pedos.csv")

#creando Grafico
sns.lineplot(x="fecha",y="pedos",data=df)

#crando un punto en el valor mas alto de el grafico
plt.plot("01-07",13,"o")

#creando el grafico
plt.show()