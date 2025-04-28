class Accion:
    def ejecutar(self, editor):
        pass
    
    def deshacer(self, editor):
        pass
    
    def rehacer(self, editor):
        pass

class Escribir(Accion):
    def __init__(self, texto, posicion):
        self.texto = texto
        self.posicion = posicion
    
    def ejecutar(self, editor):
        editor.texto = editor.texto[:self.posicion] + self.texto + editor.texto[self.posicion:]
    
    def deshacer(self, editor):
        editor.texto = editor.texto[:self.posicion] + editor.texto[self.posicion + len(self.texto):]
    
    def rehacer(self, editor):
        self.ejecutar(editor)

class Borrar(Accion):
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
        self.texto_borrado = ""
    
    def ejecutar(self, editor):
        self.texto_borrado = editor.texto[self.inicio:self.fin]
        editor.texto = editor.texto[:self.inicio] + editor.texto[self.fin:]
    
    def deshacer(self, editor):
        editor.texto = editor.texto[:self.inicio] + self.texto_borrado + editor.texto[self.inicio:]
    
    def rehacer(self, editor):
        self.ejecutar(editor)

class Copiar(Accion):
    def __init__(self, texto):
        self.texto = texto
        self.portapapeles_anterior = ""
    
    def ejecutar(self, editor):
        self.portapapeles_anterior = editor.portapapeles
        editor.portapapeles = self.texto
    
    def deshacer(self, editor):
        editor.portapapeles = self.portapapeles_anterior
    
    def rehacer(self, editor):
        editor.portapapeles = self.texto

class Pegar(Accion):
    def __init__(self, texto, posicion):
        self.texto = texto
        self.posicion = posicion
    
    def ejecutar(self, editor):
        editor.texto = editor.texto[:self.posicion] + self.texto + editor.texto[self.posicion:]
    
    def deshacer(self, editor):
        editor.texto = editor.texto[:self.posicion] + editor.texto[self.posicion + len(self.texto):]
    
    def rehacer(self, editor):
        self.ejecutar(editor)