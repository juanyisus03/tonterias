class Carta:    
    def __init__(self, palo: str, numero: str, x: int, y: int):
        self._palo = palo
        self._numero = numero
        self._x = x
        self._y = y
        self._posicionCorrecta = False

    def getPalo(self) -> str:
        return self._palo
    
    def setPalo(self, palo: str):
        self._palo = palo

    def getNumero(self) -> str:
        return self._numero
    
    def setNumero(self, numero: str):
        self._numero = numero

    def getX(self) -> int:
        return self._x
    
    def setX(self, x: int):
        self._x = x

    def getY(self) -> int:
        return self._y
    
    def setY(self, y: int):
        self._y = y

    def isPosicionCorrecta(self) -> bool:
        return self._posicionCorrecta
    
    def setPosicionCorrecta(self, correcta: bool):
        self._posicionCorrecta = correcta

    def __str__(self) -> str:
        return f"{self._numero}{self._palo}"

    def __repr__(self) -> str:
        return f"{self._numero}{self._palo}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Carta):
            return (
                self._palo == other._palo and
                self._numero == other._numero
            )
        return False
    
    def getSiguienteCarta(self) -> 'Carta':
        if self._numero == "10":
            return Carta(self._palo, "J", 0, 0)
        elif self._numero == "J":
            return Carta(self._palo, "Q", 0, 0)
        elif self._numero == "Q":
            return Carta(self._palo, "K", 0, 0)
        elif self._numero == "K":
            return self
        else:
            return Carta(self._palo, str(int(self._numero) + 1), 0, 0)
