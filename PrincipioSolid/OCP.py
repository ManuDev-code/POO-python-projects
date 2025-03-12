#Open/Closed principle: La clase se puede expandir pero no modifica su estructura base
#Si sé que en un futuro voy a mejorar mi programa, debo crear una estructura que se deje añadir más funciones pero sin modificar su estructura base. Como lo haré en este ejemplo
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
        
    def notificar(self):
        raise NotImplementedError #clase que notifica y obliga al developer a usarla
    
#Esto es suponiendo que "usuario" es otra clase y tiene la propiedad email
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje a {self.usuario.email}")
        
#Esto es suponiendo que "usuario" es otra clase y tiene la propiedad SMS
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")
        
#Esto es suponiendo que "usuario" es otra clase y tiene la propiedad whatsApp
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando whatsApp a {self.usuario.whatsapp}")