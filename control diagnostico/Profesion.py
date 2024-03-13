from Persona import Persona
class Profesion(Persona):
    def __init__(self, Nombre, Sueldo = 0, Cantidad_personas = 0):
        super().__init__(Nombre, None, None)
        self._Nombre = Nombre
        self._Sueldo = Sueldo
        self._Cantidad_personas = Cantidad_personas
        
        

    def get_sueldo(self):
        return self._Sueldo
    def get_Cantidad_p(self):
        return self._Cantidad_personas
   
    def set_sueldo(self, cambio_sueldo):
        self._Sueldo = cambio_sueldo
    def set_Cantidad_P(self, cambio_p):
        self._Cantidad_personas = cambio_p
    

