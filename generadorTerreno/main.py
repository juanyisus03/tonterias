import curses
import random
from Suelo import Suelo
ejeYCopia = 20

def main(con:curses.window):
    curses.start_color()
    curses.init_color(20, 255, 100, 0)
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2, 20, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.curs_set(0)
    suelo = [Suelo(10)]*50
    cont = 0
    con.nodelay(True)
    movimiento = -1
    imprimirPantalla(con, suelo, cont,movimiento)
    while True:
        key = con.getch()
        if key != -1:
            if key == ord('q'):
                break
            if key == curses.KEY_LEFT:
                if cont + 50 < len(suelo):
                    movimiento = 1
                    cont += 1
            if key == curses.KEY_RIGHT:
                if cont > 0:
                    cont -= 1
                elif cont == 0:
                    generarTerreno(suelo)
                movimiento = 0
            imprimirPantalla(con, suelo, cont,movimiento)
    
        curses.napms(100)
        
        clear_input_buffer(con)
      

def generarTerreno(suelo):
    
    if suelo[-1].getY() <= 6:
        suelo.append(Suelo(suelo[-1].getY() + random.randint(0, 1)))
    elif suelo[-1].getY() >= 14:
        suelo.append(Suelo(suelo[-1].getY() + random.randint(-1, 0)))
    else:
        suelo.append(Suelo(suelo[-1].getY() + random.randint(-1, 1)))
    
def clear_input_buffer(con):
 
    con.nodelay(True)  
    try:
        while con.getch() != -1:
            pass
    except curses.error:
        pass
    con.nodelay(False)
   

def imprimirPantalla(con,suelo,cont,movimiento):
    con.clear()
  
    if cont + 50 > len(suelo):
        visible = [suelo[i] for i in range(0, 50)]
    else:
        visible = [suelo[-i-cont] for i in range(1, 51)]
        visible.reverse()
    
    
    for i,bloque in enumerate(visible):
        for j in range(0,16):
            if j == bloque.getY():
                con.addstr(j,i, "█",curses.color_pair(1))
            elif j > bloque.getY():
                con.addstr(j,i, "█",curses.color_pair(2))
            else:
                con.addstr(j,i, " ",curses.color_pair(3))
    if movimiento == 0:
        con.addstr(visible[10].getY()-1,10, ">",curses.color_pair(3))
        con.addstr(visible[10].getY()-2,10, "├",curses.color_pair(3))
        
    elif movimiento == 1:
        con.addstr(visible[10].getY()-1,10, "<",curses.color_pair(3))
        con.addstr(visible[10].getY()-2,10, "┤",curses.color_pair(3))
       
    else:
        con.addstr(visible[10].getY()-1,10, "A",curses.color_pair(3))
        con.addstr(visible[10].getY()-2,10, "┼",curses.color_pair(3))
    con.addstr(visible[10].getY()-3,10, "o",curses.color_pair(3))     
    
    con.refresh()
    
curses.wrapper(main)
