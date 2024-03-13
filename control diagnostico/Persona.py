class Persona():
    def __init__(self, Nombre = "", Edad = 0,Sexo =""):
        self._Nombre = Nombre 
        self._Edad = Edad 
        self._Sexo = Sexo
    def get_nombre(self):
        return self._Nombre
    def get_Edad(self):
        return self._Edad
    def get_sexo(self):
        return self._Sexo
    
    def set_nombre(self, cambio_n):
        self._Nombre = cambio_n
    def set_Edad(self, cambio_e):
        self._Edad = cambio_e
    def set_sexo(self, cambio_s):
        self._Sexo = cambio_s
