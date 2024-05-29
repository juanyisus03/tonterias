
import curses
import random
import time
SnakeBody = []      # Cuerpo de la serpiente
PlayerX = 1         # Posición inicial X del jugador
PlayerY = 1         # Posición inicial Y del jugador
e = " "             # Carácter de espacio
Player = "o"        # Representación del jugador
Dot = "♥"           # Representación del punto a recolectar
DotX = 0            # Posición X del punto
DotY = 0            # Posición Y del punto
Points = 0          # Puntos del jugador
gameOver = False    # Estado del juego (terminado o no)
lastKey = ""        # Última tecla presionada por el jugador
surpassRecord = False  # Indica si se ha superado el récord anterior
timeStart = 0
segundos = 0
lastTimeMove = 0.0
DIRECTIONS = {'a': (-1, 0), 'd': (1, 0), 'w': (0, -1), 's': (0, 1)}

# Imprime lo que va siendo el tablero del juego
def printBorders(stdscr):

    stdscr.addstr(1, 0, "╔═════════════════╗", curses.color_pair(1))
    for a in range(8):
        stdscr.addstr(a + 2, 0, "║", curses.color_pair(1))
        stdscr.addstr(a + 2, 18, "║", curses.color_pair(1))
    stdscr.addstr(10, 0, "╚═════════════════╝", curses.color_pair(1))
    stdscr.addstr(11, 0, "Si te cansas pulse q para salir")


def printPlayer(stdscr):
    for i, body in enumerate(SnakeBody):
        stdscr.addstr(body[0]+1, body[1]+1, body[2], curses.color_pair(3))

    stdscr.addstr(PlayerY+1, PlayerX+1, Player,  curses.color_pair(3))


def deletePlayer(stdscr):
    for i, body in enumerate(SnakeBody):
        stdscr.addstr(body[0]+1, body[1]+1, " ", curses.color_pair(3))

    stdscr.addstr(PlayerY+1, PlayerX+1, " ",  curses.color_pair(3))

# Comprueba si el punto ha sido obtenido por el jugador
def checkDot(stdscr):
    global PlayerX, PlayerY, Player, DotY, DotX, Points, SnakeBody
    if (PlayerX == DotX and PlayerY == DotY):
        SnakeBody.append([PlayerY, PlayerX, Player])
        generateDot(stdscr)
        Points += 10

# Movimiento del cuerpo del jugador
def moveSnakeBody(bodyY, bodyX):
    global SnakeBody
    for i in range(len(SnakeBody) - 1, 0, -1):
        SnakeBody[i][0] = SnakeBody[i-1][0]
        SnakeBody[i][1] = SnakeBody[i-1][1]
        SnakeBody[i][2] = SnakeBody[i-1][2]
    if (len(SnakeBody) >= 1):
        SnakeBody[0][0] = bodyY
        SnakeBody[0][1] = bodyX
        SnakeBody[0][2] = Player

# Comprueba si el juego a terminado al colisionar contigo mismo
def checkStatus():
    global PlayerX, PlayerY, SnakeBody, gameOver
    for body in SnakeBody:
        if (body[0] == PlayerY and body[1] == PlayerX):
            gameOver = True

# Movimiento del jugador, dentro de este método se llama al movimiento del cuerpo y comprobación de colisiones
def movePlayer(o, stdscr):
    global PlayerX, PlayerY, Player, DotY, DotX, Points, lastKey, lastTimeMove, timeStart

    bodyY = PlayerY
    bodyX = PlayerX

    if (o == ord("a") and PlayerX > 0 and lastKey != ord("d")):
        deletePlayer(stdscr)
        lastKey = ord("a")
        bodyX = PlayerX
        PlayerX -= 1
        if (PlayerX == 0):
            PlayerX = 15
        Player = "<"
        checkDot(stdscr)
        moveSnakeBody(bodyY, bodyX)
        printPlayer(stdscr)
        lastTimeMove = time.time() - timeStart

    if (o == ord("d") and PlayerX < 16 and lastKey != ord("a")):
        deletePlayer(stdscr)
        lastKey = ord("d")
        bodyX = PlayerX
        PlayerX += 1
        if (PlayerX == 16):
            PlayerX = 1
        Player = ">"
        checkDot(stdscr)
        moveSnakeBody(bodyY, bodyX)
        printPlayer(stdscr)
        lastTimeMove = time.time() - timeStart

    if (o == ord("s") and PlayerY < 9 and lastKey != ord("w")):
        deletePlayer(stdscr)
        lastKey = ord("s")
        bodyY = PlayerY
        PlayerY += 1
        if (PlayerY == 9):
            PlayerY = 1
        Player = "v"
        checkDot(stdscr)
        moveSnakeBody(bodyY, bodyX)
        printPlayer(stdscr)
        lastTimeMove = time.time() - timeStart

    if (o == ord("w") and PlayerY > 0 and lastKey != ord("s")):
        deletePlayer(stdscr)
        lastKey = ord("w")
        bodyY = PlayerY
        PlayerY -= 1
        if (PlayerY == 0):
            PlayerY = 8
        Player = "^"
        checkDot(stdscr)
        moveSnakeBody(bodyY, bodyX)
        printPlayer(stdscr)
        lastTimeMove = time.time() - timeStart

    checkStatus()



# Genero el punto donde pondré el corazón
def generateDot(stdscr):
    global DotX, DotY
    validPosition = False
    stdscr.addstr(DotY+1, DotX+1, " ", curses.color_pair(2))
    while (validPosition == False):
        validPosition = True
        DotX = random.randint(1, 15)
        DotY = random.randint(1, 8)
        for body in SnakeBody:
            if (body[0] == DotY and body[1] == DotX):
                validPosition = False
        if (DotX == PlayerX and DotY == PlayerY):
            validPosition = False
    stdscr.addstr(DotY+1, DotX+1, Dot, curses.color_pair(2))

# Muestra la información básica del juego


def showControls(stdscr):
    stdscr.addstr(0, 0, "Juego de la serpiente")
    stdscr.addstr(1, 0, "---------------------")
    stdscr.addstr(3, 0, "-Para moverte arriba ↑ pulsa w")
    stdscr.addstr(5, 0, "-Para moverte abajo ↓ pulsa s")
    stdscr.addstr(7, 0, "-Para moverte izquierda ← pulsa a")
    stdscr.addstr(9, 0, "-Para moverte derecha → pulsa d")
    stdscr.addstr(11, 0, "Consigue corazones a para conseguir puntos")
    stdscr.addstr(13, 0, "Pulse cualquier tecla para continuar....")
    stdscr.getch()


def main(stdscr):
    global gameOver, surpassRecord, timeStart, lastKey, segundos, PlayerY, lastTimeMove
    o = ""
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    showControls(stdscr)
    stdscr.clear()
    generateDot(stdscr)
    printBorders(stdscr)
    printPlayer(stdscr)
    timeStart = time.time()

    stdscr.nodelay(1)

    # Intento obtener el record del fichero pointsSnake.csv, si este no llega a existir lo crea el fichero
    record = ""
    try:
        with open("pointsSnake.csv", "r") as file:

            record = file.readlines()[-1]

    except FileNotFoundError:
        with open("pointsSnake.csv", "w") as file:
            file.write("# Record de puntos en el juego de la serpiente\n")
            file.write("# Este archivo guarda el record del juego\n")
            file.write("# No edite manualmente este archivo\n")
            file.write("0")
            pass
    if (record == ""):
        record = 0
    else:
        record = int(record)

    # Ciclo del juego
    while (o != ord("q") and gameOver == False):
        o = stdscr.getch()
        if (o != ord("q")):
            movePlayer(o, stdscr)



        if (Points > record):
            record = Points
            surpassRecord = True

        if(Points < 20):
            diff = 1
        elif(Points//20 < 10):
            diff = Points//20 

        if (segundos - lastTimeMove > 1/diff and lastKey != ""):
            movePlayer(lastKey, stdscr)
        
        segundos = time.time() - timeStart
        stdscr.addstr(0, 0, "Points: " + str(Points) + "    Record: " + str(record) +
                      "    Time: " + "{:02d}:{:02d}".format(int(segundos) // 60, int(segundos) % 60)+ "    Velocidad: " + str(diff))

    stdscr.clear()
    stdscr.nodelay(0)
    stdscr.addstr(0,0,"Fin de la Partida")
    # Comprueba si has superado el record y lo guarda en el fichero
    if (surpassRecord):
        with open("pointsSnake.csv", "w") as file:
            file.write("# Record de puntos en el juego de la serpiente\n")
            file.write("# Este archivo guarda el record del juego\n")
            file.write("# No edite manualmente este archivo\n")
            file.write(str(Points))

        stdscr.addstr(1, 0, "Nuevo record!!!")
    stdscr.addstr(2, 0, "Pulse cualquier tecla para continuar....")
    stdscr.getch()


curses.wrapper(main)
