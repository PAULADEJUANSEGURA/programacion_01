# VARIABLES LOCALES Y GLOBALES
# Las variables locales son aquellas que se definen dentro de una función y solo pueden ser utilizadas dentro de esa función.
def funcion_con_variable_local():
    variable_local = "Soy una variable local"
    print(variable_local)
    numero_local = 10
    print(f"El número local es: {numero_local}")

funcion_con_variable_local()
# print(variable_local) # Error: variable_local no está definida fuera de la función
# print(numero_local) # Error: numero_local no está definida fuera de la función
# Las líneas de código generarán un error porque variable_local y numero_local no están definidas fuera de la función.

# Las variables globales son aquellas que se definen fuera de cualquier función y pueden ser utilizadas en cualquier parte del programa.

variable_global = "Soy una variable global" 
numero_global = 20

def funcion_con_variable_global():
    print(variable_global)
    print(f"El número global es: {numero_global}")

funcion_con_variable_global()