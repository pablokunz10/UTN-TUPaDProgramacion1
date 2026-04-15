#Ejercicio 2

usuario_correcto = "alumno"
contraseña_correcta = "python123"
intentos = 1

nombre_de_usuario = input ("Ingrese su nombre de usuario: ")
contraseña = input ("Ingrese su contraseña: ")

while (nombre_de_usuario != usuario_correcto or contraseña != contraseña_correcta) and intentos <3:
    intentos += 1
    print(f"Usuario o contraseña no válido. Intento {intentos} de 3.")
    nombre_de_usuario = input ("Ingrese su nombre de usuario: ")
    contraseña = input ("Ingrese su contraseña: ")

acceso_valido = nombre_de_usuario == usuario_correcto and contraseña == contraseña_correcta

if acceso_valido:
    print ("Acceso concedido")
else:
    print("Cuenta bloqueada")

while acceso_valido:
    print("MENÚ DE USUARIO")
    print("1 - Ver estado de inscripción")
    print("2 - Cambiar clave")
    print("3 - mensaje motivacional")
    print("4 - Salir")
    
    opcion = input("Seleccione una opción (1-4): ")

    if opcion.isdigit() and "1" <= opcion <= "4":
        if opcion == "1":
            print("Estado: Inscripto")
       
        elif opcion == "2":
            nueva_clave = input("Ingrese su nueva clave: ")
            confirmacion = input("Confirme su nueva clave: ")
            if len(nueva_clave) < 6:
                print ("La clave debe tener minimo 6 caracteres")
            elif nueva_clave == confirmacion:
                contraseña_correcta = nueva_clave
                print("¡Clave cambiada con éxito!")
            else:
                print("Error: Las claves no coinciden.")
                
        elif opcion == "3":
            print("Frase del día: 'El trabajo no se desperdicia, se acumula'")
            
        elif opcion == "4":
            print("Saliendo del sistema...")
            acceso_valido = False
            
    else:
        print(">> Error: Por favor, ingrese un número válido entre 1 y 4.")




    



    





    


