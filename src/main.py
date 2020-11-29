import pygame
from pygame.locals import *

def main():
  width, height = 640, 480
  screen_sz = (width, height)
  run_game = True
      
  
  screen = pygame.display.set_mode(screen_sz)
  pygame.display.set_caption('Mafia 2D')

  background = pygame.Surface(screen.get_size()).convert()
  background.fill((255, 255, 0))
  screen.blit(background, (0, 0))

  while run_game:
    for event in pygame.event.get():
      if event.type == QUIT:
        run_game = False
        break

    screen.blit(background, (0, 0))
    pygame.display.flip()

if __name__ == '__main__':
  pygame.init()
  main()
  
