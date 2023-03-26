#Este va a ser nuestro archivo para la creación del proyecto
#Funciones de las opciones del menú

import getpass

# Almacenamiento de usuarios
usuarios = {}

# Función para solicitar un número de cédula válido al usuario
def solicitarCedula():
    intentos = 0
    while intentos < 3:
        cedula = input("Ingrese su número de cédula (9 dígitos): ")
        if len(cedula) != 9:
            print("El número de cédula debe ser de 9 dígitos.")
        elif cedula in usuarios:
            print("El número de cédula ya está registrado.")
        else:
            return cedula
        intentos += 1
    print("Se excedió el máximo de intentos para ingresar un número de cédula válido.")
    return None

# Función para solicitar el nombre del usuario
def solicitarNombre():
    nombre = input("Ingrese su nombre completo: ")
    return nombre

# Función para solicitar un PIN válido al usuario
def solicitarPin():
    intentos = 0
    while intentos < 3:
        pin = getpass.getpass("Ingrese su PIN (4 dígitos): ")
        if len(pin) != 4:
            print("El PIN debe ser de 4 dígitos.")
        else:
            pin_confirmacion = getpass.getpass("Ingrese su PIN nuevamente para confirmar: ")
            if pin == pin_confirmacion:
                return pin
            else:
                print("Los PIN no coinciden.")
        intentos += 1
    print("Se excedió el máximo de intentos para ingresar un PIN válido.")
    return None

# Función para registrar un nuevo usuario
def registrarUsuario():
    print("== Registro de nuevo usuario ==")
    cedula = solicitarCedula()
    if cedula:
        nombre = solicitarNombre()
        pin = solicitarPin()
        if pin:
            usuarios[cedula] = {"nombre": nombre, "pin": pin}
            print("Usuario registrado correctamente.")
    input("Presione Enter para volver al menú principal.")





# Función para mostrar el menú de opciones
def mostrar_menu():
    print("1. Registro nuevo usuario")
    print("2. Usuario registrado")
    print("3. Configuración avanzada")
    print("4. Salir")

while True:
    print("Bienvenido al cajero automático")
    mostrar_menu()
    opciónElegida = int(input("Digite la opción que desea realizar\n"))
    if opciónElegida == 1:
        registrarUsuario()
    





