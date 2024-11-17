from .Persona import Persona

class PadreTutor(Persona):
    def __init__(self,nombre,edad,dni,parentesco):
        super().__init__(nombre,edad,dni)
        self.parentesco = parentesco