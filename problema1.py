def sumar_elementos_lista(lista_numeros):
    """
    Suma todos los elementos de una lista de números.

    Args:
        lista_numeros: Una lista de números (enteros o flotantes).

    Returns:
        La suma total de los elementos de la lista.
    """
    # 1. Inicialización: Crea una "caja" para la suma (una variable) y ponle el valor 0.
    #    Llamémosla acumulador_suma.
    acumulador_suma = 0

    # 2. Iteración y Repetición: Recorre cada número en la lista.
    #    Por cada número, súmalo a tu acumulador_suma.
    for numero in lista_numeros:
        acumulador_suma += numero  # Esto es equivalente a acumulador_suma = acumulador_suma + numero

    # 5. Resultado: El valor final en acumulador_suma es tu respuesta.
    return acumulador_suma

# --- Ejemplos de uso ---

# Ejemplo 1: Lista simple
numeros_ejemplo_1 = [5, 2, 8]
resultado_1 = sumar_elementos_lista(numeros_ejemplo_1)
print(f"La suma de los elementos en {numeros_ejemplo_1} es: {resultado_1}") # Salida: La suma de los elementos en [5, 2, 8] es: 15

# Ejemplo 2: Lista con más números
numeros_ejemplo_2 = [10, 4, 7, 1]
resultado_2 = sumar_elementos_lista(numeros_ejemplo_2)
print(f"La suma de los elementos en {numeros_ejemplo_2} es: {resultado_2}") # Salida: La suma de los elementos en [10, 4, 7, 1] es: 22

# Ejemplo 3: Lista vacía
numeros_ejemplo_3 = []
resultado_3 = sumar_elementos_lista(numeros_ejemplo_3)
print(f"La suma de los elementos en {numeros_ejemplo_3} es: {resultado_3}") # Salida: La suma de los elementos en [] es: 0

# Ejemplo 4: Lista con números negativos
numeros_ejemplo_4 = [1, -5, 3, -2]
resultado_4 = sumar_elementos_lista(numeros_ejemplo_4)
print(f"La suma de los elementos en {numeros_ejemplo_4} es: {resultado_4}") # Salida: La suma de los elementos en [1, -5, 3, -2] es: -3