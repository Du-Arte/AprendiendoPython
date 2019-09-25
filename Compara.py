
Numero1 = input("Dime un numero:")
Numero2 = input("Dime otro:")
salida="Numeros proporcionados: {} y {}. {}."

if (Numero1 == Numero2):
    #checa si los numeros son iguales
    print(salida.format(Numero1, Numero2, "Los numeros son iguales"))
else:
    #if dentro de otro, checa si los numeros no son iguales
    if Numero1>Numero2:
        #dice si 1 es mayor a 2
        print(salida.format(Numero1, Numero2, "El mayor es el primero"))
    else:
        #dice que si no es asi, entonces 2 es mayor a 1
        print(salida.format(Numero1, Numero2, "El mayor es el segundo"))
        
