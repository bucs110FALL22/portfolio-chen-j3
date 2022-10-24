class Coins:
  def __init__(self):
    self.position = (10,5)
    self.color = gold

class Goombas:
  def __init__(self):
    self.is_large = False #Goombas are small
    self.number = 0 #starts off with no Goombas
    self.speed = 2
    self.touchingPlayer = False

class blocks:
  def __init__(self):
    self.blocks = 3 #keeps track of the number of blocks to break
    self.hit = False