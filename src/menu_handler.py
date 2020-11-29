import pygame

# implementar la estructurar STACK para contener los estados del menu

class MenuHandler:
  def __init__(self):
    self.stack_menu = []
    self.current_state = None

  def goto(self, menu):
    self.current_state = menu

  def dispath(self):
    pass


class MLoading():
  def __init__(self, background):
    self.canvas = background
    self.val = 1

  def scheduler(self):
    self.canvas.fill((255, 0, 100))

  def events(self, event):
    pass

  def updates(self):
    self.val = self.val + 1
    if self.val == 255:
      self.val = 0
    self.canvas.fill((255, self.val, self.val))

    print('Hola')

  def drawing(self, screen):
    screen.blit(self.canvas, (0, 0))
