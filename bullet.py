# 1 is Y and 0 is X; pos[x], pos[y] = pos[0], pos[1]

class Bullet:
  
  def move(self, speed):
    if   self.dire == 'w':
      self.pos[1] += speed
    elif self.dire == 's':
      self.pos[1] -= speed
    elif self.dire == 'd':
      self.pos[0] += speed
    elif self.dire == 'a':
      self.pos[0] -= speed
  
  def __init__(self, dire, pos):
    self.dire = dire
    self.pos  = pos



