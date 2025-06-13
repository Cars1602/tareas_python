def encontrar_numero_mas_grande(lista_numeros):
    """
    Encuentra el número más grande en una lista de números.

    Args:
        lista_numeros: Una lista de números (enteros o flotantes).

    Returns:
        El número más grande de la lista.
        Retorna None si la lista está vacía.
    """
    # 1. Suposición Inicial: Asume que el primer elemento de la lista es el más grande.
    #    ¡Cuidado! ¿Qué pasa si la lista está vacía?
    if not lista_numeros:  # Verifica si la lista está vacía
        print("La lista está vacía, no se puede encontrar el número más grande.")
        return None  # Retorna None para indicar que no hay un número más grande

    mayor_temporal = lista_numeros[0]  # Asigna el primer elemento como el mayor temporal

    # 2. Iteración: Recorre los elementos restantes de la lista.
    #    Comenzamos desde el segundo elemento (índice 1) porque el primero ya lo usamos.
    for i in range(1, len(lista_numeros)):
        elemento_actual = lista_numeros[i]

        # 3. Comparación: Compara este elemento con tu mayor_temporal.
        #    Si el elemento actual es más grande, actualiza mayor_temporal.
        if elemento_actual > mayor_temporal:
            mayor_temporal = elemento_actual

    # 5. Resultado: El valor final en mayor_temporal es el número más grande.
    return mayor_temporal

# --- Ejemplos de uso ---

# Ejemplo 1: Lista estándar
numeros_ejemplo_1 = [12, 5, 23, 8]
resultado_1 = encontrar_numero_mas_grande(numeros_ejemplo_1)
print(f"En la lista {numeros_ejemplo_1}, el número más grande es: {resultado_1}") # Salida: ...el número más grande es: 23

# Ejemplo 2: Lista con el mayor al principio
numeros_ejemplo_2 = [30, 10, 20, 5]
resultado_2 = encontrar_numero_mas_grande(numeros_ejemplo_2)
print(f"En la lista {numeros_ejemplo_2}, el número más grande es: {resultado_2}") # Salida: ...el número más grande es: 30

# Ejemplo 3: Lista con el mayor al final
numeros_ejemplo_3 = [1, 7, 3, 40]
resultado_3 = encontrar_numero_mas_grande(numeros_ejemplo_3)
print(f"En la lista {numeros_ejemplo_3}, el número más grande es: {resultado_3}") # Salida: ...el número más grande es: 40

# Ejemplo 4: Lista con números negativos
numeros_ejemplo_4 = [-10, -3, -15, -1]
resultado_4 = encontrar_numero_mas_grande(numeros_ejemplo_4)
print(f"En la lista {numeros_ejemplo_4}, el número más grande es: {resultado_4}") # Salida: ...el número más grande es: -1

# Ejemplo 5: Lista con un solo elemento
numeros_ejemplo_5 = [99]
resultado_5 = encontrar_numero_mas_grande(numeros_ejemplo_5)
print(f"En la lista {numeros_ejemplo_5}, el número más grande es: {resultado_5}") # Salida: ...el número más grande es: 99

# Ejemplo 6: Lista vacía
numeros_ejemplo_6 = []
resultado_6 = encontrar_numero_mas_grande(numeros_ejemplo_6)
print(f"En la lista {numeros_ejemplo_6}, el número más grande es: {resultado_6}") # Salida: La lista está vacía, no se puede encontrar el número más grande. ...el número más grande es: None