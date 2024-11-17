from .Persona import Persona

class Estudiante(Persona):
    sexo = 'Masculino'

    def __init__(self,nombre,edad,dni,tutor,asistencia,boletines):
        super().__init__(nombre,edad,dni)
        self.tutor = tutor
        self.asistencia = asistencia
        self.boletines = boletines