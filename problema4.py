def invertir_lista_nueva(lista_original):
    """
    Invierte el orden de los elementos de una lista, creando una nueva lista.

    Args:
        lista_original: La lista cuyos elementos se quieren invertir.

    Returns:
        Una nueva lista con los elementos de la lista_original en orden inverso.
        Retorna una lista vacía si la lista_original está vacía.
    """
    # 1. Inicialización: Crea una nueva lista vacía para el resultado.
    lista_invertida = []

    # Manejar el caso de una lista vacía para evitar errores de índice.
    if not lista_original:
        return lista_invertida # Retorna una lista vacía si la original está vacía

    # 2. Iteración (Especial): Recorre la lista original comenzando desde el último elemento
    # y yendo hacia el primero.
    # len(lista_original) - 1 es el índice del último elemento.
    # -1 es el punto de parada (no se incluye, por lo que el bucle va hasta el índice 0).
    # -1 es el "paso" o incremento, indicando que el bucle va hacia atrás.
    for i in range(len(lista_original) - 1, -1, -1):
        # 3. Construcción: Toma el elemento actual de la lista original y añádelo al final
        # de tu lista_invertida.
        elemento_actual = lista_original[i]
        lista_invertida.append(elemento_actual)

    # 5. Resultado: lista_invertida contendrá todos los elementos de la original,
    # pero en orden inverso.
    return lista_invertida

# --- Ejemplos de uso ---

# Ejemplo 1: Lista de números
numeros = [10, 20, 30, 40, 50]
numeros_invertidos = invertir_lista_nueva(numeros)
print(f"Lista original: {numeros}")
print(f"Lista invertida: {numeros_invertidos}")
# Salida: Lista original: [10, 20, 30, 40, 50]
#         Lista invertida: [50, 40, 30, 20, 10]

# Ejemplo 2: Lista de cadenas de texto
letras = ["a", "b", "c", "d"]
letras_invertidas = invertir_lista_nueva(letras)
print(f"Lista original: {letras}")
print(f"Lista invertida: {letras_invertidas}")
# Salida: Lista original: ['a', 'b', 'c', 'd']
#         Lista invertida: ['d', 'c', 'b', 'a']

# Ejemplo 3: Lista con un solo elemento
un_elemento = ["único"]
un_elemento_invertido = invertir_lista_nueva(un_elemento)
print(f"Lista original: {un_elemento}")
print(f"Lista invertida: {un_elemento_invertido}")
# Salida: Lista original: ['único']
#         Lista invertida: ['único']

# Ejemplo 4: Lista vacía
lista_vacia = []
lista_vacia_invertida = invertir_lista_nueva(lista_vacia)
print(f"Lista original: {lista_vacia}")
print(f"Lista invertida: {lista_vacia_invertida}")
# Salida: Lista original: []
#         Lista invertida: []