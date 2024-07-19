import vhending_machin
import bottle_of_water

class BottleOfWaterVendingMachine(vhending_machin.VendingMachine):
  def __init__(self, products):
    super().__init__()
    self.__products = products
  def getProduct(self, name):
    for element in self.__products:
      if element.getName() == name:
        return element
  def getProduct(self, name, volume):
    for element in self.__products:
      if element.getName() == name and element.getVolume ==volume:
        return element