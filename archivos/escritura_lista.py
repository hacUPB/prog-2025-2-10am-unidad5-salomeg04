lista = ["manicomio", "soltera", "oe bebe"]
ubicacion = "C:\\Users\\salit\\OneDrive\\Desktop\\archivos"
modo = "a"
nombre_archivo = "canciones.txt"
fp = open(ubicacion + "\\" + nombre_archivo , modo, encoding="utf-8")
for cancion in lista:
    fp.write(cancion + "\n")
fp.close()