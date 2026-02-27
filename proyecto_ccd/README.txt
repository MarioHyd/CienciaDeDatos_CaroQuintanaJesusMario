Materia: Ciencia de datos 12pm - 1pm
Alumno: Jesus Mario Caro Quintana
Maestro: Mora Felix Zuriel Dathan

-main.py
def main(): main para mostrar el menu para que el usuario interactue use el sistema

-SLibro.py
def __init__(): se define los parametros del libro que son el isbn, titulo, autor, y ejemplares_totales
def __str__(): constructor str para imprimir todos los datos de los libros

-SUsuario.py
def __init__(): se definen los parametros de usuario que son id_usuario, nombre_usuario, apellido_usuario
def __str__(self): constructor str para imprimir el id del usuario y su nombre

-SBiblioteca.py
def __init__(): metodo constructor init en donde se encuentran los diccionarios de libros, usuraios y la lista de los prestamos
def alta_libro(): la siguiente funcion lo que hace es dar de alta el libro
def Catalogo_libros(): la siguiente funcion es para mostrar el catalogo de libros
def buscar_libro(): la siguiente funcion es para buscar el libro por su titulo
def alta_usuario(): la siguiente funcion es para dar de alta al usuario
def consultar_usuarios(): la siguiente funcion es para mostrar los usuarios existentes
def pretamo_libro(): la siguiente funcion es para realizar los prestamos de los libros
def devolucion_libro(): la siguiente funcion es para realizar las devoluciones de los libros
