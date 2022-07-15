import numpy as np
#from KingMovement import DAMAGE, RANGE
from src.village import Village
import os

# Damage = 1/2*Barbarian
# Health = 1/2*Barbarian
# Movement speed = 2*Barbarian
RANGE = 7
DAMAGE = 2
HEALTH = 5
'''
 Implement movement and attack
'''

'''
Huts 
(x,y)={ (x-1,y),(x-2,y+1),(x-1,y+2)
        (x,y),(x,y+1),(x,y+2)
        (x+1,y),(x+1,y+1),(x+1,y+2)} 
(x,y) = {8,11},{10,33},{8,56},{40,11},{40,56}
centres = (x,y+1)

TownHall 
1 - {(22,33),...,(22,36)
(23,33),....,(23,36)
(24,33),....,(24,36)
(25,33),....,(25,36)
(26,33),....,(26,36)}
centre = (24,35) or (24,34.5)

Cannons
1 - {(24,28),(25,28)
2 - (24,42),(25,42)}

Building_centres = [(24,35),(8,12),(10,34),(8,57),(40,12),(40,57),(24,28),(24,42)]
'''

class MovingArcher():
    def __init__(self,x,y):
        self._Xcoordinate = x
        self._Ycoordinate = y
        self._range = RANGE
        self._Health = HEALTH
    
    def nearest_step(self,m,n):
        random = []
        move = []
        xx = self._Xcoordinate
        yy = self._Ycoordinate
        random.append([xx+1,yy+1])
        random.append([xx+1,yy])
        random.append([xx+1,yy-1])
        random.append([xx,yy+1])
        random.append([xx,yy-1])
        random.append([xx-1,yy-1])
        random.append([xx-1,yy])
        random.append([xx-1,yy-1])
        for i in random:
            move.append(pow(i[0]-m,2)+pow(i[1]-n,2))
        mpos = move.index(min(move))
        next_x = random[mpos][0]
        next_y = random[mpos][1]
        result = []
        result.extend([next_x,next_y])
        return result
        # print(random)
        # print(m,n)
        # print("hhj",next_x,next_y)

    def movement(self,vill):
        # Building_centres = [(24,35),(8,12),(10,34),(8,57),(40,12),(40,57),(24,28),(24,42)]
        '''Getting all the existing Buildings'''
        Building_centres = []
        if(vill._TH_health > 0):
            Building_centres.append([24,35])
        if(vill._Hut1Health > 0):
            Building_centres.append([8,12])
        if(vill._Hut2Health > 0):
            Building_centres.append([10,34])
        if(vill._Hut3Health > 0):
            Building_centres.append([8,57])
        if(vill._Hut4Health > 0):
            Building_centres.append([40,12])
        if(vill._Hut5Health > 0):
            Building_centres.append([40,57])
        if(vill._CannsHealth[0] > 0):
            Building_centres.append([24,28])
        if(vill._CannsHealth[1] > 0):
            Building_centres.append([24,42]) 
        if(vill._WizsHealth[0] > 0):
            Building_centres.append([13,35]) 
        if(vill._WizsHealth[1] > 0):
            Building_centres.append([37,35])
        '''storing building Ends here'''

        if(len(Building_centres) == 0):
            os.system('clear')
            print("YOU WON")
            exit()

        list1 = []
        for i in Building_centres:
            list1.append(pow(self._Xcoordinate-i[0],2)+pow(self._Ycoordinate-i[1],2))
        minposition = list1.index(min(list1))
        m = Building_centres[minposition][0]
        n = Building_centres[minposition][1]
        x_next = self.nearest_step(m,n)[0]
        y_next = self.nearest_step(m,n)[1]
        self.attack(m,n,vill)
        self.move(x_next,y_next,vill)
        
        #print(list1)

    def move(self,x_next,y_next,vill):
        
            if(vill._map[x_next][y_next] == "☥"):
                vill._wall[x_next][y_next] -= 1
                if(vill._wall[x_next][y_next] == 0):
                    vill.put_on_map(x_next,y_next," ")
                        
            elif(vill._map[x_next][y_next] == " "):
                vill.put_on_map(x_next,y_next,"A")
                vill.put_on_map(self._Xcoordinate,self._Ycoordinate," ")
                vill.display()
                self._Xcoordinate = x_next
                self._Ycoordinate = y_next

    def attack(self,nearest_building_x,nearest_building_y,VILL):
        if(pow(self._Xcoordinate-nearest_building_x,2) + pow(self._Ycoordinate-nearest_building_y,2) < RANGE*RANGE):
            if(VILL._building_status[nearest_building_x][nearest_building_y] == 1):
                VILL._Hut1Health -= DAMAGE
                if(VILL._Hut1Health <= 0):
                    VILL.damage_Huts(nearest_building_x,nearest_building_y-1)
                    VILL.display()
            elif(VILL._building_status[nearest_building_x][nearest_building_y] == 2):
                VILL._Hut2Health -= DAMAGE
                if(VILL._Hut2Health <= 0):
                    VILL.damage_Huts(nearest_building_x,nearest_building_y-1)
                    VILL.display()
            elif(VILL._building_status[nearest_building_x][nearest_building_y] == 3):
                VILL._Hut3Health -= DAMAGE
                if(VILL._Hut3Health <= 0):
                    VILL.damage_Huts(nearest_building_x,nearest_building_y-1)
                    VILL.display()
            elif(VILL._building_status[nearest_building_x][nearest_building_y] == 4):
                VILL._Hut4Health -= DAMAGE
                if(VILL._Hut4Health <= 0):
                    VILL.damage_Huts(nearest_building_x,nearest_building_y-1)
                    VILL.display()
            elif(VILL._building_status[nearest_building_x][nearest_building_y] == 5):
                VILL._Hut5Health -= DAMAGE
                if(VILL._Hut5Health <= 0):
                    VILL.damage_Huts(nearest_building_x,nearest_building_y-1)
                    VILL.display()
            elif(VILL._building_status[nearest_building_x][nearest_building_y] == 6):
                VILL._CannsHealth[0] -= DAMAGE
                if(VILL._CannsHealth[0] <= 0):
                   VILL.damage_cannons(nearest_building_x,nearest_building_y)
                   VILL.display()
            elif(VILL._building_status[nearest_building_x][nearest_building_y] == 7):
                VILL._CannsHealth[1] -= DAMAGE
                if(VILL._CannsHealth[1] <= 0):
                   VILL.damage_cannons(nearest_building_x,nearest_building_y)
                   VILL.display()
            elif(VILL._building_status[nearest_building_x][nearest_building_y] == 8):
                VILL._TH_health -= DAMAGE
                if(VILL._TH_health <= 0):
                   VILL.damage_TownHall()
                   VILL.display()
            elif(VILL._building_status[nearest_building_x][nearest_building_y] == 9):
                VILL._WizsHealth[0] -= DAMAGE
                if(VILL._WizsHealth[0] <= 0):
                   VILL.dam_WizTowers(nearest_building_x,nearest_building_y)
                   VILL.display()
            elif(VILL._building_status[nearest_building_x][nearest_building_y] == 10):
                VILL._WizsHealth[1] -= DAMAGE
                if(VILL._WizsHealth[1] <= 0):
                   VILL.dam_WizTowers(nearest_building_x,nearest_building_y)
                   VILL.display()


if __name__ == '__main__':
     s = MovingArcher(9,20)
     s.movement()
    
