# Paso 1: Definir el número secreto
numero_secreto = 7

# Paso 2: Pedir al usuario que adivine
adivinanza = int(input("Adivina el número secreto entre 1 y 10: "))

# Paso 3: Bucle hasta que lo adivine
while adivinanza != numero_secreto:
    if adivinanza < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")
    
    # Volver a pedir el número
    adivinanza = int(input("Adivina otra vez: "))

# Paso 4: Mensaje final
print(f"¡Correcto! El número era {numero_secreto}. 🎉")
