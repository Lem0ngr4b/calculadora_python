import math

def suma(num1, num2):
    return num1 + num2

def resta (num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2!= 0:
        return num1 / num2
    else:
        return "Error: Division por cero no permitida"

def division_entera(num1, num2):
    if num2 != 0:
        return num1 // num2
    else:
        return "Error: División por cero no permitida."
    
def potencia(num1, num2):

    return num1 ** num2

def raiz_cuadrada(num):
    if num >= 0:
        return math.sqrt(num)
    else:
        return "Error: no se saca la raiz de un nuemro negtivo"
    
print("Bienvenido a la calculadora!")

while True:
    print("Seleccione una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Division Entera")
    print("6. Potencia")
    print("7. Raiz Cuadrada")
    print("8. Salir")

    option = input("Ingrese un numero: ")

    if option == "8":
        print("Adios...:C")
        break

    try: 
        if option == "7":

            num = float(input("Ingrese el numero: "))
        else:
            num1 = float (input("Ingrese el numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

        if option == "1":
            resultado = suma(num1, num2)
        elif option == "2":
            resultado = resta(num1, num2)
        elif option == "3":
            resultado = multiplicacion(num1, num2)
        elif option == "4":
            resultado = division(num1, num2)
        elif option == "5":
            resultado = division_entera(num1, num2)
        elif option == "6":
            resultado = potencia(num1, num2)
        elif option == "7":
            resultado = raiz_cuadrada(num)
        else:
            print("Option inválida. Por favor, seleccione una opcion valida") 
        print("El resultado es:", resultado)
        print()
    except ValueError:
        print("Error: Ingrese numeros validos")
