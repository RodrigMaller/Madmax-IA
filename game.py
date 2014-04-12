from threading import Thread
from bullet import Bullet
from player import Player
from random import randint
from map1 import Map1
import time

class GameServer(Thread): 
  def __init__ (self, num, map1):
    Thread.__init__(self)
    self.num = num
    self.map1 = map1
  
  bullets     = []
  players     = {}
  connections = {}
  
  def createPlayer(self, addr, c):
    self.connections[addr] = c
    pos = self.map1.randomPosition()
    self.players[addr] = Player(addr,pos)
    self.map1.setPos(pos[0], pos[1], 2)
    self.map1.printMap()

  def getAddrOfPlayerAt(self, pos):
    for addr,player in self.players.iteritems():
      if player.getPos() == pos:
        return addr

  def doCollision(self,bullet):
    pos   = bullet.getPos()
    value = self.map1.getPos(pos[0],pos[1])
    if   value == 1:
      return True
    elif value == 2:
      addr = self.getAddrOfPlayerAt(pos)
      self.players[addr].hit(1)
      return True

  def updateBullets(self,speed):
    while speed != 0:
      for key, bullet in enumerate(self.bullets):
        pos = bullet.getPos();
        if (self.map1.getPos(pos[0], pos[1]) == 3):
          self.map1.setPos(pos[0], pos[1], 0)

        bullet.move()
        collided = self.doCollision(bullet)
        if collided:
          del self.bullets[key]
        else:
          newPos = bullet.getPos()
          self.map1.setPos(newPos[0], newPos[1], 3)
      speed -= 1
       
  def killPlayer(self, addr):
    self.connections[addr].close()
    del self.connections[addr]
    pos = self.players[addr].getPos()
    self.map1.setPos(pos[0], pos[1], 0)
    del self.players[addr]

  def playerVision(self, player):
    return 'oi'

  def shoot(self, player):
    pos = player.getPos();
    self.bullets.append(Bullet(player.getDire(), 
                               [pos[0],pos[1]]))

  def doCommand(self, player, command):
    command = command[0]
    if   command == '-':
      self.shoot(player)
    elif command == '^':
      pos = player.getPos()
      player.move(self.map1)
    elif command == 'w':
      player.setDire('w')
    elif command == 's':
      player.setDire('s')
    elif command == 'd':
      player.setDire('d')
    elif command == 'a':
      player.setDire('a')

  def updatePlayers(self):
    deads = []
    for addr, player in self.players.iteritems():
      if player.getLife() <= 0: 
        deads.append(addr)
      else:
        conn   = self.connections[addr] 
        vision = self.playerVision(player)
        life   = player.getLife()
        msg    = vision+'|'+str(life)
        conn.send(msg)

        command = conn.recv(4)
        self.doCommand(player, command)
    for dead in deads:
      self.killPlayer(dead)

  def run(self):
    print "Esperando Jogadores"
    while len(GameServer.players) < 2:
      time.sleep(5)
    while True:
      self.updateBullets(2)
      self.updatePlayers()
      self.map1.printMap()
      time.sleep(1)
