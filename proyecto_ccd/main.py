from SBiblioteca import biblioteca

# main para mostrar el menu para que el usuario interactue use el sistema
def main():
    Labiblioteca = biblioteca()

    while True:
        print("""
            Bienbenido al sistema de la biblioteca.
            Elija la opccion deseada:
            1. Registrar libro.
            2. Mostrar Catalogo de libros.
            3. Buscar libro.
            4. Registrar usuario.
            5. Mostrar usuarios existentes.
            6. Realizar prestamo de un libro.
            7. Realizar devolucion de un libro.
            8. Salir.
            """) # este es el menu principal
        opcion = input()
        
        # dependiendo de la opcion que se elija, llama a las distintas funciones de SBiblioteca
        if opcion == "1":
            Labiblioteca.alta_libro()
        elif opcion == "2":
            Labiblioteca.Catalogo_libros()
        elif opcion == "3":
            Labiblioteca.buscar_libro()
        elif opcion == "4":
            Labiblioteca.alta_usuario()
        elif opcion == "5":
            Labiblioteca.consultar_usuarios()
        elif opcion == "6":
            Labiblioteca.pretamo_libro()
        elif opcion == "7":
            Labiblioteca.devolucion_libro()
        elif opcion == "8": # sale del sistema
            print("Saliendo del sistema, adios :D")
            break

main()