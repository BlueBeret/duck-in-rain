#alpaca_ascii
from random import randint, choice
from os import system
from time import sleep
import platform

# https://textart.io/art/ft1qjWJ5kTNGFilh01U8xgeF/duckling-swimming
class Duck():
  def __init__(self, WIDTH):
    self.duck="""  __
<(o )___
 ( ._> /
  `---'"""
    self.duck_right="""    __
___( o)>
\  <_.)
 `---'"""
    self.face_left = True
    self.height = 4
    self.width = 8
    self.position = WIDTH//3

  def face(self, face_left):
    self.face_left = face_left
    return self

  def move(self, step):
    if step > 0:
      self.face(False)
    elif step < 0:
      self.face(True)
    self.position += step
    return self
  
  def display(self):
    if self.face_left:
      print(self.duck)
    else:
      print(self.duck_right)

  def display_with_rain(self, width):
    duck = self.duck if self.face_left else self.duck_right
    duck = duck.split("\n")
    for i in range(self.height):
      rain_right = [choice("                     |          ") for _ in range(width - self.position)]
      rain_left = [choice("                     |          ") for _ in range(self.position)]
      print("".join(rain_left + [duck[i]] + rain_right))
  




def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

def display(duck: Duck, heigth, width, river):
    clear()
    for _ in range(heigth - duck.height, -1, -1):
      print("".join([choice("                     |          ") for _ in range(width)]))
    Pupi.display_with_rain(WIDTH)
    for _ in range(river):
      print("".join(["^" for _ in range(width)]))
    
WIDTH = 120
HEIGTH = 20

if __name__ == "__main__":
  Pupi = Duck(WIDTH)
  while 1:
    sleep(0.05)
    if Pupi.face_left:
      Pupi.move(choice([-1,-1,-1,0,1]) * 3)
    else:
      Pupi.move(choice([-1,0,1,1,1]) * 4)
    if Pupi.position > HEIGTH - Pupi.height:
      Pupi.position = HEIGTH
    elif Pupi.position < Pupi.width:
      Pupi.position = Pupi.width

    display(Pupi, HEIGTH, WIDTH, 10)





