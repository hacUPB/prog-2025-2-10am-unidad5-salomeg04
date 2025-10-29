import csv
import matplotlib.pyplot as plt


archivo_csv = "C:/Users/salit/OneDrive/Documentos/repo-programacion/prog-2025-2-10am-unidad5-salomeg04/unidad 5 reto/Normales_climatológicas_del_Ozono_20251028.csv"
archivo_txt = "C:/Users/salit/OneDrive/Documentos/repo-programacion/prog-2025-2-10am-unidad5-salomeg04/unidad 5 reto/La calidad del aire en Colombia.txt"


def ver_csv():
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for i, fila in enumerate(lector):
            print(fila)
            if i == 14:
                break

def calcular_estadisticas():
    columna = input("Escribe el nombre de la columna que quieres analizar: ")
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        datos = []
        for fila in lector:
            valor = fila.get(columna)
            if valor:
                try:
                    datos.append(float(valor))
                except:
                    pass
    if len(datos) == 0:
        print("No hay datos numéricos.")
        return
    datos.sort()
    total = len(datos)
    promedio = sum(datos) / total
    mediana = datos[total//2] if total % 2 == 1 else (datos[total//2 - 1] + datos[total//2]) / 2
    desviacion = (sum((x - promedio) ** 2 for x in datos) / total) ** 0.5
    print("Cantidad:", total)
    print("Promedio:", promedio)
    print("Mediana:", mediana)
    print("Desviación estándar:", desviacion)
    print("Mínimo:", min(datos))
    print("Máximo:", max(datos))

def graficos_csv():
    columna = input("Escribe el nombre de la columna que quieres graficar: ")
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        datos = []
        for fila in lector:
            valor = fila.get(columna)
            if valor != "":
                try:
                    datos.append(float(valor))
                except:
                    pass
    if len(datos) == 0:
        print("No hay datos numéricos.")
        return
    plt.scatter(range(len(datos)), datos)
    plt.title("Gráfico de dispersión")
    plt.show()
    plt.bar(range(len(datos)), sorted(datos))
    plt.title("Gráfico de barras")
    plt.show()

def contar_txt():
    with open(archivo_txt, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
        palabras = texto.split()
        print("Palabras:", len(palabras))
        print("Con espacios:", len(texto))
        print("Sin espacios:", len(texto.replace(" ", "").replace("\n", "")))


def cambiar_txt():
    vieja = input("Palabra que quieres cambiar: ")
    nueva = input("Palabra nueva: ")
    with open(archivo_txt, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    texto = texto.replace(vieja, nueva)
    with open(archivo_txt, "w", encoding="utf-8") as archivo:
        archivo.write(texto)
    print("Listo, ya se cambió.")

def vocales_txt():
    with open(archivo_txt, "r", encoding="utf-8") as archivo:
        texto = archivo.read().lower()
    vocales = ["a", "e", "i", "o", "u"]
    cantidades = [texto.count(v) for v in vocales]
    plt.bar(vocales, cantidades)
    plt.title("Vocales en el texto")
    plt.show()


def menu_txt():
    print("\nOpciones para el archivo TXT:")
    print("1. Contar palabras y letras")
    print("2. Cambiar una palabra")
    print("3. Ver cuántas vocales hay")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        contar_txt()
    elif opcion == "2":
        cambiar_txt()
    elif opcion == "3":
        vocales_txt()


def menu_csv():
    print("\nOpciones para el archivo CSV:")
    print("1. Ver primeras filas")
    print("2. Ver estadísticas")
    print("3. Ver gráficos")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        ver_csv()
    elif opcion == "2":
        calcular_estadisticas()
    elif opcion == "3":
        graficos_csv()

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Usar archivo TXT")
        print("2. Usar archivo CSV")
        print("3. Salir")
        opcion = input("Escribe tu opción: ")
        if opcion == "1":
            menu_txt()
        elif opcion == "2":
            menu_csv()
        elif opcion == "3":
            print("Gracias por usar mi programa :)")
            break

main()