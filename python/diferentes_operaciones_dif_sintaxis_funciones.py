#Ejercicio de funciones con diferentes formas de hacer lo mismo en diferentes modos de sintaxis, con diferentes tipos de datos, y con diferentes formas de imprimir el resultado.

#importamos la librería math para usar funciones matemáticas si es necesario, aunque en este caso no es estrictamente necesario para sumar dos números.
import math

# Funcion que suma dos numeros
def sumar_dos_numeros(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

# Llamada a la función con números específicos
suma1 = sumar_dos_numeros(5, 3) # Resultado: 8
suma2 = sumar_dos_numeros(10, 15) # Resultado: 25
print(f"La suma de 5 y 3 es: {suma1}")
print(f"La suma de 10 y 15 es: {suma2}")

# Llamada a la función con números ingresados por el usuario
numero_usuario1 = int(input("Ingrese el primer número: "))      
numero_usuario2 = int(input("Ingrese el segundo número: "))
suma_usuario = sumar_dos_numeros(numero_usuario1, numero_usuario2)
print(f"La suma de {numero_usuario1} y {numero_usuario2} es: {suma_usuario}")

# Función que suma dos números
def sumar_e_imprimir(numero1, numero2):
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    print(f"La suma de {numero1} y {numero2} es usando la función creada anteriormente: {sumar_dos_numeros(numero1, numero2)}")
    print(f"La suma de {numero1} y {numero2} es usando la operación directa aqui mismo: {numero1 + numero2}")
    print("La suma de los dos numeros es:", numero1 + numero2)

# Llamada a la función para sumar e imprimir el resultado
sumar_e_imprimir(0, 0) # Los valores no importan ya que se solicitan dentro de la función en los inputs para numero1 y numero2. Pero tenemos que pasarle algo para que no de error, por eso se le pasan 0 y 0.


def sumar_e_imprimir2(a, b):
   print(f"La suma de {a} y {b} es: {a + b}")
   print("La suma de los dos numeros es:", a + b)

sumar_e_imprimir2(7, 8) # Resultado: La suma de 7 y 8 es: 15
sumar_e_imprimir2(12, 5) # Resultado: La suma de 12 y 5 es: 17

# Función que intenta usar la función sum para sumar números.
# Creamos una tupla con los números que queremos sumar.
tupla_numeros = (4, 6, 8, 10, 12, 14, 16, 18, 20)
# Resultado: La suma de los números en la tupla es: 108   

def sumar_con_funcion_sumar(tupla_numeros):
    return print(f"La suma de los números en la tupla es: {sum(tupla_numeros)}")

sumar_con_funcion_sumar(tupla_numeros) 

# La forma mas sencilla de sumar dos números es usando el operador + directamente, sin necesidad de crear una función adicional. Por ejemplo:
print("-" * 30 + "SUMA DE DOS NÚMEROS USANDO EL OPERADOR + DIRECTAMENTE" + "-" * 10)
numero_a = int(input("Ingrese el primer número: "))
numero_b = int(input("Ingrese el segundo número: "))

def sumar(numero_a, numero_b):
    return numero_a + numero_b

resultado_suma = sumar(numero_a, numero_b)
print(f"La suma de {numero_a} y {numero_b} es: {resultado_suma}")
print("La suma de los dos numeros es:", numero_a + numero_b)
print("La suma de los dos numeros es:", resultado_suma)


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