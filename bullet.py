# 1 is Y and 0 is X; pos[x], pos[y] = pos[0], pos[1]

class Bullet:
  def getPos(self):
    return self.pos

  def move(self):
    if   self.dire == 'w':
      self.pos[1] += 1
    elif self.dire == 's':
      self.pos[1] -= 1
    elif self.dire == 'd':
      self.pos[0] += 1
    elif self.dire == 'a':
      self.pos[0] -= 1
  
  def __init__(self, dire, pos):
    self.dire = dire
    self.pos  = pos



