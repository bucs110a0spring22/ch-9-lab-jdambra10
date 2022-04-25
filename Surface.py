from Rectangle import Rectangle
class Surface:
  def __init__(self, filename, x, y, h, w):
    self.image = str(filename)
    self.x = x
    self.y = y
    self.height = h
    self.width = w

    self.rect = Rectangle(self.x,self.y,self.height,self.width)

  def getRect(self):
    r = self.rect
    return r
    
    