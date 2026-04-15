#Ejercicio 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0

import os
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear') #me gusta ponerle esta accion como en el ejercicio anterior para q no se acumulen en pantalla los intentos fallidos 

nombre_agente = input("Ingrese el nombre del agente: ")
while not nombre_agente.replace(" ", "").isalpha():
    limpiar_pantalla()
    nombre_agente = input("Ingrese su nombre (solo letras): ")
    print(f"Bienvenido agente {nombre_agente.upper()}")
    print("Misión: Abrir las 3 cerraduras de la bóveda.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma and tiempo <= 3:
        print("¡SISTEMA BLOQUEADO! La alarma se activó y el tiempo se agotó")
        break

    print(f"ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ON' if alarma else 'OFF'} | Código: [{codigo_parcial}]")
    
    print("MENÚ DE ACCIONES:")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")
    
    opcion = ""
    while not opcion.isdigit():
        opcion = input("Seleccione una acción: ")
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")

    if opcion == "1":
        energia -= 20
        tiempo -= 2
        forzar_seguidos += 1
        
        if forzar_seguidos >= 3:
            alarma = True
            print("¡LA CERRADURA SE TRABÓ! Has intentado forzar demasiado. Alarma activada.")
        else:
            if energia < 40:
                print("RIESGO DE ALARMA ALTO (Energía baja)")
                n_riesgo = ""
                while not n_riesgo.isdigit():
                    n_riesgo = input("Elija un número de seguridad (1-3): ")
                    if not n_riesgo.isdigit():
                        print("Ingrese un número.")
                
                if n_riesgo == "3":
                    alarma = True
                    print("¡ERROR! Activaste los sensores de movimiento.")
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura forzada con éxito!")

    elif opcion == "2":
        forzar_seguidos = 0 
        energia -= 10
        tiempo -= 3
        
        print("Hackeando sistema...")
        for i in range(1, 5):
            print(f"Paso {i} de 4...")
            codigo_parcial += "A"
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completado! Una cerradura se abrió remotamente.")

    elif opcion == "3":
        forzar_seguidos = 0 
        recuperacion = 15
        if alarma:
            recuperacion -= 10
            print("El ruido de la alarma no te deja descansar bien...")
        
        energia += recuperacion
        if energia > 100: energia = 100
        tiempo -= 1
        print(f"Has descansado. Energía actual: {energia}")

    else:
        print("Opción no válida. Pierdes tiempo intentando decidir.")
        tiempo -= 1

print("RESULTADO FINAL")
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El Agente {nombre_agente} ha abierto la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA: Te has quedado sin recursos. Los guardias te atraparon.")
else:
    print("DERROTA: El sistema se bloqueó permanentemente.")
