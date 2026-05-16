# Desarollo de un algoritmo que permita calcular un cambio de moneda.
# INICIO del Algoritmo 
# Datos que vamos a utilizar
CONSTANTE_EURO = 1
CONSTANTE_RUPIA = 87.34
 
def convertir_euros_a_rupias():
    try:
        # Fase de ENTRADA
        cantidad_de_dinero_convertir = float(input("Escriba la cantidad de dinero en euros que necesita convertir en rupias: "))
        # Fase de PROCESAMIENTO y SALIDA   
        if cantidad_de_dinero_convertir > 0:
            resultado_rupias = cantidad_de_dinero_convertir * CONSTANTE_RUPIA
            print(f"El resultado de la conversión de {cantidad_de_dinero_convertir} euros a rupias es: {resultado_rupias} rupias.")
        elif cantidad_de_dinero_convertir == 0:
            print("Cantidad mal introducida. La cantidad debe ser mayor que cero.")
            convertir_euros_a_rupias()  # Llamada recursiva para solicitar una nueva entrada
        else:
            print("Cantidad mal introducida. La cantidad no puede ser negativa.")
            convertir_euros_a_rupias()  # Llamada recursiva para solicitar una nueva entrada
    except ValueError:
        print("Error: Por favor, introduzca un número válido.")

# Llamada a la función para realizar la conversión
# Se llama a la función sin argumentos, ya que se solicitará la entrada dentro de la función.
convertir_euros_a_rupias()

# FIN del Algoritmo