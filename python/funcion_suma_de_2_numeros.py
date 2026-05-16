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
