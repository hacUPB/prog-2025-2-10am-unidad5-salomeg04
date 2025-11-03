'''
with open("nombres.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    print("Número de líneas:", len(lineas))
'''

'''
import csv
import matplotlib.pyplot as plt

productos = []
cantidades = []

with open("ventas.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        productos.append(fila["producto"])
        cantidades.append(int(fila["cantidad"]))

plt.bar(productos, cantidades)
plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad")
plt.show()
'''

'''
with open ("frases.txt" , "r" , encoding="utf-8") as archivo:
    texto = archivo.read()
    palabras = texto.split()
    print("palabras:" ,  len(palabras))
'''


'''
import csv 

with open ('alumnos.csv' , "r" , encoding="utf-8") as archivo: 
    lector = csv.DictReader(archivo)
columnas = lector.fieldnames

nota = columnas[2]
if nota >= 3.0:
    print(columnas[0])
'''


'''
import csv 
import matplotlib.pyplot as plt

producto = []
precio = []
with open("productos.csv" , "r" , encoding="utf-8")as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        producto.append(fila["producto"])
        precio.append(float(fila["precio"]))

plt.bar(producto, precio)
plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("precio")
plt.show()
'''
'''
with open ("frases.txt" , "r " , encoding="utf-8") as archivo:
    texto = archivo.read()
    palabras = texto.split()

    print( "conteo total palabras: " , len(palabras))
'''

'''
import csv

with open("alumnos.csv" , "r" , encodig="utf-8")as archivo:
    lector = csv.DictReader(archivo) 
    for fila in lector:
        print(fila ["nombre_columna"])
    if fila in lector:
        fila(float["nota"]) >= 3.0
        print(fila["nombre"])
'''

'''
suma = 0
with open("ventas.txt" , "r" , encoding="utf-8") as archivo:
    for linea in archivo
    suma+= linea.strip()
    print("suma:" , suma)
'''

'''
import csv
import matplotlib.pyplot as plt

producto = []
cantidad = []
with open("productos.csv" , "r" , encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for i in lector:
        producto.append(i["producto"])
        cantidad.append(int(i["cantidad"]))
plt.bar(producto , cantidad)
plt.title(producto)
plt.xlabel(producto)
plt.ylabel(cantidad)
plt.show()
'''

'''
with open("frutas.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()
    palabra = texto.split()

    print(palabra.count("manzana")))
'''

import csv
import matplotlib.pyplot as plt

producto = []
cantidad = []

with open("ventas.csv","r",encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        producto.append(fila["producto"])
        cantidad. append(int(fila["cantidad"]))

plt.bar(producto,cantidad)
plt.texto("ventas de cada producto")
plt.xlabel(producto)
plt.ylabel(cantidad)
plt.show()