from .Persona import Persona

class Directivo(Persona):
    
    def __init__(self,nombre,edad,dni,referencias):
        super().__init__(nombre,edad,dni)
        self.referencias = referencias
        
    