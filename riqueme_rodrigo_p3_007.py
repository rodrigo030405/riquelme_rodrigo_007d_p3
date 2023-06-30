#prueba3
import funciones_prueba as fn
import numpy 
import msvcrt
import time
import os
os.system('cls')
salas=numpy.zeros((2,5),int)
while True:
    print("""bienvenido a mascota segura
    elija una opcion
    1. grabar datos(registrar)
    2. buscar 
    3. retirarse
    4. salir""")
    opcion=fn.validar_opcion()
    if opcion==1:
        fn.grabar()
        
    elif opcion==2:
        fn.buscar()
    elif opcion==3:
       fn.pagar() 
    elif opcion==4:
        fn.salir()
        break
    else:
        print("ingrese una opcion valida") 

