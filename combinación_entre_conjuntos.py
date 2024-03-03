lista1 = [1,3,5,7,9]
lista2 = [2,3,5,7,10]
lista3 = [8,9,10]
universal = [20,40,60,80]


interseccion = set()
union = set()
diferencia = set()
complemento = []

#Función que realiza la interseccion (lista1 interseccion lista2)
def interseccionConjunto():
    #Añadir la intersección de la lista 1 y la lista 2
    for elemento in lista1:
        if elemento in lista2: 
            interseccion.add(elemento)
    print(interseccion)

#Función que realiza la unión entre lista 1 y lista 3
def unionConjunto():
    for elemento in lista1:
        union.add(elemento)
    for elemento in lista3:
        union.add(elemento)
    print(union)
    

#Función que realiza la diferencia entre la lista 3 y la lista 2 (lista3 - lista2)
def diferencia_conjuntos():
    for elemento in lista3:
        if elemento not in lista2:
            diferencia.add(elemento)
    print(diferencia)


# Función para realizar (A U B) - (A)
def union_diferencia_A():
    union = set(lista1) | set(lista2)  # Unión de lista1 y lista2
    diferencia = union - set(lista1)   # Diferencia de la unión con lista1
    return diferencia

def complemento():
    for elemento in universal:
        if elemento not in lista1:
            complemento.append(elemento)

def menu():
    opcion = 0
    while opcion != 4:
        print("----- Menú de Operaciones entre Conjuntos -----")
        print("Presione 1 para realizar (A U B) - (A)")
        print("Presione 2 para realizar (A) complemento")
        print("Presione 3 para ver: interseccion entre 2 conjuntos, union entre 2 conjuntos y diferencia entre 2 conjuntos")
        print("Presione 4 para salir del programa")

        opcion = int(input("Ingrese el número de la opción que desea realizar: "))

        if opcion == 1:
            # Lógica para realizar (A U B) - (A)
           print(" (Lista1 U lista2) - lista1 ",union_diferencia_A())

        elif opcion == 2:
            # Lógica para realizar (A) complemento
            print("Complemento de A", complemento)

        elif opcion == 3:
            # Lógica para ver intersección, unión y diferencia entre 2 conjuntos
            print("Lista 1: ", lista1)
            print("Lista 2: ", lista2)
            print("Lista 3: ", lista3)
            print("Intersección entre 2 conjuntos: lista 1 y lista 2")
            interseccionConjunto()
            print("Unión entre 2 conjuntos lista 1 y lista 3")
            unionConjunto()
            print("Diferencia entre 2 conjuntos: lista 3 y lista 2")
            diferencia_conjuntos()

        elif opcion == 4:
            print("Saliendo del programa...")
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida del menú.")


menu()


