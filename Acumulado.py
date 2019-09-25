#Declamramos las variables explictamente
acumulado = int(0)
numero = str("")
#cuando usas true como condicion de while se hace un ciclo infinito
#hasta que no se use break
while True:
    numero = input("Dame un numero entero:")
    if numero == "":
        #si numero es vacio lo dice y sale del ciclo
        print("Vacio. Salida del programa.")
        break
    else:
        #si si hay,se hace calculo usando suma incluyente
        acumulado +=int(numero)
        salida = "Monto acumulado: {}"
        print(salida.format(acumulado))
