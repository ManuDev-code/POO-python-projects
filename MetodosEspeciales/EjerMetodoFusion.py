class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre}: (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro):
        nuevo_nombre = self.nombre + "_" + otro.nombre
        nueva_fuerza = round(((self.fuerza+otro.fuerza)/2)**2)
        nueva_velocidad = round(((self.fuerza + otro.fuerza)/2)**2)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
personaje1 = Personaje("Twilight", 100, 100)
personaje2 = Personaje("Spike", 10, 5)
personaje3 = Personaje("Rarity", 60, 80)

print(personaje1)
print(personaje2)
print(personaje3)
fusion = personaje1 + personaje2 + personaje3
print(fusion)