import funciones as fn

librería=[]

while True:
    print("(1)Registrar libro")
    print("(2)Listar todos los libros")
    print("(3)Registrar venta")
    print("(4)Imprimir reporte de ventas")
    print("(5)Generar txt")
    print("(6)Salir")
    opc=int(input("Seleccione la opcion que usted desee: "))

    try:
        if opc==1:
            fn.registrar_libro(librería)
        elif opc==2:
            fn.Listar_libros(librería)
        elif opc==3:
            fn.Registrar_venta(librería)
        elif opc==4:
            fn.Imprimir_reportes(librería)
        elif opc==5:
            fn.Generar_txt(librería)
        elif opc==6:
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("Opcion invalida reintente nuevamente")        