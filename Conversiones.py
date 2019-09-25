# Declaramos una variable str
Numero = "2001"
#Mostramos el tipo de la variable
print(type(Numero))
#Numero pasa a ser de tipo int
Numero = int(Numero)
print(type(Numero))
#Declaramos un str con una sustitucion donde iran valores del format
salida = "El numero utilizado es {}"
#Mostramos el resultado
print(salida.format(Numero))