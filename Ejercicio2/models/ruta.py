from models.clases import Estacion

class MapaRuta:
    def __init__(self):
        self.cabeza = None
        self._inicializar_ruta()
    
    def _inicializar_ruta(self):

        estaciones = [
            ("Masaya", None),
            ("Universidad Americana", 8),
            ("Galerias Santo Domingo", 5),
            ("Veracruz", 12),
            ("Parque Japones", 10)
        ]
        
        for nombre, tiempo in estaciones:
            self.agregar_estacion(nombre, tiempo)
    
    def agregar_estacion(self, nombre, tiempo_anterior=None):
        nueva_estacion = Estacion(nombre)
        
        if not self.cabeza:
            self.cabeza = nueva_estacion
            self.actual = self.cabeza
        else:
            self.actual.siguiente = nueva_estacion
            self.actual.tiempo_siguiente = tiempo_anterior
            self.actual = nueva_estacion
    
    def obtener_estaciones(self):
        estaciones = []
        actual = self.cabeza
        while actual:
            estaciones.append(actual.nombre)
            actual = actual.siguiente
        return estaciones
    
    def calcular_tiempo(self, inicio, destino):
        estacion_actual = self._buscar_estacion(inicio)
        tiempo_total = 0
        
        while estacion_actual and estacion_actual.nombre != destino:
            tiempo_total += estacion_actual.tiempo_siguiente
            estacion_actual = estacion_actual.siguiente
        
        return tiempo_total if estacion_actual else -1
    
    def _buscar_estacion(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None