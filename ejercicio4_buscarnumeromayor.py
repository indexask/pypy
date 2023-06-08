"""
TAREA
1. Primera parte
   a) Crear una función que reciba dos números
   b) La función debe retorna el mayor de los dos
   c) Desde el Main leer dos números y llamar a la función
      para buscar al mayor

2. Parte
   a) Agregar validaciones y excepciones
   b) Qué cambios hay que realizar para verificar, además si los
      números son iguales
   c) Agregar funciones para leer los números y repetir el proceso
"""
def numeroMayor(a,b):
    if a > b:
        return a
    else:
        return b
    
def numeroIgual(a,b):
    return a==b
    

def leerNumero():
    while True:
        try:
            num1 = int(input("Ingresar numero 1: "))
            num2 = int(input("Ingresar numero 2: "))
            print("Numero mayor es:", numeroMayor(num1,num2))
            if numeroIgual(num1,num2):
                print("Los numeros son iguales")
            else:
                print("los numeros no son iguales")
            break
        except:
            print("Ingresar un numero correcto")
leerNumero()
