from random import randint, choice
from os import system
from time import sleep
import platform

HEIGTH = 30
WIDTH = 120

position = [HEIGTH//2 for i in range(WIDTH)]

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

def display(position, width, heigth):
    clear()
    for i in range(heigth, -1, -1):
        print("".join(["^" if position[j] > i else choice("                     |          ") for j in range(width)]))

while 1:
    sleep(0.05)
    for i in range(WIDTH-1):
        position[i] = position[i+1]
    
    position[-1] += randint(-1,1)
    if position[-1] > HEIGTH:
        position[-1] = HEIGTH
    elif position[-1] < 0:
        position[-1] = 0
    display(position, WIDTH, HEIGTH)

