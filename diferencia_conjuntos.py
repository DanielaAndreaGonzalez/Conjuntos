
#Llenado de conjuntos
lista1 = [2,4,6,8,10]
lista2 = [1,3,6,8,10]

#Declaracion conjunto
resultado_diferencia_conjuntos= set()

#Función que calcula la diferencia entre lista1 y lista 2 -  lista1-lista2
def diferencia_conjuntos():

    for elemento in lista1:
        if elemento not in lista2:
            resultado_diferencia_conjuntos.add(elemento)
        else:
            print(f"El elemento  {elemento} está en los dos conjuntos")

    print(resultado_diferencia_conjuntos)


def calcularCardinalidad():
     # Calcula  la cardinalidad
    cardinalidad = 0
    for _ in resultado_diferencia_conjuntos:
        cardinalidad += 1
    print("Cardinalidad de la unión:", cardinalidad)

def esSubconjunto():
    # Calcular  si lista1 es un subconjunto de la diferencia de los conjuntos
    es_subconjunto = True
    for elemento in lista1:
        if elemento not in resultado_diferencia_conjuntos:
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
        if elemento in resultado_diferencia_conjuntos:
            son_disjuntos = False
            break

    if son_disjuntos:
        print("Los conjuntos *SON* disjuntos.")
    else:
        print("Los conjuntos *NO* son disjuntos.")

diferencia_conjuntos()
calcularCardinalidad()
esSubconjunto()
esDisjunto()
