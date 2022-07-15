import time
import os
from src.barbarians import MovingBarbarians
from src.Balloons import MovingBalloon

from src.king import MovingKing
from src.village import Village
import src.input
import numpy as np
from src.archer import MovingArcher

NUMBER_OF_ROWS = 5
NUMBER_OF_COLUMNS = 7
WALL_HEALTH = 6
TOWN_HALL_HEALTH = 6
HUTS_HEALTH = 6
RANGE = 6
DAMAGE = 3
SIZE = 1
SAMPLE_HEALTH = 6
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


class KING_MOVEMENT():
    
    def KingMovement():
        V = Village.prepare_board()
        King = MovingKing(0,0)
        V.put_on_map(0,0,King._king)
        V.display()
        K = []
        Balloons = []
        Barbarians = []
        number_archers = 0
        number_barbarians = 0
        number_balloons = 0
        while(1):
            time.sleep(0.02)
            inp = src.input
            p = King._Xdistance
            q = King._Ydistance
            if(((p-25)**2 + (q-28)**2) < 30 or ((p-25)**2 + (q-42)**2) < 30):
                King.Health -= DAMAGE
            if(((p-13)**2 + (q-35)**2) < 30 or ((p-37)**2 + (q-35)**2) < 30):
                King.Health -= DAMAGE
            # if(King.Health <= 0):
            #     os.system('clear')
            #     print("DEFEAT")
            #     break
            
            c = inp.input_to(inp.Get())
            
            # king moves up
            if c == 'W':
                if(King._Xdistance == 0 and ( 0 <= King._Ydistance and King._Ydistance <= 70 )):
                    continue
                elif(V._map[King._Xdistance-1][King._Ydistance] == " "):
                    x = King._Xdistance
                    y = King._Ydistance
                    King.Left()
                    V.put_on_map(x,y," ")
                    V.put_on_map(King._Xdistance,King._Ydistance,King._king)
                    V.display()
                else:
                    continue

            elif c == 'A':
                if(King._Ydistance == 0 and ( 0 <= King._Xdistance and King._Xdistance <= 50 )):
                    continue
                elif(V._map[King._Xdistance][King._Ydistance-1] == " "):
                    x = King._Xdistance
                    y = King._Ydistance
                    King.Down()
                    V.put_on_map(x,y," ")
                    V.put_on_map(King._Xdistance,King._Ydistance,King._king)
                    V.display()
                else:
                    continue

            elif c == 'S':
                if(King._Xdistance == 49 and ( 0 <= King._Ydistance and King._Ydistance <= 70 )):
                    continue
                elif(V._map[King._Xdistance+1][King._Ydistance] == " "):
                    x = King._Xdistance
                    y = King._Ydistance
                    King.Right()
                    V.put_on_map(x,y," ")
                    V.put_on_map(King._Xdistance,King._Ydistance,King._king)
                    V.display()
                else:
                    continue

            elif c == 'D':
                if(King._Ydistance == 69 and ( 0 <= King._Xdistance and King._Xdistance <= 50 )):
                    continue
                elif(V._map[King._Xdistance][King._Ydistance+1] == " "):
                    x = King._Xdistance
                    y = King._Ydistance
                    King.Up()
                    V.put_on_map(x,y," ")
                    V.put_on_map(King._Xdistance,King._Ydistance,King._king)
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
                 if(V._wall[King._Xdistance+1][King._Ydistance] != 0):
                      V._wall[King._Xdistance+1][King._Ydistance] -= 1
                      if(V._wall[King._Xdistance+1][King._Ydistance] == 0):
                          V.put_on_map(King._Xdistance+1,King._Ydistance," ")
                          V.display()
                 elif(V._wall[King._Xdistance-1][King._Ydistance] != 0):
                      V._wall[King._Xdistance-1][King._Ydistance] -= 1
                      if(V._wall[King._Xdistance-1][King._Ydistance] == 0):
                          V.put_on_map(King._Xdistance-1,King._Ydistance," ")
                          V.display()
                 elif(V._wall[King._Xdistance][King._Ydistance+1] != 0):
                      V._wall[King._Xdistance][King._Ydistance+1] -= 1
                      if(V._wall[King._Xdistance][King._Ydistance+1] == 0):
                          V.put_on_map(King._Xdistance,King._Ydistance+1," ")
                          V.display()
                 elif(V._wall[King._Xdistance][King._Ydistance-1] != 0):
                      V._wall[King._Xdistance][King._Ydistance-1] -= 1
                      if(V._wall[King._Xdistance][King._Ydistance-1] == 0):
                          V.put_on_map(King._Xdistance,King._Ydistance-1," ")
                          V.display()
                 elif(V._map[King._Xdistance+1][King._Ydistance] == "⬜" or V._map[King._Xdistance][King._Ydistance+1] == "⬜"
                        or V._map[King._Xdistance-1][King._Ydistance] == "⬜" or V._map[King._Xdistance][King._Ydistance-1] == "⬜"):
                        if (King._Xdistance <28 and King._Xdistance > 23):
                           V._TH_health -= 1
                           if(V._TH_health == 0):
                              King._damage_by_king += 35
                              V.damage_TownHall()
                              V.damage_update(King._damage_by_king,"King")
                              V.display()
                        elif(King._Xdistance < 43 and King._Xdistance > 39):
                             if(King._Ydistance <= 14 and 10 <= King._Ydistance):
                                 V._Hut4Health -= 1
                                 if(V._Hut4Health == 0):
                                   King._damage_by_king += 13
                                   V.damage_Huts(40,11)
                                   V.damage_update(King._damage_by_king,"King")
                                   V.display()
                             else:
                                 V._Hut5Health -= 1
                                 if(V._Hut5Health == 0):
                                    King._damage_by_king += 13
                                    V.damage_Huts(40,56)
                                    V.damage_update(King._damage_by_king,"King")
                                    V.display()
                        else:
                            if(King._Ydistance <= 14 and 10 <= King._Ydistance):
                                 V._Hut1Health -= 1
                                 if(V._Hut1Health == 0):
                                    King._damage_by_king += 13
                                    V.damage_Huts(8,11)
                                    V.damage_update(King._damage_by_king,"King")
                                    V.display()
                            elif(King._Ydistance <= 59 and 55 <= King._Ydistance):
                                 V._Hut3Health -= 1
                                 if(V._Hut3Health == 0):
                                    King._damage_by_king += 13
                                    V.damage_Huts(8,56)
                                    V.damage_update(King._damage_by_king,"King")
                                    V.display()
                            else:
                                 V._Hut2Health -= 1
                                 if(V._Hut2Health == 0):
                                    King._damage_by_king += 13
                                    V.damage_Huts(10,33)
                                    V.damage_update(King._damage_by_king,"King")
                                    V.display()
                            
            elif c == 'q':
                os.system('clear')
                print("Bye!!")
                break
            if (King._damage_by_king == 100):
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
                if(len(Barbarians) == 0 and len(K) == 0 and len(Balloons) == 0 and King.Health <= 0):
                    os.system('clear')
                    print("DEFEAT")
                    break
                 

