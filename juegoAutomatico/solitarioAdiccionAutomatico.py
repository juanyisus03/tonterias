from carta import Carta
import funciones as util
import sys
from time import sleep as sl
numeros:list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
juegoGanado = False
palos:list = ["♥","♦", "♣", "♠"]
tablero = [[Carta for i in numeros] for j in palos]  
shuffles:int  = 3
movimiento:bool = False
cont = 1

util.inicializaVariables(numeros, palos, tablero)


util.imprimirTablero(tablero)


            

while juegoGanado == False:
# while not juegoGanado and shuffles != -1: 
    mensaje = ""
    
    cartaDisponible = util.hallarCartaDisponible(tablero) 
    if isinstance(cartaDisponible,Carta):
        
        
        cartaBuscada = cartaDisponible.getSiguienteCarta()

        for i in range(len(tablero)):
            try:
                cartaBuscada.setY(tablero[i].index(cartaBuscada))
                cartaBuscada.setX(i)
                break
            except ValueError:
                continue
        tablero[cartaBuscada.getX()][cartaBuscada.getY()] = None
        cartaBuscada.setX(cartaDisponible.getX())
        cartaBuscada.setY(cartaDisponible.getY()+1)
        cartaBuscada.setPosicionCorrecta(cartaDisponible.isPosicionCorrecta())
        tablero[cartaBuscada.getX()][cartaBuscada.getY()] = cartaBuscada
        mensaje = ("Movimiento realizado: " + str(cartaBuscada) + " al lado de  " +  str(cartaDisponible))
        
    
    elif cartaDisponible is None:
        shuffles -= 1
        
        print("No hay movimientos")
        
        if(shuffles == -1):
            print("Empezando otra partida", end="")
            for _ in range(3): 
                print(".", end="") 
                sys.stdout.flush() 
                sl(1) 
            print("")
            util.inicializaVariables(numeros, palos, tablero)
            shuffles = 3
            cont += 1
        else:
            if(shuffles == 0):
                print("Última oportunidad")
            else:
                print("Te quedan " + str(shuffles) + " mezclas")
            
            util.mezclarCartas(tablero)
            print("Barajando", end="") 
            sys.stdout.flush()

            for _ in range(3): 
                print(".", end="") 
                sys.stdout.flush() 
                sl(1) 
            print("")
                
            print("Repartiendo Cartas", end="") 
            sys.stdout.flush()

            for _ in range(3): 
                print(".", end="") 
                sys.stdout.flush() 
                sl(1)  
            print("")  

    else:
        tablero[cartaDisponible[0].getX()][cartaDisponible[0].getY()] = None
        cartaDisponible[0].setX(cartaDisponible[1])
        cartaDisponible[0].setY(0)
        cartaDisponible[0].setPosicionCorrecta(True)
        tablero[cartaDisponible[1]][0] = cartaDisponible[0]
        mensaje = ("Movimiento realizado: " + str(cartaDisponible[0]) + " al principio de la fila " + str(cartaDisponible[1] +1 ))
    
    util.imprimirTablero(tablero,mensaje)
    juegoGanado = util.esJuegoCompletado(tablero)
    sl(0)
    
print("\n\nJuego Acabado")  

if(juegoGanado):
    print("Enhorabuena Ganaste pero tuviste que reiniciar la partida " + str(cont) + " veces")  


    
    