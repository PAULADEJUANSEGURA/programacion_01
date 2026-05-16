# ENUNCIADO: Diseña un algoritmo que calcule la suma de una cantidad de números contiguos determinada, consultando con el usuario desde qué número se debe empezar a realizar la suma y cuántos números se deben sumar.
numero_inicial = int(input("Ingrese el numero desde el cual desea empezar a sumar: "))
total_numeros = int(input("Ingrese hasta que numero desea sumar: ")) 
resultado = 0
i = numero_inicial
while i <= total_numeros:
        print(f"i = {i}")
        print(f"Resultado antes de sumar: {resultado}")
        resultado = resultado + i 
        print(f"Resultado después de sumar: {resultado}")
        i = i + 1
print("La suma total es:", resultado)
