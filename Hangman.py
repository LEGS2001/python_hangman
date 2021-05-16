import random 
import os, sys

palabras = []


def Menu():
    palabras.clear()
    opcion = int(input("Ingrese el numero de la categoria deseada.\n1)Anime\n2)Videojuegos\n3)Salir\n"))
    if opcion == 1:
        categoria = "Anime.txt"
    elif opcion == 2:
        categoria = "Videojuegos.txt"
    elif opcion == 3:
        quit()
    else:
        print("La opcion ingresada no es valida")
        pass

    try:
        archivo = open(os.path.join(sys.path[0], "Hangman_%s" %categoria), 'r')
        for line in archivo:
            if line != "\n":
                palabras.append(line.strip("\n"))
        archivo.close()
    except:
        print("No se ha encontrado el archivo deseado")
        Menu()

def Juego():
    palabra = palabras[random.randint(0,len(palabras) - 1)]
    palabra_encriptada = []
    intentos = 6
    palabra = palabra.upper()
    palabra_lista = list(palabra.upper())
    letras_usadas = []

    #Crea lista de la palabra encriptada
    for i in palabra:
        if i == " ":
            palabra_encriptada.append(" ")
        else:
            palabra_encriptada.append("-")
    print(",".join(palabra_encriptada).replace(",",""))

    #Pregunta por una letra
    while(True):
        respuesta = input("Ingrese una letra \n").upper()
        if respuesta == "SALIR":
            break
        if len(respuesta) != 1:
            print("La letra ingresada no es valida")
            continue


        if respuesta not in letras_usadas:
            #Remplazar la palabra encriptada con letras adivinadas correctamente
            for i in range(0, len(palabra)):
                if respuesta == palabra_lista[i]:
                    palabra_encriptada[i] = respuesta
                    if respuesta not in letras_usadas:
                        letras_usadas.append(respuesta)
                        
            #Revisar si la letra no esta en la palabra
            if respuesta not in palabra and respuesta not in letras_usadas:
                intentos -= 1
                print("Te quedan ", intentos, " intentos")
                letras_usadas.append(respuesta)
        else:
            print("Ya intentaste con esta letra")

        #Revisa si ya se han adivinado todas las letras
        if "".join(palabra_encriptada) == palabra:
            print("Felicidades! Has ganado!")
            continuar = int(input("Desea continuar?\n 1)Si\n 2)No\n"))
            if continuar == 1:
                Menu()
                Juego()
            else:
                quit()

        if intentos <= 0:
            print("Te has quedado sin intentos")
            print("La respuesta correcta era " + palabra)
            Menu()
            Juego()
        
        print(",".join(palabra_encriptada).replace(",",""))
        print("Las letras que has intentado son: " + ",".join(letras_usadas))
        print("========================================================================================")

Menu()
Juego() 

