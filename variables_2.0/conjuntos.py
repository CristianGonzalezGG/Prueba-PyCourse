#crando un conjunto

conjunto = set(["dato1", "dato2"])  

#como meter un conjunto dentro de otro conjunto se usa (fronzenset)
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1,"dato3","dato4"}        
print(conjunto2)   

#crear conjuntos y mirar si son subconjuntos o superconjuntos
conjunto1 = {1,2,3,4}
conjunto2 = {1,2,4}  

#Para saber si es subconjunto usamos issubset      
resolt = conjunto2.issubset(conjunto1)

#Para saber si es supeconjunto usamos issuperset
resolt1 = conjunto1.issuperset(conjunto2)
print(resolt)
print(resolt1)