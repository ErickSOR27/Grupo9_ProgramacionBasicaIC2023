#ENCABEZADO
#DEFINIR BIBLIOTECAS
import os
import getpass
import random
import json  # Investigar más 

#import requests # investigar más

#DEFINIR FUNCIONES


def solicitudCedula(): # Funcion para solicitar el número de cedula al usuario para su posterior registro                                       
    global cedula   # Global sirve para hacer global la variable y poder llamarla desde otras funciones     
    intentos = 3       # Se establece que deben de ser 3 intentos para ingresar la cedula correcamente
    file = open("proyecto/usuarios_pines.txt", "a") # Se abre ell archivo para crearlo y que no de errores más adelante
    
    while intentos > 0:  # mientras que los intentos sean mayores a 0 sigue el programa
        cedula = input("Ingrese su número de cédula (9 dígitos):\n ") # se pide al usuario ingresar el numero de cedula especificando que deben de ser (9 digitos)
        if len(cedula) != 9:
            print("El número de cédula debe ser de (9 dígitos)")
            intentos -= 1 # Se resta un intento a la variable intentos
            print("Le quedan {} intentos restantes".format(intentos))# Se imprime un mensaje con la cantidad de intentos restantes utilizando el format (USAR ESTO EN LOS DEMAS)
            continue
        with open("proyecto/usuarios_pines.txt", "r") as file:
            cedulas_registradas = file.read().splitlines()
            if cedula in cedulas_registradas:
                print("Error: La cédula ya ha sido registrada")
                intentos -= 1
                print("Le quedan {} intentos restantes".format(intentos))
                continue
        with open("proyecto/usuarios_pines.txt", "a") as file:
            file.write(cedula)
            file.write("\n")
            
        print("Cédula registrada correctamente")
        break
    else:
        print("No se pudo registrar la cédula")   
           


def solicitudNombre ():  #Funcion para la Solicitud del nombre del usuario y su posterior registro
    nombre = input("Ingrese su nombre completo:\n")
    with open("proyecto/usuarios_pines.txt","a") as archivo: # 
                    archivo.write(nombre) 
                    archivo.write("\n")
                    
                    print("Su nombre ha sido registrado correctamente")
                 #  return nombre


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
   
               
 
def depositoObligatorio():   #Funcion para efectuar el deposito obligatorio  de 100 000 colones para poder ser registrado correctamente
     print("A que cuenta (colones, dólares o bitcoin) desea hacer el deposito")
     subMenuDeposito=0
     
     opcionCuentas = int(input("A cual cuenta desea acreditar el deposito del dinero?\n"))
   
     if opcionCuentas == 1:
          global deposito
          intentos = 3
          while intentos > 0:
              deposito = input("Ingrese la cantidad del depósito:\n")
              try:
                  deposito = float(deposito)
                  if deposito < 100000:
                      print("Error: El depósito debe ser mayor a 100000.")
                      intentos -= 1
                      print(f"Intentos restantes: {intentos}") # Cambiar 
                  else:
                       crearCarpetas ()
                       crearCarpetaServicios()
                       
                       print("Depósito ingresado correctamente.")
                       
                       return deposito
              except ValueError:
                  print("Error: Ingrese un número válido.")
                  intentos -= 1
                  print("Intentos restantes: {intentos}")
          else:
               print("No se pudo ingresar el depósito.")
         
         
              
        
        

def crearCarpetas (): #Esta funcion crea todas las carpetas anidadas para cada usuario con sus jerarquias
     ruta_carpeta = "C:/Users/danin/workspace/Proyecto/" + cedula + "/Servicios/"
     ruta_carpeta = "C:/Users/danin/workspace/Proyecto/" + cedula + "/Servicios/"
     os.makedirs(ruta_carpeta)
     os.makedirs("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/")
     
     file = open("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/saldos.txt","a")

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

       
def crearCarpetaServicios():
     archivos = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt']
     for archivo in archivos:
      ruta = os.path.join('C:/Users/danin/workspace/Proyecto/' +  cedula + '/Servicios/', archivo)
      with open(ruta, 'w') as f:
        f.write('')
        file = open("C:/Users/danin/workspace/Proyecto/" +  cedula + "/Saldos/saldos.txt","a")
        file.write("colones")

    
                                    
                
def mostrarDatos():
    try:
         file = open("C:/Users/danin/workspace/Proyecto/" + cedula + "/Saldos/saldos.txt","r")
         saldos = file.read()
         file.close()
         print(saldos)
    except IOError:
        print("El archivo no existe")
                 

 #cedulaUsuario = input("Ingrese el numero de cedula:\n")
    #elif opcionCuentas == 2:
                                    
     #print("Eligio dólares")
      #elif opcionCuentas == 3:
       #print("Eligio bitcoin")  
    
        
    