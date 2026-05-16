Algoritmo asignaturasAlumno
	Imprimir "¿Cuántas asignaturas ha cursado el alumno: ?"
	Leer numero_asignaturas_alumno
	Imprimir numero_asignaturas_alumno
	Definir tipo_asignaturas Como Caracter
	Dimension tipo_asignaturas[numero_asignaturas_alumno]
	Definir nota_asignaturas Como Entero
	Dimension nota_asignaturas[numero_asignaturas_alumno]
	Para iterador = 0 Hasta numero_asignaturas_alumno - 1 Con Paso 1 Hacer
			Escribir "Dime el nombre de la asignatura que has cursado: "
			Leer tipo_asignaturas[iterador]
			Escribir "Dime tu nota para la asignatura: "
			Leer nota_asignaturas[iterador]
	Fin Para
	Para indice = 0 Hasta numero_asignaturas_alumno - 1 Con Paso 1 Hacer
		Imprimir 'Valor [', indice, ']  TIPO ASIGNATURA = ', tipo_asignaturas[indice]
		Imprimir 'Valor [', indice, '] NOTAS ASIGNATURAS = ', nota_asignaturas[indice]
	Fin Para
	Para indice = 0 Hasta numero_asignaturas_alumno -1 Con Paso 1 Hacer
		Si nota_asignaturas[indice] >= 5 Entonces
			Imprimir 'Valor [', indice, '] NOTA ASIGNATURA Está aprobada = ', nota_asignaturas[indice]
		SiNo
			Imprimir 'Valor [', indice, '] NOTA ASIGNATURA Está suspendida = ', nota_asignaturas[indice]
		Fin Si
	Fin Para	
FinAlgoritmo
