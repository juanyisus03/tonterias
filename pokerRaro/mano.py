from baraja import Baraja
from carta import Carta

class Mano:
    
    def __init__(self, baraja: Baraja):
        self._mano: list[Carta] = []
        self._pareja = False
        self._trio = False
        self._poker = False
        self._doblePareja = False
        self._escalera = False
        self._full = False
        self._escaleraColor = False
        self._color = False
        self._escaleraReal = False
        self._puntos = 0
        self._jugada: list[Carta] = []
        self.repartirCartas(baraja)
        self.ordenarMano()
    
    def reiniciarPuntos(self):
        self._pareja = False
        self._trio = False
        self._poker = False
        self._doblePareja = False
        self._escalera = False
        self._full = False
        self._escaleraColor = False
        self._color = False
        self._escaleraReal = False
        self._puntos = 0
        self._jugada = []
    
    def repartirCartas(self, baraja: Baraja):
        for _ in range(5):
            self._mano.append(baraja.obtenerCarta())
    
    def setCartas(self, cartas: list[Carta]):
        self._mano = cartas
    
    def getCartas(self) -> list[Carta]:
        return self._mano
    
    def setJugada(self, cartas: list[Carta]):
        self._jugada = cartas
    
    def getJugada(self) -> list[Carta]:
        return self._jugada
    
    def ordenarMano(self):
        self._mano.sort(key=lambda carta: carta.getPuntos(), reverse=False)
    
    
    def isPareja(self) -> bool:
        return self._pareja
    
    def setPareja(self, valor: bool):
        self._pareja = valor
    

    def isTrio(self) -> bool:
        return self._trio
    
    def setTrio(self, valor: bool):
        self._trio = valor
    
    
    def isPoker(self) -> bool:
        return self._poker
    
    def setPoker(self, valor: bool):
        self._poker = valor
    
    
    def isDoblePareja(self) -> bool:
        return self._doblePareja
    
    def setDoblePareja(self, valor: bool):
        self._doblePareja = valor
    
    
    def isEscalera(self) -> bool:
        return self._escalera
    
    def setEscalera(self, valor: bool):
        self._escalera = valor
    
    
    def isColor(self) -> bool:
        return self._color
    
    def setColor(self, valor: bool):
        self._color = valor
        
    def isFull(self) -> bool:
        return self._full
    
    def setFull(self, valor: bool):
        self._full = valor
    
    def isEscaleraColor(self) -> bool:
        return self._escaleraColor
    
    def setEscaleraColor(self, valor: bool):
        self._escaleraColor = valor
    
    def isEscaleraReal(self) -> bool:
        return self._escaleraReal
    
    def setEscaleraReal(self, valor: bool):
        self._escaleraReal = valor

    def getPuntos(self) -> int:
        return self._puntos
    
    def setPuntos(self, valor: int):
        self._puntos = valor
