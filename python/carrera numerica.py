import random

print("=== CARRERA NUMÉRICA ===")

while True:
    jugadores = int(input("Cantidad de jugadores (2-4): "))

    if jugadores >= 2 and jugadores <= 4:
        break

    print("Debe ingresar entre 2 y 4 jugadores")

print("\nNIVELES")
print("1. Básico = 20")
print("2. Intermedio = 30")
print("3. Avanzado = 50")
print("4. Experto = 100")

nivel = input("Elija un nivel: ")

if nivel == "1":
    meta = 20
elif nivel == "2":
    meta = 30
elif nivel == "3":
    meta = 50
elif nivel == "4":
    meta = 100
else:
    meta = 20

posiciones = [0, 0, 0, 0]
dobles = [0, 0, 0, 0]

ganador = False
turno = 0

while ganador == False:

    print("\nTurno jugador", turno + 1)
    input("ENTER para lanzar dados")

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    print("Dado 1:", dado1)
    print("Dado 2:", dado2)

    suma = dado1 + dado2
    posiciones[turno] = posiciones[turno] + suma

    if posiciones[turno] > meta:
        posiciones[turno] = meta

    print("Posición jugador", turno + 1, ":", posiciones[turno])

    if dado1 == dado2:
        dobles[turno] = dobles[turno] + 1
        print("Dobles consecutivos:", dobles[turno])

        if dobles[turno] == 3:
            print("\nJugador", turno + 1, "gana por 3 dobles consecutivos")
            ganador = True
    else:
        dobles[turno] = 0

    if posiciones[turno] == meta:
        print("\nJugador", turno + 1, "ganó la carrera")
        ganador = True

    turno = turno + 1

    if turno == jugadores:
        turno = 0