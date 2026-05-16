# ----- DIFERENCIA ENTRE PRINT Y RETURN ------
# Una función existe de forma independiente.
# Un método es una función que pertenece a un objeto o clase.

print(f"------ DIFERENCIA ENTRE PRINT Y RETURN ------")

def ejemplo_print_suma(numero_a, numero_b):
    print(numero_a + numero_b)

def ejemplo_con_return_suma(num_a, num_b):
    return num_a + num_b

ejemplo_print_suma(2, 3)
resultado_con_print = ejemplo_print_suma(5,5)
# El resultado con print es None
print(f"El resultado con print es {ejemplo_print_suma(5,5)}")
# El resultado con print es None
print(f"El resultado con print es {resultado_con_print}")

resultado_con_return = ejemplo_con_return_suma(2, 3)
print(f"El resultado con return es {resultado_con_return}")
resultado_con_return_2 = ejemplo_con_return_suma(5, 5)
print(f"El resultado con return es {resultado_con_return_2}")