from abc import ABC, abstractclassmethod

class MHandler(ABC):
  @abstractclassmethod
  def scheduler(self):
    pass

  @abstractclassmethod
  def events(self, event):
    pass

  @abstractclassmethod
  def updates(self):
    pass

  @abstractclassmethod
  def drawing(self):
    pass


# implementar la estructurar STACK para contener los estados del menu

class MenuHandler:
  def __init__(self, flag):
    self.stack_menu = []
    self.flags = None

    self.current_state = None

  def change(self, flag):
    pass

  def current(self):
    return current_state


