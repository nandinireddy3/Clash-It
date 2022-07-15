import numpy as np

class king():
      def __init__(self,x,y):
          self._Xdistance = x
          self._Ydistance = y
          self._king = "👑"
          self._damage_by_king = 0
          self.Health = 20
          #print(self._king)
         # self._Location = np.full((self._Xdistance,self._Ydistance),dtype=int)
          
         

class MovingKing(king):
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
    
    def attack(self):
        # first wall damage

        if(self._Xdistance == 14 and ( 24 < self._Ydistance and self._Ydistance < 45 )):
            # damage the wall
            return 5
        elif(self._Xdistance == 16 and ( 24 < self._Ydistance and self._Ydistance < 45 )):
            # damage the wall
            return 6
        elif(self._Xdistance == 34 and ( 24 < self._Ydistance and self._Ydistance < 45 )):
            # damage the wall
            return 5
        elif(self._Xdistance == 36 and ( 24 < self._Ydistance and self._Ydistance < 45 )):
            # damage the wall
            return 6
        elif(self._Ydistance == 24 and ( 14 < self._Xdistance and self._Xdistance < 36 )):
            # damage the wall
            return 7
        elif(self._Ydistance == 26 and ( 14 < self._Xdistance and self._Xdistance < 36 )):
            # damage the wall
            return 8
        elif(self._Ydistance == 43 and ( 14 < self._Xdistance and self._Xdistance < 36 )):
            # damage the wall
            return 7
        elif(self._Ydistance == 45 and ( 14 < self._Xdistance and self._Xdistance < 36 )):
            # damage the wall
            return 8
        
        # 2nd wall damage
        if(self._Xdistance == 4 and ( 7 < self._Ydistance and self._Ydistance < 63 )):
            # damage the wall
            return 1
        elif(self._Xdistance == 46 and ( 7 < self._Ydistance and self._Ydistance < 63 )):
            # damage the wall
            return 2
        elif(self._Ydistance == 7 and ( 4 < self._Xdistance and self._Xdistance < 46 )):
            # damage the wall
            return 3
        elif(self._Ydistance == 63 and ( 4 < self._Xdistance and self._Xdistance < 46 )):
            # damage the wall
            return 4

if __name__ == '__main__':
    MovingKing()
    