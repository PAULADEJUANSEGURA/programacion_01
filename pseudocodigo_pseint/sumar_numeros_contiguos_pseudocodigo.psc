Algoritmo sumar_numeros_contiguos
	Escribir "Ingrese el numero desde el cual desea empezar a sumar: "
	Leer numero_inicial
	Escribir "Ingrese la cantidad de numeros contiguos que desea sumar: "
	Leer cantidad_de_sumas
	resultado = 0
	Para iterador = 0 + numero_inicial Hasta cantidad_de_sumas Con Paso 1 Hacer
		resultado = resultado + iterador
	Fin Para
	Escribir resultado
FinAlgoritmo