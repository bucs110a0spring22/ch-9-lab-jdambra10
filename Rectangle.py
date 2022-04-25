class Rectangle:
  def __init__(self, x, y, h, w):
    if x<0: 
      self.x = 0
    else:
      self.x = x
      
    if y<0: 
      self.y = 0
    else:
      self.y = y
      
    if h<0: 
      self.height = 0
    else:
      self.height = h

    if w<0: 
      self.width = 0
    else:
      self.width = w

    self.string = str("(X: " + str(self.x) + " Y: " + str(self.y) + ") Width: " + str(self.width) + " Height: " + str(self.height))

  def __str__(self):
    obj_string = str(self.string)
    return obj_string