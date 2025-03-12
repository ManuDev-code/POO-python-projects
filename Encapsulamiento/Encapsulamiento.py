class Persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, new_name):
        self.nombre = new_name
        
manuela = Persona("Manuela", 18)

nombre = manuela.get_nombre()
print(nombre)
manuela.set_nombre("Manuelita")
nombre = manuela.get_nombre()
print(nombre)
