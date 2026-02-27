class usuario:

    # se definen los parametros de usuario que son id_usuario, nombre_usuario, apellido_usuario
    def __init__(self, id_usuario, nombre_usuario, apellido_usuario):
        self.id_usuario=id_usuario
        self.nombre_usuario=nombre_usuario
        self.apellido_usuario=apellido_usuario

    # constructor str para imprimir el id del usuario y su nombre
    def __str__(self):
        return "id del usuario: {} - Nombre del usuario: {} {}".format(self.id_usuario, self.nombre_usuario, self.apellido_usuario)