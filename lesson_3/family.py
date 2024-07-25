class Family():
  def __init__(self, humans : list):
    self.__humans = humans
  def append_human(self, human : object):
    self.__humans.append(human)
  def view_family(self):
    for element in self.__humans:
      print(element.get_info())