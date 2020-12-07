import pygame
from pygame.locals import *

from platform import platform
from player import Player
 
pygame.init()
 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

 
PT1 = platform(WIDTH, HEIGHT)
P1 = Player(ACC, FRIC, WIDTH)

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  P1.move()

  displaysurface.fill((0,0,0))

  for entity in all_sprites:
    displaysurface.blit(entity.surf, entity.rect)

  pygame.display.update()
  FramePerSec.tick(FPS)