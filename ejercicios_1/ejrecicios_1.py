#EJERCICIOS PRACTICOS NUMERO 1

#ejercicio: Se recopilaron los datos de cuanto tarda un curso de Py
#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7 
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion de crudos 
crudo_pronmedio = 5 
crudo_dalto = 3.5

#Diferencias de duracion 
diferencias_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencias_con_max =  100 - dalto_curso*1000 // otros_cursos_max /10
diferencias_con_promedio =  100 - dalto_curso / otros_cursos_promedio * 100

#calculando % tiempo vacio
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_pronmedio /10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10


#Imprimir diferencias
print("------------------------------")
print(f"El Curso de Dalto dura {diferencias_con_min}% menos que el mas rapido")
print(f"El Curso de Dalto dura {diferencias_con_max}% menos que el mas lento")
print(f"El Curso de Dalto dura {diferencias_con_promedio}% menos que el promedio")

#imprimir crudos calculo de espacios vacios
print("------------------------------")
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'El curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')

#mostrando diferencias si duraran 10hrs
print("------------------------------")
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso')