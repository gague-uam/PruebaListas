"""Problema#1
Una escuela de educación primaria requiere un algoritmo que muestre los datos de los
estudiantes de un salón de clase ordenados de forma ascendente, según un parámetro
indicado; este parámetro puede ser cualquiera de los siguientes campos: carnet, nombres,
apellidos, peso, estatura, sexo, promedio."""

from models.nodo import ListaEnlazada
from controllers.dao import ingresar_estudiante

def mostrar_menu_principal():
    print("\nMENÚ PRINCIPAL")
    print("1. Agregar estudiante")
    print("2. Ordenar y mostrar estudiantes")
    print("3. Salir")

def mostrar_menu_ordenamiento():
    print("\nCRITERIOS DE ORDENAMIENTO:")
    print("1. Carnet")
    print("2. Nombres")
    print("3. Apellidos")
    print("4. Peso")
    print("5. Estatura")
    print("6. Sexo")
    print("7. Promedio")

def obtener_clave(opcion):
    claves = {
        '1': 'carnet',
        '2': 'nombres',
        '3': 'apellidos',
        '4': 'peso',
        '5': 'estatura',
        '6': 'sexo',
        '7': 'promedio'
    }
    return claves.get(opcion)

def main():
    lista = ListaEnlazada()
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            lista.agregar(ingresar_estudiante())
            print("\nEstudiante agregado exitosamente!")
        
        elif opcion == '2':
            if not lista.cabeza:
                print("\nNo hay estudiantes para ordenar!")
                continue
            
            while True:
                mostrar_menu_ordenamiento()
                criterio = input("Seleccione criterio de ordenamiento: ").strip()
                clave = obtener_clave(criterio)
                
                if clave:
                    lista.ordenar(clave)
                    print("\nEstudiantes ordenados:")
                    lista.mostrar()
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
        
        elif opcion == '3':
            print("\nSaliendo del sistema...")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()