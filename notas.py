# Accediendo a Elementos (Leer un "Cajan"): Usamos el nombre de la lista seguido de corchetes com indice deseado.
notas_parciales = [80,95,73,60,88]
primera_nota=notas_parciales[0] # Indice 0 para el PRIMER elemento
print(f"La primera nota fue: ¨{primera_nota}") # Imprimir 80
tercera_nota = notas_parciales[2]  # Indice 2 para el TERCER elemento
print(f"La tercera nota fue: {tercera_nota}") # Imprimir 73

# Modificando Elementos ( Cambiar el contenido de un "cajon"):
print(f"Lista original: {notas_parciales}")
# Supongamos que se recalifico el 4to (indice 3)
notas_parciales[3]=65 # Asignamos un nuevo valor al indice 3
print(f"Lista modificada: {notas_parciales}")

# Obteniendo el Tamaño (len()):
cantidad_de_notas = len(notas_parciales)
print (f"Tenemos un total de {cantidad_de_notas} notas.") #Imprimira 5