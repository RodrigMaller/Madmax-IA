#!/bin/python
from game import GameServer
from random    import randint
import socket
from threading import Thread
from map1 import Map1
import time

def runServer(game):
  s    = socket.socket()         
  host = socket.gethostname() 
  port = 6666#randint(6666,8080)
  s.bind(('', port))   
  print "\n",port,"\n"
  s.listen(5)
  while True:
    c, addr = s.accept()     
    print 'Got connection from', addr
    game.createPlayer(addr[0]+'|'+str(addr[1]), c)     

gameThread = GameServer(1, Map1());
gameThread.start();
runServer(gameThread);
