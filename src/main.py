import pygame

# game
from cgame import CGame

def main():
  try:
    CGame().run()
  except Exception as e:
    print(e)

if __name__ == '__main__':
  pygame.init()
  main()
  
