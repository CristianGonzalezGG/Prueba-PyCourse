ingreso_mensual = 10010
gastos_mensuales = 8000

if ingreso_mensual > 10000:
    if gastos_mensuales < 7000:
        print("Salario Melo ")
    elif gastos_mensuales > 7000:
        print("Muy apretado Bajale a los costos")
    else: 
        print("Estas gastando demasiado")
        
elif ingreso_mensual > 1000:
    print("Pasable pero apretado")
    
else: 
    print("Matese")