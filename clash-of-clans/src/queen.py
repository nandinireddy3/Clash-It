import numpy as np

class queen():
      def __init__(self,x,y):
          self._Xdistance = x
          self._Ydistance = y
          self._queen = "👸"
          self._damage_by_queen = 0
          self.Health = 20
          
         

class MovingQueen(queen):
    def __init__(self,x,y):
        super().__init__(x,y)
    
    def Up(self):
        self._Ydistance = self._Ydistance + 1
    def Left(self):
        self._Xdistance = self._Xdistance - 1
    def Down(self):
        self._Ydistance = self._Ydistance - 1
    def Right(self):
        self._Xdistance = self._Xdistance + 1