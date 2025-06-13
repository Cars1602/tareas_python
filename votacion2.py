edad_str = input("Bienvenido a las elecciones de nuestro próximo tirano, saqueador. Ingrese su edad: ")
edad = int(edad_str)

if edad >= 18:
    print("Eres mayor de edad, puedes votar por el próximo dictador :D")
    print("Candidatos disponibles:")
    print("1. Capitán Lara")
    print("2. General Patán")
    print("3. Señor de los Memes")

    opcion = input("Ingresa el número de tu candidato favorito: ")

    if opcion == "1":
        print("Has votado por Capitán Lara. ¡Buena suerte con eso!")
    elif opcion == "2":
        print("Has votado por General Patán. Esperemos que sobrevivas.")
    elif opcion == "3":
        print("Has votado por el Señor de los Memes. El caos te bendiga.")
    else:
        print("Opción no válida. ¡Has desperdiciado tu voto como buen ciudadano!")
elif edad >= 13:
    print("¿Qué haces aquí? ¡Ve a hacer tus deberes, maldito vago!")
elif edad >= 5:
    print("¡Cámbiate los pañales, puerco!")
else:
    print("Eres un puberto. Vuelve cuando sepas atarte los zapatos.")
