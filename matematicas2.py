from cgi import print_arguments


def encontrar_numero_mas_grande (lista_numero):
    if not lista_numero:
        print("La lista esta vacia, no se puede encontrar numero mas grande.")
        return None
    mayor_temporal = lista_numero[0]
    for i in range(1, len (lista_numero)):
        elemento_actual = lista_numero[i]
        if elemento_actual > mayor_temporal:
            mayor_temporal = elemento_actual
    return mayor_temporal

numeros_ejemplo_1 = [12,5,23,8]
resultado_1 = encontrar_numero_mas_grande(numeros_ejemplo_1)
print(f"En la lista {numeros_ejemplo_1}, el numero mas grande es: {resultado_1}")