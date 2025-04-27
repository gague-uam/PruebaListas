from models.clases import Estudiante

class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, estudiante):
        nuevo_nodo = Nodo(estudiante)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def ordenar(self, clave):
        claves_validas = {'carnet', 'nombres', 'apellidos', 'peso', 'estatura', 'sexo', 'promedio'}
        if clave not in claves_validas:
            raise ValueError(f"Clave de ordenamiento inválida: {clave}")
        
        nodos = []
        actual = self.cabeza
        while actual:
            nodos.append(actual)
            actual = actual.siguiente
        
        nodos.sort(key=lambda nodo: getattr(nodo.datos, clave))
        
        if not nodos:
            self.cabeza = None
            return
        
        self.cabeza = nodos[0]
        actual = self.cabeza
        for nodo in nodos[1:]:
            actual.siguiente = nodo
            actual = nodo
        actual.siguiente = None
    
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.datos)
            actual = actual.siguiente