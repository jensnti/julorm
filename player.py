import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
  def __init__(self, ACC, FRIC, WIDTH):
    super().__init__() 

    self.ACC = ACC
    self.FRIC = FRIC
    self.WIDTH = WIDTH
    self.jumping = False

    self.vec = pygame.math.Vector2  # 2 for two dimensional

    self.surf = pygame.Surface((30, 30))
    self.surf.fill((255,255,0))
    self.rect = self.surf.get_rect()

    self.pos = self.vec((10, 360))
    self.vel = self.vec(0,0)
    self.acc = self.vec(0,0)

  def move(self):
    self.acc = self.vec(0,0.5)
 
    pressed_keys = pygame.key.get_pressed()
            
    if pressed_keys[K_LEFT]:
        self.acc.x = -self.ACC
    if pressed_keys[K_RIGHT]:
        self.acc.x = self.ACC

    self.acc.x += self.vel.x * self.FRIC
    self.vel += self.acc
    self.pos += self.vel + 0.5 * self.acc

    if self.pos.x > self.WIDTH:
      self.pos.x = 0
    if self.pos.x < 0:
      self.pos.x = self.WIDTH
     
    self.rect.midbottom = self.pos

  def jump(self, platforms):
    hits = pygame.sprite.spritecollide(self, platforms, False)
    if hits and not self.jumping:
      self.jumping = True
      self.vel.y = -15

  def cancel_jump(self):
    if self.jumping:
      if self.vel.y < -3:
        self.vel.y = -3

  def update(self, platforms):
    hits = pygame.sprite.spritecollide(self ,platforms, False)
    if self.vel.y > 0:
      if hits:
        if self.pos.y < hits[0].rect.bottom:
          self.pos.y = hits[0].rect.top +1
          self.vel.y = 0
          self.jumping = False
