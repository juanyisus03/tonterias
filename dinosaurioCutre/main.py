import curses
import time
import random
from Pincho import Pincho
from Jugador import Jugador
def main(con):

    palomas = []
    nubes = []
    tiempoNubes = time.time()
    tiempoNubeCreada = 0
    tiempoPaloma = time.time()
    tiempoUltimaPalomaCreada = 0
    curses.start_color()
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_CYAN)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_CYAN)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_GREEN)
    curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_WHITE)
    curses.curs_set(0)
    player = Jugador()
    tiempo = time.time()
    con.nodelay(True)
    tiempoAire = None
    tiempoMalo = time.time()
    pinchos:list[Pincho] = [] 
    jumping = False
    juegoAcabado = False
    
    pintarEscenario(con)
    
    while not juegoAcabado:
        
        if len(nubes) < 20 and time.time() - tiempoNubeCreada > random.randint(5,9)/10:
            tiempoNubeCreada = time.time()
            nubes.append([random.randint(1, 6), 49])
        
        if time.time() - tiempoNubes > 0.3:
            for nube in nubes:
                nube[1] -=1
                if nube[1] == 0:
                    nubes.remove(nube)
                    tiempoNubeCreada = 0
            
            tiempoNubes = time.time()
            
       
            
            
        if len(palomas) < 4 and time.time() - tiempoUltimaPalomaCreada > random.randint(5, 9)/10:
            tiempoUltimaPalomaCreada = time.time()
            palomas.append([random.randint(1, 6), 49, "^"])
        
        if time.time() - tiempoPaloma > 0.2:
            for paloma in palomas:
                paloma[1] -=1
                if paloma[1] == 0:
                    palomas.remove(paloma)
                    tiempoPaloma = 0
                else:
                    if paloma[1]%2 == 0:
                        paloma[2] = "^"
                    else:
                        paloma[2] = "─"
            tiempoPaloma = time.time()
                        
        if time.time() - tiempoMalo > random.randint(4,10)/10 :
            tiempoMalo = time.time()
            pinchos.append(Pincho())
             
        if time.time() - tiempo > 0.1:  
            tiempo = time.time()
            key = con.getch()
            if key == 10 or key == 32:
                jumping = True
            
                
            if jumping :
                if tiempoAire == None:
                    tiempoAire = tiempo
                    player.setY(player.getY() - 1)
                elif time.time() - tiempoAire  > 0.3:
                    player.setY(player.getY() + 1)
                    tiempoAire = None
                    jumping = False
                
            
            
            con.clear()
            pintarEscenario(con)
            
            for nube in nubes:
                    con.addstr(nube[0], nube[1], " ",curses.color_pair(4))
            
            if len(palomas) != 0:
                for paloma in palomas:
                    enNube = False
                    for nube in nubes:
                        if nube[0] == paloma[0] and nube[1] == paloma[1]:
                            enNube = True
                            break
                    if enNube:
                        con.addstr(paloma[0], paloma[1], paloma[2],curses.color_pair(4))
                    else:
                        con.addstr(paloma[0], paloma[1], paloma[2],curses.color_pair(1))
            
            con.addstr(player.getY()-2, player.getX(),"o",curses.color_pair(1))
            con.addstr(player.getY()-1, player.getX(),"┼",curses.color_pair(1))
            con.addstr(player.getY(), player.getX(), "A",curses.color_pair(1))
            for i in range(len(pinchos)-1,0,-1):                
                pinchos[i].setX(pinchos[i].getX()-1)
                if pinchos[i].getX() == player.getX() and pinchos[i].getY() == player.getY():
                    juegoAcabado = True
                    break
                if pinchos[i].getX() == 0:
                    pinchos.remove(pinchos[i])
                else:
                    con.addstr(pinchos[i].getY(), pinchos[i].getX(), "▲",curses.color_pair(2))
            
            
            
            con.addstr(0,0,"")
            con.refresh()

            # Wait briefly to control animation speed
            time.sleep(0.1)
def pintarEscenario(con):
    for i in range(11):
        con.addstr(i,0,"                                                  ",curses.color_pair(1))
    con.addstr(11,0,"                                                  ",curses.color_pair(3))

curses.wrapper(main)
