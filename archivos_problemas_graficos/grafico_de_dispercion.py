import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Llamando a los datos de un CSV 
df = pd.read_csv("archivos_problemas_graficos\\dispersion.csv")

#creando Grafico
sns.scatterplot(x="tiempo",y="dinero",data=df)


#creando el grafico
plt.show()