# Ejercicio: Verificador de Edad para Películas usando Funciones

def obtener_clasificacion_pelicula(edad_persona):
    """
    Función que determina qué tipo de películas puede ver una persona según su edad.
    
    Parámetro:
        edad_persona (int): La edad de la persona
    
    Retorna:
        str: Mensaje con la clasificación de película recomendada
    """
    
    # Validar que la edad sea válida
    if edad_persona < 0 or edad_persona > 120:
        return "Edad no válida."
    
    # Lógica de clasificación por edad
    if edad_persona < 13:
        return "Te recomendamos películas G (General Audiences)."
    elif edad_persona < 17:
        return "Puedes ver películas G y PG-13."
    elif edad_persona >= 17:
        return "¡Puedes ver películas de cualquier clasificación incluyendo R!"
    

def main():
    """
    Función principal del programa
    """
    print("=== VERIFICADOR DE EDAD PARA PELÍCULAS ===")
    print()
    
    try:
        # Solicitar edad al usuario
        edad_ingresada = int(input("Por favor, ingresa tu edad: "))
        
        # Llamar a la función para obtener la clasificación
        mensaje_cine = obtener_clasificacion_pelicula(edad_ingresada)
        
        # Mostrar el resultado
        print(f"\nResultado: {mensaje_cine}")
        
    except ValueError:
        print("Error: Por favor ingresa un número válido para la edad.")
    
    print("\n¡Gracias por usar nuestro verificador!")


# Programa adicional para probar múltiples edades
def probar_multiples_edades():
    """
    Función para probar la función con diferentes edades de ejemplo
    """
    print("\n=== PRUEBAS CON DIFERENTES EDADES ===")
    
    edades_prueba = [5, 12, 13, 16, 17, 25, 65, -5, 150]
    
    for edad in edades_prueba:
        resultado = obtener_clasificacion_pelicula(edad)
        print(f"Edad {edad}: {resultado}")


# Ejecución del programa principal
if __name__ == "__main__":
    # Ejecutar el programa principal
    main()
    
    # Preguntar si quiere ver las pruebas
    print()
    ver_pruebas = input("¿Quieres ver las pruebas con diferentes edades? (s/n): ").lower()
    if ver_pruebas == 's' or ver_pruebas == 'si':
        probar_multiples_edades()