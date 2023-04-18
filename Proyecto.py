#Este va a ser nuestro archivo para la creación del proyecto
#Funciones de las opciones del menú

import getpass

# Almacenamiento de usuarios
usuarios = {}

# Función para solicitar un número de cédula válido al usuario
def solicitarCedula() :
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
    

# Submenú
# opcion = ""
    while opcion != "7":
        print("Submenú:")
        print("1. Retirar dinero")
        print("2. Depositar dinero")
        print("3. Ver saldo actual")
        print("4. Pagar servicios")
        print("5. Compra/Venta de Divisas")
        print("6. Eliminar usuario")
        print("7. Salir")
        opcion = input("Ingrese el número de opción deseada: ")

    if opcion == "1":
                                # Retirar dinero
                                cuenta = input("¿De qué cuenta desea retirar dinero? (1. Colones, 2. Dólares, 3. Bitcoin): ")
                                monto = float(input("Ingrese el monto que desea retirar: "))
                                # Verificación de saldo suficiente
                                # ...

    elif opcion == "2":
                                # Depositar dinero
                                cuenta = input("¿A qué cuenta desea acreditar el depósito de dinero? (1. Colones, 2. Dólares, 3. Bitcoin): ")
                                monto = float(input("Ingrese el monto que desea depositar: "))
                                # Advertencia para monto negativo
                                # ...

    elif opcion == "3":
        pass                       
    
                                 # Ver saldo actual
                                 # ...
                                
                                 
    elif opcion == "4":
                                # Pagar servicios
         servicio = input("Seleccione el servicio que desea pagar: ")
                                # Verificación de servicio activo
                                # ...
                                # Mostrar saldo a pagar
                                # ...
                                # Seleccionar cuenta de pago
                                # ...
                                # Verificación de saldo suficiente
                                # ...
                                # Conversión de divisas automática, si aplica
                                # ...

    elif opcion == "5":
        pass                   
                                # Compra/Venta de Divisas
                                # ...
    
    elif opcion == "6":
        pass                    
                                # Eliminar usuario
                                # ...
                                # 
                                # 
    elif opcion == "7":
                                # Salir
                                print("Saliendo del sistema. Gracias por utilizar nuestros servicios.")
                                # Actualización de saldos en archivos de texto
                                # ..

    else:    
        
         print("Se ha retirado el dinero solicitado.")
         #imprimir el saldo actual
         #Regresar al submenu
         #Despositar el dinero

         Credito= input("¿De qué cuenta desea acreditar el deposito de dinero? (4. Colones, 5. Dólares, 6. Bitcoin): ")
         Deposito= float(input("cuanto quiere depositar: "))
         #verificacion deposito suficiente
         #advertencia para el deposito negativo
        
    print("su transaccion se hizo de forma correcta")
    
        
    