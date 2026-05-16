Algoritmo sumarNumerosConWhile
	Escribir "Ingrese el numero desde el cual desea empezar a sumar: "
	Leer numero_inicial
	Escribir "Ingrese hasta que numero desea sumar: "
	Leer total_numeros
	resultado = 0
	iterador = numero_inicial
	Mientras iterador <= total_numeros Hacer
		Imprimir 'Iterador = ', iterador 
		resultado = resultado + iterador
		Imprimir 'Resultado = ' , resultado
		iterador = iterador + 1
	Fin Mientras
	Imprimir resultado
FinAlgoritmo
