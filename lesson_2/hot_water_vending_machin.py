# Создать наследника реализованного класса ГорячийНапиток с дополнительным полем int температура.
# Создать класс ГорячихНапитковАвтомат реализующий интерфейс ТорговыйАвтомат и реализовать 
# перегруженный метод getProduct(int name, int temperatura, int temperature), выдающий продукт соответствующий 
# имени, объёму и температуре
# В main проинициализировать несколько ГорячихНапитков и ГорячихНапитковАвтомат и воспроизвести логику, 
# заложенную в программе
# Всё вышеуказанное создать согласно принципам ООП, пройденным на семинаре

import vhending_machin

class Hot_water_vending_machin(vhending_machin.VendingMachine):
  def __init__(self, products):
    self.__products = products
  def getProduct(self, name):
    for element in self.__products:
      if element.getName() == name:
        return element
  def getProduct(self, name, temperatura, volume):
    for element in self.__products:
      if element.getName() == name and element.get_temperatura() ==temperatura and element.getVolume() == volume:
        return element.getName()