entrada = input()
print(type(entrada))
#Si es digito y si encuentra punto sera decimales osea float
#si es verdadero lo capturado es entero
esEntero = (entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    print("Dato entero. ¡Muy bien!")
else:
    print("Dato no es entero. ¡Muy bien")
