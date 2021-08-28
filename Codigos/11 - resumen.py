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


##------------------Estructuras y Variables Globales------------------##

#Estructuras
#() [] {} -> {}

cuentas = {}



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

    elif (opcion_principal == 2):
        print("\nMenu Cajero Automático")

    elif (opcion_principal == 3):
        print("\nVuelva pronto :)")
        break

    else:
        print(f"\nLa opción: {opcion_principal} no es valida. Por favor ingrese una opción entre [1-3]")
