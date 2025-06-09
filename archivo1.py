try:
    mi_archivo = open("C://texto_file.txt", "r")
    contenido = mi_archivo.read()
    print(contenido)
    mi_archivo.close()
except FileNotFoundError:
    print("El archivo no se encuentra")
