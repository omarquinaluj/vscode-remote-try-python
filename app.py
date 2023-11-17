
import random

# lista de opciones de juego
opciones = ["piedra", "papel", "tijeras"]

# función que elige una opción aleatoria de la lista de opciones
def opcion_aleatoria():
    return random.choice(opciones)

# función que pide al jugador que elija una opción y la valida
def elegir_opcion():
    while True:
        opcion = input("Elige una opción (piedra, papel o tijeras): ").lower()
        if opcion in opciones:
            return opcion
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# función que compara la opción del jugador con la opción del oponente y determina el resultado de la ronda
def comparar_opciones(jugador, oponente):
    if jugador == oponente:
        return "empate"
    elif jugador == "piedra":
        if oponente == "tijeras":
            return "ganaste"
        else:
            return "perdiste"
    elif jugador == "papel":
        if oponente == "piedra":
            return "ganaste"
        else:
            return "perdiste"
    elif jugador == "tijeras":
        if oponente == "papel":
            return "ganaste"
        else:
            return "perdiste"

# función que muestra el resultado de la ronda y actualiza la puntuación del jugador
def mostrar_resultado(resultado, puntuacion):
    if resultado == "ganaste":
        puntuacion += 1
    elif resultado == "perdiste":
        puntuacion -= 1
    print(f"Resultado: {resultado}")
    print(f"Puntuación: {puntuacion}")
    return puntuacion

# función que pregunta al jugador si quiere jugar de nuevo
def jugar_de_nuevo():
    while True:
        respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("Respuesta no válida. Inténtalo de nuevo.")

# función que muestra la puntuación final del jugador
def mostrar_puntuacion_final(puntuacion):
    print(f"Puntuación final: {puntuacion}")

# función principal del juego
def jugar():
    print("¡Bienvenido al juego de piedra, papel o tijeras!")
    puntuacion = 0
    while True:
        oponente = opcion_aleatoria()
        jugador = elegir_opcion()
        resultado = comparar_opciones(jugador, oponente)
        puntuacion = mostrar_resultado(resultado, puntuacion)
        if not jugar_de_nuevo():
            mostrar_puntuacion_final(puntuacion)
            break

# ejecutar el juego
jugar()



