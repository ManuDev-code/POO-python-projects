class CuentaBancaria:
    def __init__(self, nombre, saldo, contraseña):
        self.__nombre = nombre
        self.__saldo = saldo
        self.__contraseña = contraseña
     
    #Getters  
    @property 
    def lechuga(self):
        return self.__nombre
    
    @property 
    def pimenton(self):
        return self.__saldo
    
    @property 
    def champiñon(self):
        return self.__contraseña
    
    #Setters
    @lechuga.setter
    def lechuga(self, new_name):
        self.__nombre = new_name
        
    @pimenton.setter
    def pimenton(self, new_saldo):
        self.__saldo = new_saldo
        
    @champiñon.setter
    def champiñon(self, new_contraseña):
        self.__contraseña = new_contraseña
        
    #Deleter
    @lechuga.deleter #Esto borra el nombre, pero no lo ejecuto en este código porque dejarían de funcionar las demás funciones
    def lechuga(self):
        del self.__nombre

#Crear la instancia de la clase    
victima1 = CuentaBancaria("Elon Musk", "infinito", "MarcianosMisAmores")

#Acceder a las propiedades (getter)
olla_arrocera = victima1.lechuga
limpia_pisos = victima1.pimenton
sarten = victima1.champiñon

print(f"Datos re importantes pero con nombres distractores: \n {olla_arrocera}, {limpia_pisos}, {sarten}")    

#Cambiar el nombre usando el setter
victima1.lechuga = "Cambio de nombre"
print(victima1.lechuga)

#ManuExperimento: Para imprimir cada atributo de victima1
for propiedad in ['lechuga', 'pimenton', 'champiñon']:
    value = getattr(victima1, propiedad)
    #getattr = (el objeto del que queremos obtener atributo, nombre del atributo)
    print(f"{propiedad} = {value}")

# lechuga = Elon Musk
# pimenton = infinito
# champiñon = MarcianosMisAmores


