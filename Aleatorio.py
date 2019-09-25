#importamos un modulo
import random
#definimos una variable float con un valor
numero1=float(6.9)
#usamos una funcion
def miFuncion():
    #convertimos a float el numero random
    numero2=float(random.randrange(1,10))
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

#ejecutamos la funcion del codigo
miFuncion()
