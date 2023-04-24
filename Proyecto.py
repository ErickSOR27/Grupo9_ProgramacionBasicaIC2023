#ENCABEZADO
#DEFINIR BIBLIOTECAS
import os      #Vista en clase
import getpass
import random  #Esta biblioteca sirve para elegir datos,listas,datos de arreglos aleatoreamente  #Elegir de 7 servivios 3 
import shutil # Esta biblioteca sirve para manejo de archivos es similar a (os)   #Eliminar carpetas completas de usuarios
#import json  # Investigar más 
#import requests # INVESTIGAR
import string # Se usa para generar contraseñas con los caracteres que contiene Está biblioteca contiene cadenas de caracteres como letras minusculas y mayusculas numeros etc
              #Generar contraseña aleatoriamente de configuracion avanzada

#import requests # investigar más

#DEFINIR FUNCIONES


#----------------------------------------FUNCION SUBPRINCIPAL SOLICITAR CEDULA DE OPCION PRINCIPAL REGISTRAR USUARIOS----------------------------------------------------------------------

def solicitudCedula(): # Funcion para solicitar el número de cedula al usuario para su posterior registro                                       
    global cedula  # Global sirve para hacer global la variable y poder llamarla desde otras funciones     
    global cedulas_registradas
    intentos = 3       # Se establece que deben de ser 3 intentos para ingresar la cedula correcamente
    file = open("proyecto/usuarios_pines.txt", "a") # Se abre ell archivo para crearlo y que no de errores más adelante
    generarCodigoRandom()
    
    while intentos > 0:  # mientras que los intentos sean mayores a 0 sigue el programa
        cedula = input("Ingrese su número de cédula (9 dígitos):\n ") # se pide al usuario ingresar el numero de cedula especificando que deben de ser (9 digitos)
        if len(cedula)  !=9: # condicion de si cedula no es de 9 digitos  #len para leer tamaño de cedula ingresada
            print("El número de cédula debe ser de (9 dígitos)")
            intentos -= 1 # Se resta un intento a la variable intentos
            
            if intentos == 0:
                print("No tienes más intentos volviendo al menú principal")
                return False
            print("Le quedan {} intentos restantes".format(intentos))# Se imprime un mensaje con la cantidad de intentos restantes utilizando el format (USAR ESTO EN LOS DEMAS)
            continue  # Investigar
        with open("proyecto/usuarios_pines.txt", "r") as file:
            cedulas_registradas = file.read().splitlines()
            if cedula in cedulas_registradas:
                print("Error: La cédula ya ha sido registrada")
                intentos -= 1
                print("Le quedan {} intentos restantes".format(intentos))
                if intentos == 0:
                    print("No tienes más intentos volviendo al menú principal")
                    return False 
                
                continue
        with open("proyecto/usuarios_pines.txt", "a") as file:
            file.write(cedula)
            file.write("\n")
           
            
            print("Cédula registrada correctamente")
            
            solicitudNombre()
            escogerPin()
            depositoObligatorio()
            
        
    
        return False

      
#----------------------------------------FUNCION SUBPRINCIPAL SOLICITAR NOMBRE DE OPCION PRINCIPAL REGISTRAR USUARIOS----------------------------------------------------------------------


def solicitudNombre ():  #Funcion para la Solicitud del nombre del usuario y su posterior registro
    global nombre
    nombre = input("Ingrese su nombre completo:\n")
    with open("proyecto/usuarios_pines.txt","a") as archivo: # 
                    archivo.write(nombre) 
                    archivo.write("\n")
                    
                    print("Su nombre ha sido registrado correctamente")
                    return nombre


#----------------------------------------FUNCION SUBPRINCIPAL SOLICITAR PIN DE OPCION PRINCIPAL REGISTRAR USUARIOS----------------------------------------------------------------------

def escogerPin ():       #Funcion de creación de pin para el ingreso del usuario con dicho pin
    while True:
          
          pin = getpass.getpass("Ingrese su PIN (4 digitos):\n") # Se utiliza funcion getpass para que el pin no sea visible en la terminal
          if len(pin) != 4:   # con if y len se le dice al usuario que si el pin no es de 4 digitos debe intentarlo nuevamente
           print("El pin debe ser de 4 digitos intente nuevamente")
          else:
               pin_confirmacion = getpass.getpass("Ingrese su PIN nuevamente para confirmar:\n") # Se crea una variable getpass para solicitar el pin nuevamente 
               if pin == pin_confirmacion: # Si el pin es igual al primero ingresado se continua con el programa (auntentificación)
                    with open("proyecto/usuarios_pines.txt","a") as archivo: # Whit sirve para que los archivos se cierren despues de usarse
                     archivo.write( pin)
                     archivo.write("\n")
                     
                     print("Su pin ha sido registrado correctamente:\n")
                     return pin
               
               else:
                    print("Los pin no coinciden intentelo nuevamente")
   
               
 
#----------------------------------------FUNCION SUBPRINCIPAL DEPOSITO OBLIGATORIO DE OPCION PRINCIPAL REGISTRAR USUARIOS----------------------------------------------------------------------

def depositoObligatorio():   #Funcion para efectuar el deposito obligatorio  de 100 000 colones para poder ser registrado correctamente
     print("A que cuenta (colones, dólares o bitcoin) desea hacer el deposito")
     subMenuDeposito()
     
     opcionCuentas = int(input("A cual cuenta desea acreditar el deposito del dinero?\n"))

 #------------------------------------------------------OPCION DEPOSITO COLONES---------------------------------------------------------------------------------------     
     if opcionCuentas == 1:
          
          global deposito
          intentos = 3
          while intentos > 0:
              deposito = int(input("Ingrese la cantidad del depósito:\n"))
              try:
                  deposito = float(deposito)
                  if deposito < 100000:
                      print("Error: El depósito debe ser mayor a 100000.")
                      intentos -= 1
                      print(f"Intentos restantes: {intentos}") # Cambiar 
                  else:
                       crearCarpetas1 ()
                       crearCarpetaServicios()
                      # randomAcces() # modificar o dejar asi
                       print("Depósito ingresado correctamente.")
                       return deposito
                      
                       
                       
              except ValueError:
                  print("Error: Ingrese un número válido.")
                  intentos -= 1
                  print("Intentos restantes{}".format(intentos))
          else:
               print("No se pudo ingresar el depósito.")
               input("Presione enter para regresar al menú principal")


#-----------------------------------------------------OPCION DEPOSITO DOLARES---------------------------------------------------------------------------------------   
    
     if opcionCuentas == 2:
                                                                           
        
         global depositoDollar
         
         intentos = 3
         while intentos > 0:
              tasaDeCambio = 600
              depositoDollar = int(input("Ingrese la cantidad del depósito:\n"))
              ConversionColones = depositoDollar * tasaDeCambio
            #  print(f"{depositoDollar} dólares equivale a {ConversionColones} colones.") #Otra manera de imprimir la F sirve para que las variables de adentro no se comenten y se imprima correctamente

        

              try:
                  depositoDollar = float(depositoDollar)
                  if ConversionColones < 100000:
                      print("Error: El depósito debe ser mayor a 100000.")
                      intentos -= 1
                      print(f"Intentos restantes: {intentos}") # Cambiar 
                  else:
                       crearCarpetas2 ()
                       crearCarpetaServicios()
                       print("Depósito ingresado correctamente.")
                       return depositoDollar
                       
                       
              except ValueError:
                  print("Error: Ingrese un monto válido.")
                  intentos -= 1
                  print(f"Intentos restantes: {intentos}")
         else:
            print("No se pudo ingresar el depósito.")
         
 #-------------------------------------------------OPCION DEPOSITO BITCOINS--------------------------------------------------------------------------------------- 

#CAMBIAR
     if opcionCuentas == 3:
                                                                                
         global depositoBitcoin
         print
         intentos = 3
         while intentos > 0:
              tasaDeCambio = 0.000000068
              depositoBitcoin = float(input("Ingrese la cantidad del depósito:\n"))
              conversionColones = depositoBitcoin / tasaDeCambio
              #print(f"{depositoBitcoin} bitcoins equivale a {conversionColones} colones.")

        

              try:
                  conversionColones = float(conversionColones)
                  if conversionColones < 100000:
                      print("Error: El depósito debe ser mayor a 100000.")
                      intentos -= 1
                      print(f"Intentos restantes: {intentos}") # Cambiar 
                  else:
                       
                       crearCarpetas3 ()
                       crearCarpetaServicios()
                       print("Depósito ingresado correctamente.")
                       return depositoBitcoin
                       
                       
              except ValueError:
                  print("Error: Ingrese un número válido.")
                  intentos -= 1
                  print("Intentos restantes: {intentos}")
         else:
            print("No se pudo ingresar el depósito.")





#-------------------------------------------FUNCION PARA ELEGIR SERVICIOS ALEATOREAMENTE--------------------------------------------------------------------------------------------
def randomAcces():
    
      
      
    carpeta_principal = 'C:/Users/danin/workspace/Proyecto/' +  cedula + '/Servicios'

# Recorre el árbol de directorios y agrega los archivos a la lista   EXPLICAR
    for raiz, dirs, archivos in os.walk(carpeta_principal): #EXPLICAR
        for archivo in archivos: #CAMBIAR
            # Asegura que el archivo tenga la extensión .txt EXPLICAR
            if archivo.endswith('.txt'): #EXPLICAR
                listaArchivos.append(os.path.join(raiz, archivo)) #EXPLICAR

    # Selecciona 3 archivos aleatorios de la lista
    archivos_seleccionados = random.sample(listaArchivos, 3) #EXPLICAR

    # Lee el contenido de cada archivo seleccionado
    for archivo in archivos_seleccionados: #EXPLICAR
        with open(archivo, 'r') as f: # CAMBIAR
            contenido = f.read()
            print(contenido)
#--------------------------------------------FUNCION GUARDAR DATOS DE DEPOSITO COLONES---------------------------------------------------------------------------------

def crearCarpetas1 (): #Esta funcion crea todas las carpetas anidadas para cada usuario con sus jerarquias
     ruta_carpeta = "C:/Users/danin/workspace/Proyecto/" + cedula + "/Servicios/"
    
     os.makedirs(ruta_carpeta)
     os.makedirs("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/")
     
     #file = open("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/saldos.txt","a")

     file = open("C:/Users/danin/workspace/Proyecto/" +  cedula + "/Saldos/saldos.txt","a")
     file.write("colones")
     file.write("\n")
     file.write(str(deposito))
     file.write("\n")
     file.write("dolares")
     file.write("\n")
     file.write("0")
     file.write("\n")
     file.write("bitcoin")
     file.write("\n")
     file.write("0")
     file.close()            
#--------------------------------------------FUNCION GUARDAR DATOS DE DEPOSITO DOLARES---------------------------------------------------------------------------------


def crearCarpetas2 (): #Esta funcion crea todas las carpetas anidadas para cada usuario con sus jerarquias
     ruta_carpeta = "C:/Users/danin/workspace/Proyecto/" + cedula + "/Servicios/"
    
     os.makedirs(ruta_carpeta)
     os.makedirs("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/")
     
    # file = open("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/saldos.txt","a")

     file = open("C:/Users/danin/workspace/Proyecto/" +  cedula + "/Saldos/saldos.txt","a")
     file.write("colones")
     file.write("\n")
     file.write("0")
     file.write("\n")
     file.write("dolares")
     file.write("\n")
     file.write(str(depositoDollar))
     file.write("\n")
     file.write("bitcoin")
     file.write("\n")
     file.write("0")
     file.close()            
 #--------------------------------------------FUNCION GUARDAR DATOS DE DEPOSITO BICOINS---------------------------------------------------------------------------------     


def crearCarpetas3 (): #Esta funcion crea todas las carpetas anidadas para cada usuario con sus jerarquias
     ruta_carpeta = "C:/Users/danin/workspace/Proyecto/" + cedula + "/Servicios/"
    
     os.makedirs(ruta_carpeta)
     os.makedirs("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/")
     
     #file = open("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/saldos.txt","a")

     file = open("C:/Users/danin/workspace/Proyecto/" +  cedula + "/Saldos/saldos.txt","a")
     file.write("colones")
     file.write("\n")
     file.write("0")
     file.write("\n")
     file.write("dolares")
     file.write("\n")
     file.write("0")
     file.write("\n")
     file.write("bitcoin")
     file.write("\n")
     file.write(str(depositoBitcoin))
     file.close()            






#---------------------------------------------FUNCION CREAR LOS 7 ARCHIVOS POR USUARIO-----------------------------------------------------------------

def crearCarpetaServicios():
     archivos = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt']
     for archivo in archivos:
      ruta = os.path.join('C:/Users/danin/workspace/Proyecto/' +  cedula + '/Servicios/', archivo)
      with open(ruta, 'w') as f:
        f.write('')


#--------------------------------------------------------------------------------------------------------------
     file = open('C:/Users/danin/workspace/Proyecto/' +  cedula + '/Servicios/1.txt','a')
     file.write("Electricidad")
     file.write("\n")
     file.write("0")
     file.write("\n")
     file.write("60000")
     file.write("\n")
     
     file.close()
#--------------------------------------------------------------------------------------------------------------           
     file = open('C:/Users/danin/workspace/Proyecto/' +  cedula + '/Servicios/2.txt',"a")
     file.write("Agua")
     file.write("\n")
     file.write("0")
     file.write("\n")
     file.write("30000")
     file.write("\n")
    
     file.close()
#--------------------------------------------------------------------------------------------------------------

     file = open('C:/Users/danin/workspace/Proyecto/' +  cedula + '/Servicios/3.txt',"a")
     file.write("Telefonia")
     file.write("\n")
     file.write("0")
     file.write("\n")
     file.write("12000")
     file.write("\n")
    
     file.close()
#--------------------------------------------------------------------------------------------------------------
     file = open('C:/Users/danin/workspace/Proyecto/' +  cedula + '/Servicios/4.txt',"a")
     file.write("Internet")
     file.write("\n")
     file.write("0")
     file.write("\n")
     file.write("18000")
     file.write("\n")
    
#--------------------------------------------------------------------------------------------------------------
     file = open('C:/Users/danin/workspace/Proyecto/' +  cedula + '/Servicios/5.txt',"a")
     file.write("Impuestos")
     file.write("\n")
     file.write("0")
     file.write("\n")
     file.write("46000")
     file.write("\n")
    
     file.close()
#--------------------------------------------------------------------------------------------------------------
     file = open('C:/Users/danin/workspace/Proyecto/' +  cedula + '/Servicios/6.txt',"a")
     file.write("Colegios Profesionales")
     file.write("\n")
     file.write("0")
     file.write("\n")
     file.write("57000")
     file.write("\n")
    
     file.close()
#--------------------------------------------------------------------------------------------------------------
     file = open('C:/Users/danin/workspace/Proyecto/' +  cedula + '/Servicios/7.txt',"a")
     file.write("Tarjeta de credito")
     file.write("\n")
     file.write("0")
     file.write("\n")
     file.write("100000")
     file.write("\n")
    
     file.close()
                    
#--------------------------------------------------------------------------------------------------------------
     
def mostrarDatos():
    try:
         file = open("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/saldos.txt","r")
         saldos = file.read()
         file.close()
         print(saldos)
    except IOError:
        print("El archivo no existe")



#--------------------------------------------------------------------------------------------------------------                         
def subMenuDeposito():
    print("1. Colones")
    print("2. Dólares")
    print("3. Bitcoin")
#------------------------------------------------------FUNCIONES PARA USUARIO REGISTADO---------------------------------------------------------------------------------------------------------------  

#-----------------------------------------------------SUB MENÚ USUARIOS REGISTRADOS----------------------------------------------------------------------

#-----------------------------------------------------FUNCION RETIRAR DINERO-----------------------------------------------------------------------------------

def retirarDinero():
    # Abrir archivo de saldos
    ruta_archivo = "C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/saldos.txt"
    with open(ruta_archivo, "r") as f:
        saldos = f.readlines()    # Investigar
        #codigo para modificar archivos
        saldoColones = float(saldos[1])
        saldoDolares = float(saldos[3])
        saldoBitcoin = float(saldos[5])
    
    # Pedir al usuario que seleccione la cuenta
    print("Cuentas disponibles:")
    print("1. Colones")
    print("2. Dólares")
    print("3. Bitcoin")
    opcionCuenta = int(input("¿De qué cuenta desea retirar dinero?\n "))
    
    # Pedir al usuario que ingrese el monto a retirar
    intentos = 3
    while intentos > 0:
        montoRetiro = float(input("Ingrese el monto que desea retirar:\n "))
        if opcionCuenta == 1 and montoRetiro > saldoColones:
            print("Error: El monto ingresado es mayor que el saldo actual de la cuenta.")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")
        elif opcionCuenta == 2 and montoRetiro > saldoDolares:
            print("Error: El monto ingresado es mayor que el saldo actual de la cuenta.")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")
        elif opcionCuenta == 3 and montoRetiro > saldoBitcoin:
            print("Error: El monto ingresado es mayor que el saldo actual de la cuenta.")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")
        else:
            break
    
    # Si se agotaron los intentos, mostrar mensaje de error
    if intentos == 0:
        print("No se pudo realizar el retiro.")
        return 
    
    # Actualizar saldo de la cuenta seleccionada
    if opcionCuenta == 1:
        saldoColones -= montoRetiro
    elif opcionCuenta == 2:
        saldoDolares -= montoRetiro
    elif opcionCuenta == 3:
        saldoBitcoin -= montoRetiro
    
    # Actualizar saldo en el archivo
    with open(ruta_archivo, "w") as f:
     f.write("colones\n")
     f.write(str(saldoColones)  +"\n")
     f.write("dolares\n")
     f.write(str(saldoDolares) + "\n")
     f.write("bitcoin\n")
     f.write(str(saldoBitcoin) + "\n")
#-----------------------------------------------------FUNCION DEPOSITAR DINERO----------------------------------------------------------------------
def depositarDinero():
     # Abrir archivo de saldos
    ruta_archivo = "C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/saldos.txt"
    with open(ruta_archivo, "r") as f:
        saldos = f.readlines()    # Investigar
        #codigo para modificar archivos
        saldoColones = float(saldos[1])
        saldoDolares = float(saldos[3])
        saldoBitcoin = float(saldos[5])
    
    # Pedir al usuario que seleccione la cuenta
    print("Cuentas disponibles:")
    print("1. Colones")
    print("2. Dólares")
    print("3. Bitcoin")
    opcionCuenta = int(input("¿De qué cuenta desea retirar dinero?\n "))
    
    # Pedir al usuario que ingrese el monto a retirar
    intentos = 3
    while intentos > 0:
        montoRetiro = float(input("Ingrese el monto que desea retirar:\n "))
        if opcionCuenta == 1 and montoRetiro > saldoColones:
            print("Error: El monto ingresado es mayor que el saldo actual de la cuenta.")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")
        elif opcionCuenta == 2 and montoRetiro > saldoDolares:
            print("Error: El monto ingresado es mayor que el saldo actual de la cuenta.")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")
        elif opcionCuenta == 3 and montoRetiro > saldoBitcoin:
            print("Error: El monto ingresado es mayor que el saldo actual de la cuenta.")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")
        else:
            break
    
    # Si se agotaron los intentos, mostrar mensaje de error
    if intentos == 0:
        print("No se pudo realizar el retiro.")
        return 
    
    # Actualizar saldo de la cuenta seleccionada
    if opcionCuenta == 1:
        saldoColones += montoRetiro
    elif opcionCuenta == 2:
        saldoDolares += montoRetiro
    elif opcionCuenta == 3:
        saldoBitcoin += montoRetiro
    
    # Actualizar saldo en el archivo
    with open(ruta_archivo, "w") as f:
     f.write("colones\n")
     f.write(str(saldoColones)  +"\n")
     f.write("dolares\n")
     f.write(str(saldoDolares) + "\n")
     f.write("bitcoin\n")
     f.write(str(saldoBitcoin) + "\n")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

























































































































































#------------------------------------------------------FUNCION PARA ELIMINAR EL USUARIO-----------------------------------------------------------------------------------------------------------

def eliminarCarpeta():
 carpetaCedula = input("Ingrese su numero de cedula para eliminar sus datos personales:\n") # Se pide numero de cedula para borrar la carpeta con el numero de cedula del usuario
 rutaCarpeta = "Proyecto\\" + carpetaCedula  #Aqui se empezo a implementar las rutas relativas sustituyendo las absolutas barra invertida para windows
 if os.path.isdir(rutaCarpeta):       #Aca con este codigo se comprueba si la ruta es una carpeta
     shutil.rmtree(rutaCarpeta)      # Esta orden se usa eliminar carpetas en ubicaciones ramificadas 
     print("Datos del usuario con la cedula {} eliminado ".format(carpetaCedula))
 else:
     print("El usuario con la cedula {} no existe".format(carpetaCedula))





#----------------------------------------SUB MENÚ USUARIOS REGISTRADOS----------------------------------------------------------------------
#Submenú para el apartado de usuario registrado 
def submenúUsuarioRegistrado ():
     print("Submenú:")
     print("1. Retirar dinero")
     print("2. Depositar dinero")
     print("3. Ver saldo actual")
     print("4. Pagar servicios")
     print("5. Compra/Venta de Divisas")
     print("6. Eliminar usuario")
     print("7. Salir")
#------------------------------------------------fUNCION PARA QUE FUNCIONE EL SUBMENÚ------------------------------------------------------------------------------------------------------------------
def usuariosRegistradosMenu():

    while True:
     opcion = input("Presione enter para ingresar\n")
     print("Bienvenido al cajero automático")
     submenúUsuarioRegistrado()
     opciónElegida = int(input("Digite la opción que desea realizar\n"))
     if opciónElegida == 1:
            retirarDinero()
            print(" Retirar dinero")
        
           
         
     elif opciónElegida == 2:
         depositarDinero()
         print(" Depositar dinero")
        


     elif opciónElegida == 3:

         print("Ver saldo actual")

     elif opciónElegida == 4:
        print(" Pagar servicios")

        
    
     elif opciónElegida == 5:
         print("Compra/Venta de Divisas")

     elif opciónElegida == 6:
        print(" Eliminar usuario")
        eliminarCarpeta()

     
     elif opciónElegida == 7 :
        print("Salir")
        print("Gracias por usar el programa")
        break
     
     else:
         print("Ingrese otro valor")



















#--------------------------------------------------------------------------------------------------------------    



# Estas son las 3 funciones principales del menú

#-----------------------------------FUNCION PRINCIPAL DE PRIMER OPCION REGISTRAR USUARIO VERIFICAR ALMENOS 1 USUARIO REGISTRADO---------------------------------------------------------------------------
def agregarDatosUsuariosArreglo():

    try:  # manejo de errores
         archivo = open("proyecto/usuarios_pines.txt", "r")  # se abre el archivo
         contenido = archivo.read()  # se lee el contenido del archivo
         usuariosRegistrados.append(contenido)  # se agrega el contenido del archivo al arreglo
         
          # se cierra el archivo
         
    except FileNotFoundError: # manejo de errores por si el archivo no existe
        print("no hay usuarios registrados")

  
#--------------------------------------------------------FUNCIONES USUARIO REGISTRADO VERIFICAR CEDULA--------------------------------------------------------------------------    

def vericarRegistroCedula():
    intentos = 3
    global cedula
    try:
    
     with open("proyecto/usuarios_pines.txt", "r") as file:
           usuariosRegistrados = file.read().splitlines()
    except FileNotFoundError:
        print("Error la cedula no se encuentra registrada")
        return False

    while intentos > 0:
          cedula = input("Ingrese su número de cédula registrado (9 dígitos):\n ")
          if len(cedula) != 9:
             
             print("Error: La cédula debe contener 9 dígitos.")
             intentos -= 1
             print("Le quedan {} intentos restantes".format(intentos))
             
          elif cedula in usuariosRegistrados:
               print("Su cedula se encuentra registrada continue con el proceso")
               
               return True
               
               
               
               
             

          else:
              intentos -= 1
              print("Su cedula no está registrada Le quedan {} intentos restantes".format(intentos))
              
                  
        
   
    print("No tienes más intentos volviendo al menu principal")
    return False
        
#--------------------------------------------------FUNCION USUARIOS REGISTRADOS VERIFICAR PIN-----------------------------------------------------------------------------------------------
def verificarPin():
    intentos = 3
    try:
    
     with open("proyecto/usuarios_pines.txt", "r") as file:
           usuariosRegistrados = file.read().splitlines()
    except FileNotFoundError:
        print("Error el pin no  se encuentra registrada")
       # return

    while intentos > 0:
          pin = getpass.getpass("Ingrese su PIN (4 digitos):\n")
          if len(pin) != 4:
             
             print("Error: El pin debe contener 4 dígitos.")
             intentos -= 1
             print("Le quedan {} intentos restantes".format(intentos))
             
          elif pin in usuariosRegistrados:
               #print("Bienvenido{}".format(nombre))
              
              
               return
               
               
             

          else:
              intentos -= 1
              print("Su pin no está registrada Le quedan {} intentos restantes".format(intentos))
            #return pin
              
                  
        
   
    print("Se excedio el maximo de intentos para ingresar su pin  volviendo al menú principal")
 

#--------------------------------------------------------FUNCIONES USUARIO REGISTRADO--------------------------------------------------------------------------    


     


'''def registrarUsuario():
     
   
     cedula = solicitudCedula()
     if not cedula:
        return
     else:
        with open("proyecto/usuarios_pines.txt", "r") as file:
            cedulas_registradas = file.read().splitlines()
            if cedula in cedulas_registradas:
                print("Error: La cédula ya ha sido registrada")
                return # cambiar continue por return
            else:
                with open("proyecto/usuarios_pines.txt", "a") as file:
                    file.write(cedula)
                    file.write("\n")
                    print("Cédula registrada correctamente")
                    
        print("Usuario registrado exitosamente")

#input("Presione enter para ingresar al menú principal\n") def registrarUsuario():
     
 
     cedula = solicitudCedula()
     if not cedula:
        return
     else:
        with open("proyecto/usuarios_pines.txt", "r") as file:
            cedulas_registradas = file.read().splitlines()
            if cedula in cedulas_registradas:
                print("Error: La cédula ya ha sido registrada")
                return # cambiar continue por return
            else:
                with open("proyecto/usuarios_pines.txt", "a") as file:
                    file.write(cedula)
                    file.write("\n")
                    print("Cédula registrada correctamente")
                    
        print("Usuario registrado exitosamente")

#input("Presione enter para ingresar al menú principal\n")

  




#----------------------------------------------------------------------------------------------------------------------------------


def mostrarInfoUusarios():
     
    try:
         file = open("C:/Users/danin/workspace/Proyecto/usuarios_pines.txt","r")
         usuarios = file.read()
         file.close()
         print(usuarios)
    except FileNotFoundError:
 
        print("El archivo no existe")
 '''
#------------------------------------------FUNCION VERIFICAR QUE HAY ALMENOS 1 USUARIO REGISTRADO----------------------------------------------------------------------------------------
def VerificarDatosArreglo():
        
  if len(usuariosRegistrados) > 0:
    print("La lista tiene al menos un dato.")
  else:
    print("La lista está vacía.")



#----------------------------------------------FUNCIONES PARA VERIFICAR USUARIO REGISTRADO---------------------------------------------------------------------------
#FUNCION PARA VERIFICAR CEDULA
'''
def vericarRegistroCedula():
    try:
     
       intentos = 3
     
       with open("proyecto/usuarios_pines.txt", "r") as file:
           usuariosRegistrados = file.read().splitlines()

       while intentos > 0:
          
          cedula = input("Ingrese su número de cédula (9 dígitos):\n ")
          if len(cedula) != 9:
             
             print("Error: La cédula debe contener 9 dígitos.")
             intentos -= 1
             print("Le quedan {} intentos restantes".format(intentos))
          elif intentos == 0:
                 
                 print("No tienes más intentos volviendo al menú principal")
                 return False
          elif cedula in usuariosRegistrados:
             
             print("pin")
            
            
          elif intentos == 0:
                 
                 print("No tienes más intentos volviendo al menú principal")
                 return False
          else:
             
             return cedula
        
    except FileNotFoundError: # manejo de errores por si el archivo no existe
         print("no hay usuarios registrados")

'''

#-------------------------------------------------------------------------------------------------------------------------------------------------        

 #---------------------------------------------------------------IMPRIMIR ARREGLO USUARIOS-------------------------------------------------------------------------------  

def imprimirArregloUsuarios():
    print("Bienvenido usuario x")
    print(usuariosRegistrados)
    print("Estos son sus datos")
    imprimirSaldos()
   
    
    
#--------------------------------------------------------------------
def imprimirSaldos():
    try:
         file = open("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/saldos.txt","r")
         saldos = file.read()
         file.close()
         print(saldos)

         
    except IOError:
        print("El archivo no existe")

#------------------------------------------------------------------------------------------------------------------------------------------------------

def imprimitrServiciosRamdom():
    carpeta_principal = 'C:/Users/danin/workspace/Proyecto/' +  cedula + '/Servicios'

# Recorre el árbol de directorios y agrega los archivos a la lista   EXPLICAR
    for raiz, dirs, archivos in os.walk(carpeta_principal): #EXPLICAR
        for archivo in archivos: #CAMBIAR
            # Asegura que el archivo tenga la extensión .txt EXPLICAR
            if archivo.endswith('.txt'): #EXPLICAR
                listaArchivos.append(os.path.join(raiz, archivo)) #EXPLICAR

    # Selecciona 3 archivos aleatorios de la lista
    archivos_seleccionados = random.sample(listaArchivos, 3) #EXPLICAR

    # Lee el contenido de cada archivo seleccionado
    for archivo in archivos_seleccionados: #EXPLICAR
        with open(archivo, 'r') as f: # CAMBIAR
            contenido = f.read()
            print(contenido)




#-----------------------------------------FUNCION PRINCIPAL USUARIO REGISTRADO---------------------------------------------------------------------
def usuarioRegistrado():
    agregarDatosUsuariosArreglo()
    vericarRegistroCedula()
    verificarPin()
    imprimirArregloUsuarios()
    imprimitrServiciosRamdom()
    usuariosRegistradosMenu()
    

    pass
  

     
'''  
    while True:
          pin = getpass.getpass("Ingrese su PIN (4 digitos):\n") # Se utiliza funcion getpass para que el pin no sea visible en la terminal
          if len(pin) != 4:   # con if y len se le dice al usuario que si el pin no es de 4 digitos debe intentarlo nuevamente
           print("El pin debe ser de 4 digitos intente nuevamente")
          else:
               pin_confirmacion = getpass.getpass("Ingrese su PIN nuevamente para confirmar:\n") # Se crea una variable getpass para solicitar el pin nuevamente 
               if pin == pin_confirmacion: # Si el pin es igual al primero ingresado se continua con el programa (auntentificación)
                    with open("proyecto/usuarios_pines.txt","a") as archivo: # Whit sirve para que los archivos se cierren despues de usarse
                     archivo.write( pin)
                     archivo.write("\n")
                     
                     print("Su pin ha sido registrado correctamente:\n")
                     return pin
               
               else:
                    print("Los pin no coinciden intentelo nuevamente")
   
     

'''
#-----------------------------------------------FUNCION PRINCIPAL CONFIGURACION AVANZADA-------------------------------------------------------------------

def generarCodigoRandom():  # Funcion para generar un pin aleatorio que se le asignara a el usuario para la funcionc configuracion avanzada
    
  

  caracteres = string.ascii_letters + string.digits # Generar una cadena de caracteres aleatoria que contenga letras y números
  pin = ' '.join(random.sample(caracteres, 5))

  with open("proyecto/usuarios_pines.txt", "a") as file:# Guardar el PIN generado en un archivo txt
    file.write(f' {pin}\n') # Otra manera de imprimir 
    file.write("\n")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

def verificarPinUsuarioAvanzado():
    
    try:
    
     with open("proyecto/usuarios_pines.txt", "r") as file:
           usuariosRegistrados = file.read().splitlines()
    except FileNotFoundError:
          print("Error el pin no  se encuentra registrado")
       # return
    pinEspecial = getpass.getpass("Ingrese su PIN Avanzado de 5 digitos:\n")
    if len(pinEspecial) != 5:
             print("Error: El pin debe contener 5 dígitos.")
             
    elif pinEspecial in usuariosRegistrados:
      print("Sigue con el programa")
     #print("Bienvenido{}".format(nombre))
      return










#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def configuraciónAvanzada():
     verificarPinUsuarioAvanzado()
     retirarDinero()
     
     
    
     
     
     pass
 #-------------------------------------FUNCION DE MENU PRINCIPAL-------------------------------------------------------------------  

#Funcion para mostrar el menú
def mostrar_menu_Principal():
    print("1. Registrar nuevo usuario")
    print("2. Usuario registrado")
    print("3. Configuración avanzada")
    print("4. Salir")



  
#DEFINIR ARREGLOS
global listaArchivos
listaArchivos = []
usuariosRegistrados = []

#PROGRAMA PRINCIPAL
registrado = False #EXPLICAR
global opcion
while True:
    opcion = input("Presione enter para ingresar\n")
    print("Bienvenido al cajero automático")
    mostrar_menu_Principal()
    opciónElegida = int(input("Digite la opción que desea realizar\n"))
    if opciónElegida == 1:
        if solicitudCedula():
           
           
            registrado = True
        else:
             continue
             
    elif opciónElegida == 2:
        usuarioRegistrado()

        
    
    elif opciónElegida == 3:
        configuraciónAvanzada()
        
        pass

      

         

    elif opciónElegida == 4 :
        print("Gracias por usar el programa")
        break
    else:
         print("Ingrese otro valor")
    






