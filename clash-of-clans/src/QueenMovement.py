import time
import os

from src.queen import MovingQueen
from src.village import Village
import src.input
import numpy as np
from src.archer import MovingArcher
from src.Balloons import MovingBalloon
from src.barbarians import MovingBarbarians

NUMBER_OF_ROWS = 5
NUMBER_OF_COLUMNS = 7
WALL_HEALTH = 6
TOWN_HALL_HEALTH = 6
HUTS_HEALTH = 6
RANGE = 6
DAMAGE = 3
SIZE = 1
SAMPLE_HEALTH = 6
H1_XCENTRE = 8
H1_YCENTRE = 12
H2_XCENTRE = 10
H2_YCENTRE = 34
H3_XCENTRE = 8
H3_YCENTRE = 57
H4_XCENTRE = 40
H4_YCENTRE = 12
H5_XCENTRE = 40
H5_YCENTRE = 57
X_JSPAWN = 0
Y_JSPAWN = 30
X_MSPAWN = 3
Y_MSPAWN = 5
X_XSPAWN = 1
Y_XSPAWN = 68
X_YSPAWN = 45
Y_YSPAWN = 4
X_ZSPAWN = 0
Y_ZSPAWN = 29

class Queen_MOVEMENT():
    
    def QueenMovement():
        x = ''
        V = Village.prepare_board()
        Queen = MovingQueen(0,0)
        V.put_on_map(0,0,Queen._queen)
        K = []
        Balloons = []
        Barbarians = []
        number_archers = 0
        number_barbarians = 0
        number_balloons = 0
        V.display()
        while(1):
            time.sleep(0.02)
            inp = src.input
            p = Queen._Xdistance
            q = Queen._Ydistance
            if(((p-25)**2 + (q-28)**2) < 30 or ((p-25)**2 + (q-42)**2) < 30):
                Queen.Health -= DAMAGE
            if(((p-13)**2 + (q-35)**2) < 30 or ((p-37)**2 + (q-35)**2) < 30):
                Queen.Health -= DAMAGE
            # if(Queen.Health <= 0):
            #     os.system('clear')
            #     print("DEFEAT")
            #     break

            c = inp.input_to(inp.Get())
            
            # Queen moves up
            if c == 'W':
                if(Queen._Xdistance == 0 and ( 0 <= Queen._Ydistance and Queen._Ydistance <= 70 )):
                    continue
                elif(V._map[Queen._Xdistance-1][Queen._Ydistance] == " "):
                    x = Queen._Xdistance
                    y = Queen._Ydistance
                    Queen.Left()
                    V.put_on_map(x,y," ")
                    V.put_on_map(Queen._Xdistance,Queen._Ydistance,Queen._queen)
                    V.display()
                else:
                    continue

            elif c == 'A':
                if(Queen._Ydistance == 0 and ( 0 <= Queen._Xdistance and Queen._Xdistance <= 50 )):
                    continue
                elif(V._map[Queen._Xdistance][Queen._Ydistance-1] == " "):
                    x = Queen._Xdistance
                    y = Queen._Ydistance
                    Queen.Down()
                    V.put_on_map(x,y," ")
                    V.put_on_map(Queen._Xdistance,Queen._Ydistance,Queen._queen)
                    V.display()
                else:
                    continue

            elif c == 'S':
                if(Queen._Xdistance == 49 and ( 0 <= Queen._Ydistance and Queen._Ydistance <= 70 )):
                    continue
                elif(V._map[Queen._Xdistance+1][Queen._Ydistance] == " "):
                    x = Queen._Xdistance
                    y = Queen._Ydistance
                    Queen.Right()
                    V.put_on_map(x,y," ")
                    V.put_on_map(Queen._Xdistance,Queen._Ydistance,Queen._queen)
                    V.display()
                else:
                    continue

            elif c == 'D':
                if(Queen._Ydistance == 69 and ( 0 <= Queen._Xdistance and Queen._Xdistance <= 50 )):
                    continue
                elif(V._map[Queen._Xdistance][Queen._Ydistance+1] == " "):
                    x = Queen._Xdistance
                    y = Queen._Ydistance
                    Queen.Up()
                    V.put_on_map(x,y," ")
                    V.put_on_map(Queen._Xdistance,Queen._Ydistance,Queen._queen)
                    V.display()
                else:
                    continue
            elif c == 'P':
                if(number_barbarians < 6):
                    Barbarians.append(MovingBarbarians(X_JSPAWN,Y_JSPAWN))
                    number_barbarians += 1
                    length = len(Barbarians)
                    Barbarians[length-1].movement(V)
            elif c == 'Q':
                if(number_barbarians < 6):
                    Barbarians.append(MovingBarbarians(X_MSPAWN,Y_MSPAWN))
                    number_barbarians += 1
                    length = len(Barbarians)
                    Barbarians[length-1].movement(V)
            elif c == 'R':
                if(number_barbarians < 6):
                    Barbarians.append(MovingBarbarians(X_XSPAWN,Y_XSPAWN))
                    number_barbarians += 1
                    length = len(Barbarians)
                    Barbarians[length-1].movement(V)
                    
            elif c == 'J':
                if(number_archers < 6):
                    K.append(MovingArcher(X_JSPAWN,Y_JSPAWN))
                    number_archers += 1
                    length = len(K)
                    K[length-1].movement(V)
            
            elif c == 'M':
                if(number_archers < 6):
                    K.append(MovingArcher(X_MSPAWN,Y_MSPAWN))
                    number_archers += 1
                    length = len(K)
                    K[length-1].movement(V)
            elif c == 'N':
                if(number_archers < 6):
                    K.append(MovingArcher(47,65))
                    number_archers += 1
                    length = len(K)
                    K[length-1].movement(V)

            elif c == 'X':
                if(number_balloons < 3):
                    Balloons.append(MovingBalloon(X_XSPAWN,Y_XSPAWN))
                    number_balloons += 1
                    length = len(Balloons)
                    Balloons[length-1].movement(V)
            
            elif c == 'Y':
                if(number_balloons < 3):
                    Balloons.append(MovingBalloon(X_YSPAWN,Y_YSPAWN))
                    number_balloons += 1
                    length = len(Balloons)
                    Balloons[length-1].movement(V)
            elif c == 'Z':
                if(number_balloons < 3):
                    Balloons.append(MovingBalloon(X_ZSPAWN,Y_ZSPAWN))
                    number_balloons += 1
                    length = len(Balloons)
                    Balloons[length-1].movement(V)
            elif c == ' ':
                 if(x == 'W'):
                     AOE_x = Queen._Xdistance - 8
                     AOE_y = Queen._Ydistance 
        
                 elif(x == 'A'):
                     AOE_x = Queen._Xdistance
                     AOE_y = Queen._Ydistance - 8
                                          
                 elif(x == 'S'):
                     AOE_x = Queen._Xdistance + 8
                     AOE_y = Queen._Ydistance 
                      
                 elif(x == 'D'):
                     AOE_x = Queen._Xdistance
                     AOE_y = Queen._Ydistance + 8


                 if(abs((AOE_x-H1_XCENTRE) + (AOE_y - H1_YCENTRE)) + abs((AOE_x-H1_XCENTRE) - (AOE_y - H1_YCENTRE)) <= 7):
                    V._Hut1Health -= 1
                    if(V._Hut1Health == 0):
                       Queen._damage_by_queen += 13
                       V.damage_Huts(8,11)
                       V.damage_update(Queen._damage_by_queen,"Queen")
                       V.display()
                 elif(abs((AOE_x-H2_XCENTRE) + (AOE_y - H2_YCENTRE)) + abs((AOE_x-H2_XCENTRE) - (AOE_y - H2_YCENTRE)) <= 7):
                      V._Hut2Health -= 1
                      if(V._Hut2Health == 0):
                         Queen._damage_by_queen += 13
                         V.damage_Huts(10,33)
                         V.damage_update(Queen._damage_by_queen,"Queen")
                         V.display()
                 elif(abs((AOE_x-H3_XCENTRE) + (AOE_y - H3_YCENTRE)) + abs((AOE_x-H3_XCENTRE) - (AOE_y - H3_YCENTRE)) <= 7):
                      V._Hut3Health -= 1
                      if(V._Hut3Health == 0):
                         Queen._damage_by_queen += 13
                         V.damage_Huts(8,56)
                         V.damage_update(Queen._damage_by_queen,"Queen")
                         V.display()
                 elif(abs((AOE_x-H4_XCENTRE) + (AOE_y - H4_YCENTRE)) + abs((AOE_x-H4_XCENTRE) - (AOE_y - H4_YCENTRE)) <= 7):
                      V._Hut4Health -= 1
                      if(V._Hut4Health == 0):
                         Queen._damage_by_queen += 13
                         V.damage_Huts(40,11)
                         V.damage_update(Queen._damage_by_queen,"Queen")
                         V.display()
                 elif(abs((AOE_x-H5_XCENTRE) + (AOE_y - H5_YCENTRE)) + abs((AOE_x-H5_XCENTRE) - (AOE_y - H5_YCENTRE)) <= 7):
                      V._Hut5Health -= 1
                      if(V._Hut5Health == 0):
                         Queen._damage_by_queen += 13
                         V.damage_Huts(40,56)
                         V.damage_update(Queen._damage_by_queen,"Queen")
                         V.display()
                 elif(abs((AOE_x-24) + (AOE_y - 35)) + abs((AOE_x-24) - (AOE_y - 35)) <= 9):
                      V._TH_health -= 1
                      if(V._TH_health == 0):
                         Queen._damage_by_queen += 35
                         V.damage_TownHall()
                         V.damage_update(Queen._damage_by_queen,"Queen")
                         V.display()
                 else:
                     if(V._wall[Queen._Xdistance+1][Queen._Ydistance] != 0):
                          V._wall[Queen._Xdistance+1][Queen._Ydistance] -= 1
                          if(V._wall[Queen._Xdistance+1][Queen._Ydistance] == 0):
                             V.put_on_map(Queen._Xdistance+1,Queen._Ydistance," ")
                             V.display()
                     elif(V._wall[Queen._Xdistance-1][Queen._Ydistance] != 0):
                          V._wall[Queen._Xdistance-1][Queen._Ydistance] -= 1
                          if(V._wall[Queen._Xdistance-1][Queen._Ydistance] == 0):
                             V.put_on_map(Queen._Xdistance-1,Queen._Ydistance," ")
                             V.display()
                     elif(V._wall[Queen._Xdistance][Queen._Ydistance+1] != 0):
                          V._wall[Queen._Xdistance][Queen._Ydistance+1] -= 1
                          if(V._wall[Queen._Xdistance][Queen._Ydistance+1] == 0):
                             V.put_on_map(Queen._Xdistance,Queen._Ydistance+1," ")
                             V.display()
                     elif(V._wall[Queen._Xdistance][Queen._Ydistance-1] != 0):
                          V._wall[Queen._Xdistance][Queen._Ydistance-1] -= 1
                          if(V._wall[Queen._Xdistance][Queen._Ydistance-1] == 0):
                             V.put_on_map(Queen._Xdistance,Queen._Ydistance-1," ")
                             V.display()

            # some part for when Archery queen can't enter the village
                            
            elif c == 'q':
                os.system('clear')
                print("Bye!!")
                break
            if(c == 'W' or c == 'A' or c == 'S' or c == 'D'):
                x = c                                         # gets previous direction

            if (Queen._damage_by_queen == 100):
                os.system('clear')
                print("VICTORY")
                break
            for a in range(0,len(K)):
                K[a].movement(V)
            for b in range(0,len(Balloons)):
                Balloons[b].movement(V)
            for d in range(0,len(Barbarians)):
                Barbarians[d].movement(V)
            # cannons with Barbarians and Archers
            for e in range(len(Barbarians)):
               # print(e)
                if(e >= len(Barbarians) or e < 0):
                       break
                if(V._CannsHealth[0] > 0):
                   p = Barbarians[e]._Xcoordinate
                   q = Barbarians[e]._Ycoordinate
                   if(((p-25)**2 + (q-28)**2) < 30):
                      Barbarians[e]._Health -= DAMAGE
                   if(Barbarians[e]._Health <= 0):
                     V.put_on_map(p,q," ")
                     V.display()
                     Barbarians.pop(e)
                if(e >= len(Barbarians) or e < 0):
                       break
                if(V._CannsHealth[1] > 0):
                   p = Barbarians[e]._Xcoordinate
                   q = Barbarians[e]._Ycoordinate
                   if(((p-25)**2 + (q-42)**2) < 30):
                      Barbarians[e]._Health -= DAMAGE
                   if(Barbarians[e]._Health <= 0):
                     V.put_on_map(p,q," ")
                     V.display()
                     Barbarians.pop(e)
            for e in range(len(K)):
                #print(e)
                if(e >= len(K) or e < 0):
                    break
                if(V._CannsHealth[0] > 0):
                    p = K[e]._Xcoordinate
                    q = K[e]._Ycoordinate
                    if(((p-25)**2 + (q-28)**2) < 30):
                       K[e]._Health -= DAMAGE
                    if(K[e]._Health <= 0):
                       V.put_on_map(p,q," ")
                       V.display()
                       K.pop(e)
                if(e >= len(K) or e < 0):
                       break
                if(V._CannsHealth[1] > 0):
                    p = K[e]._Xcoordinate
                    q = K[e]._Ycoordinate
                    if(((p-25)**2 + (q-42)**2) < 30):
                       K[e]._Health -= DAMAGE
                    if(K[e]._Health <= 0):
                       V.put_on_map(p,q," ")
                       V.display()
                       K.pop(e)
            # Wizard tower with Barbarians,Archers and Balloons
            for e in range(len(Barbarians)):
                if(e >= len(Barbarians) or e < 0):
                   break
                if(V._WizsHealth[0] > 0):
                   p = Barbarians[e]._Xcoordinate
                   q = Barbarians[e]._Ycoordinate
                   if(((p-13)**2 + (q-35)**2) < 30):
                      Barbarians[e]._Health -= DAMAGE
                   if(Barbarians[e]._Health <= 0):
                     V.put_on_map(p,q," ")
                     V.display()
                     Barbarians.pop(e)
                if(e >= len(Barbarians) or e < 0):
                       break
                if(V._WizsHealth[1] > 0):
                   p = Barbarians[e]._Xcoordinate
                   q = Barbarians[e]._Ycoordinate
                   if(((p-37)**2 + (q-35)**2) < 30):
                      Barbarians[e]._Health -= DAMAGE
                   if(Barbarians[e]._Health <= 0):
                     V.put_on_map(p,q," ")
                     V.display()
                     Barbarians.pop(e)
            for e in range(len(K)):
                if(e >= len(K) or e < 0):
                    break
                if(V._WizsHealth[0] > 0):
                    p = K[e]._Xcoordinate
                    q = K[e]._Ycoordinate
                    if(((p-13)**2 + (q-35)**2) < 30):
                       K[e]._Health -= DAMAGE
                    if(K[e]._Health <= 0):
                       V.put_on_map(p,q," ")
                       V.display()
                       K.pop(e)
                if(e >= len(K) or e < 0):
                       break
                if(V._WizsHealth[1] > 0):
                    p = K[e]._Xcoordinate
                    q = K[e]._Ycoordinate
                    if(((p-37)**2 + (q-35)**2) < 30):
                       K[e]._Health -= DAMAGE
                    if(K[e]._Health <= 0):
                       V.put_on_map(p,q," ")
                       V.display()
                       K.pop(e)
            for e in range(len(Balloons)):
                if(e >= len(Balloons) or e < 0):
                    break
                if(V._WizsHealth[0] > 0):
                    p = Balloons[e]._Xcoordinate
                    q = Balloons[e]._Ycoordinate
                    if(((p-13)**2 + (q-35)**2) < 30):
                       Balloons[e]._Health -= DAMAGE
                    if(Balloons[e]._Health <= 0):
                       V.put_on_map(p,q," ")
                       V.display()
                       Balloons.pop(e)
                if(e >= len(Balloons) or e < 0):
                       break
                if(V._WizsHealth[1] > 0):
                    p = Balloons[e]._Xcoordinate
                    q = Balloons[e]._Ycoordinate
                    if(((p-37)**2 + (q-35)**2) < 30):
                       Balloons[e]._Health -= DAMAGE
                    if(Balloons[e]._Health <= 0):
                       V.put_on_map(p,q," ")
                       V.display()
                       Balloons.pop(e)
            
            if(number_balloons == 3 and number_barbarians == 6 and number_archers == 6):
                if(len(Barbarians) == 0 and len(K) == 0 and len(Balloons) == 0 and Queen.Health <= 0):
                    os.system('clear')
                    print("DEFEAT")
                    break
            
        


