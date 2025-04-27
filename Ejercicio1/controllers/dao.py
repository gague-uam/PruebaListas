from models.clases import Estudiante

def ingresar_estudiante():
    print("\nIngrese los datos del estudiante:")
    carnet = input("Carnet: ").strip()
    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()
    
    while True:
        try:
            peso = float(input("Peso (kg): ").strip())
            if peso <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido mayor que 0")
    
    while True:
        try:
            estatura = float(input("Estatura (cm): ").strip())
            if estatura <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido mayor que 0")
    
    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in {'M', 'F'}:
            break
        print("Error: Ingrese M o F")
    
    while True:
        try:
            promedio = float(input("Promedio académico: ").strip())
            if not 0 <= promedio <= 100:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un valor entre 0 y 100")
    
    return Estudiante(carnet, nombres, apellidos, peso, estatura, sexo, promedio)