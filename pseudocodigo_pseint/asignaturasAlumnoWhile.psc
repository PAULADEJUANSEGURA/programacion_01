Algoritmo asignaturasAlumno
	Imprimir "¿Cuántas asignaturas ha cursado el alumno: ?"
	Leer numero_asignaturas_alumno
	Imprimir numero_asignaturas_alumno
	Definir tipo_asignaturas Como Caracter
	Dimension tipo_asignaturas[numero_asignaturas_alumno]
	Definir nota_asignaturas Como Entero
	Dimension nota_asignaturas[numero_asignaturas_alumno]
	iterador = 0
	Mientras iterador < numero_asignaturas_alumno  Hacer
		Escribir "Dime el nombre de la asignatura que has cursado: "
		Leer tipo_asignaturas[iterador]
		Escribir "Dime tu nota para la asignatura: "
		Leer nota_asignaturas[iterador]
		iterador = iterador + 1
	Fin Mientras
	indice = 0
	Mientras indice < numero_asignaturas_alumno Hacer
		Imprimir 'Valor de la asignatura ', tipo_asignaturas[indice], ' tiene una nota de ',  nota_asignaturas[indice]
		Si nota_asignaturas[indice] >= 5 Entonces
			Imprimir 'Tiene una nota de ', nota_asignaturas[indice] ,' y esta APROBADA ' 
		SiNo
			Imprimir 'Tiene una nota de ', nota_asignaturas[indice] ,' y esta SUSPENSO '
		Fin Si
		indice = indice + 1
	Fin Mientras
FinAlgoritmo
