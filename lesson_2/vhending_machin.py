import abc

class VendingMachine(abc.ABC):
  @abc.abstractclassmethod
  def getProduct(self):
    pass