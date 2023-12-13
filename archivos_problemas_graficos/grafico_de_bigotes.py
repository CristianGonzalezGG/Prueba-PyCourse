import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Llamando a los datos de un CSV 
df = pd.read_csv("archivos_problemas_graficos\\bigotes.csv")

#creando Grafico
sns.boxplot(x="categoria",y="valor",data=df)



#creando el grafico
plt.show()