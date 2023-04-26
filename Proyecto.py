#ENCABEZADO
#DEFINIR BIBLIOTECAS
import os      #Vista en clase Manejo de archivos
import getpass # Sirve para que el codigo no sea visible en la terminal
import random  #Esta biblioteca sirve para elegir datos,listas,datos de arreglos aleatoreamente  #Elegir de  3 de 7 servicios #Generar contraseña aleatoriamente de configuracion avanzada
import shutil # Esta biblioteca sirve para manejo de archivos es similar a Os   #Eliminar carpetas completas de usuarios
import string # Se usa para generar contraseñas con los caracteres que contiene Está biblioteca contiene cadenas de caracteres como letras minusculas y mayusculas numeros etc
              #Generar contraseña aleatoriamente de configuracion avanzada
#import json  # Investigar más 
#import requests # INVESTIGAR


#DEFINIR FUNCIONES


#----------------------------------------FUNCION SUBPRINCIPAL SOLICITAR CEDULA DE OPCION PRINCIPAL REGISTRAR USUARIOS----------------------------------------------------------------------

      
def solicitudCedula(): # Funcion para solicitar el número de cedula al usuario para su posterior registro                                       
    global cedula  # Global sirve para hacer global la variable y poder llamarla desde otras funciones     
    global cedulas_registradas
    intentos = 3       # Se establece que deben de ser 3 intentos para ingresar la cedula correcamente
    file = open("proyecto/usuarios_pines.txt", "a") # Se abre ell archivo para crearlo y que no de errores más adelante
    generarCodigoRandom()  # Generar contraseña random
    
    while intentos > 0:  # mientras que los intentos sean mayores a 0 sigue el programa
        cedula = input("Ingrese su número de cédula (9 dígitos):\n ") # se pide al usuario ingresar el numero de cedula especificando que deben de ser (9 digitos)
        if len(cedula) != 9:  # Si es diferente de 9 tira error
            print("El número de cédula debe ser de (9 dígitos)")
            intentos -= 1 # Se resta un intento a la variable intentos
            
            if intentos == 0:
                print("No tienes más intentos volviendo al menú principal")
                return False
            print("Le quedan {} intentos restantes".format(intentos))# Se imprime un mensaje con la cantidad de intentos restantes utilizando el format (USAR ESTO EN LOS DEMAS)
            continue   
        with open("proyecto/usuarios_pines.txt", "r") as file:  # Se usa para no cerrar el archivo 
            cedulasRegistradas = file.read().splitlines()   #Leer linea por linea del archivo
            if cedula in cedulasRegistradas:
                print("Error: La cédula ya ha sido registrada")
                intentos -= 1
                print("Le quedan {} intentos restantes".format(intentos))
                if intentos == 0:
                    print("No tienes más intentos volviendo al menú principal")
                    return False 
                
                continue
        with open("proyecto/usuarios_pines.txt", "a") as file:
            file.write(cedula)
            file.write("\n")  # Mejorar visualmente el archivo para que se vea abajo
          
            
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

                    
#-----------------------------------------------------------SUB MENÚ DEPOSITO-----------------------------------------------------------------------------------------   
def subMenuDeposito():
    print("1. Colones")
    print("2. Dólares")
    print("3. Bitcoin")


#----------------------------------------FUNCION SUBPRINCIPAL DEPOSITO OBLIGATORIO DE OPCION PRINCIPAL REGISTRAR USUARIOS----------------------------------------------------------------------


def depositoObligatorio():   #Funcion para efectuar el deposito obligatorio  de 100 000 colones para poder ser registrado correctamente
     print("A que cuenta (colones, dólares o bitcoin) desea hacer el deposito obligatorio debe ser de minimo 100000 colones")
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
                      print(f"Intentos restantes: {intentos}") # Otra forma de imprimir
                  else:
                       crearCarpetas1 ()# crear carpetas anidadas
                       crearCarpetaServicios()# crear carpetas
                      # randomAcces() # modificar o dejar asi
                       print("Depósito ingresado correctamente.")
                       return deposito
                      
                       
                       
              except ValueError: # investigas
                  print("Error: Ingrese un número válido.")
                  intentos -= 1
                  print("Intentos restantes{}".format(intentos))
          else:
               print("No se pudo ingresar el depósito.")
             #  input("Presione enter para regresar al menú principal")


#---------------------------------------------------------------OPCION DEPOSITO DOLARES---------------------------------------------------------------------------------------   
    
     if opcionCuentas == 2:
                                                                           
        
         global depositoDollar
         
         intentos = 3
         while intentos > 0:
              tasaDeCambio = 540
              depositoDollar = int(input("Ingrese la cantidad del depósito:\n"))
              ConversionColones = depositoDollar * tasaDeCambio
              print(f"{depositoDollar} dólares equivale a {ConversionColones} colones.") #Otra manera de imprimir la F sirve para que las variables de adentro no se comenten y se imprima correctamente

        

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


#--------------------------------------------FUNCION GUARDAR DATOS DE DEPOSITO COLONES---------------------------------------------------------------------------------

def crearCarpetas1 (): #Esta funcion crea todas las carpetas anidadas para cada usuario con sus jerarquias
     ruta_carpeta = "C:/Users/danin/workspace/Proyecto/" + cedula + "/Servicios/"
    
     os.makedirs(ruta_carpeta) # Carpetas anidas
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

#rutaCarpeta = 'C:/Users/danin/workspace/Proyecto/' + cedula + '/Servicios/'

def crearCarpetaServicios():
   #  archivos = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt']
     for archivo in archivos:
      ruta = os.path.join('C:/Users/danin/workspace/Proyecto/'+cedula +'/Servicios/', archivo) # unir
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
                    
#-----------------------------------------------fUNCION-DE------PRUEBA---------------------------------------------------------------
     
def mostrarDatos():
    try:
         file = open("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/saldos.txt","r")
         saldos = file.read()
         file.close()
         print(saldos)
    except IOError:
        print("El archivo no existe")



                       

#------------------------------------------------------FUNCIONES PARA USUARIO REGISTADO---------------------------------------------------------------------------------------------------------------  


#-----------------------------------FUNCION PRINCIPAL DE PRIMER OPCION REGISTRAR USUARIO VERIFICAR ALMENOS 1 USUARIO REGISTRADO---------------------------------------------------------------------------

def VerificarDatosArreglo():
        
  if len(usuariosRegistrados) > 0:
    print("La lista tiene al menos un dato.")
  else:
    print("La lista está vacía.")



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
           usuariosRegistrados = file.read().splitlines() #funcion splitlines para leer archivo linea por linea
    except FileNotFoundError: #Manejo de errores por si el archivo no existe o el pin no esta registrado
        print("Error el pin no  se encuentra registrado")
       # return

    while intentos > 0:
          pin = getpass.getpass("Ingrese su PIN (4 digitos):\n") # getpass para que no se vea el usuario en la terminal
          if len(pin) != 4:
             
             print("Error: El pin debe contener (4 dígitos.)")
             intentos -= 1
             print("Le quedan {} intentos restantes".format(intentos))
             
          elif pin in usuariosRegistrados:
              # print("Bienvenido{}".format(nombre)) # no se logro
              
              
               return
               
               
             

          else:
              intentos -= 1
              print("Su pin no está registrado le quedan {} intentos restantes".format(intentos))
            #return pin
              
                  
        
   
    print("Se excedio el maximo de intentos para ingresar su pin  volviendo al menú principal")
 




#----------------------------------------------FUNCIONES PARA AGREGAR DATOS A ARREGLO---------------------------------------------------------------------------

def agregarDatosUsuariosArreglo():

    try:  # manejo de errores
         archivo = open("proyecto/usuarios_pines.txt", "r")  # se abre el archivo
         contenido = archivo.read()  # se lee el contenido del archivo
         usuariosRegistrados.append(contenido)  #appen se agrega el contenido del archivo al arreglo
         
          # se cierra el archivo
         
    except FileNotFoundError: # manejo de errores por si el archivo no existe
 
        print("no hay usuarios registrados")

 #---------------------------------------------------------------IMPRIMIR ARREGLO USUARIOS-------------------------------------------------------------------------------  

def imprimirArregloUsuarios():
   # print("Bienvenido{}".format(nombre))
    print("Bienvenido usuario () ")
    print(usuariosRegistrados) # Arreglar  para imprimir solo una parte del arreglo
    print("Estos son sus datos")
    imprimirSaldos()  #Imprimir  saldos de cada usuario
   

   
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



#--------------------------------------------------FUNCION RETIRAR DINERO-----------------------------------------------------------------------------------

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
    opcionCuenta = int(input("¿En qué cuenta desea retirar dinero?\n "))
    
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
    opcionCuenta = int(input("¿En qué cuenta desea depositar dinero?\n "))
    
    # Pedir al usuario que ingrese el monto a retirar
    intentos = 3
    while intentos > 0:
        montoRetiro = float(input("Ingrese el monto que desea depositar:\n "))
        if opcionCuenta == 1 and montoRetiro <0:
            print("Error: El monto ingresado debe ser positivo.")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")
        elif opcionCuenta == 2 and montoRetiro >0:
            print("Error: Error: El monto ingresado debe ser positivo.")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")
        elif opcionCuenta == 3 and montoRetiro >0:
            print("Error: Error: El monto ingresado debe ser positivo.")
            intentos -= 1
            print(f"Intentos restantes: {intentos}")
        else:
            break
    
    # Si se agotaron los intentos, mostrar mensaje de error
    if intentos == 0:
        print("No se pudo realizar el deposito.")
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



#------------------------------------------------------FUNCION VER SALDO ACTUAL----------------------------------------------------------------------------------------    
     
def saldoActual():
    try:
         file = open("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/saldos.txt","r")
         saldoActual = file.read()
         file.close()
         print(saldoActual)
    except IOError:
        print("El archivo no existe")




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
            print("Su retiro fue realizado  correctamente")
    
           
         
     elif opciónElegida == 2:
         depositarDinero()
         print(" Deposito ingresado correctamente")
        


     elif opciónElegida == 3:
         print("Su saldo actual es")
         saldoActual()
         

     elif opciónElegida == 4:  #Falta
          print("Escoja el servicio a pagar")
          menuServicios()
          funcionMenu()

          
         
       
         

        
    
     elif opciónElegida == 5:
         print("Compra/Venta de Divisas") #FALTA

     elif opciónElegida == 6:
                                     #DETALLES
        eliminarCarpeta()

     
     elif opciónElegida == 7 :
        print("Saliendo del cajero automatico")
        print("Gracias por usar nuestro programa")
        break
     
     else:
         print("Ingrese otro valor")

 


#-----------------------------------------------------FUNCION MENÚ DE SERVICIOS-----------------------------------------------------------------------------------------------------------------

def menuServicios():
     print("Menú servicios:")
     print("1. Electricidad")
     print("2. Agua ")
     print("3. Telefonía")
     print("4. Internet")
     print("5. Impuestos")
     print("6. Colegios Profesionales")
     print("7. Tarjeta de crédito")
     print("8. Salir")
 

#--------------------------------------------------------MENU SERVICIOS---------------------------------------------------------------------------------------------------------------------


def funcionMenu():

    while True:
     opcion = input("Presione enter para ingresar\n")
     print("Escoja el servicio que desea pagar")
     menuServicios()
     opciónElegida = int(input("Digite el servicio que desea pagar \n"))
     
     if opciónElegida == 1:
        print("Pagar Electricidad ")
        
     elif opciónElegida == 2:
       print("Pagar Agua ")
        

     elif opciónElegida == 3:
          print("Pagar Telefonía ")
       
    
     elif opciónElegida == 4: 
         
        print("Pagar Internet ")

    
     elif opciónElegida == 5:
       print("Pagar Impuestos ")

     elif opciónElegida == 6:
          print("Pagar Colegios Profesionales ")       


     elif opciónElegida == 7:
         print("Pagar Tarjeta de crédito ")
    

     elif opciónElegida == 8 :
        print("Saliendo del cajero automatico")
        print("Gracias por usar nuestro programa")
        break



#------------------------------------------------------FUNCION PARA ELIMINAR EL USUARIO-----------------------------------------------------------------------------------------------------------

def eliminarCarpeta():
 carpetaCedula = input("Ingrese su numero de cedula para eliminar sus datos personales:\n") # Se pide numero de cedula para borrar la carpeta con el numero de cedula del usuario
 rutaCarpeta = "Proyecto\\" + carpetaCedula  #Aqui se empezo a implementar las rutas relativas sustituyendo las absolutas barra invertida para windows
 if os.path.isdir(rutaCarpeta):       #Aca con este codigo se comprueba si la ruta es una carpeta
     shutil.rmtree(rutaCarpeta)      # Esta orden se usa eliminar carpetas en ubicaciones ramificadas 
     print("Datos del usuario con la cedula {} eliminado ".format(carpetaCedula))
 else:
     print("El usuario con la cedula {} no existe".format(carpetaCedula)) 

#-----------------------------------------FUNCION PRINCIPAL USUARIO REGISTRADO---------------------------------------------------------------------
def usuarioRegistrado():
    agregarDatosUsuariosArreglo()
    vericarRegistroCedula()
    verificarPin()
    imprimirArregloUsuarios()
    imprimitrServiciosRamdom()
    usuariosRegistradosMenu()
   
    

    pass



#-----------------------------------------FUNCION PRINCIPAL CONFIURACION AVANZADA ---------------------------------------------------------------------


# Estas son las 3 funciones principales del menú

def configuraciónAvanzada():
     verificarPinUsuarioAvanzado()



#--------------------------------------------------------FUNCION GENERAR CODIGO RANDOM --------------------------------------------------------------------------------------------------------

def generarCodigoRandom():  # Funcion para generar un pin aleatorio que se le asignara a el usuario para la funcionc configuracion avanzada
    
  

  caracteres = string.ascii_letters + string.digits # Generar una cadena de caracteres aleatoria que contenga letras y números
  pin = ' '.join(random.sample(caracteres, 5))

  with open("proyecto/usuarios_pines.txt", "a") as file:# Guardar el PIN generado en un archivo txt
    file.write(f' {pin}\n') # Otra manera de ingresar o escribir datos     

   
     


#-----------------------------------------------FUNCION PRINCIPAL CONFIGURACION AVANZADA-------------------------------------------------------------------


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






#------------------------------------------PRUEBA------------------------------------------



def mostrarServiciosMofidicados():
    
    global  cedula
    rutaCarpeta = 'C:/Users/danin/workspace/Proyecto/'+ cedula + 'Servicios/'
    #rutaCarpetaCompleta = rutaCarpeta + cedula + "/Servicios/"
    for archivo in os.listdir(rutaCarpeta): # Itera sobre todos los archivos en la carpeta
        if archivo.endswith(".txt"): # Verifica si el archivo es de texto
            ruta_completa = os.path.join(rutaCarpeta, archivo) # Obtiene la ruta completa del archivo
        
            with open(ruta_completa, "r+") as f: # Abre el archivo en modo lectura y escritura
                contenido = f.readlines() # Lee todas las líneas del archivo
                nueva_linea = contenido[1].strip() + contenido[0] # Modifica la línea que necesites
            
            # Coloca el cursor al inicio del archivo, escribe el contenido modificado y agrega un salto de línea
                f.seek(0)
                f.write(nueva_linea + "\n" + "".join(contenido[2:]))



 #-------------------------------------FUNCION DE MENU PRINCIPAL-------------------------------------------------------------------  

#Funcion para mostrar el menú
def mostrarMenuPrincipal():
    print("1. Registrar nuevo usuario")
    print("2. Usuario registrado")
    print("3. Configuración avanzada")
    print("4. Salir")


  
#DEFINIR ARREGLOS
global listaArchivos
listaArchivos = []
usuariosRegistrados = []
archivos = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt']

#PROGRAMA PRINCIPAL
registrado = False #EXPLICAR  
global opcion
while True:
    opcion = input("Presione enter para ingresar al menu principal \n")
    print("Bienvenido al cajero automático")
    mostrarMenuPrincipal()  # Cambiar
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
        
        pass # Es una estructura pasiva que sirve para detener posibles errores cuando una funcion o desicion esta vacia

      
    elif opciónElegida == 4 :
        print("Gracias por usar el programa")
        break
    else:
         print("Ingrese otro valor")
 






