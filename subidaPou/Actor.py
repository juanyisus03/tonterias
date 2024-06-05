class Actor:
    def __init__(self,x=4,y=13) -> None:
        self._x = x
        self._y = y
    
    def getX(self):
        return self._x
    
    def setX(self,x):
        self._x = x
        
    def getY(self):
        return self._y
    
    def setY(self,y):
        self._y = y