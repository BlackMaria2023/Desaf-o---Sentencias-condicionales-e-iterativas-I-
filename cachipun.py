import random

def jugar_cachipun():
    opciones = ["piedra", "papel", "tijera"]
    
    eleccion_usuario = input("Elige piedra, papel o tijera: ")
    print(f"Jugaste: {eleccion_usuario}")
    
    eleccion_computador = random.choice(opciones)
    
    print(f"El computador jugó: {eleccion_computador}")

    if eleccion_usuario == eleccion_computador:
       print ("Oh, es un empate!!")
    elif eleccion_usuario == "piedra" and eleccion_computador == "tijera":
         print ("Ganaste!!")
    elif  eleccion_usuario == "papel" and eleccion_computador == "piedra":
        print ("Ganaste!!")
    elif  eleccion_usuario == "tijera" and eleccion_computador == "papel":
        print ("Ganaste!!")
    elif  eleccion_usuario != (opciones) :
        print ("Argumento inválido: Debe ser piedra, papel o tijera")
    else:
        print ("Perdiste!!")

jugar_cachipun()