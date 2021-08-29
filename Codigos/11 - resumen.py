#Creación de Cuentas
# -> nombre_cliente
# -> num_cuenta
# -> saldo_inicial
# -> tipo_de_cuenta
    #ahorro
    #monetaria

#Operaciones del cajera automatico
#Solicitud de salo
#Realizar transacciones
    #Realizar transacciones a terceros
    #Realizar transacciones a cuentas propias
#realizar Retiros
#realizar deposito
    #Depositos a terceros
    #Depositos a cuentas propias

#Manejo de Excepciones
#try - except 
# 'try' ':'
# '   ' bloque_código
# 'except' [clase] ':'
# '   ' bloque_código   

#Importaciones de librerias
# 'import' nombre_librería o paquete
# 'from' nombre_librería o paquete 'import' nombre_metodo o clase
from datetime import datetime

##------------------Estructuras y Variables Globales------------------##

#Estructuras
#() [] {} -> {}

cuentas = {}

# Variables globales

nombre_cliente = ""
saldo_inicial = 0



#Inicio del Programa

print("Bienvenido al Banco Patitaspaquelasquier, S.A.");

while (True):
    
    print("\nMENÚ PRINCIPAL\n\n1. Crear Cuenta\n2. Cajero Automático\n3. Salir")
    
    try:
        opcion_principal = int(input("\nEscoja una opción: "))
    except:
        print(f"\nLa opción no es un número")
        continue

    if (opcion_principal == 1):
        print("\nCreación de Cuentas")

        while (True):
                
            print("\nTIPOS DE CUENTA\n\n1. Monetaria\n2. Ahorro\n3. Volver al menu principal")
            try:
                tipo_cuenta = int(input("\nIngrese el tipo de cuenta a crear: "))
            except:
                print(f"\nLa opción no es un número")
                continue

            if (tipo_cuenta == 1):
                nombre_cliente = input("\nPor favor, ingrese su nombre: ")

                while(True):
                    try:
                        saldo_inicial = float(input(f"\n{nombre_cliente} por favor, ingrese su saldo inicial"))
                    except:
                        print(f"\nEl Saldo debé ser un número")
                        continue

                    if (saldo_inicial < 100):
                        print(f"\n{nombre_cliente} el saldo ingresado no es valido, deber ser mayor o igual a $100.00")
                        continue

                    num_cuenta = str(datetime.now()).split(' ')[0] + str(nombre_cliente[0]) + str(nombre_cliente[-1])

                    cuentas[num_cuenta] = {'num_cuenta': num_cuenta, 'nombre': nombre_cliente, 'saldo': saldo_inicial, 'tipo_cuenta': 1}
                    break

            elif (tipo_cuenta == 2):
                nombre_cliente = input("\nPor favor, ingrese su nombre: ")

                while(True):
                    try:
                        saldo_inicial = float(input(f"\n{nombre_cliente} por favor, ingrese su saldo inicial"))
                    except:
                        print(f"\nEl Saldo debé ser un número")
                        continue

                    if (saldo_inicial < 50):
                        print(f"\n{nombre_cliente} el saldo ingresado no es valido, deber ser mayor o igual a $50.00")
                        continue

                    num_cuenta = str(datetime.now()).split(' ')[0] + str(nombre_cliente[0]) + str(nombre_cliente[-1])

                    cuentas[num_cuenta] = {'num_cuenta': num_cuenta, 'nombre': nombre_cliente, 'saldo': saldo_inicial, 'tipo_cuenta': 2}
                    break
        
            elif (tipo_cuenta == 3):
                break

            else:
                print(f"\nLa opción: {tipo_cuenta} no es valida. Por favor ingrese una opción entre [1-3]")

    elif (opcion_principal == 2):
        print("\nMenu Cajero Automático")

    elif (opcion_principal == 3):
        print("\nVuelva pronto :)")
        break

    else:
        print(f"\nLa opción: {opcion_principal} no es valida. Por favor ingrese una opción entre [1-3]")
