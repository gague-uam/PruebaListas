from models.lista import ColaPacientes
from controllers.entrada_paciente import ingresar_paciente

def mostrar_menu():
    print("\n--- Sistema de Gestion Clinica ---")
    print("1. Registrar nuevo paciente")
    print("2. Mostrar lista de espera")
    print("3. Atender siguiente paciente")
    print("4. Salir")

def main():
    cola = ColaPacientes()
    
    while True:
        mostrar_menu()
        opcion = input("Elija una opcion: ").strip()
        
        if opcion == "1":
            cola.agregar_paciente(ingresar_paciente())
            print("\nPaciente registrado")
        
        elif opcion == "2":
            if cola.esta_vacia():
                print("\nNo hay pacientes en espera")
            else:
                print(f"\nPacientes en espera ({cola.contador}):")
                cola.mostrar_cola()
        
        elif opcion == "3":
            if cola.esta_vacia():
                print("\nNo hay pacientes para atender")
            else:
                paciente = cola.atender_paciente()
                print("\nPaciente atendido:")
                print(paciente)
        
        elif opcion == "4":
            print("\nNos vemos pronto")
            break
        
        else:
            print("\nDigite una opcion valida")

if __name__ == "__main__":
    main()