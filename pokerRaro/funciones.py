
from carta import Carta 
from baraja import Baraja
from mano import Mano
    
def cambiarCartas(mano:Mano, baraja:Baraja):
    cartas = mano.getCartas()
    for i in range(len(cartas)):
        if cartas[i].isSelected():
            cartas[i] = baraja.obtenerCarta()   


def comprobarPareja(mano:Mano,cartas:list[Carta]):
    for i in range(len(cartas)-1):
        for j in range(i+1,len(cartas)):
            if cartas[i].getNumero() == cartas[j].getNumero() :
                mano.getJugada().append(cartas.pop(j))
                mano.getJugada().append(cartas.pop(i))
                if(mano.isPareja()):
                    mano.setDoblePareja(True)
                    mano.setPareja(False)
                else:
                    mano.setPareja(True)
                return
                     

def comprobarTrio(mano:Mano, cartas:list[Carta]):
    
    for i in range(len(cartas)-2):
        for j in range(i+1,len(cartas)-1):
            for k in range(j+1,len(cartas)):
                if cartas[i].getNumero() == cartas[j].getNumero() and  cartas[i].getNumero() == cartas[k].getNumero():
                    
                    mano.getJugada().append(cartas.pop(k))
                    mano.getJugada().append(cartas.pop(j))
                    mano.getJugada().append(cartas.pop(i))
                
                    mano.setTrio(True)
                    return 
            
  

def comprobarColor(mano:Mano):
    color = [carta.getColor() for carta in mano.getCartas()]
    
    if color.count("red") == 5 or color.count("black") == 5:
        mano.setColor(True)
    else:
        mano.setColor(False)

def comprobarEscalera(mano:Mano, puntos:list[int]):
    bandera:bool = True
    for i in range(1, len(puntos)):
        if puntos[i] != puntos[i - 1] + 1:
            bandera = False
            
    if 13 in puntos and set(puntos) == {1, 2, 3, 4, 5}:
        bandera = True
                
    mano.setEscalera(bandera)
 
def comprobarPoker(mano:Mano, cartas:list[Carta]):
    
    if (cartas[0].getNumero() == cartas[1].getNumero() == cartas[2].getNumero() == cartas[3].getNumero()) :
        mano.setPoker(True)
        
    elif (cartas[1].getNumero() == cartas[2].getNumero() == cartas[3].getNumero() == cartas[4].getNumero()):
        mano.setPoker(True)
    else:
        mano.setPoker(False)      

def comprobarEscaleraReal(mano:Mano, puntos:list[int]):
    
    if mano.isEscaleraColor():
        if puntos.count(13) == 1 and puntos.count(9) == 1:
            mano.setEscaleraReal(True)
            
def comprobarEscaleraColor(mano:Mano):
    if mano.isEscalera():
        palos = [carta.getPalo() for carta in mano.getCartas()]
        if all(palo == palos[0] for palo in palos ):
            mano.setEscaleraColor(True)
            mano.setEscalera(False)
        
       
        

def comprobarFull(mano:Mano):
    
    mano.setFull(mano.isPareja() and mano.isTrio())
    if mano.isFull():
        mano.setTrio(False)
        mano.setPareja(False)
    
    
def hacerComprobacionesMano(mano:Mano):
    cartas = mano.getCartas().copy()
    puntos = [carta.getPuntos() for carta in mano.getCartas()]
    comprobarColor(mano)
    comprobarEscalera(mano,puntos)
    comprobarEscaleraColor(mano)
    comprobarEscaleraReal(mano,puntos)
    comprobarPoker(mano,cartas)
    if(not mano.isPoker()):
        comprobarTrio(mano,cartas)
        comprobarPareja(mano,cartas)
        comprobarPareja(mano,cartas)
        comprobarFull(mano)
    darPuntos(mano)
    
def darPuntos(mano:Mano):
    if(mano.isEscaleraReal()):
        mano.setPuntos(1000)
        mano.getJugada().extend(mano.getCartas())
    elif(mano.isEscaleraColor()):
        mano.setPuntos(900)
        mano.getJugada().extend(mano.getCartas())
    elif(mano.isPoker()):
        mano.setPuntos(800)
    elif(mano.isFull()):
        mano.setPuntos(700)
    elif(mano.isColor()):
        mano.getJugada().append(mano.getCartas()[-1])
        mano.setPuntos(600)
    elif(mano.isEscalera()):
        mano.getJugada().extend(mano.getCartas())
        mano.setPuntos(500)
    elif(mano.isTrio()):
        mano.setPuntos(400)
    elif(mano.isDoblePareja()):
        mano.setPuntos(300)
    elif(mano.isPareja()):
        mano.setPuntos(200)
    else:
        mano.getJugada().append(mano.getCartas()[-1])
        mano.setPuntos(mano.getCartas()[-1].getPuntos())
       
def desempate(mano:Mano, manoCPU:Mano) -> bool:
    ganaJugador:bool
    if mano.isEscaleraReal():
        ganaJugador =  None
    elif mano.isEscaleraColor() or mano.isEscalera() or mano.isColor() or mano.isPoker() or mano.isTrio() or mano.isPareja():
        if mano.getJugada()[-1].getPuntos() == manoCPU.getJugada()[-1].getPuntos():
            ganaJugador = None
        else:
            ganaJugador = mano.getJugada()[-1].getPuntos() > manoCPU.getJugada()[-1].getPuntos() 
            
    elif mano.isFull():
        if mano.getJugada()[0].getPuntos() == manoCPU.getJugada()[0].getPuntos():
            if mano.getJugada()[-1].getPuntos() == manoCPU.getJugada()[-1].getPuntos():
                ganaJugador = None
            else:
                ganaJugador = mano.getJugada()[-1].getPuntos() > manoCPU.getJugada()[-1].getPuntos()
        else:
            ganaJugador = mano.getJugada()[0].getPuntos() > manoCPU.getJugada()[0].getPuntos()
            
    else:
        puntosJugador:list[int] = [carta.getPuntos() for carta in mano.getJugada()]
        puntosCPU:list[int] = [carta.getPuntos() for carta in manoCPU.getJugada()]
        if max(puntosCPU) == max(puntosJugador):
            if min(puntosJugador) == min(puntosCPU):
                ganaJugador = None
            else:
                ganaJugador = min(puntosJugador) > min(puntosCPU)
        else:
            ganaJugador  = max(puntosJugador) > max(puntosCPU)
    
    return ganaJugador
        