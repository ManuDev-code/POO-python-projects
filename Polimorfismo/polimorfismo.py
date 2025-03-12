#Al enviar el mismo mensaje las respuestas de los objetos, clases y métodos son totalmente diferentes
class Gato():
    
    #Vamos a aplicar str para que al llamar al objeto se muestre el nombre de la clase de la que se instancio
    def sonido(self):
        return("Miau")
    
    def __str__(self):
        return "gato"  #El str evuelve un texto que representa al objeto de manera más legible: "gato"
    
class Perro():
    def sonido(self):
        return("Guau")
    
    def __str__(self):
        return "perro"
    
    
def hacer_sonido(animal):
    print(f"el {animal} esta haciendo {animal.sonido()}")
    
#Aplicar polimorfismo: El método es el mismo pero salen mensajes diferentes
gato = Gato()
perro = Perro()
print(gato.sonido()) #Sale miau
print(perro.sonido()) #Sale guau
hacer_sonido(perro)
hacer_sonido(gato)