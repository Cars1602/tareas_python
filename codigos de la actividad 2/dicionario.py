#Paso 1: Variables Globales
lista_de_tareas = []
proximo_id_tarea = 1 # Para generar IDs únicos
#Paso 2: Implementar agregar_tarea
def agregar_tarea(descripcion, prioridad="media"):
 global proximo_id_tarea # ¡Necesario para modificar una variable global!
 nueva_tarea = {
 "id": proximo_id_tarea,
 "descripcion": descripcion,
 "completada": False,
 "prioridad": prioridad
 }
 lista_de_tareas.append(nueva_tarea)
 proximo_id_tarea += 1
 print(f" Tarea '{descripcion}' añadida con éxito.")
#Paso 3: Implementar mostrar_tareas
def mostrar_tareas():
 print("\n--- LISTA DE TAREAS ---")
 if not lista_de_tareas:
  print("¡No hay tareas pendientes! ¡A disfrutar!")
 return

for tarea in lista_de_tareas:
  estado = " " if tarea["completada"] else " "
  print(f"{estado} ID: {tarea['id']} | {tarea['descripcion']} (Prioridad: {tarea['prioridad']})")
  print("------------------------")
agregar_tarea("Estudiar para el examen de Cálculo")
agregar_tarea("Hacer las compras", prioridad="alta")
mostrar_tareas()
def buscar_tarea_por_id(id_buscado):
 """Recorre la lista de tareas y devuelve el diccionario de la tarea
 que coincide con el id_buscado. Si no la encuentra, devuelve None."""
 for tarea in lista_de_tareas:
  if tarea["id"] == id_buscado:
   return tarea # ¡Éxito! Devolvemos el diccionario completo
 return None # Si el bucle termina, no se encontró
# Asumiendo que ya agregaste tareas con IDs 1 y 2...
tarea_encontrada = buscar_tarea_por_id(1)
if tarea_encontrada:
 print(f"\nBúsqueda exitosa: {tarea_encontrada['descripcion']}")
else:
 print("\nBúsqueda fallida: Tarea no encontrada.")
tarea_fantasma = buscar_tarea_por_id(99)
if not tarea_fantasma:
 print("Búsqueda de tarea inexistente funcionó correctamente.")