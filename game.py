from threading import Thread
from bullet import Bullet
from player import Player
from random    import randint

class GameServer(Thread): 
  def __init__ (self, num):
    Thread.__init__(self)
    self.num = num
  
  map1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

  bullets     = {}
  players     = {}
  connections = {}

  def printMap(self):
    for line in self.map1:
      print "|",
      for square in line: 
        if   square == 2:
          print("$"),
        elif square == 0: 
          print(" "),
        elif square == 1:
          print("*"),
      print "|"
  
  def isValidPosition(self,pos):
    return (pos[0] > 0) and (pos[0] < len(self.map1)) and (pos[1] > 0) and (pos[1] < len(self.map1[0])) and (self.map1[pos[0]][pos[1]] == 0)

  def randomPosition(self):
    pos = [-1,-1]
    while (not self.isValidPosition(pos)):
      pos[0] = randint(0,len(self.map1))
      pos[1] = randint(0,len(self.map1[0]))
    return pos

  def createPlayer(self, addr, c):
    self.connections[addr] = c
    pos = self.randomPosition()
    self.players[addr]        = Player(addr,pos)
    self.map1[pos[0]][pos[1]] = 2
    self.printMap()

  def updateBullets(self,speed):
    for bullet, key in bullets:
      bullet.move(speed)
      checkColisions(bullet)
       
  #def updatePlayers(self):

  def run(self):
#    self.updateBullets(2)
#    self.updatePlayers()
    self.printMap()


