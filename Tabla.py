
Numero = input("Dame un numero del 1 al 9: ")
Numero = int(Numero)
#for ejecutara el bloque de codigo n veces con un rango de valores
#en range el ultimo numero no se utiliza
for i in range(1,11):
    salida="{} x {} = {}"
    print(salida.format(Numero,i,i*Numero))
