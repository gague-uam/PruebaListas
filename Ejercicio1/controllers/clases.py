class Estudiante:
    def __init__(self, carnet, nombre, apellido, estatura, sexo, promedio):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.estatura = estatura
        self.sexo = sexo
        self.promedio = promedio

    def __str__(self):
        return f"Carnet: {self.carnet}, Nombre: {self.nombre}, Apellido: {self.apellido}, Estatura: {self.estatura}, Sexo: {self.sexo}, Promedio: {self.promedio}"