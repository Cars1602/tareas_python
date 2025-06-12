#El Algoritmo (La Receta):
#1. Inicialización: Crea una "caja" para la suma (una variable) y ponle el valor 0. Llamémosla acumulador_suma.
#2. Iteración: Toma el primer número de la lista y súmalo a tu acumulador_suma.
#3. Repetición: Toma el siguiente número de la lista y súmalo a tu acumulador_suma.
#4. Condición de Fin: Repite el paso 3 hasta que hayas procesado todos los números de la lista.
#5. Resultado: El valor final en acumulador_suma es tu respuesta.****
def acumulador_suma(lista):
    acumulador_suma = 0
    for numero in lista:
        acumulador_suma += numero
    return acumulador_suma
print(acumulador_suma([6, 9, 0, 45, 9]))  


#Problema 2: Encontrar el número más grande de una lista.
#El Algoritmo (La Receta):
#1. Suposición Inicial: Asume que el primer elemento de la lista es el más grande hasta ahora. Guárdalo en una
#variable mayor_temporal. (¡Cuidado! ¿Qué pasa si la lista está vacía?).
#2. Iteración: Toma el siguiente elemento de la lista.
#3. Comparación: Compara este elemento con tu mayor_temporal.
#● Si el elemento actual es más grande que mayor_temporal, ¡desecha el valor antiguo y actualiza
#mayor_temporal con este nuevo número más grande!
#● Si no, no hagas nada y continúa.
#4. Condición de Fin: Repite los pasos 2 y 3 hasta que hayas revisado todos los elementos.
#5. Resultado: El valor final en mayor_temporal es el número más grande de toda la lista.
# Pedir al usuario que ingrese los números separados por comas
entrada = input("Ingresa varios números separados por comas: ")

# Convertir la entrada en una lista de números
numeros = entrada.split(",")

# Suponer que el primer número es el mayor (convertido a entero)
mayor = int(numeros[0])

# Recorrer el resto de los números
for n in numeros:
    numero = int(n)
    if numero > mayor:
        mayor = numero

# Mostrar el número más grande
print("El número más grande es:", mayor)

#El Algoritmo (La Receta):
#1.	Inicialización: Crea un contador y ponle el valor 0.
#2.	Iteración: Recorrer cada elemento de la lista, uno por uno.
#3.	Comparación: En cada paso, pregunta: "¿Es este elemento igual al que estoy buscando?" 
# ●	Si la respuesta es "Sí", incrementa tu contador en 1. ●	Si la respuesta es "No", no hagas nada.
#4.	Condición de Fin: Continúa hasta haber revisado todos los elementos.
#5.	Resultado: El número final en tu contador es la respuesta.
# Debería imprimir 3 porque hay tres '1' en la lista
# Paso 1: Inicialización
contador = 0
lista = [1, 3, 1, 5, 1, 7, 9]
buscar = 1
for elemento in lista:
    if elemento == buscar:
        contador += 1
print("El número", buscar, "aparece", contador, "veces.")


#Problema 4: Invertir el orden de una lista (creando una lista nueva).
#El Algoritmo (La Receta):
#1.	Inicialización: Crea una nueva lista vacía para el resultado, llamémosla lista_invertida.
#2.	Iteración (Especial): Recorre la lista original pero ¡comenzando desde el último elemento y yendo hacia el primero!
#3.	Construcción: En cada paso, toma el elemento actual de la lista original y añádelo al final de tu lista_invertida.
#4.	Condición de Fin: Continúa hasta que hayas procesado todos los elementos (desde el último hasta el primero).
#5.	Resultado: lista_invertida contendrá todos los elementos de la original, pero en orden inverso.

lista_original = [1, 2, 3, 4, 5]
lista_original.reverse()
print("Lista original:", lista_original)

