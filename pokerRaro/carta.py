class Carta:    
    def __init__(self, palo: str, numero: str):
        self._palo = palo
        self._numero = numero
        self._selected = False
        self._puntos:int

        if palo == "♥" or palo == "♦":
            self.__color = "red"
        else:
            self.__color = "black"
        self.setPuntos()

    def setPuntos(self):
        if self._numero == "A":
            self._puntos = 13
        elif self._numero == "J":
            self._puntos = 10
        elif self._numero == "Q":
            self._puntos = 11
        elif self._numero == "K":
            self._puntos = 12
        else: 
            self._puntos = int(self._numero)-1
            
    
    def getColor(self) -> str:
       return self.__color
    
    def setColor(self, color: str):
        self.__color = color
    
    def getPuntos(self) -> int:
        return self._puntos
    
    def getPalo(self) -> str:
        return self._palo
    
    def setPalo(self, palo: str):
        self._palo = palo

    def getNumero(self) -> str:
        return self._numero
    
    def setNumero(self, numero: str):
        self._numero = numero

    def isSelected(self) -> bool:
        return self._selected
    
    def setSelected(self, selected: bool):
        self._selected = selected

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
            return Carta(self._palo, "J")
        elif self._numero == "J":
            return Carta(self._palo, "Q")
        elif self._numero == "Q":
            return Carta(self._palo, "K")
        elif self._numero == "K":
            return Carta(self._palo, "A")
        else:
            return Carta(self._palo, str(int(self._numero) + 1))
