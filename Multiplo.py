numero=int(input("Dame un numero entero: "))
#almacenamos en valores booleanos el residual, si es cero
#entonces el numero es multiplo
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
#and cuando todo es verdadero, or si al menos una es verdadera
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")
