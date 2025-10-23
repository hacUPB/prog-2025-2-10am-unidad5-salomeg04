nombre_archivo = "./archivos/texto1.txt"
# ubicacion = "C:\\Users\\salit\\OneDrive\\Desktop\\archivos"
with open(nombre_archivo, "r" , encoding="utf-8") as archivo:
    #leer todos los items dentro de una lista
   lista = archivo.readlines()


for c in lista:
   print(c)
