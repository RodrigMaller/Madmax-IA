import sys, os
import pygame
from Shot import Shot
from pygame.locals import *

class Player(pygame.sprite.Sprite):
  def __init__ (self, addr, pos, image):
    pygame.sprite.Sprite.__init__(self)
    self.image, self.rect = image
    self.addr = addr
    self.pos  = pos
    self.life = 1
    self.dire = 'w'
  
  def move(self, map1):
    newPos = [self.pos[0],self.pos[1]]
    if   self.dire == 'w':
      newPos[1] += 1
    elif self.dire == 's':
      newPos[1] -= 1
    elif self.dire == 'd':
      newPos[0] += 1
    elif self.dire == 'a':
      newPos[0] -= 1
    if map1.isBlockPosition(newPos):
      map1.setPos(self.pos[0], self.pos[1], 0)
      map1.setPos(newPos[0], newPos[1], 2)
      self.pos = newPos

  def getPos(self):
    return self.pos

  def hit(self, value):
    self.life -= value

  def getDire(self):
    return self.dire

  def setDire(self, dire):
    self.dire = dire

  def getLife(self):
    return self.life
