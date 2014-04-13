from random import randint
from mapGenerator import MapGenerator
import os
import math

class Map1:
  map1 = MapGenerator().getMap()
  '''[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
          [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,1,0,0,0,0,1,0,0,1,1,0],
          [0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
          [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,1,1,1,1,0,0,0,0,0,0,0,1,1],
          [0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]'''

  def printMap(self):
    os.system('clear')
    for line in self.map1:
      print "|",
      for square in line:
        if square == 2:
          print("$"),
        elif square == 0:
          print(" "),
        elif square == 1:
          print("*"),
        elif square == 3:
          print("."),
      print "|"
 
  def isValidPosition(self,pos):
    return (pos[0] > 0) and (pos[0] < len(self.map1)) and (pos[1] > 0) and (pos[1] < len(self.map1[0])) 

  def isBlockPosition(self, pos):
    return self.isValidPosition(pos) and (pos[1] < len(self.map1[0])) and (self.map1[pos[0]][pos[1]] == 0 or self.map1[pos[0]][pos[1]] == 3) 

  def randomPosition(self):
    pos = [-1,-1]
    while (not self.isBlockPosition(pos)):
      pos[0] = randint(0,len(self.map1))
      pos[1] = randint(0,len(self.map1[0]))
    return pos

  def getPos(self, x, y):
    if self.isValidPosition([x,y]):
      return self.map1[x][y]
    else:
      return 1

  def setPos(self, x, y, value):
    self.map1[x][y] = value

#  def vision(self, x, y, dire):
#    if   dire == "w":
#      angle = 135
#    elif dire == "s":
#      angle = 315 
#    elif dire == "d":  
#      angle = 45
#    elif dire == "a":
#      angle = 225
#    f1 = (lambda xa: tan(radians(angle))*(xa - x) + y)
#    f2 = (lambda xa: tan(radians(angle-90))*(xa - x) + y)
#    i,j = 0
#    for lines in self.map1:
#      j=0;
#      for square in line:
#        if(dire == "w" or dire == "s"):
#          
#        else:
#
#        j+=1
#      i+=1
