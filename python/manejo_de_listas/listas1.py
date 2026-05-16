# Manejo de listas

# Las listas son estructuras de datos que permiten almacenar múltiples valores en una sola variable. Son mutables, lo que significa que puedes modificar su contenido después de haberlas creado.

frutas = ["manzana", "banana", "naranja"]
print(frutas)  # Imprime la lista completa

# print(frutas[0])  # Imprime el primer elemento de la lista
# print(frutas[1])  # Imprime el segundo elemento de la lista
# print(frutas[2])  # Imprime el tercer elemento de la lista

"""for fruta in frutas:
    print(fruta)  # Imprime cada fruta en la lista """

# Puedes modificar los elementos de la lista
frutas[1] = "pera"
print(frutas)  # Imprime la lista modificada

# Puedes agregar elementos a la lista
frutas.append("uva")
print(frutas)  # Imprime la lista con el nuevo elemento

# Puedes eliminar elementos de la lista
frutas.remove("naranja")
print(frutas)  # Imprime la lista sin el elemento eliminado

# Puedes obtener la longitud de la lista
print(len(frutas))  # Imprime el número de elementos en la lista

numeros = [2, 5, 8, 1, 4]
print(numeros)  # Imprime la lista de números

numeros.sort()  # Ordena la lista de números
print(numeros)  # Imprime la lista de números ordenada

numeros.reverse()  # Invierte el orden de la lista de números
print(numeros)  # Imprime la lista de números invertida

suma_de_los_numeros = sum(numeros)  # Suma todos los elementos de la lista de números
print(suma_de_los_numeros)  # Imprime la suma de los números

numeros_2 = [10, 20]
numeros_2.append(30)  # Agrega un nuevo número a la lista numeros_2)
print(numeros_2)  # Imprime la lista numeros_2 con el nuevo número agregado
numeros_2.extend([40, 50, 60, 70, 80, 90, 100])  # Agrega otros números a la lista 
print(numeros_2)  # Imprime la lista numeros_2 con los nuevos números agregados

numeros_2.insert(0, 5)  # Inserta el número 5 en la posición 0 de la lista numeros_2
print(numeros_2)  # Imprime la lista numeros_2 con el número 5 insertado

for i in range(0, 101, 5):  # Itera desde 0 hasta 100 con un paso de 5
    if i not in numeros_2:
        numeros_2.append(i)

# Imprime la lista numeros_2 con los múltiplos de 5 insertados y ordenados
numeros_2.sort()
print(numeros_2)

lista_pares = []  # Crea una lista vacía
for i in range(0, 81, 2):
    lista_pares.append(i)  # Agrega los números pares del 0 al 80 a la lista vacía
print(lista_pares)  # Imprime la lista vacía con los números pares

lista_impares = []  # Crea otra lista vacía
for i in range(1, 81,2):
    lista_impares.append(i)  # Agrega los números impares del 1 al 80 a la lista vacía
print(lista_impares)  # Imprime la lista vacía con los números impares

lista_multiplos_de_3 = []  # Crea otra lista vacía
for i in range(0, 81, 3):
    lista_multiplos_de_3.append(i)  # Agrega los números múltiplos de 3 del 0 al 80 a la lista vacía
print(lista_multiplos_de_3)  # Imprime la lista vacía con los números múltiplos de 3

lista__multiplos_de_9 = []  # Crea otra lista vacía
for i in range(0, 181, 9):   
    lista__multiplos_de_9.append(i)  # Agrega los números múltiplos de 9 del 0 al 81 
print(lista__multiplos_de_9)  # Imprime la lista vacía con los números múltiplos de 9