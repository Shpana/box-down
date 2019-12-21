
import pygame

class Screen:

    def __init__ (self, width, height, color):
        self.w                  = width
        self.h                  = height
        self.color              = color

        self.screen             = self.create()

    def create (self):
        screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Box Down")
        return screen

    def update (self):
        pygame.display.update()
        self.screen.fill(self.color)
