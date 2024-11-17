from .Persona import Persona

class Preceptor(Persona):
    def __init__(self,nombre,edad,dni,salario):
        super().__init__(nombre,edad,dni)
        self.salario = salario