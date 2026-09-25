# Practica 1 de Python Avanzado Tecno3F

# Definición de listas
L1= [1,2,3,4,5,6,11,12,13,14,15]
L2= [1,2,3,4,5,6,7,8,9,10]
# Convertir a conjuntos
conj_A= set(L1)
conj_B= set(L2)
print ("Conjunto A:",type(conj_A))
print ("Conjunto B:",type(conj_B))
# Punto 1 
# Menu inicial
print ("Ingrese una opción para ver los conjuntos")
select= input("1:Conjunto A, 2:Conjunto B, 3:Todos los elementos o cualquier teclas para continuar: ")
# Tratamiento de selección
match select : 
    case "1" :
        print (conj_A)
    case "2" :
        print (conj_B)
    case "3" :
     print (conj_A|conj_B)
    case _ :
     print ("Se seleccionó continuar.....")

# Punto 2 Elementos de A y B
print ("Los elementos de A y B son : ", conj_A|conj_B)

# Punto 3 Elementos de A o B pero no comunes a ambos
# Menu inicial
print ("Ingrese una opción para ver")
select= input("1:Elementos de A no comunes a B, 2:Elementos de B no comunes a A o cualquier teclas para continuar: ")
# Tratamiento de selección
match select : 
    case "1" :
        print (conj_A - conj_B)
    case "2" :
        print (conj_B - conj_A)
    case _ :
     print ("Se seleccionó continuar.....")

# Punto 4 Subconjuntos 
# Análisis es conjunto A subconjunto de B?
check_conj= conj_A.issubset(conj_B)     
print (check_conj)
if check_conj:
   print ("El conjunto A SI es Subconjunto del conjunto B")
else:
   print ("El conjunto A NO es subconjunto de conjunto B")

# Punto 5 Cantidad de elementos del conjunto A
print (f"el conjunto A tiene {len(conj_A)} elementos.")   
print ("fin del trabajo 1")
         
            

