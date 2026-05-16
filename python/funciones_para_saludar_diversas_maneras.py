# Función con parámetros
def saludar(nombre):
    print(f"¡Hola, {nombre}! Bienvenido al curso de Python.")

saludar("Paula")
saludar("Adrián")

# Aqui se muestra la función con parámetros, pero el valor del parámetro se le asigna a través de una variable que obtiene su valor por medio de input().
nombre_usuario = input("Por favor, escribe tu nombre: ")
nombre_usuario_2 = input("Por favor, escribe tu nombre: ")
saludar(nombre_usuario)
saludar(nombre_usuario_2)

# Función que pida el nombre al usuario: Aqui el input se encuentra dentro de la función, por lo que cada vez que se llame a la función, se le pedirá al usuario que introduzca su nombre.
def pedir_nombre(nombre_usuario):
    nombre_usuario = input("Por favor, escribe tu nombre: ")
    print(f"¡Hola, {nombre_usuario}! Bienvenido al curso de Python.")
# Llamada a la función con un String vacío, ya que el valor del parámetro se asignará dentro de la función a través del input().
pedir_nombre("")





