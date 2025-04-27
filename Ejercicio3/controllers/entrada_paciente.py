from models.clases import Paciente

def ingresar_paciente():
    print("\nIngrese datos del paciente:")
    
    nombre = input("Nombre completo: ").strip()
    while not nombre:
        print("El nombre no puede estar vacio")
        nombre = input("Nombre completo: ").strip()
    
    while True:
        try:
            edad = int(input("Edad: ").strip())
            if edad <= 0:
                raise ValueError
            break
        except:
            print("Ingrese una edad valida")
    
    sintoma = input("Sintoma principal: ").strip()
    while not sintoma:
        print("El sintoma no puede estar vacio")
        sintoma = input("Sintoma principal: ").strip()
    
    while True:
        try:
            prioridad = int(input("Prioridad (1-5): ").strip())
            if 1 <= prioridad <= 5:
                break
            raise ValueError
        except:
            print("Ingrese un valor entre 1 y 5")
    
    return Paciente(nombre, edad, sintoma, prioridad)