class Product():
  def __init__(self,name, cost):
    self.__name = name
    self.__cost = cost
  def getName(self):
    return self.__name
  def setName(self, name):
    self.__name = name
  def getCost(self):
    return self.__cost
  def setCost(self, cost):
    self.__cost = cost
  def toString(self):
    return  "Product(" + str(self.__name) + "," + str(self.__cost) + ")"

