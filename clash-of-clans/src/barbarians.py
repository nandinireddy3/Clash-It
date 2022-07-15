import numpy as np
import os


DAMAGE =1
HEALTH = 10

class MovingBarbarians():
    def __init__(self,x,y):
        self._Xcoordinate = x
        self._Ycoordinate = y
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
        #self.attack(m,n,vill)
        self.move(x_next,y_next,m,n,vill)
        
        #print(list1)

    def move(self,x_next,y_next,p,q,vill):
        
            if(vill._map[x_next][y_next] == "☥"):
                vill._wall[x_next][y_next] -= 1
                if(vill._wall[x_next][y_next] == 0):
                    vill.put_on_map(x_next,y_next," ")
                        
            elif(vill._map[x_next][y_next] == " "):
                vill.put_on_map(x_next,y_next,"B")
                vill.put_on_map(self._Xcoordinate,self._Ycoordinate," ")
                vill.display()
                self._Xcoordinate = x_next
                self._Ycoordinate = y_next
            elif(vill._map[x_next][y_next] == "B" or vill._map[x_next][y_next] == "A" or vill._map[x_next][y_next] == "O"):
                pass
            else:
                self.attack(p,q,vill)

    def attack(self,nearest_building_x,nearest_building_y,VILL):
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
