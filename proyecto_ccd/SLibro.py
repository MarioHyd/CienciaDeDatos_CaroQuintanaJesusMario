class libro:
    # se define los parametros del libro que son el isbn, titulo, autor, y ejemplares_totales
    def __init__(self, isbn, titulo, autor, ejemplares_totales):
        self.isbn=isbn
        self.titulo=titulo
        self.autor=autor
        self.ejemplares_totales=ejemplares_totales

    # constructor str para imprimir todos los datos de los libros
    def __str__(self):
        return "isbn:[{}] Titulo: {} - Autor: {} ({} unidades)".format(self.isbn, self.titulo, self.autor, self.ejemplares_totales)
