class Animal():
    def comer(self):
        print("El animal está comiendo")
        
class Ave(Animal):
    def volar(self):
        print("El animal está volando")
        
class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando")
        
class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()
murcielago.comer()
murcielago.volar()
murcielago.amamantar()

#MRO (Orden de Resolución de Métodos) es un aspecto crucial en la programación orientada a objetos en Python. Es el orden en que Python busca en las clases base de un objeto para encontrar un método o atributo durante la ejecución12

print(Murcielago.mro())