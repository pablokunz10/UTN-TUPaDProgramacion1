#Ejercicio 5

nombre_valido = False
nombre_jugador = ""

while not nombre_valido:
    nombre_jugador = input("Nombre del Gladiador: ")
    if nombre_jugador.isalpha():
        nombre_valido = True
else:
        print("Error: Solo se permiten letras.")

hp_jugador = 100            
hp_enemigo = 100           
pociones = 3     
ataque_pesado_base = 15
ataque_enemigo = 12
juego_activo = True  

print("Comienza el combate")

while hp_jugador > 0 and hp_enemigo > 0:
    print(f"{nombre_jugador} (HP: {hp_jugador}) vs Enemigo (HP: {hp_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion_valida = False
    opcion = ""
    
    while not opcion_valida:
        opcion = input("Opción: ")
        if opcion.isdigit():
            if opcion == "1" or opcion == "2" or opcion == "3":
                opcion_valida = True
            else:
                print("Error: Elige 1, 2 o 3.")
        else:
            print("Error: Ingrese un número válido.")

    if opcion == "1":
        danio_final = float(ataque_pesado_base)
        if hp_enemigo < 20:
            danio_final = ataque_pesado_base * 1.5
            print("¡GOLPE CRÍTICO!")
        
        hp_enemigo -= int(danio_final)
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3): 
            hp_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")

    elif opcion == "3":
        if pociones > 0:
            hp_jugador += 30
            pociones -= 1
            print(f"Te has curado. Vida actual: {hp_jugador}")
        else:
            print("¡No quedan pociones!")

    if hp_enemigo > 0:
        hp_jugador -= ataque_enemigo
        print(f">> ¡El enemigo te atacó por {ataque_enemigo} puntos de daño!")
    
    print("NUEVO TURNO")

if hp_jugador > 0:
    print(f"¡VICTORIA! {nombre_jugador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
