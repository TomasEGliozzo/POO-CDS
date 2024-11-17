from .Stock import Stock

class Libro(Stock):
    def __init__(self, id, descripcion,estado,titulo,edicion):
        super().__init__(id, descripcion,estado)
        self.titulo = titulo
        self.edicion = edicion
        
