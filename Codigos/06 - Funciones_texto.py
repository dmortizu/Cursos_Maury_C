#Funciones para manipular cadenas de texto

#lower -> convierte la cadena a minúsculas
nombre = "Elian EStrada".lower()
print(nombre)

#upper -> convierte la cadena a mayúscula
nombre2 = "Saúl Urbina".upper()
print(nombre2)

#capitalize -> pone la primera letra de una palabra en mayúscula
print("hola mundo".capitalize())

#replace -> remplaza uno o unos caracteres de una cadea por otros
cadena = "Elian Diego Pablo Roger"

print(cadena.replace(' ', ','))

#format -> le da un formato de salida al texto
texto = "Listado de estudiantse: {}".format(cadena.replace(' ', ','))
print(texto)

#split -> Separa el texto según un caracter y devuelve una lista.
nombres = cadena.replace(' ', ',')
print(nombres)
lista_nombres = nombres.split(',')
print(lista_nombres[1])

#string-f -> sirve para interpolar variables en texto
texto_prueba = f"Mi nombre es: {lista_nombres[0]}"
print(texto_prueba)
