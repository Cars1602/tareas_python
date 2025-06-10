edad_str = input("Bienvenido al cine, ¿cuál es tu edad?: ")
edad = int(edad_str)

if edad < 0:
    print("Edad no válida. Por favor, ingresa un número positivo.")
elif edad >= 18:
    print("¡Puedes ver películas clasificadas R!")
elif edad >= 13:  
    print("Puedes ver películas clasificadas PG-13.")
else: 
    print("Te recomendamos películas clasificadas G o PG.")