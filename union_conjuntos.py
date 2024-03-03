#Ingreso de elementos 
#Conjunto número 1
lista1 = [1,2,3,4,5,5]
#Conjunto número 2
lista2 = [4,5,6,7,8,8]
#Conjunto número 3
lista3 = [8,9,10,10,11,12]

#Declaracion conjunto
union_conjunto = set()


#Función que hace la unión de tres conjuntos sin repetir elementos
def unionConjunto():
    for elemento in lista1:
        if elemento not in union_conjunto: 
            union_conjunto.add(elemento)
        else:
            print(f"El número {elemento} ya está en el conjunto. ")

    for elemento in lista2:
        if elemento not in union_conjunto:
            union_conjunto.add(elemento)
        else:
            print(f"El número {elemento} ya está en el conjunto.")
    for elemento in lista3:
        if elemento not in union_conjunto:
            union_conjunto.add(elemento)
        else:
            print(f"El número {elemento} ya está en el conjunto.")

    print("Unión entre conjuntos: ", union_conjunto)


def calcularCardinalidad(unionConjunto):
     # Calcula manualmente la cardinalidad
    cardinalidad = 0
    for _ in union_conjunto:
        cardinalidad += 1
    print("Cardinalidad de la unión:", cardinalidad)


def esSubconjunto():
    # Calcular manualmente si lista1 es un subconjunto de la unión de los conjuntos
    es_subconjunto = True
    for elemento in lista1:
        if elemento not in union_conjunto:
            es_subconjunto = False
            break

    if es_subconjunto: 
        print("lista1 es un subconjunto de la unión de los conjuntos.")
    else:
        print("lista1 NO es un subconjunto de la unión de los conjuntos.")


# Calcular manualmente si los conjuntos son disjuntos
def esDisjunto():
    son_disjuntos = True
    for elemento in lista1:
        if elemento in union_conjunto:
            son_disjuntos = False
            break

    if son_disjuntos:
        print("Los conjuntos *SON* disjuntos.")
    else:
        print("Los conjuntos *NO* son disjuntos.")

unionConjunto()
calcularCardinalidad(unionConjunto)
esSubconjunto()
esDisjunto()
