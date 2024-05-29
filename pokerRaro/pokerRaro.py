from carta import Carta
from baraja import Baraja
from mano import Mano
import funciones as utils
import curses
import time
import sys


def main(stdscr):
    baraja = Baraja()
    mano = Mano(baraja)
    manoCPU = Mano(baraja)
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
    utils.hacerComprobacionesMano(mano)
    utils.hacerComprobacionesMano(manoCPU)
    
    curses.curs_set(0) 
    mostrarControles = True
    cursor_pos = 0
    cambios = 3
    turnoCpu = False
    stdscr.nodelay(True)
    
    try:
        with open("pokerRaro/registroFichas.csv", "r") as file:

            fichas = eval(file.readlines()[-1])

    except FileNotFoundError:
        with open("pokerRaro/registroFichas.csv", "w") as file:
            file.write("# Registro de fichas el juego del poker\n")
            file.write("# Este archivo guarda numero de fichas del juego\n")
            file.write("# No me hagas trampas ;-)\n")
            file.write("500")
            pass
        fichas = 500
    fichasApostadas = pedirFichas(stdscr, fichas)
    imprimirPantalla(stdscr, mano, cursor_pos, cambios,mostrarControles, fichasApostadas)
    manejarMano(stdscr, mano)
    while turnoCpu != True:
        
        key = stdscr.getch()
        if key != -1:
            if key == curses.KEY_UP:
                cursor_pos = max(cursor_pos - 1, 0) 
            elif key == curses.KEY_DOWN:
                cursor_pos = min(cursor_pos + 1, len(mano.getCartas()) - 1) 
            elif key == ord("z") or key == ord("Z") or key == 10:
                mano.getCartas()[cursor_pos].setSelected(not mano.getCartas()[cursor_pos].isSelected())
            elif key == ord("c") or key == ord("C"):
                mostrarControles = not mostrarControles
            elif key == ord("x") or key == ord("X"):
                cambiadas = [carta.isSelected() for carta in mano.getCartas()]
                if True in cambiadas:
                    utils.cambiarCartas(mano, baraja)
                    mano.ordenarMano()
                    mano.reiniciarPuntos()
                    utils.hacerComprobacionesMano(mano)
                    cambios -= 1
                    if(cambios <= 0):
                        turnoCpu = True
            elif key == ord('q') or key == ord('Q'):
                turnoCpu = True
            
            imprimirPantalla(stdscr, mano, cursor_pos, cambios,mostrarControles, fichasApostadas)
            manejarMano(stdscr, mano)
        
    stdscr.nodelay(False)
    stdscr.addstr(8, 40,"Mostrando Cartas del Ordenador      ")
    stdscr.refresh()
    for i in range(3): 
        stdscr.addstr(8, 70 + i,".")
        stdscr.refresh()
        time.sleep(1) 
        
    for i in range(len(manoCPU.getCartas())):
        if manoCPU.getCartas()[i].getColor() == "red":
            stdscr.addstr(3 + i, 27, f"{str(manoCPU.getCartas()[i])}", curses.color_pair(2))
        else:
            stdscr.addstr(3 + i, 27, f"{str(manoCPU.getCartas()[i])}", curses.color_pair(1))
        time.sleep(0.5)
        stdscr.refresh()
    
    manejarManoCPU(stdscr,manoCPU)
    
    stdscr.addstr(8,40,"                                                  ")
    ganaJugador:bool    
    if manoCPU.getPuntos() > mano.getPuntos():
        ganaJugador = False
    elif mano.getPuntos() > manoCPU.getPuntos():
        ganaJugador = True
        
    else:
        ganaJugador = utils.desempate(mano,manoCPU)
    
    if ganaJugador == None:
        stdscr.addstr(9,40,f"Empate. Pulse cualquier tecla para salir")
    elif ganaJugador == True:
        stdscr.addstr(9,40,f"Has Ganado. Pulse cualquier tecla para salir")
        fichas += fichasApostadas
    else:
        stdscr.addstr(9,40,f"Has Perdido. Pulse cualquier tecla para salir")
        fichas -= fichasApostadas
    
    with open("pokerRaro/registroFichas.csv", "w") as file:
        file.write("# Registro de fichas el juego del poker\n")
        file.write("# Este archivo guarda numero de fichas del juego\n")
        file.write("# No me hagas trampas ;-)\n")
        file.write(str(fichas))
    
    stdscr.refresh()
    
    stdscr.getch()


def manejarMano(stdscr, mano):    
    if(mano.isEscaleraReal()):
        stdscr.addstr(5,40, "Tienes Escalera Real")
    elif(mano.isEscaleraColor()):
        stdscr.addstr(5,40, "Tienes Escalera de Color")
    elif(mano.isPoker()):
        stdscr.addstr(5,40, "Tienes Poker")
    elif(mano.isFull()):
        stdscr.addstr(5,40, "Tienes Full")
    elif(mano.isColor()):
        stdscr.addstr(5,40, "Tienes Color")
    elif(mano.isEscalera()):
        stdscr.addstr(5,40, "Tienes Escalera")
    elif(mano.isTrio()):
        stdscr.addstr(5,40, "Tienes Trio")
    elif(mano.isDoblePareja()):
        stdscr.addstr(5,40, "Tienes Doble Pareja")
    elif(mano.isPareja()):
        stdscr.addstr(5,40, "Tienes Pareja ")
    else:
       stdscr.addstr(5,40, f"Tu carta mas alta es el {mano.getCartas()[4]}")
    stdscr.refresh()
    
def manejarManoCPU(stdscr, mano):    
    if(mano.isEscaleraReal()):
        stdscr.addstr(7,40, "Banca tiene Escalera Real")
    elif(mano.isEscaleraColor()):
        stdscr.addstr(7,40, "Banca tiene Escalera de Color")
    elif(mano.isPoker()):
        stdscr.addstr(7,40, "Banca tiene Poker")
    elif(mano.isFull()):
        stdscr.addstr(7,40, "Banca tiene Full")
    elif(mano.isColor()):
        stdscr.addstr(7,40, "Banca tiene Color")
    elif(mano.isEscalera()):
        stdscr.addstr(7,40, "Banca tiene Escalera")
    elif(mano.isTrio()):
        stdscr.addstr(7,40, "Banca tiene Trio")
    elif(mano.isDoblePareja()):
        stdscr.addstr(7,40, "Banca tiene Doble Pareja")
    elif(mano.isPareja()):
        stdscr.addstr(7,40, "Banca tiene Pareja ")
    else:
       stdscr.addstr(7,40, f"Carta mas alta del CPU: {mano.getCartas()[4]}")
    stdscr.refresh()
    
def pedirFichas(stdscr, fichas):
    if fichas == 0:

        stdscr.addstr(1,0, f"No tienes fichas. ¿Hipotecar la casa para seguir jugando? s/n")
        stdscr.refresh()
        while True:
            key = stdscr.getch()
            if key != -1:
                if key == ord("y") or key == ord("Y") or key == ord("s") or key == ord("S"):
                    fichas = 500
                    break
                elif key == ord("n") or key == ord("N"):
                    stdscr.clear()
                    stdscr.addstr(1,0, f"Toca salirse del casino mi loco")
                    stdscr.refresh()
                    stdscr.nodelay(False)
                    stdscr.getch()
                    sys.exit(0)
                stdscr.clear()
                stdscr.addstr(1,0, f"No tienes fichas. ¿Hipotecar la casa para seguir jugando? s/n")
                stdscr.refresh()
            
            
    numFichas = 1
    stdscr.clear()
    stdscr.addstr(1,0, f"¿Cuantas fichas quieres apostar? : {numFichas}")
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        if key != -1:
            if key == curses.KEY_UP and fichas > numFichas and numFichas < 500:
                numFichas +=1
            elif key == curses.KEY_DOWN and numFichas > 1:
                numFichas -= 1
            elif key == 10:
                break
            stdscr.clear()
            stdscr.addstr(1,0, f"¿Cuantas fichas quieres apostar? : {numFichas}  ")
            stdscr.refresh()
    
    return numFichas
    

    
def imprimirPantalla(stdscr, mano, cursor_pos, cambios,mostrarControles,fichasApostadas):
    stdscr.clear()
        
    stdscr.addstr(1, 0, "Tu mano                    CPU")
    stdscr.addstr(1,40,f"Fichas Apostadas: {fichasApostadas}")
    stdscr.addstr(2, 0, f"-------------------------------")
    if cambios > 1:
        stdscr.addstr(3,40,f"Te quedan {cambios} cambios")
    else:
        stdscr.addstr(3, 40, "Ultimo cambio")
        
    for i in range(len(mano.getCartas())):
        if(mano.getCartas()[i].isSelected()):
            if mano.getCartas()[i].getColor() == "red":
                stdscr.addstr(3 + i, 3, f"{str(mano.getCartas()[i])}", curses.color_pair(2))
            else:
                stdscr.addstr(3 + i, 3, f"{str(mano.getCartas()[i])}", curses.color_pair(1))
        else:
            if mano.getCartas()[i].getColor() == "red":
                stdscr.addstr(3 + i, 1, f"{str(mano.getCartas()[i])}", curses.color_pair(2))
            else:
                stdscr.addstr(3 + i, 1, f"{str(mano.getCartas()[i])}", curses.color_pair(1))
        stdscr.addstr(3 + i, 27, "??")
        

            
    stdscr.addstr(3 + cursor_pos, 0, ">")
        
    if mostrarControles:
        stdscr.addstr(10, 0, "Marcar Cartas: z/ENTER")
        stdscr.addstr(11, 0, "Cambiar Cartas Marcadas: x")
        stdscr.addstr(12, 0, "Quedarse con las cartas: q")
        stdscr.addstr(13, 0, "Puedes cambiar todas las cartas que quieras el numero de cambios de la derecha")
        stdscr.addstr(14, 0, "Quitar Controles: c")
    else:
        stdscr.addstr(10, 0, "Mostrar Controles: c")
    stdscr.refresh()
    


curses.wrapper(main)
