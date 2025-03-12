from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad, grado):
        super().__init__(nombre, edad, sexo, actividad)
        self.grado = grado
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy actualmente estoy trabajando en el campo de: {self.actividad}")
        
estudiante = Estudiante("Manuela", 18, "Femenino", "programacion", 11)
trabajador = Trabajador("Elon Musk", 45, "Masculino", "magnate millonario")
estudiante.presentarse()
estudiante.hacer_actividad()
trabajador.presentarse()
trabajador.hacer_actividad()