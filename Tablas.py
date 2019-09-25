for i in range(1,11):
    Titulo="Tabla del {}"
    print(Titulo.format(i))
#usamos for y else
    for j in range(1,11):
        #i es numero base y j el elemento de la tabla
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #al acabar saltamos de linea
        print()
        
