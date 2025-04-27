class Nodo:
    def __init__(self, paciente):
        self.paciente = paciente
        self.siguiente = None

class ColaPacientes:
    def __init__(self):
        self.frente = None
        self.final = None
        self.contador = 0
    
    def agregar_paciente(self, paciente):
        nuevo_nodo = Nodo(paciente)
        if self.final is None:
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.contador += 1
    
    def atender_paciente(self):
        if self.frente is None:
            return None
        
        atendido = self.frente.paciente
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.contador -= 1
        return atendido
    
    def mostrar_cola(self):
        actual = self.frente
        posicion = 1
        while actual:
            print(f"[{posicion}] {actual.paciente}")
            actual = actual.siguiente
            posicion += 1
    
    def esta_vacia(self):
        return self.frente is None