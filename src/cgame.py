import pygame

class CGame:
  def __init__(self):
    self.width = 640
    self.height = 480
    self.size = (self.width, self.height)
    self.running = False

    self.screen = None
    self.background = None

    self.scheduler()


  def scheduler(self):
    self.screen = pygame.display.set_mode(self.size)
    self.background = pygame.Surface(self.size).convert()
    self.background.fill((200, 200, 0))
    self.screen.blit(self.background, (0, 0))

    self.running = True

  def events(self, event):
    if event.type == pygame.QUIT:
      self.running = False

  def drawing(self):
    self.screen.blit(self.background, (0, 0))

  def run(self):
    while self.running:
      for event in pygame.event.get():
        self.events(event)

      self.drawing()

      pygame.display.flip()
