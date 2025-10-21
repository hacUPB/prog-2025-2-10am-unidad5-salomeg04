'''
ubicacion = "C:\\Users\\salit\\OneDrive\\Desktop\\archivos"
#\ se usa para comando de texto, por eso usamos \\ 

nombre_archivo = "futas.txt"
modo = "w" # modo escitura, sobreescribe
fp = open(ubicacion +"\\"+ nombre_archivo, modo,encoding="utf-8" )
frase = input("Por favor ingrese una frase: ")


edad = int(input("ingrese su edad: "))
estatura = float(input("ingrese su estatura: "))
fp.write(frase + "\n")
fp.write(str(edad))
fp.write("\n")
fp.write(str(estatura ))
fp.write("\n")
fp.close()
'''

'''
ubicacion = "C:\\Users\\salit\\OneDrive\\Desktop\\archivos"
#\ se usa para comando de texto, por eso usamos \\ 

nombre_archivo = "futas.txt"
modo = "a" # modifica archichos, sin borrar lo anterior
fp = open(ubicacion +"\\"+ nombre_archivo, modo,encoding="utf-8" )
frase = input("Por favor ingrese una frase: ")


edad = int(input("ingrese su edad: "))
estatura = float(input("ingrese su estatura: "))
fp.write(frase + "\n")
fp.write(str(edad))
fp.write("\n")
fp.write(str(estatura ))
fp.write("\n")
fp.close()
'''

ubicacion = "C:\\Users\\salit\\OneDrive\\Desktop\\archivos"
#\ se usa para comando de texto, por eso usamos \\ 

nombre_archivo = "futas.txt"
modo = "x" # crea archivo y guarda texto puesto 
fp = open(ubicacion +"\\"+ nombre_archivo, modo,encoding="utf-8" )
frase = input("Por favor ingrese una frase: ")


edad = int(input("ingrese su edad: "))
estatura = float(input("ingrese su estatura: "))
fp.write(frase + "\n")
fp.write(str(edad))
fp.write("\n")
fp.write(str(estatura ))
fp.write("\n")
fp.close()