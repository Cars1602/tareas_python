# Ejemplo de código a refactorizar:
# Rectángulo 1
base1 = 10 
altura1 = 5 
area1 = base1 * altura1
print(f"El área del rectángulo 1 ({base1}x{altura1}) es: {area1}")
# Rectángulo 2
base2 = 7 
altura2 = 3 
area2 = base2 * altura2
print(f"El área del rectángulo 2 ({base2}x{altura2}) es: {area2}")
def mostrar_area_rectangulo(numero, base, altura):
 def calcular_area_rectangulo(base, altura):
     return base * altura    
 area = calcular_area_rectangulo(base, altura)    
 print(f"El área del rectángulo {numero} ({base}x{altura}) es: {area}")
# Ahora: 1 línea por rectángulo 
mostrar_area_rectangulo(1, 10, 5)
