#funciones prueba
import numpy
arreglo_salas=numpy.zeros((2,5),int)
lista_ruts=[]
lista_nom_dueño=[]
lista_nom_mascota=[]
lista_identificador=[]
lista_dias=[]
num_verificador=1
import os
import time
import msvcrt

def validar_nombre_dueño():
    while True:
        nom = input("Ingrese su nombre: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")

def validar_nombre_mascota():
    while True:
        nom = input("Ingrese nombre de su mascota: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")

def validar_rut():
    while True:
        try:
            rut2 = int(input("Ingrese rut: "))
            if rut2 >= 1000000 and rut2 <= 99999999:
                return rut2
            else:
                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_cant_dias():
      while True:
            try:
                cant_dias=int(input("cuantos dias alojara la mascota?: "))
                if cant_dias>=0 :
                    return cant_dias
                else:
                    print("error,no ha registrado dias")
                    time.sleep(3)
            except:
                print("error, ingrese un numero positivo")         

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")

def grabar():
    rut=validar_rut()
    nombre_dueño=validar_nombre_dueño()
    identificador=1
    if rut  is not lista_ruts:
        identificador+=1
    nombre_mascota=validar_nombre_mascota()
    dias=validar_cant_dias()
    print("su numero verificador es",num_verificador)
    for x in range(2):
        for y in range(5):
            print(arreglo_salas[x][y], end=" ")
        print()
    print("salas disponibles")
    fila=int(input("ingrese una fila"))
    columna=int(input("ingrese una columna")) 
    arreglo_salas[fila][columna]==1
    
    lista_ruts.append(rut)
    lista_nom_dueño.append(nombre_dueño)
    lista_nom_mascota.append(nombre_mascota)
    lista_identificador.append(identificador)
    lista_dias.append(dias)
    print("registrado con exito")
    time.sleep(3)
    os.system('cls')

def buscar():
    rut=validar_rut()
    if rut in lista_ruts:
        for x in lista_nom_mascota:
            print(x) 

def pagar():
    rut3=validar_rut()
    if rut3 in lista_ruts:
        for x in lista_dias:
            print("monto a pagar",x*15000)
            return x
    print(x)
    lista_nom_mascota.pop(x)
    lista_dias.pop(x)
    lista_identificador.pop(x)
    lista_nom_dueño.pop(x)
    lista_ruts.pop(x)    
def salir():
    print("gracias que tenga un buen dia")
    