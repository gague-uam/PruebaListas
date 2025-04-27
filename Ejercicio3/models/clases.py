class Paciente:
    def __init__(self, nombre, edad, sintoma, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma
        self.prioridad = prioridad

    def __str__(self):
        return f"Nombre: {self.nombre.ljust(20)} | Edad: {str(self.edad).ljust(3)} | Sintoma: {self.sintoma.ljust(15)} | Prioridad: {self.prioridad}"
        