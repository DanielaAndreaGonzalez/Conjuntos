#Declaración de conjuntos

lista1 = ["a","e","i","o","u"]
lista2 = ["a","e","i","c","u"]
lista3 = ["a","o","i","c","u"]

#Declaracion conjunto
conjuntoTotal = set()


#Función que hace la interseccion de tres conjuntos 
def interseccionConjunto():
    global conjuntoTotal  # Declarar conjuntoTotal como global
    
    # Declarar conjuntos locales para cada intersección
    interseccion_conjunto1 = set()
    interseccion_conjunto2 = set()
    interseccion_conjunto3 = set()

    #Añadir la intersección de la lista 1 y la lista 2
    for elemento in lista1:
        if elemento in lista2: 
            interseccion_conjunto1.add(elemento)
        else:
            print(f"El número {elemento} no está en el conjunto. ")

    for elemento in lista2:
        if elemento  in lista3:
            interseccion_conjunto2.add(elemento)
        else:
            print(f"El número {elemento} no está en el conjunto.")
    for elemento in lista3:
        if elemento in lista1:
            interseccion_conjunto3.add(elemento)
        else:
            print(f"El número {elemento} no está en el conjunto.")
    
    conjuntoTotal = interseccion_conjunto1 & interseccion_conjunto2 & interseccion_conjunto3
    
    print("Intersección entre conjunto 1 y 2",interseccion_conjunto1)
    print("Intersección entre conjunto 2 y 3",interseccion_conjunto2)
    print("Intersección entre conjunto 1 y 3",interseccion_conjunto3)
    print("TOTAL: Intersección entre conjunto 1,2 y 3",conjuntoTotal)


# Función para calcular la cardinalidad 
def calcularCardinalidad():
    cardinalidad = 0
    for i in conjuntoTotal:
        cardinalidad += 1
    print("Cardinalidad de la intersección:", cardinalidad)

def esSubconjunto():
    # Calcular  si lista1 es un subconjunto de la interseccion de los conjuntos
    es_subconjunto = True
    for elemento in lista1:
        if elemento not in conjuntoTotal:
            es_subconjunto = False
            break

    if es_subconjunto: 
        print("lista1 es un subconjunto de la unión de los conjuntos.")
    else:
        print("lista1 NO es un subconjunto de la unión de los conjuntos.")


# Calcular  si los conjuntos son disjuntos
def esDisjunto():
    son_disjuntos = True
    for elemento in lista1:
        if elemento in conjuntoTotal:
            son_disjuntos = False
            break

    if son_disjuntos:
        print("Los conjuntos *SON* disjuntos.")
    else:
        print("Los conjuntos *NO* son disjuntos.")


interseccionConjunto()
calcularCardinalidad()
esSubconjunto()
esDisjunto()