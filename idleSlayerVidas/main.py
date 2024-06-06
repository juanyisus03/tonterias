import curses
import time
import random
import sys
from Actor import Actor

tiempoUltimaPalomaCreada = 0
tiempoMalo = time.time()
tiempoMoneda = None
tiempoAire = None
jumping = False
puntos = 0
tiempoAtaque = 0
vidas = 3
ataque = False
juegoAcabado = False
invulnerable = False
tiempoInvul = None

def main(con):
    inicializarColores()
    palomas = [] 
    player = Actor(5,10)
    monstruos:list[Actor] = [] 
    monedas:list[Actor]= []
    
    
    con.addstr(1,0,"Instrucciones del juego")
    con.addstr(2,0,"=======================")
    con.addstr(4,0,"Pulse la flecha Arriba o espacio para saltar")
    con.addstr(5,0,"Pulse la flecha Derecha para atacar")
    con.addstr(6,0,"Pulse la tecla q para salir del juego")
    con.addstr(8,0,"Cada vez que le golpee un monstruo perderá una vida, posee de 3")
    con.addstr(11,0,"Pulse cualquier tecla para continuar....")
    con.refresh()
    con.getch()
    con.clear()
    con.nodelay(True)
    while not juegoAcabado:
        manejoEntidades(con, palomas, player, monstruos, monedas)
        pintarEscena(con, palomas, player, monstruos, monedas)
        clear_input_buffer(con)
        time.sleep(0.1)
    
    pintarGameOver(con)

def pintarGameOver(con):
    con.clear()
    con.nodelay(False)
    con.addstr(3,10,"********************",curses.color_pair(7))
    con.addstr(4,10,"*                  *",curses.color_pair(7))
    con.addstr(5,10,"*    GAME OVER!    *",curses.color_pair(7))
    con.addstr(6,10,"*                  *",curses.color_pair(7))
    con.addstr(7,10,"*  ¡Has perdido!   *",curses.color_pair(7))
    con.addstr(8,10,"*                  *",curses.color_pair(7))
    con.addstr(9,10,"********************",curses.color_pair(7))
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
   

    

def pintarEscena(con, palomas, player, monstruos, monedas):
    global ataque, invulnerable, tiempoInvul
    con.clear()
    pintarEscenario(con)
    pintarPalomas(con, palomas)
    pintarMonstruos(con, monstruos) 
    pintarMonedas(con, monedas)
    if not invulnerable or (invulnerable and int((time.time() - tiempoInvul)*10)%2 == 0 ):
        if ataque:
            pintarJugadorAtacando(con, player)
        else:
            pintarJugador(con,player)
    manejarColisionMonstruoPlayer(player, monstruos)
    manejoColisionPlayerMoneda(player, monedas)
    
    
  


    con.refresh()

def manejoEntidades(con, palomas, player, monstruos, monedas):
    manejarPalomas(palomas)
    manejarMonstruos(monstruos)     
    manejarJugador(con, player)
    manejoMonedas(monedas)

def manejoColisionPlayerMoneda(player, monedas):
    global puntos
    for i in range(len(monedas)-1,-1,-1):
        if monedas[i].getX() in range(player.getX()+2,player.getX()-2,-1) and monedas[i].getY() in range(player.getY(),player.getY()-3,-1):
            monedas.remove(monedas[i])
            puntos += 10
def pintarMonedas(con, monedas):
    for moneda in monedas:
        con.addstr(moneda.getY(), moneda.getX(), "$",curses.color_pair(5))

def manejoMonedas(monedas):
    global tiempoMoneda
    if len(monedas) == 0:
        if random.randint(0,10) == 7:
            tiempoMoneda = None
    if len(monedas) == 10:
        tiempoMoneda = time.time()
    
    if tiempoMoneda is None :
        monedas.append(Actor(47,6))
        
    for i in range(len(monedas)-1,-1,-1):
        monedas[i].setX(monedas[i].getX() - 1)
        if monedas[i].getX() == 0:
            monedas.remove(monedas[i])
    

def manejarJugador(con, player):
    global tiempoAire, jumping, tiempoAtaque, ataque, invulnerable, tiempoInvul
    key = con.getch()
    if key == 32 or key == curses.KEY_UP:
        jumping = True 
    elif key == ord("q") or key == ord("Q"):
        sys.exit(0)
    elif key == curses.KEY_RIGHT:
        ataque = True
        tiempoAtaque = time.time()

    if ataque:
        if tiempoAtaque and time.time() - tiempoAtaque > 0.2:
            ataque = False
            tiempoAtaque = None
    
    if invulnerable:
        if tiempoInvul and time.time() - tiempoInvul > 1.9:
            invulnerable = False
            tiempoInvul = None
    
    if jumping :
        if tiempoAire == None:
            tiempoAire = time.time()
            player.setY(player.getY() - 1)
        elif time.time() - tiempoAire  > 0.8:
            player.setY(player.getY() + 1)
            tiempoAire = None
            jumping = False
        elif time.time() - tiempoAire  > 0.6:
            player.setY(player.getY() + 1)
            
        elif time.time() - tiempoAire  > 0.3:
            player.setY(player.getY())
        elif time.time() - tiempoAire > 0.1:
            player.setY(player.getY() - 1)

def manejarColisionMonstruoPlayer(player, monstruos):
    global puntos, ataque, tiempoAtaque,juegoAcabado, invulnerable, tiempoInvul, vidas
    for i in range(len(monstruos)-1,-1,-1):
        for j in range(0,5,1):
                
            if ataque:
                if monstruos[i].getX()+j in range(player.getX()-2,player.getX()+3,1)and monstruos[i].getY() == player.getY():
                    monstruos.remove(monstruos[i])
                    puntos -= -100
                    ataque = False
                    tiempoAtaque = None
                    break
            else:
                if monstruos[i].getX()+j == player.getX() + 1 and monstruos[i].getY() == player.getY():
                    if not invulnerable:
                        vidas += -1
                        if puntos > 10:
                            puntos -= +10
                        else:
                            puntos = 0
                        invulnerable = True
                        tiempoInvul = time.time() 
                        if vidas == 0:
                            juegoAcabado = True
                    break

def pintarMonstruos(con, monstruos):

    for monstruo in monstruos:
        con.addstr(monstruo.getY() -1,monstruo.getX(), "\\  /", curses.color_pair(1))
        con.addstr(monstruo.getY(),monstruo.getX(), "(--)", curses.color_pair(1))

def manejarMonstruos(monstruos):
    global tiempoMalo
    if time.time() - tiempoMalo > random.randint(5,10) :
        tiempoMalo = time.time()
        monstruos.append(Actor())
            
    for monstruo in monstruos:
        monstruo.setX(monstruo.getX()-1)

    for i in range(len(monstruos)-1,-1,-1):
        if monstruos[i].getX() == 0:
            monstruos.remove(monstruos[i])
        

def inicializarColores():
    curses.start_color()
    curses.init_color(20, 250, 250, 185)
    curses.init_color(30, 255, 100, 0)
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_CYAN)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_CYAN)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_GREEN)
    curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_WHITE)
    curses.init_pair(5, 20 ,curses.COLOR_CYAN)
    curses.init_pair(6, 30,30)
    curses.init_pair(7,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(8,curses.COLOR_RED,curses.COLOR_CYAN)
    
    curses.curs_set(0)

def manejarPalomas(palomas):
    global  tiempoUltimaPalomaCreada
    if len(palomas) < 8 and time.time() - tiempoUltimaPalomaCreada > random.randint(5, 9)/10:
        tiempoUltimaPalomaCreada = time.time()
        palomas.append([random.randint(1, 4), 49, "^"])
        
    
    for i in range(len(palomas)-1,-1,-1):
        palomas[i][1] -=1
        if palomas[i][1] == 0:
            palomas.remove(palomas[i])
        else:
            if palomas[i][1]%3 == 0:
                palomas[i][2] = "^"
            elif palomas[i][1]%3 == 1:
                palomas[i][2] = "─"
            else: 
                palomas[i][2] = "v"
        

def pintarJugador(con, player):
    con.addstr(player.getY()-2, player.getX(),"o /",curses.color_pair(1))
    con.addstr(player.getY()-1, player.getX(),"┼%",curses.color_pair(1))
    con.addstr(player.getY(), player.getX(), "A",curses.color_pair(1))

def pintarJugadorAtacando(con, player):
    con.addstr(player.getY()-2, player.getX(),"o ",curses.color_pair(1))
    con.addstr(player.getY()-1, player.getX(),"┼┼──",curses.color_pair(1))
    con.addstr(player.getY(), player.getX(), "A",curses.color_pair(1))    

def pintarPalomas(con, palomas):
    if len(palomas) != 0:
        for paloma in palomas:   
            con.addstr(paloma[0], paloma[1], paloma[2],curses.color_pair(1))
            
def pintarEscenario(con):
    global puntos, vidas
    for i in range(11):
        con.addstr(i,0,f"                                                  ",curses.color_pair(1))
    for i in range(vidas):
        con.addstr(0, 1 + i*2, "♥", curses.color_pair(8))
    con.addstr(11,0,"                                                  ",curses.color_pair(3))
    con.addstr(12,0,"                                                  ",curses.color_pair(6))
    con.addstr(13,0,"                                                  ",curses.color_pair(6))
    
    con.addstr(2,52,"      PUNTOS   ")
    con.addstr(3,52,"  ==============   ")
    con.addstr(5,52,"     $ -> 10          ")
    con.addstr(7,52,"   \  /          ")
    con.addstr(8,52,"   (xx) -> 100          ")
    con.addstr(10,52,"   \  /          ")
    con.addstr(11,52,"   (--) -> -10          ")
    
    
    con.addstr(0,52, f"Puntos: {puntos}")

curses.wrapper(main)
