import pygame

# game
from cgame import CGame

def main():
  try:
    CGame().run()
  except Exception:
    print('Error')

if __name__ == '__main__':
  pygame.init()
  main()
  
