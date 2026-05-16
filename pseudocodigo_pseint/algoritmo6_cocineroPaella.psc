Algoritmo algoritmo6_cocineroPaella
	arroz_1persona_gramos = 100
	langostinos_1persona_gramos = 50
	pimientos_1persona_gramos = 20
	Escribir "¿Cuantos comensales habrá para preparar la paella?"
	Leer numero_de_comensales
	Escribir "¿Cuál es el coste de 100 gramos de arroz?"
	Leer coste_arroz_1persona 
	Escribir "¿Cual es el coste de los 50 gramos langostinos?"
	Leer coste_langostinos_1persona
	Escribir "¿Cual es el coste de los 20 gramos de pimientos?"
	Leer coste_pimientos_1persona
	
	coste_total_arroz = arroz_1persona_gramos * numero_de_comensales * coste_arroz_1persona
	Imprimir 'El coste total del arroz para ' , numero_de_comensales, ' es ', coste_total_arroz, ' euros.'
	coste_total_langostinos = langostinos_1persona_gramos * numero_de_comensales * coste_langostinos_1persona
	Imprimir 'El coste total de los langostinos para ', numero_de_comensales, ' es ', coste_total_langostinos, ' euros.'
	coste_total_pimientos = pimientos_1persona_gramos * numero_de_comensales * coste_pimientos_1persona
	Imprimir 'El coste total de los pimientos para ', numero_de_comensales, ' es ', coste_total_pimientos, ' euros.'
	
	total_paella = coste_total_arroz + coste_total_langostinos + coste_total_pimientos
	Imprimir 'El total de la paella costará: ', total_paella
FinAlgoritmo
