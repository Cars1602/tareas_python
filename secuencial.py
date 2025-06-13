# clase06_busquedas.py

def busqueda_lineal(lista, clave):
    """
    Implementa el algoritmo de búsqueda lineal.

    Args:
        lista (list): La lista en la que buscar (puede estar desordenada).
        clave: El elemento a buscar.

    Returns:
        int: El índice de la clave si se encuentra, o -1 si no.
    """
    # Usa un bucle for con range(len(lista)) para obtener los índices i.
    for i in range(len(lista)):
        # Dentro del bucle, si lista[i] == clave: return i.
        if lista[i] == clave:
            return i
    # Si el bucle termina sin encontrar nada, return -1 (después del bucle!).
    return -1

# Prueba tu función con assert:
if __name__ == "__main__":
    mi_lista_desordenada = [10, 5, 42, 8, 17, 30, 25]

    print("Probando busqueda_lineal...")

    # Test cases using assert
    assert busqueda_lineal(mi_lista_desordenada, 42) == 2, "Test Falló: 42 debería estar en el índice 2"
    assert busqueda_lineal(mi_lista_desordenada, 10) == 0, "Test Falló: 10 debería estar en el índice 0 (Al inicio)"
    assert busqueda_lineal(mi_lista_desordenada, 25) == 6, "Test Falló: 25 debería estar en el índice 6 (Al final)"
    assert busqueda_lineal(mi_lista_desordenada, 99) == -1, "Test Falló: 99 no debería existir"
    assert busqueda_lineal([], 5) == -1, "Test Falló: Búsqueda en lista vacía debería retornar -1"

    print("¡Pruebas para busqueda_lineal pasaron! ✅")

    # Optional: Additional test cases
    print("\nEjemplos adicionales:")
    print(f"Buscando 8 en {mi_lista_desordenada}: {busqueda_lineal(mi_lista_desordenada, 8)}")
    print(f"Buscando 17 en {mi_lista_desordenada}: {busqueda_lineal(mi_lista_desordenada, 17)}")
    print(f"Buscando 100 en {mi_lista_desordenada}: {busqueda_lineal(mi_lista_desordenada, 100)}")