control = True

while control == True:
    print("1. Listar Archivos\n2. Procesar(.txt)\n3. Procesar(.csv)" \
        "\n4. Salir")
    opcion = int(input("elija una opcion: "))
    match opcion:
        case 1:
            listar_archivos =()