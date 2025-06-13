# Crear una lista con notas numericas
mis_notas = [85.5, 92, 78, 88.5, 95, 82]
# Inicializar variable para la suma
suma_total = 0
# Usar bucle for para calcular la suma total sin usar sum()
for nota in mis_notas:
    suma_total += nota
# Calcular el promedio
promedio = suma_total /len(mis_notas)
# Imprimir resultados de forma clara
print(f"Suma total de las notas: {suma_total}")
print(f"Promedio de las notas: {promedio: .2f}")
print(f"La nota promedio de Adaniel: {promedio: .1f}")
    