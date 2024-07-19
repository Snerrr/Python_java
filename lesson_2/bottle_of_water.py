import product

class BottleOfWater(product.Product):
  def __init__(self, name, cost, volume):
    super().__init__(name, cost)
    self.__volume = volume
  def getVolume(self):
    return self.__volume
  def set_volum(self, volume):
    self.__volume = volume
  def equals(self,o):
    if self == o:
      return True
    else:
      return False
    
  