import pygame
from menu_handler import MenuHandler, MLoading

class CGame:
  def __init__(self):
    self.width = 640
    self.height = 480
    self.size = (self.width, self.height)
    self.running = False

    self.screen = None
    self.background = None
    self.current_state : MLoading

    self.scheduler()


  def scheduler(self):
    self.screen = pygame.display.set_mode(self.size)
    self.background = pygame.Surface(self.size).convert()
    
    self.current_state = MLoading(self.background)
    self.current_state.scheduler()

    self.running = True

  def events(self, event):
    if event.type == pygame.QUIT:
      self.running = False

    self.current_state.events(event)

  def updates(self):
    self.current_state.updates()
    pass

  def drawing(self):
    self.current_state.drawing(self.screen)

  def run(self):
    while self.running:
      for event in pygame.event.get():
        self.events(event)

      self.updates()
      self.drawing()

      pygame.display.flip()
