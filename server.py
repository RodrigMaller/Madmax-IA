#!/bin/python
from game import GameServer
from random    import randint
import socket
from threading import Thread

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
