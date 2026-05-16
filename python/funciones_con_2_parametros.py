# Funciones con varios parámetros
def mostrar_informacion(nombre, edad):
    print(f"Nombre: {nombre}, Edad: {edad}")

mostrar_informacion("Paula", 38)    

# Función con parámetros, pero el valor de los parámetros se le asigna a través de variables que obtienen su valor por medio de input().
nombre = input("Por favor, escribe tu nombre: ")
edad = int(input("Por favor, escribe tu edad: "))

# Llamada a la función con las variables que contienen los valores obtenidos por medio de input().
mostrar_informacion(nombre, edad)