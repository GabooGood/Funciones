Genero=["ACCION","TERROR","DRAMA"]

def registrar_libro(Librería):
    titulo=input("Cual es el titulo del libro: ")
    Autor=input("Quien es el autor del libro: ")
    Género=input("Que genero de libro quiere: (Accion / Drama / Terror) ").lower()
    Precio=int(input("Cual es el costo del libro: "))

    Librería.append({
        'titulo': titulo,
        'Autor': Autor,
        'Genero': Genero,
        'Precio': Precio
    })

def Listar_libros(Librería):
    for librerias in Librería:
        print(Librería)

def Registrar_venta(librería):
    print()

def Imprimir_reportes(Librería):
    genero_seleccionado=input("Ingrese un genero para imprimir la plantillaa o bien presione ENTER para imprimir todos").lower()
    if genero_seleccionado == "":
        Imprimir_libreria=librerias	
        nombre_archivo=f"planilla_todos.txt"
    elif genero_seleccionado in librerias:
        Imprimir_libreria=[]
        for librerias in Librería:
            if librerias['genero']==genero_seleccionado:
                Imprimir_libreria.append(librerias)
                nombre_archivo=f"planilla_{genero_seleccionado}.txt"
            else:
                print("genero no valido")
                return


def Generar_txt(Librería):
    print()
    
            
    