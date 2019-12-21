
import pygame
import random

from vector2 import Vector2

class Box:

    def __init__ (self, surface):
        self.surface            = surface
        self.mass               = random.randint(10, 50)
        self.w                  = self.mass * 2
        self.h                  = self.mass * 2
        self.gravity_scale      = 1
        self.velocity           = Vector2 ()
        self.position           = Vector2 (random.randint(0, 800 - self.w), -self.h)
        self.color              = (255, 150, 100)
        self.slow_mo_const      = 1
        self.active             = True
        self.image              = pygame.image.load('res/box.png')
        self.image              = pygame.transform.scale(self.image, (self.w, self.h))

    def render (self):
        self.surface.blit(self.image, (self.position.x, self.position.y))

    def update (self):

        self.gravity()
        # Y moving
        self.position.y += self.velocity.y * self.slow_mo_const

    def gravity (self):
        self.velocity.y += (self.gravity_scale * self.mass) / 100
