# Parametros opcionales
hora = 0
def saludar(nombre, hora=9, mensaje="Hola!"):
    if hora >= 6 and hora < 13:
        mensaje = mensaje + " Buenos días"
    elif hora < 20: 
        mensaje = mensaje + " Buenas tardes"
    else:
        mensaje = mensaje + " Buenas noches" + " Que descanses y a dormir!"   

    print(f"{mensaje}, {nombre}, son las {hora}!")

saludar("Paula", 23, "Hola mundo!")     
saludar("Pedro", 19, "Bienvenido!") 
saludar("María", hora=10)  # Usa el mensaje predeterminado "Hola!" 
saludar("Jose", 7, "Que aproveche el desayuno!")  