from ntpath import join
import numpy as np
from colorama import Fore, Back, Style
import subprocess as sp
from scipy import rand
import time
import os

from src.king import MovingKing
from src.village import Village
import src.input
from src.KingMovement import KING_MOVEMENT
from src.QueenMovement import Queen_MOVEMENT



class GamePlay():

    def start_game():
        c = input("Press K for King or Q for Archer Queen: ")
        r = input("Select the Level: ")
        if(r != "1"):
            print("Sorry Your input Levels not exist")
            exit()
        if(c == 'K'):
            KING_MOVEMENT.KingMovement()
        elif(c == 'Q'):
            Queen_MOVEMENT.QueenMovement()
        else:
            print("Valid Input is not Given")

    

if __name__ == '__main__':
    print("WELCOME TO CLASH OF CLANS MY FRIEND !!")
    print("Please enter your name: ")
    name = input()
    print("Hii",name,"!!")
    
    sp.call('clear', shell=True)  # Clears the screen. 
    
    GamePlay.start_game()
    