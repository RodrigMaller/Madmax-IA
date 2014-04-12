import random
import socket

def forestGump():
  s = socket.socket()                  
  s.connect(('', 6666))

  while True:
    print s.recv(2048)
    command = random.choice(['-','^','m','m']);
    if command == 'm':
      command = random.choice(['w','s','a','d'])
    s.send(command)
    print command
  
  s.close 
forestGump()
