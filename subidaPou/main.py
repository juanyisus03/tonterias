import curses
import time
import random
import sys
from Actor import Actor

tiempoAire = None
puedeSaltar = True
juegoAcabado = False

def main(con:curses.window):
    global puedeSaltar,juegoAcabado,tiempoAire
    inicializarColores()
    plataformas = [Actor()]
    for plataforma in plataformas:
        if len(plataformas) == 4:
            break
        else:
            plataformas.append(Actor(plataforma.getX() + random.randint(-5,5), plataforma.getY() - random.randint(4,6)))
            if plataformas[-1].getX() > 16:
                plataformas[-1].setX(16)
            elif plataformas[-1].getX() < 0:
                plataformas[-1].setX(0)
             
    player = Actor(5,15)
    
    
    mostrarInstrucciones(con)
    curses.curs_set(0)
    while not juegoAcabado:
        
        key = con.getch()
        if key == curses.KEY_LEFT:
            if player.getX() != 0:
                player.setX(player.getX() - 1)
            else:
                player.setX(20)
        elif key == curses.KEY_RIGHT:
            if player.getX() != 20:
                player.setX(player.getX() + 1)
            else:
                player.setX(0)
    
        if tiempoAire == None and puedeSaltar == True:
            tiempoAire = time.time()
            if player.getY() > 3:
                player.setY(player.getY() - 1)
            puedeSaltar == False
        elif time.time() - tiempoAire  > 0.9:
            player.setY(player.getY() + 1)
            if player.getY() == 15:
                juegoAcabado = True    
        elif time.time() - tiempoAire  > 0.6:
            player.setY(player.getY())
            puedeSaltar = True
        elif time.time() - tiempoAire > 0.1:
            if player.getY() > 4:
                player.setY(player.getY() - 1)
           
            for i in range(len(plataformas)-1,-1,-1):
                plataformas[i].setY(plataformas[i].getY()+ 1)
                if plataformas[i].getY() == 15:
                    plataformas.remove(plataformas[i])
                    if plataformas[-1].getX() < 3:
                        plataformas.append(Actor(plataformas[-1].getX() + random.randint(0,5), plataformas[-1].getY() - random.randint(4,6)))
                    elif plataformas[-1].getX() > 16:
                        plataformas.append(Actor(plataformas[-1].getX() + random.randint(-5,0), plataformas[-1].getY() - random.randint(4,6)))
                    else:
                        plataformas.append(Actor(plataformas[-1].getX() + random.randint(-5,5), plataformas[-1].getY() - random.randint(4,6)))
                    if plataformas[-1].getX() > 16:
                        plataformas[-1].setX(16)
                    elif plataformas[-1].getX() < 0:
                        plataformas[-1].setX(0)
            puedeSaltar = False
        
        
        for plataforma in plataformas:
            if player.getY() == plataforma.getY()-1:
                if player.getX() in range(plataforma.getX(), plataforma.getX()+4):
                    if puedeSaltar:
                        tiempoAire = None
                
        
        con.clear()
        con.refresh()
        pintarFondo(con)

        pintarPlataformas(con, plataformas)
                    
        pintarJugador(con, plataformas, player)
            
        clear_input_buffer(con)
        time.sleep(0.07)
    
    pintarGameOver(con)

def mostrarInstrucciones(con):
    con.addstr(1,0,"Instrucciones del juego")
    con.addstr(2,0,"=======================")
    con.addstr(4,0,"Pulse la flecha izquierda para ir a la izquierda")
    con.addstr(5,0,"Pulse la flecha Derecha para ir derecha")
    con.addstr(6,0,"Pulse la tecla q para salir del juego")
    con.addstr(11,0,"Pulse cualquier tecla para continuar....")
    con.refresh()
    con.getch()
    con.clear()
    con.nodelay(True)

def pintarJugador(con, plataformas, player):
    for plataforma in plataformas:
        pintarPatas,pintarTronco,pintarCabeza = False,False,False
        if player.getX() in range(plataforma.getX(), plataforma.getX() + 4, 1):
            if player.getY() - 2 == plataforma.getY():
                pintarCabeza = True
                break
            if player.getY() - 1 == plataforma.getY():
                pintarTronco = True
                break
            if player.getY() == plataforma.getY():
                pintarPatas = True
                break
    if pintarCabeza:
        con.addstr(player.getY()-2, player.getX(),"o",curses.color_pair(2))
    else:
        con.addstr(player.getY()-2, player.getX(),"o",curses.color_pair(1))
    if pintarTronco:
        con.addstr(player.getY()-1, player.getX(),"┼",curses.color_pair(2))
    else:
        con.addstr(player.getY()-1, player.getX(),"┼",curses.color_pair(1))
    if pintarPatas:
        con.addstr(player.getY(), player.getX(), "A",curses.color_pair(2))
    else:
        con.addstr(player.getY(), player.getX(), "A",curses.color_pair(1))

def pintarPlataformas(con, plataformas):
    for plataforma in plataformas:
        if plataforma.getY() in range(0,16):
                con.addstr(plataforma.getY(), plataforma.getX(), "████",curses.color_pair(3))

def pintarFondo(con):
    for i in range(16):
        con.addstr(i,0,"                     ", curses.color_pair(1))

def pintarGameOver(con):
    con.clear()
    con.nodelay(False)
    con.addstr(3,10,"********************")
    con.addstr(4,10,"*                  *")
    con.addstr(5,10,"*    GAME OVER!    *")
    con.addstr(6,10,"*                  *")
    con.addstr(7,10,"*  ¡Has perdido!   *")
    con.addstr(8,10,"*                  *")
    con.addstr(9,10,"********************")
    con.addstr(11,0, "Pulse cualquier tecla para finalizar el programa")
    con.refresh()
    con.getch()



def clear_input_buffer(con):
 
    con.nodelay(True)  
    try:
        while con.getch() != -1:
            pass
    except curses.error:
        pass
    con.nodelay(True)
   

    
def inicializarColores():
    curses.start_color()
    curses.init_color(20, 250, 250, 185)
    curses.init_color(30, 255, 100, 0)
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_CYAN)
    curses.init_pair(2,curses.COLOR_WHITE,20)
    curses.init_pair(3, 20 ,curses.COLOR_CYAN)


    
  




curses.wrapper(main)
