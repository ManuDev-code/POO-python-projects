class Auto():
    def __init__ (self):
        self._estado = "apagado"
        
    def encender(self):
        self._estado = "encendido"
        print("El auto está encendido")
        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
mi_mercedes = Auto()
#Acá ya hay abstracción porque el user no sabe que hacemos la validación del if para que se muestre el mensaje.
#Le damos el método conducir() que le simplifica la vida porque ya nosotros le creamos la lógica y le entregamos todo hecho.
mi_mercedes.conducir()
