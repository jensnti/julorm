import pygame
from pygame.locals import *
import sys
import random
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

def check(platform, groupies):
  if pygame.sprite.spritecollideany(platform,groupies):
    return True
  else:
    for entity in groupies:
      if entity == platform:
        continue
      if (abs(platform.rect.top - entity.rect.bottom) < 50) and (abs(platform.rect.bottom - entity.rect.top) < 50):
        return True
    C = False

def plat_gen():
  while len(platforms) < 6 :
    width = random.randrange(50,100)
    p  = platform(WIDTH, HEIGHT)
    C = True

    while C:
      p = platform(WIDTH, HEIGHT)
      p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(-50, 0))
      C = check(p, platforms)

    platforms.add(p)
    all_sprites.add(p)

#------------------------------------------

PT1 = platform(WIDTH, HEIGHT)
P1 = Player(ACC, FRIC, WIDTH)

PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255,0,0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

for x in range(random.randint(4,5)):
  C = True
  pl = platform(WIDTH, HEIGHT)
  while C:
    pl = platform(WIDTH, HEIGHT)
    C = check(pl, platforms)
  platforms.add(pl)
  all_sprites.add(pl)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:    
      if event.key == pygame.K_SPACE:
        P1.jump(platforms)
    if event.type == pygame.KEYUP:    
      if event.key == pygame.K_SPACE:
        P1.cancel_jump() 

  if P1.rect.top <= HEIGHT / 3:
    P1.pos.y += abs(P1.vel.y)
    for plat in platforms:
      plat.rect.y += abs(P1.vel.y)
      if plat.rect.top >= HEIGHT:
        plat.kill()

  plat_gen()
  displaysurface.fill((0,0,0))
  P1.update(platforms)
  

  for entity in all_sprites:
    displaysurface.blit(entity.surf, entity.rect)
    entity.move()

  pygame.display.update()
  FramePerSec.tick(FPS)