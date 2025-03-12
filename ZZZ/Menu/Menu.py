from Operaciones import Sum, Rest, Mult, Div #Importa las operaciones de mi otro archivito
while True:
    print("===========MENÚ PRINCIPAL===========")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir \n")
    opc = int(input("Ingrese una opción: \n"))
    
    #Se pone esta opción antes que el usuario ingrese datos número ya que son innecesarios porque decidió salir del menú
    if opc == 5:
        print("Saliste del menú.")
        break #Sale automáticamente del ciclo while porque lo interrumple
    
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))
    
    match opc:
        case 1:
            print (f"El resultado de la suma es: {Sum(n1, n2)}")
        case 2:
            print (f"El resultado de la resta es: {Rest(n1, n2)}")
        case 3:
            print (f"El resultado de la multiplicación es: {Mult(n1, n2)}")
        case 4:
            print (f"El resultado de la división es: {Div(n1, n2)}")
        case _:
            print("Opción no válida.")   
            
print("Gracias por usar la ManuCalculadora") 
        
            