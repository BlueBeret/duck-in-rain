import random
from time import sleep
from os import system

system('clear')

current_pos=0

def display(current_pos, length):
   half = length//2
   current_index = current_pos + half
   right = "_" * ( length - current_index)
   left = "_" * (current_index-1)
   print(f'\r{left}v{right}', end="") 


while 1:
   sleep(0.25)
   current_pos += random.randint(-1,1)
   display(current_pos,101)
   # print(current_pos)
