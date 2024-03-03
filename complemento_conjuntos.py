#Declaración de conjuntos
lista1 = [4,5,8,6,3]
lista2 = [1,3,8,9,11]

#Conjunto universal
universal = [1,2,3,4,5,6,7,8,9,10,11]

#Declaracion conjunto complemento
complemento=set()

#Función que realiza el complemento de los conjuntos
def complemento_conjuntos():
    for elemento in lista1:
        if elemento not in universal:
            complemento.add(elemento)
    for elemento in lista2:
        if elemento not in universal:
            complemento.add(elemento)   
    for elemento in universal:
        if elemento not in complemento:
            complemento.add(elemento) 

    print(complemento)

def calcularCardinalidad():
     # Calcula  la cardinalidad
    cardinalidad = 0
    for _ in complemento:
        cardinalidad += 1
    print("Cardinalidad de la unión:", cardinalidad)


def esSubconjunto():
    # Calcular  si lista1 es un subconjunto de la unión de los conjuntos
    es_subconjunto = True
    for elemento in lista1:
        if elemento not in complemento:
            es_subconjunto = False
            break

    if es_subconjunto: 
        print("lista1 es un subconjunto de la unión de los conjuntos.")
    else:
        print("lista1 NO es un subconjunto de la unión de los conjuntos.")

# Calcular si los conjuntos son disjuntos
def esDisjunto():
    son_disjuntos = True
    for elemento in lista1:
        if elemento in complemento:
            son_disjuntos = False
            break

    if son_disjuntos:
        print("Los conjuntos *SON* disjuntos.")
    else:
        print("Los conjuntos *NO* son disjuntos.")


#Llamado de función complemento
complemento_conjuntos()
calcularCardinalidad()
esSubconjunto()
esDisjunto()