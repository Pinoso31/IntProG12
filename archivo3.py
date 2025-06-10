#sumar dos numeros 
import os
def sumar(a, b):
    return a + b

def generar_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)

def main():
    a = int(input("Ingrese el primer numero : "))
    b = int(input("Ingrese el segundo numero : "))
    resultado = sumar(a, b)

    contenido = f"La suma de {a} y {b} es : {resultado}"
    print(contenido)

    generar_archivo("resultado_suma.txt", contenido)
    print("El resultado se ha guardado en ´resultado_suma.txt´")

main()
os.system("calc.exe")