from time import time as time
import curses


def main(con):
    con.nodelay(True)
    puntos = 0
    multiplicador = 0
    curses.curs_set(0)
    clickAuto = False
    tiempoAuto = 0
    tiempoClickAuto = 0
    puntosPorClick = 1 * (multiplicador + 1)
    puntosPorClickAuto = 5
    clickAutoMejorado = False
    mostrarAuto = False
    dibujarBotonSinPulsar(con)

    tiempoAbajo = None
    while True:
        coste = round(100 * multiplicador + 100 * (1+multiplicador/10))
        key = con.getch()
        if key == 32 and tiempoAbajo == None:
            dibujarBotonPulsado(con)
            tiempoAbajo = time()

        if (key == ord("x") or key == ord("X")) and mostrarAuto:
            if not clickAuto:
                if puntos >= 500:
                    puntos -=500
                    clickAuto = True
                    tiempoClickAuto = 3
                    tiempoAuto = time()
            else:
                if puntos >= 1000:
                    puntos -= 1000
                    clickAutoMejorado = True
                    con.addstr(9, 0, f"                                                                                          ")

        if key == ord("c") or key == ord("C"):
            if puntos >= coste:
                puntos -= coste
                multiplicador += 1
                puntosPorClick = 1 * (multiplicador + 1)

        if tiempoAbajo != None and time() - tiempoAbajo > 0.1:
            dibujarBotonSinPulsar(con)
            puntos += puntosPorClick
            tiempoAbajo = None

        if clickAuto:

            if time() - tiempoAuto >= tiempoClickAuto:
                dibujarBotonSinPulsar(con)
                tiempoAuto = time()
                if clickAutoMejorado:
                    puntos += puntosPorClick
                else:
                    puntos += puntosPorClickAuto
            elif time() - tiempoAuto >= tiempoClickAuto-0.1:
                dibujarBotonPulsado(con)
        if multiplicador == 4:
            mostrarAuto = True
        con.addstr(7, 0, f"Puntos: {puntos}     ")
        con.addstr(
            8, 0, f"Pulse c para gastar {coste} y conseguir un multiplicador al hacer click")
        if mostrarAuto:
            if not clickAuto:

                con.addstr(9, 0, f"Pulse x para gastar {500} y conseguir 5 puntos cada 3 segundos")

            elif not clickAutoMejorado:
                con.addstr(9, 0, f"Pulse x para mejorar los puntos por click automaticos al actual tuyo por 1000 puntos")

        con.refresh()


def dibujarBotonSinPulsar(con):
    con.addstr(0, 0, "     ___________ ")
    con.addstr(1, 0, "   /|           |")
    con.addstr(2, 0, "  / |   Space   |")
    con.addstr(3, 0, "  | |___________|")
    con.addstr(4, 0, "  | /          / ")
    con.addstr(5, 0, "  |/__________/  ")


def dibujarBotonPulsado(con):
    con.addstr(0, 0, "                  ")
    con.addstr(1, 0, "     ___________  ")
    con.addstr(2, 0, "  /|           |  ")
    con.addstr(3, 0, "  ||   Space   |  ")
    con.addstr(4, 0, "  ||___________|  ")
    con.addstr(5, 0, "  |/__________/   ")


curses.wrapper(main)
