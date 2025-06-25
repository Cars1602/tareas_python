producto = {'codigo': 'P001', 'nombre': 'cafe', 'precio': 38.0, 'stock': 100}
print("(\n-- Clave del producto ---")
for clave in producto:
    print(clave)
print("\n-- clave y producto---")
for clave in producto:
    valor = producto[clave]
    print(f"{clave.capitalize()}: {valor}")
