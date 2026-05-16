# Iniciamos el Algoritmo que calcula el área de un círculo

# Entrada
PI = 3.1416
radio = float(input("Dime el valor del radio del círculo = ")) 
				
# Procesamiento
# El algoritmo que calcula es la Fórmula: A = π * r ** 2 (es decir, r elevado al cuadrado)
area = PI * radio ** 2
# El algoritmo que calcula la longitud de la circunferencia es la Fórmula: Longitud = 2 * π * r
longitud_circunferencia = 2 * PI * radio				

# Salida
print(f"El resultado del area es = {area}")
print(f"La longitud de la circunferencia es = {longitud_circunferencia}")
