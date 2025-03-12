#Aprendiendo a crear clases
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
        
manuela = Estudiante("Manuela", "18", "Pregrado")
print(manuela.grado)