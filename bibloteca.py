import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados(cod_libro):
    for lib in libros:
        if cod_libro == lib['cod']:
            libro_elegido= print(f" Titulo: {lib['titulo']} \n Autor : {lib['autor']} \n Cantidad de Libros prestados: {lib['cant_ej_pr']}")
        else:
            libro_elegido=print("Error, el codigo no coincide con ninguno existente")
        
    return libro_elegido
            

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro(cod_libro):
    for lib in libros:
        if cod_libro == lib['cod']:
            cantejemp_libro = lib['cant_ej_ad']
            prestamo_libro = print(f" Autor :{lib['autor']} \n Titulo {lib['titulo']} \n Cant. de Ejemplares {cantejemp_libro} ")
            if cantejemp_libro ==0:
                print("No hay disponiblidad para el prestamo de este libro")
            else :
                rta= input("confirmar prestamo: S/N \n")
                respuesta= rta.lower()
                if respuesta == 's':
                    lib['cant_ej_ad']= int(cantejemp_libro) -1
                    lib['cant_ej_pr']=int(cantejemp_libro) +1
                    print("El prestamo del libro se Realizo con exito")
                else:
                    print("No se ha realizado el prestamo del libro")
                    
    prestamo_libro=print("Error, el codigo no coincide con ninguno existente")
    
    return prestamo_libro

def devolver_ejemplar_libro():
    #completar
    return None

def nuevo_libro():
    #completar
    return None