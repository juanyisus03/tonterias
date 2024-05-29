class Suelo:
    def __init__(self,y) -> None:
        self._y = y
        
    def getY(self):
        return self._y
    
    def setY(self,y):
        self._y = y