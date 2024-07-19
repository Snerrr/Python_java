# Создать наследника реализованного класса ГорячийНапиток с дополнительным полем int температура.
# Создать класс ГорячихНапитковАвтомат реализующий интерфейс ТорговыйАвтомат и реализовать 
# перегруженный метод getProduct(int name, int volume, int temperature), выдающий продукт соответствующий 
# имени, объёму и температуре
# В main проинициализировать несколько ГорячихНапитков и ГорячихНапитковАвтомат и воспроизвести логику, 
# заложенную в программе
# Всё вышеуказанное создать согласно принципам ООП, пройденным на семинаре

import bottle_of_water

class Hot_water(bottle_of_water.BottleOfWater):
  def __init__(self, name, cost, volume, temperatura):
    super().__init__(name, cost, volume)
    self.__temperatura = temperatura
  def get_temperatura(self):
    return self.__temperatura
  def set_temperatura(self, temperatura):
    self.__temperatura = temperatura
  

