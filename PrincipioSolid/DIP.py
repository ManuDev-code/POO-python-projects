#Dependency Inversion Principle
# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #Lógica para verificar palabras
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self, texto):
#         #usamos el diccionario para corregir texto
#         pass

from abc import ABC, abstractmethod

#Acá Corrector ortográfico (clase principal) no depende del diccionario, sino que se implementa verificador ortografico para la abstracción y más adelante poder implementar mejoras
class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        #Lógica para verificar palabra
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Lógica para verificar si la palabra está en diccionario
        pass
    
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(Self, texto):
        #Usamos el verificador para corregir texto
        pass