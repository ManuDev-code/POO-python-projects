#Liskov's substitution principle: Las clases derivadas pueden ser sustituidas por su clase base
# class Ave:
#     def volar(self):
#         return "Estoy volando wiiii"
    
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar :("
    
# def hacer_volar(ave: Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))

class Ave:
    pass #Acá se ponen todas las características que comparten voladoras y no voladoras

class AveVoladora(Ave):
    def volar(self): #Acá se definen solo las características de las aves voladoras
        return "Estoy volando"
    
class AveNoVoladora(Ave): #Acá solo características que tienen las clases que no vuelan
    pass

#Así cuando creemos un objeto de AveVoladora, hereda todas las características de Ave y de AveVoladora.
#Cuando creemos un AveNoVoladora, también hereda de Ave, pero no incorpora características como volar que no pertenecen a su nicho

#Esto permite un código más limpio y mantenible a lo largo del tiempo
