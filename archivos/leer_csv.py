'''
import csv
                                            #with abre y cierra automaticamente el archivo
with open('C:\\Users\\salit\\OneDrive\\Desktop\\variables.csv', 'r', ) as csvfile:   #csvfile es el nombre que le ponemos a la variable
    lector = csv.reader(csvfile, delimiter = ";") #se utiliza el método reader
    print(lector)
    encabezado = next(lector)               #corta la primer linea y se guarda en la variable encabezado
    #print(encabezado)                       #muestra el encabezado
    presion = []
    print(encabezado[0])
    for fila in lector:          #con el for se itera sobre el objeto para leer
        dato = int(fila[0])
        presion.append(dato)

print(presion)      
'''


import csv
                                            #with abre y cierra automaticamente el archivo
with open('C:\\Users\\salit\\OneDrive\\Desktop\\variables.csv', 'r', ) as csvfile:   #csvfile es el nombre que le ponemos a la variable
    lector = csv.reader(csvfile, delimiter = ";") #se utiliza el método reader
    print(lector)
    encabezado = next(lector)               #corta la primer linea y se guarda en la variable encabezado
    #print(encabezado)                       #muestra el encabezado
    presion = []
    print(encabezado[3])
    for fila in lector:          #con el for se itera sobre el objeto para leer
        fila[3] = fila[3].replace("," , ".")
        dato = float(fila[3])
        presion.append(dato)

print(presion) 
suma = sum(presion)
print(suma)
promedio = (suma / 19 )
print(promedio)