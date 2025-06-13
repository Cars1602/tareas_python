def contar_apariciones(lista, elemento_buscado):
    """
    Cuenta cuántas veces aparece un elemento específico en una lista.

    Args:
        lista: La lista donde se buscará el elemento.
        elemento_buscado: El elemento cuyo número de apariciones se quiere contar.

    Returns:
        El número de veces que el elemento buscado aparece en la lista.
    """
    # 1. Inicialización: Crea un contador y ponle el valor 0.
    contador = 0

    # 2. Iteración: Recorrer cada elemento de la lista, uno por uno.
    # 3. Comparación: En cada paso, pregunta: "¿Es este elemento igual al que estoy buscando?"
    #    Si la respuesta es "Sí", incrementa tu contador en 1.
    #    Si la respuesta es "No", no hagas nada.
    for elemento in lista:
        if elemento == elemento_buscado:
            contador += 1  # Incrementa el contador si el elemento coincide

    # 4. Condición de Fin: Continúa hasta haber revisado todos los elementos. (El bucle 'for' se encarga de esto)
    # 5. Resultado: El número final en tu contador es la respuesta.
    return contador

# --- Ejemplos de uso ---

# Ejemplo 1: Contar números
mi_lista_numeros = [1, 2, 3, 2, 4, 2, 5, 2]
elemento_a_contar_1 = 2
veces_aparece_1 = contar_apariciones(mi_lista_numeros, elemento_a_contar_1)
print(f"El número {elemento_a_contar_1} aparece {veces_aparece_1} veces en {mi_lista_numeros}")
# Salida: El número 2 aparece 4 veces en [1, 2, 3, 2, 4, 2, 5, 2]

# Ejemplo 2: Contar cadenas de texto
mi_lista_frutas = ["manzana", "banana", "manzana", "pera", "manzana", "kiwi"]
elemento_a_contar_2 = "manzana"
veces_aparece_2 = contar_apariciones(mi_lista_frutas, elemento_a_contar_2)
print(f"'{elemento_a_contar_2}' aparece {veces_aparece_2} veces en {mi_lista_frutas}")
# Salida: 'manzana' aparece 3 veces en ['manzana', 'banana', 'manzana', 'pera', 'manzana', 'kiwi']

# Ejemplo 3: Elemento que no está en la lista
mi_lista_colores = ["rojo", "verde", "azul"]
elemento_a_contar_3 = "amarillo"
veces_aparece_3 = contar_apariciones(mi_lista_colores, elemento_a_contar_3)
print(f"'{elemento_a_contar_3}' aparece {veces_aparece_3} veces en {mi_lista_colores}")
# Salida: 'amarillo' aparece 0 veces en ['rojo', 'verde', 'azul']

# Ejemplo 4: Lista vacía
mi_lista_vacia = []
elemento_a_contar_4 = 10
veces_aparece_4 = contar_apariciones(mi_lista_vacia, elemento_a_contar_4)
print(f"'{elemento_a_contar_4}' aparece {veces_aparece_4} veces en {mi_lista_vacia}")
# Salida: '10' aparece 0 veces en []