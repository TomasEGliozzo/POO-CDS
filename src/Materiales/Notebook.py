from .Stock import Stock

class Notebook(Stock):
    def __init__(self, id, descripcion, estado,direccion_gps):
        super().__init__(id, descripcion,estado)
        self.direccion_gps = direccion_gps