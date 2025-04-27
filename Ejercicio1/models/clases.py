class Estudiante:
    def __init__(self, carnet, nombre, apellido, peso, estatura, sexo, promedio):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.peso = peso
        self.estatura = estatura
        self.sexo = sexo
        self.promedio = promedio
        self.estatura = estatura
        self.sexo = sexo
        self.promedio = promedio

    def __str__(self):
        return f"Carnet: {self.carnet}, Nombre: {self.nombre}, Apellido: {self.apellido}, Peso: {self.peso} Estatura: {self.estatura}, Sexo: {self.sexo}, Promedio: {self.promedio}"