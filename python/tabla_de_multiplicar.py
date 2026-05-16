print("Programa que muestra la tabla de multiplicar de un numero dado:")

print("Usando el ciclo while:")
#Programa que muestra la tabla de multiplicar de un numero dado:
tabla_del_numero = int(input("Ingrese el numero del cual desea conocer su tabla de multiplicar: "))
operador = 0

while(operador <= 10):
    print(tabla_del_numero, "x", operador,"=", tabla_del_numero * operador)
    operador = operador + 1

print("Usando el ciclo for:")
#Programa que muestra la tabla de multiplicar de un numero dado:
tabla_del_numero = int(input("Introduzca el numero del cual desea conocer su tabla de multiplicar: "))
i = 0
for i in range (i, 11):
	print(tabla_del_numero, " x ", i , " = ", tabla_del_numero * i)
	i += 1
