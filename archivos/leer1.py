# 1. abrir archivo y definir el modo 
archivo = open("./archivos/texto1.txt","r")
# 2. leer el archivo
# datos = archivo.read(100)               #archivo.read() lee cierta cantidad de caracteres 
#for i in range(5):
    #datos = archivo.readline()              #archivo.readline() lee hasta que encuentre un enter en la escritura
#for datos in archivo: 
 #print(datos[0])     
datos = archivo.readline()   
print(datos) 
# 3. cerramos el archivo
archivo.close()                    # hay que cerrar el archivo si no se puede dañar

