
from carta import Carta 
import random
import os

def inicializaVariables(numeros:list[str], palos:list[str], tablero:list[list[Carta]]):
    baraja:list[Carta] = []
    for j in palos:
        for k in numeros:
            baraja.append(Carta(j,k,0,0))
    random.shuffle(baraja)
    
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if baraja[i*13+j].getNumero() == "A":
                tablero[i][j] = None
            else:
                baraja[i*13+j].setX(i)
                baraja[i*13+j].setY(j)
                tablero[i][j] = baraja[i*13+j]
    
    comprobarCartas(tablero)


                


def imprimirTablero(tablero , mensaje:str = ""):
    os.system("clear")
    
    for index,fila in enumerate(tablero):
        if(index == 0 and mensaje != ""):
            print(fila , end="")
            print("               " + mensaje)
        else:
            print(fila)

    
def hallarCartaDisponible(tablero: list[list[Carta]]):
    for index,fila in enumerate(tablero):
        for i in range(len(fila)):
            if fila[i] is None:
                if i == 0:
                    for fila2 in tablero:
                            for carta in fila2:
                                if carta is not None and carta.getNumero() == "2" and not carta.isPosicionCorrecta():
                                    return [carta, index]
                elif fila[i-1] is not None and fila[i-1].getNumero() != "K":
                    return fila[i-1]

def mezclarCartas(tablero:list[list[Carta]]):
    palos:list = ["♥","♦", "♣", "♠"]
    baraja:list[Carta] = []
    for palo in palos:
        baraja.append(Carta(palo,"A",0,0))
    
    for fila in tablero:
        for carta in fila:
            if(carta and not carta.isPosicionCorrecta()):
                baraja.append(carta)
    random.shuffle(baraja)
    repartirCartas(tablero, baraja)
    
def repartirCartas(tablero:list[list[Carta]], baraja:list[Carta]):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if (tablero[i][j] is None) or (not tablero[i][j].isPosicionCorrecta()):
                carta:Carta = baraja.pop()
                if carta.getNumero() == "A":
                    tablero[i][j] = None
                else:
                    carta.setX(i)
                    carta.setY(j)
                    tablero[i][j] = carta
                      
    comprobarCartas(tablero)
    
             
def comprobarCartas(tablero:list[list[Carta]]):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if j == 0:
                if tablero[i][j] is not None and tablero[i][j].getNumero() == "2":
                    tablero[i][j].setPosicionCorrecta(True)
                elif tablero[i][j] is not None:
                    tablero[i][j].setPosicionCorrecta(False)
            elif tablero[i][j] is not None:
                if tablero[i][j-1] is not None and tablero[i][j-1].isPosicionCorrecta():
                    tablero[i][j].setPosicionCorrecta(tablero[i][j-1].getSiguienteCarta() == tablero[i][j])

        
def esJuegoCompletado(tablero:list[list[Carta]])-> bool: 
    for fila in tablero:
        for carta in fila:
            if carta is not None and not carta.isPosicionCorrecta():
                return False

    return True