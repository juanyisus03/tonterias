from carta import Carta
import random
class Baraja:
        
    def __init__(self):
        self.__baraja:list[Carta] = []
        self.__crearBaraja()
        

    def __crearBaraja(self):
        for palo in ["♥","♦", "♣", "♠"]:
            for numero in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.__baraja.append(Carta(palo,numero))
        self.mezclarBaraja()
    
    def mezclarBaraja(self):
        random.shuffle(self.__baraja)
        
    def obtenerCarta(self):
        if not self.__baraja:
            self.__crearBaraja()
        return self.__baraja.pop(0)