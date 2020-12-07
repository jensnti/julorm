import pygame
from pygame.locals import *
import random

class platform(pygame.sprite.Sprite):
  def __init__(self, WIDTH, HEIGHT):
    super().__init__()
    self.surf = pygame.Surface((WIDTH, 20))
    self.surf.fill((255,0,0))
    self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10), random.randint(0, HEIGHT-30)))

  def move(self):
    pass