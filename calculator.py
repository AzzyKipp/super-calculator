print ("Hola Usuario! En este programa podrás realizar las operaciones aritméticas básicas.")
print("Presiona el número indicado según la operación que desees realizar")

calculating = True

def resta(n1, n2):
    return n1 - n2

while calculating:
    print ("1. Sumar")
    print ("2. Restar")
    print ("3. Multiplicar ")
    print ("4. Dividir")
    print ("5. Salir")
    
    user_input = int(input())
    
    if user_input == 2:
        n1 = int(input("Escribe el primer número: "))
        n2 = int(input("Escribe el número con el que deseas restar: "))
        print(f"{n1} - {n2} = {resta(n1,n2)}")
        break

