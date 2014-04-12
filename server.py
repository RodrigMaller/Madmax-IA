#!/bin/python
import socket
from threading import Thread
from random    import randint

class Player:
  life = 10
  dire = 'w' 
  def __init__ (self, addr, pos):
    self.addr = addr
    self.pos  = pos

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

  def run(self):
    self.printMap()


def runServer(game):
  s    = socket.socket()         
  host = socket.gethostname() 
  port = randint(6666,8080)
  s.bind(('', port))   
  print "\n",port,"\n"
  s.listen(5)
  while True:
    c, addr = s.accept()     
    print 'Got connection from', addr
    game.createPlayer(addr, c)     

gameThread = GameServer(1);
gameThread.start();
runServer(gameThread);
