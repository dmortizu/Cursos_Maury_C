#Conversiones de tipos de datos

# Todo tipo de dato se puede convertir a string (str)
#-> str, int, float, bool

numero = 10
print(type(numero))

#numero = str(numero)
print(type(numero))

decimal = 10.234234234
print(type(decimal))

print(type(str(decimal)))

print("Mi edad es: ", numero)


#int a float

num_entero = 10
num_decimal = float(num_entero)

print(type(num_entero)) #-> int
print(type(num_decimal)) # -> float

print(num_entero, num_decimal) # -> 10 10.0

# float a int
num_decimal = 13.6
num_entero2 = int(num_decimal)
print(num_entero2)

# bool a int

boolean = False
num_bool = int(boolean)
print(boolean)
print(num_bool)

boolean = bool('hola')
print(boolean)