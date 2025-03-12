#Interface Segregation Principle
from abc import ABC, abstractmethod

#Acá cada clase se encarga de una pequeña funcionalidad, segregamos la interfaz.
#Porque si tenemos todas las características de trabajador: Trabajar, comer y dormir,
# robot no duerme ni come entonces no implementa esos métodos y sale error si no los llamamos, 
# pero crear solo una función con 'PASS' es inútil así que segregamos la interfaz trbajador y 
# creamos dos más para poder implementar solo lo que queramos.
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass
    
    
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Trabajador, Comedor, Durmiente):
    
    def comer(self):
        print("El humano está comiendo")
    
    def trabajar(self):
        print("El humano está trabajando")
        
    
    def dormir(self):
        print("El humano está durmiendo")
        

class Robot(Trabajador):
    def trabajar(self):
        print("El robot está trabajando")
        
robot = Robot()
robot.trabajar()

humano = Humano()
humano.trabajar()
humano.comer()
humano.dormir()
        
        
    