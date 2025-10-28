import csv

with open('C:\\Users\\salit\\OneDrive\\Desktop\\salida.csv', 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile)
    lista1 = [10,15,20,25]
    nombres = ['sofia','valentina','isabela','tatiana']
    carros = ['mazda','audi','bmw','ferrari']

    escritor.writerow(lista1)
    escritor.writerow(nombres)
    escritor.writerow(carros)
