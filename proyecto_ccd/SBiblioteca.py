from SLibro import libro
from SUsuario import usuario

class biblioteca:

    # metodo constructor init en donde se encuentran los diccionarios de libros, usuraios y la lista de los prestamos
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.prestamos = []

    # la siguiente funcion lo que hace es dar de alta el libro
    def alta_libro(self):
     
        isbn = input("ISBN: ") # pedimos el isbn del libro
        if isbn in self.libros: # valida el isbn para ver si el libro existe
            print(f"el isbn: {isbn} del libro ya esta registrado")
        else:
            titulo = input("Titulo: ") # pedimos el titulo del libro
            autor = input("Autor: ") # pedimos el autor del libro
            ejemplares_totales = int(input("Ejemplares totales: ")) # pedimos el total de ejemplares
            alta = libro(isbn, titulo, autor, ejemplares_totales) # aqui es para crear un libro con los datos guardandolo en alta
            self.libros[isbn]=alta # aqui se guarda el objeto dentro del diccionario y se usa isbn como clave
            print(f"El libro: {titulo} se ha registrado exitosamente :D")

    # la siguiente funcion es para mostrar el catalogo de libros
    def Catalogo_libros(self):
        if not self.libros: # valida si el diccionario esta vacio para indicar que no hay libros si este esta vacio
            print("No hay libros disponibles")
        else: 
            for datos_libros in self.libros.values(): # aqui es para recorrer todos los libros guardados y mostrarlos
                print(datos_libros)

    # la siguiente funcion es para buscar el libro por su titulo
    def buscar_libro(self):
        titulo_buscar = input("Dame el nombre del titulo que deseas buscar: ")

        for Tlibro in self.libros.values(): # aqui es para recorrer todos los libros
            if Tlibro.titulo == titulo_buscar: # si el titulo es igual al titulo que nos dieron imprime el libro
                print(Tlibro)
                return
        print("libro no encontrado.")
    
    # la siguiente funcion es para dar de alta al usuario
    # funciona practicamente igual que alta_libro() solamente que usarmos el diccionario de usuarios
    def alta_usuario(self):
        id_usuario = input("Ingresa el numero de tu INE: ")
        if id_usuario in self.usuarios:
            print("el INE del usuario ya existe")
        else:
            nombre_usuario = input("Dame el nombre del usuario: ")
            apellido_usuario = input("Dame el apellido del usuario: ")
            altaU = usuario(id_usuario, nombre_usuario, apellido_usuario)
            self.usuarios[id_usuario] = altaU
            print(f"El usuario: {nombre_usuario} {apellido_usuario} se ha registrado exitosamente :D")
    
    # la siguiente funcion es para mostrar los usuarios existentes
    # funciona practicamente igual que la funcion catalogo_libros() solo que usaremos el diccionario de usuarios
    def consultar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados")
        else:
            for datos_usuarios in self.usuarios.values():
                print(datos_usuarios)

    # la siguiente funcion es para realizar los prestamos de los libros
    def pretamo_libro(self):
        isbn = input("dame el isbn del libro que deseas llevarte: ")
        id_usuario = input("dame tu INE: ")
        fecha_prestamo = input("dame la fecha del prestamo: ")

        # en este if se verifica que exista el libro si el isbn no esta en el diccionario de libros
        if isbn not in self.libros:
            print("el libro no lo tenemos en la biblioteca.")
            return
        
        # en este if se verifica que el usuario este registrado si el id_usario no se encuentra en el diccionario de usuarios
        if id_usuario not in self.usuarios:
            print("el usuario no existe, por favor registrese.")
            return
        libro_prestado = self.libros[isbn] # aqui obtiene el libro usando isbn como clave y lo guarda en una variable

        # si los ejemplares_totales son menor o igual a 0 indica que no hay ejemplares del libro que esta pidiendo prestado
        if libro_prestado.ejemplares_totales <= 0:
            print("no hay ejemplares disponibles de este libro en este momento")
            return
        
        # en este for es para verificar que el usuario no se le preste el mismo libro
        for prestamo in self.prestamos:
            # en la tupla de prestamo 0 se encuantra el isbn y en 1 se encuanetra el id del usuario 
            # verifica que el isbn y el id_usuario estan en la tupla para ver si a ese usario ya se le presto el libro
            if prestamo[0] == isbn and prestamo[1] == id_usuario:
                print("a este usuario ya se le presto este libro")
                return

        # en esta seccion es para validar que a un usuario no se le preste mas de 3 libros
        conta = 0
        for prestamo in self.prestamos:
            if prestamo[1] == id_usuario: # si el id_usuario es el mismo que nos dio usa un contador
                conta += 1
        if conta >= 3: # si el contador llega a 3 ya no se le presta mas libros
            print("al usuario ya se le ha prestado una cantidad de 3 libros")
            return
        
        self.prestamos.append((isbn, id_usuario, fecha_prestamo)) # se agrega los datos proporcionados a la tupla de prestamos

        libro_prestado.ejemplares_totales -= 1 # se le resta 1 a los ejemplares totales
        print("prestamo realizado exitosamente :D")

    # la siguiente funcion es para realizar las devoluciones de los libros
    def devolucion_libro(self):
        isbn = input("dame el isbn del libro que deseas devolver: ")
        id_usuario = input("dame tu INE: ")

        for prestamo in self.prestamos:
            # verifica que el isbn y el id_usuario estan en la tupla
            if prestamo[0] == isbn and prestamo [1] == id_usuario:
                self.prestamos.remove(prestamo) # usamos el remove para eliminar el prestamo
                libro_devuelto = self.libros[isbn]
                libro_devuelto.ejemplares_totales += 1 # le sumamos 1 al numero de ejemplares_totales
                print("Libro devuelto exitosamente :D")
                return
        print("no se encontro un prestamo con esos datos.")

