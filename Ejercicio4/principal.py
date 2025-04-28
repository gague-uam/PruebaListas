from models.editor import EditorTexto
from models.clases import Escribir, Borrar, Copiar, Pegar

def mostrar_menu():
    print("\n--- Editor de Texto ---")
    print("1. Escribir texto")
    print("2. Borrar texto")
    print("3. Copiar texto")
    print("4. Pegar texto")
    print("5. Deshacer")
    print("6. Rehacer")
    print("7. Mostrar texto actual")
    print("8. Mostrar historial")
    print("9. Salir")

def main():
    editor = EditorTexto()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            texto = input("Texto a escribir: ")
            pos = int(input("Posición: "))
            editor.ejecutar_accion(Escribir(texto, pos))
        
        elif opcion == "2":
            inicio = int(input("Posición inicial: "))
            fin = int(input("Posición final: "))
            editor.ejecutar_accion(Borrar(inicio, fin))
        
        elif opcion == "3":
            inicio = int(input("Posición inicial: "))
            fin = int(input("Posición final: "))
            texto = editor.texto[inicio:fin]
            editor.ejecutar_accion(Copiar(texto))
        
        elif opcion == "4":
            pos = int(input("Posición: "))
            editor.ejecutar_accion(Pegar(editor.portapapeles, pos))
        
        elif opcion == "5":
            editor.deshacer()
            print("Acción deshecha!")
        
        elif opcion == "6":
            editor.rehacer()
            print("Acción rehecha!")
        
        elif opcion == "7":
            print(f"\nTexto actual:\n{editor.texto}")
        
        elif opcion == "8":
            print("\nHistorial de acciones:")
            for i, acc in enumerate(editor.obtener_historial(), 1):
                print(f"{i}. {acc}")
        
        elif opcion == "9":
            print("Saliendo del editor...")
            break
        
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()