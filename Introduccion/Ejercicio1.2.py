#Creando clases interactivas con el usuario
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
            print("Estudiando")
            
nombre = input("Escribe tu nombre: ")
edad = input("Escribe tu edad: ")
grado = input("Escribe tu grado: ")

estudiante = Estudiante(nombre, edad, grado) #Pasamos los argumentos del constructor con las variables que llenó el usuario en el input()
print(f"""
      el estudiante se llama: {estudiante.nombre} \n
      tiene {estudiante.edad} \n
      y se encuentra en {estudiante.grado}
      """)

while True:
    estudiar = input()
    if(estudiar.lower() == "estudiar"):
        estudiante.estudiar()
