from models.clases import Estacion

class MapaRuta:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregar_estacion(self, nombre, tiempo_anterior=None):
        nueva_estacion = Estacion(nombre)
        
        if not self.cabeza:
            self.cabeza = nueva_estacion
            self.cola = nueva_estacion
        else:
            self.cola.siguiente = nueva_estacion
            self.cola.tiempo_siguiente = tiempo_anterior
            self.cola = nueva_estacion
    
    def buscar_estacion(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None
    
    def calcular_tiempo(self, inicio, destino):
        estacion_actual = self.buscar_estacion(inicio)
        tiempo_total = 0
        
        while estacion_actual and estacion_actual.nombre != destino:
            tiempo_total += estacion_actual.tiempo_siguiente
            estacion_actual = estacion_actual.siguiente
        
        return tiempo_total if estacion_actual else -1