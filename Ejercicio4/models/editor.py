from models.clases import *

class EditorTexto:
    def __init__(self):
        self.texto = ""
        self.portapapeles = ""
        self.pila_deshacer = []
        self.pila_rehacer = []
    
    def ejecutar_accion(self, accion):
        accion.ejecutar(self)
        self.pila_deshacer.append(accion)
        self.pila_rehacer.clear()
    
    def deshacer(self):
        if self.pila_deshacer:
            accion = self.pila_deshacer.pop()
            accion.deshacer(self)
            self.pila_rehacer.append(accion)
    
    def rehacer(self):
        if self.pila_rehacer:
            accion = self.pila_rehacer.pop()
            accion.rehacer(self)
            self.pila_deshacer.append(accion)
    
    def obtener_historial(self):
        return [type(acc).__name__ for acc in self.pila_deshacer]