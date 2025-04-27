from models.ruta import MapaRuta

def mostrar_menu():
    print("\n--- Calculador de Rutas Automático ---")
    print("1. Calcular tiempo de viaje")
    print("2. Ver estaciones disponibles")
    print("3. Salir")

def main():
    mapa = MapaRuta()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\nEstaciones disponibles:", ", ".join(mapa.obtener_estaciones()))
            inicio = input("Estación de partida: ").strip()
            destino = input("Estación destino: ").strip()
            
            tiempo = mapa.calcular_tiempo(inicio, destino)
            
            if tiempo == -1:
                print("\nError: Ruta no válida o estaciones incorrectas")
            else:
                print(f"\nTiempo estimado: {tiempo} minutos")
        
        elif opcion == "2":
            print("\nEstaciones en la ruta:")
            for estacion in mapa.obtener_estaciones():
                print(f"- {estacion}")
        
        elif opcion == "3":
            print("\n Nos vemos pronto!")
            break
        
        else:
            print("\nOpción no válida")

if __name__ == "__main__":
    main()