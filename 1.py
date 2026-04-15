# Ejercicio 1

nombre = input("Ingrese su nombre: " )
while not nombre.isalpha():
    nombre = input("Ingrese su nombre (solo letras): ")

while not cant_productos.isdigit() or cant_productos == "0":
    print("Error: Por favor ingresa un número entero mayor a cero")
    cant_productos = input("¿Cuántos productos vas a comprar? ")

cantidad = int(cant_productos)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, int(cant_productos) + 1):
    print(f" Producto {i} ")

    precio = input(f"Ingrese el precio del producto {i}: ")
    while not precio.isdigit():
        print("Error: El precio debe ser un número entero.")
        precio = input(f"Ingrese el precio del producto {i}: ")

    precio_original = int(precio)

    tiene_descuento = input(f"¿El producto {i} tiene descuento? (S/N): ").lower()
    while tiene_descuento not in ['s', 'n']:
        print("Error: Ingrese solo 'S' o 'N'.")
        tiene_descuento = input(f"¿Tiene descuento? (S/N): ").lower()
    
    if tiene_descuento == 's':
        precio_actual = precio_original * 0.90
        print(f"¡Descuento aplicado! Precio con rebaja: ${precio_actual:.2f}")
    else:
        precio_actual = precio_original

    total_sin_descuento += precio_original 
    total_con_descuento += precio_actual
        
ahorro_total = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad if cantidad > 0 else 0

print(f"\nTotal sin descuentos:  ${total_sin_descuento:.2f}")
print(f"Total con descuentos:  ${total_con_descuento:.2f}")
print(f"Ahorro total:          ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")