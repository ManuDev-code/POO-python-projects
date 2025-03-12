#UTILIZAR DECORADORES AHORA
def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar la función saludo")
        funcion()
    return funcion_modificada

@decorador
def saludo():
    print("Hola cómo vas")
    
saludo()



#ANTES PARA CREAR DECORADORES ERA ASÍ
# def decorador(funcion):
#     #La función decoradora crea una función
#     def funcion_modificada():
#         #Primero se ejecuta este códgio
#         print("Antes de llamar a la funcion")
#         #Después se ejecuta la función que pasamos como parámetro
#         funcion()
#         #Ejcueta un código después
#         print("Despues de llamar a la funcion")
#     #Y al final nos devuelve la funcion que creó    
#     return funcion_modificada

# def saludo():
#     print("Hola mundo")
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()