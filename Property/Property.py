#No confundir con propiedades de clase, son getters, setter y deletters
class Persona:
    def __init__ (self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    def set_nombre(self, new_name):
        self._nombre = new_name
        
manuela = Persona("Manuela", 18)

nombre = manuela.get_nombre
print(nombre)

