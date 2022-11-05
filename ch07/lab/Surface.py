from Rectangle import Rectangle

class Surface:
  def __init__(self, filename, x, y, h, w):
    self.rect = Rectangle(x,y,h,w)
    self.image = str(filename)

  def getRect(self):
 #  ‘’’
	# returns the rectangle object
	# args: self
	# returns rectangle object from instance variable
	# ‘’’
    return self.rect