import numpy as np
from colorama import Fore, Back, Style
import os

NUMBER_OF_ROWS = 5
NUMBER_OF_COLUMNS = 7
WALL_HEALTH = 6
TOWN_HALL_HEALTH = 6
HUTS_HEALTH = 6
RANGE = 6
DAMAGE = 1
SIZE = 1
SAMPLE_HEALTH = 6
CANNONS_HEALTH  = 15

# Building_centres = [(24,35),(8,12),(10,34),(8,57),(40,12),(40,57),(24,28),(24,42)]

class map():

    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._map = np.full((self._rows*10, self._columns*10)," ")
        self._wall = np.full((self._rows*10, self._columns*10),0,dtype=int)
        self._TH_health = TOWN_HALL_HEALTH
        self._Hut1Health = HUTS_HEALTH
        self._Hut2Health = HUTS_HEALTH
        self._Hut3Health = HUTS_HEALTH
        self._Hut4Health = HUTS_HEALTH
        self._Hut5Health = HUTS_HEALTH
        self._CannsHealth = []
        self._CannsHealth.extend([CANNONS_HEALTH,CANNONS_HEALTH])
        # self._C1Health =  CANNONS_HEALTH
        # self._C2Health = CANNONS_HEALTH
        self._building_status = np.full((self._rows*10, self._columns*10),0,dtype=int)
        self._WizsHealth = []
        self._WizsHealth.extend([CANNONS_HEALTH,CANNONS_HEALTH])
        self.status()
        #print(self._wall)
        
    def status(self):
        self._building_status[8][12] = 1
        self._building_status[10][34] = 2
        self._building_status[8][57] = 3
        self._building_status[40][12] = 4
        self._building_status[40][57] = 5
        self._building_status[24][28] = 6
        self._building_status[24][42] = 7
        self._building_status[24][35] = 8
        self._building_status[13][35] = 9
        self._building_status[37][35] = 10         # Wizard Towers Building status

    def put_on_map(self, X, Y, ASCII):
        self._map[X][Y] = ASCII
        #print(self._map[25][35])
    
    def insert_health_of_wall(self,X,Y,health):
        self._wall[X][Y] = health

class Village(map):

    def __init__(self, rows, columns):
        super().__init__(rows, columns)
    
    def prepare_board():
        V = Village(NUMBER_OF_ROWS,NUMBER_OF_COLUMNS)
        V.walls(WALL_HEALTH)
        V.TownHall(TOWN_HALL_HEALTH)
        V.Huts(8,11)
        V.Huts(10,33)
        V.Huts(8,56)
        V.Huts(40,11)
        V.Huts(40,56)
        V.cannons(RANGE,DAMAGE)
        #V.damage_update(0,"")
        V.king_health_update(20)
        V.Wizard_Towers(13,35)
        V.Wizard_Towers(37,35)
        V.display()
        return V

    def display(self) :  
        os.system('clear')
        terminal_sz = os.get_terminal_size()
        print(' ' * (20 + (terminal_sz.columns - 100) // 2 - 1), 'Terminal CoC', ' ' * 20)
        for i in self._map :
            row = []
            for j in i :
                if(j == "☥"):
                    row.append(Back.RED + '☥☥' + Back.RESET)
                elif(j == "⬜"):
                    row.append(Back.RED + '⬜' + Back.RESET)
                elif(j == "╱"):
                    row.append(' ╱')
                elif(j == "╲"):
                    row.append('╲ ')
                elif(j == "⟶"):
                    row.append('⸏⸏')
                elif(j == "⚗"):
                    row.append('╃ ')
                elif(j == "c"):
                    row.append('▧ ')
                elif(j == "🗼"):
                    row.append('🗼')
                elif(j == "👑"):
                    row.append('👑')
                elif(j == "👸"):
                    row.append('👸')
                elif((j <= "Z" and "A" <= j) or (j <= "9" and j >= "0") or j ==":" or (j <= "z" and "a" <= j)):
                    row.append(j)
                else:
                    row.append('  ')
            
            #print(' ', ''.join(row))
            print(''.join(row))
            #print(' ' * ((terminal_sz.columns - 100) // 2 - 1), ''.join(row))
        
    def damage_update(self,damage,string):
        '''
        Displays the damage on the top right corner of the game board on the top bar 
        The score is left padded with 0s
        '''
        scorename = 'DAMAGE BY '+ str(string) +': ' +str(damage)
        leng = len(scorename)
        startat = self._columns*10-2-leng
        for i in range(leng):
            self.put_on_map(1, i+startat, scorename[i])

    def king_health_update(self,health):
        '''
        Displays the damage on the top right corner of the game board on the top bar 
        The score is left padded with 0s
        '''
        scorename = 'KING_HEALTH: '
        leng = len(scorename)
        startat = self._columns*10-2-leng
        for i in range(leng):
            self.put_on_map(2, i+startat, scorename[i])
        
    def walls(self,health):
# first loop wall
         for x in range(25,45):
             self.put_on_map(15,x,"☥")
             self.insert_health_of_wall(15,x,WALL_HEALTH)
             self.put_on_map(35,x,"☥")
             self.insert_health_of_wall(35,x,WALL_HEALTH)
         for x in range(16,35):
             self.put_on_map(x,25,"☥")
             self.insert_health_of_wall(x,25,WALL_HEALTH)
             self.put_on_map(x,44,"☥")
             self.insert_health_of_wall(x,44,WALL_HEALTH)

# 2nd loop wall
         for x in range(8,63):
             self.put_on_map(5,x,"☥")
             self.insert_health_of_wall(5,x,WALL_HEALTH)
             self.put_on_map(45,x,"☥")
             self.insert_health_of_wall(45,x,WALL_HEALTH)
         for x in range(5,46):
             self.put_on_map(x,8,"☥")
             self.insert_health_of_wall(x,8,WALL_HEALTH)
             self.put_on_map(x,62,"☥")
             self.insert_health_of_wall(x,62,WALL_HEALTH)
         

    def TownHall(self,health):
         for x in range(24,27):
             for y in range(33,37):
                 self.put_on_map(x,y,"⬜")
         self.put_on_map(23,33,"╱")
         self.put_on_map(23,36,"╲")
         self.put_on_map(22,34,"⟶")
         self.put_on_map(22,35,"⟶")
    
    def damage_TownHall(self):
         for x in range(24,27):
             for y in range(33,37):
                 self.put_on_map(x,y," ")
         self.put_on_map(23,33," ")
         self.put_on_map(23,36," ")
         self.put_on_map(22,34," ")
         self.put_on_map(22,35," ")
         self._building_status[24][35] = 0

    def Huts(self,X,Y):
        for x in range(X,X+2):
             for y in range(Y,Y+3):
                 self.put_on_map(x,y,"⬜")
        self.put_on_map(X-1,Y,"╱")
        self.put_on_map(X-1,Y+2,"╲")
        self.put_on_map(X-2,Y+1,"⟶")
    
    def damage_Huts(self,X,Y):
        for x in range(X,X+2):
             for y in range(Y,Y+3):
                 self.put_on_map(x,y," ")
        self.put_on_map(X-1,Y," ")
        self.put_on_map(X-1,Y+2," ")
        self.put_on_map(X-2,Y+1," ")
        self._building_status[X][Y+1] = 0
    
    def cannons(self,ran,dam):
        self.put_on_map(24,28,"⚗")
        self.put_on_map(24,42,"⚗")
        self.put_on_map(25,28,"c")
        self.put_on_map(25,42,"c")
    
    def damage_cannons(self,X,Y):
        self.put_on_map(X,Y," ")
        self.put_on_map(X+1,Y," ")
        self._building_status[X][Y] = 0
    
    def Wizard_Towers(self,x,y):
        self.put_on_map(x,y,"🗼")

    def dam_WizTowers(self,x,y):
        self.put_on_map(x,y," ")
        self._building_status[x][y] = 0


