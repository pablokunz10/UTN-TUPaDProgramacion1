# Ejercicio 3

import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

lunes_t1 = "(libre)"
lunes_t2 = "(libre)"
lunes_t3 = "(libre)"
lunes_t4 = "(libre)"

martes_t1 = "(libre)"
martes_t2 = "(libre)"
martes_t3 = "(libre)"

operador = input("Ingrese nombre del operador: ")
while not operador.replace(" ", "").isalpha():
    limpiar_pantalla()
    operador = input("Ingrese nombre del operador (solo letras): ")

while True:
    print(f"SISTEMA DE TURNOS (Operador: {operador})")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        print("RESERVAR")
        while True:
            dia = input("Seleccione día (1. Lunes / 2. Martes / 0. Volver): ")
            if dia == "0": break
            
            if dia not in ["1", "2"]:
                print("Día no válido.")
                continue

            while True:
                nombre = input("Ingrese el nombre del paciente: ")
                if nombre.replace(" ", "").isalpha(): break
                print("Error: El nombre debe contener solo letras.")

            if dia == "1":
                n_turno = input("Ingrese turno para Lunes (1 al 4): ")
                if n_turno == "1":
                    if lunes_t1 == "(libre)":
                        lunes_t1 = nombre
                        print("¡Turno 1 reservado!"); break
                    else: print("Error: El Turno 1 ya está ocupado. Elija otro.")
                elif n_turno == "2":
                    if lunes_t2 == "(libre)":
                        lunes_t2 = nombre
                        print("¡Turno 2 reservado!"); break
                    else: print("Error: El Turno 2 ya está ocupado. Elija otro.")
                elif n_turno == "3":
                    if lunes_t3 == "(libre)":
                        lunes_t3 = nombre
                        print("¡Turno 3 reservado!"); break
                    else: print("Error: El Turno 3 ya está ocupado. Elija otro.")
                elif n_turno == "4":
                    if lunes_t4 == "(libre)":
                        lunes_t4 = nombre
                        print("¡Turno 4 reservado!"); break
                    else: print("Error: El Turno 4 ya está ocupado. Elija otro.")
                else: print("Número de turno inválido.")

            elif dia == "2":
                n_turno = input("Ingrese turno para Martes (1 al 3): ")
                if n_turno == "1":
                    if martes_t1 == "(libre)":
                        martes_t1 = nombre
                        print("¡Turno 1 reservado!"); break
                    else: print("Error: El Turno 1 ya está ocupado. Elija otro.")
                elif n_turno == "2":
                    if martes_t2 == "(libre)":
                        martes_t2 = nombre
                        print("¡Turno 2 reservado!"); break
                    else: print("Error: El Turno 2 ya está ocupado. Elija otro.")
                elif n_turno == "3":
                    if martes_t3 == "(libre)":
                        martes_t3 = nombre
                        print("¡Turno 3 reservado!"); break
                    else: print("Error: El Turno 3 ya está ocupado. Elija otro.")
                else: print("Número de turno inválido.")

    elif opcion == "2":
        print("CANCELAR")
        dia = input("Seleccione día (1. Lunes / 2. Martes): ")
        if dia == "1":
            n_turno = input("Liberar turno Lunes (1-4): ")
            if n_turno == "1": lunes_t1 = "(libre)"
            elif n_turno == "2": lunes_t2 = "(libre)"
            elif n_turno == "3": lunes_t3 = "(libre)"
            elif n_turno == "4": lunes_t4 = "(libre)"
        elif dia == "2":
            n_turno = input("Liberar turno Martes (1-3): ")
            if n_turno == "1": martes_t1 = "(libre)"
            elif n_turno == "2": martes_t2 = "(libre)"
            elif n_turno == "3": martes_t3 = "(libre)"
        print("Turno actualizado a (libre).")

    elif opcion == "3":
        print("AGENDA")
        dia = input("Día a ver (1. Lunes / 2. Martes): ")
        if dia == "1":
            print(f"Lunes:T1:{lunes_t1} - T2:{lunes_t2} - T3:{lunes_t3} - T4:{lunes_t4}")
        elif dia == "2":
            print(f"Martes:T1:{martes_t1} - T2:{martes_t2} - T3:{martes_t3}")

    elif opcion == "4":
        ocupados = 0
        if lunes_t1 != "(libre)": ocupados += 1
        if lunes_t2 != "(libre)": ocupados += 1
        if lunes_t3 != "(libre)": ocupados += 1
        if lunes_t4 != "(libre)": ocupados += 1
        if martes_t1 != "(libre)": ocupados += 1
        if martes_t2 != "(libre)": ocupados += 1
        if martes_t3 != "(libre)": ocupados += 1
        print(f"Resumen General: {ocupados} turnos ocupados.")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break




    
        



