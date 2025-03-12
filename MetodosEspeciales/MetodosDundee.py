class Persona:
    def __init__(self, nombre, edad): #init es un método especiañ
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self): #str es un método especial que permite imprimir en pantalla los valores del objeto creado como una cadena de texto
        return f"persona: {self.nombre}, {self.edad}"
    
    def __repr__(self): #Genera representación del objeto y también se puede imprimir en pantalla
        return f"Persona('{self.nombre}', {self.edad})"
    
    #Decir cómo se comportan los objetos de la clase persona cuando se suman
    #Se conoce como sobrecarga de operadores
    def __add__ (self, otro):
        nueva_edad = self.edad + otro.edad
        nuevo_nombre = "AwiMawe"
        return Persona(nuevo_nombre, nueva_edad)
    
persona1 = Persona("Manu", 18)
persona2 = Persona("Osmer", 50)
persona3 = Persona("Ana", 40)

resultado = persona1 + persona2 + persona3
print(resultado)