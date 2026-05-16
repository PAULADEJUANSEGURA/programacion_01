# Importamos la biblioteca math para poder usar funciones matemáticas como sqrt y cbrt.
import math

# Función que hace la potencia y eleva al cuadrado un número dado por el usuario.
print("-" * 30 + "POTENCIA DE UN NÚMERO USANDO EL OPERADOR **" + "-" * 10)
def elevar_al_cuadrado(numero):
    return numero ** 2

numero_usuario = int(input("Ingrese un número para elevarlo al cuadrado: "))
resultado_cuadrado = elevar_al_cuadrado(numero_usuario)
print(f"El cuadrado de {numero_usuario} es: {resultado_cuadrado}")
print("El cuadrado de", numero_usuario, "es:", elevar_al_cuadrado(numero_usuario))

# Funcion que hace la raiz cuadrada de un número dado por el usuario.
print("-" * 30 + "RAÍZ CUADRADA DE UN NÚMERO" + "-" * 10)
def raiz_cuadrada(numero):
    return math.sqrt(numero)    

numero_usuario = float(input("Ingrese un número para calcular su raíz cuadrada: "))
resultado_raiz = raiz_cuadrada(numero_usuario)
print(f"La raíz cuadrada de {numero_usuario} es: {resultado_raiz}") 

# Función para elevar un numero al cubo usando el operador ** directamente.
print("-" * 30 + "ELEVAR UN NÚMERO AL CUBO USANDO EL OPERADOR **" + "-" * 10)
def elevar_al_cubo(numero):
    return numero ** 3          

numero_usuario = int(input("Ingrese un número para elevarlo al cubo: "))
resultado_cubo = elevar_al_cubo(numero_usuario) 
print(f"El cubo de {numero_usuario} es: {resultado_cubo}")
print("El cubo de", numero_usuario, "es:", elevar_al_cubo(numero_usuario))

# Funcion que hace la raiz cubica de un número dado por el usuario.
print("-" * 30 + "RAÍZ CÚBICA DE UN NÚMERO" + "-" * 10)
def raiz_cubica(numero):
    return math.cbrt(numero)

numero_usuario = float(input("Ingrese un número para calcular su raíz cubica: "))
resultado_raiz_cubica = raiz_cubica(numero_usuario)
print(f"La raíz cubica de {numero_usuario} es: {resultado_raiz_cubica}") 

# Función que hace la potencia de un número dado por el usuario elevado a otro número dado por el usuario.
print("-" * 30 + "POTENCIA DE UN NÚMERO ELEVADO A OTRO NÚMERO" + "-" * 10)
def potencia(numero, exponente):
    return numero ** exponente

numero_usuario = int(input("Ingrese un número para elevarlo a una potencia: "))
exponente_usuario = int(input("Ingrese el exponente al que desea elevar el número: "))  

resultado_potencia = potencia(numero_usuario, exponente_usuario)
print(f"{numero_usuario} elevado a la potencia de {exponente_usuario} es: {resultado_potencia}")

# Función que hace la raiz enesima de un número dado por el usuario.
print("-" * 30 + "RAÍZ ENESIMA DE UN NÚMERO" + "-" * 10)
def raiz_enesima(numero, n):
    return math.pow(numero, 1/n)

numero_usuario = float(input("Ingrese un número para calcular su raíz enesima: "))
n_usuario = int(input("Ingrese el valor de indice n para la raíz enesima: "))
resultado_raiz_enesima = raiz_enesima(numero_usuario, n_usuario)
print(f"La raíz {n_usuario} de {numero_usuario} es: {resultado_raiz_enesima}") 

# Función que hace la raiz enesima de un número dado por el usuario.
print("-" * 30 + "RAÍZ ENESIMA DE UN NÚMERO" + "-" * 10)
def raiz_enesima(numero, n):
    return math.pow(numero, 1/n)

numero_usuario = float(input("Ingrese un número para calcular su raíz enesima: "))
n_usuario = int(input("Ingrese el valor de indice n para la raíz enesima: "))
resultado_raiz_enesima = raiz_enesima(numero_usuario, n_usuario)
print(f"La raíz {n_usuario} de {numero_usuario} es: {resultado_raiz_enesima}") 
