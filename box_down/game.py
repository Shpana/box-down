
import pygame
import time

from screen     import Screen
from vector2    import Vector2
from player     import Player
from box        import Box

class Game:

    def __init__ (self):
        # Screen setup
        self.screen_width       = 800
        self.screen_height      = 600
        self.screen_color       = (18, 19, 25)
        self.screen             = Screen(self.screen_width, self.screen_height, self.screen_color)

        # Player setup
        self.player             = Player (self.screen.screen)
        self.slow_mo_const      = self.player.slow_mo_const

        # Box setup
        self.boxes              = list()
        self.hard               = 1
        self.start_time         = time.time()
        self.flag = True

        # Game setup
        self.running            = True
        self.frame_rate         = 60

    def render (self):
        for i in self.boxes:
            i.render()
        self.player.render()

    def update (self):
        self.slow_mo_const = self.player.slow_mo_const
        if self.player.health <= 0:
            self.boxes = list()
            self.hard = 1

        self.screen.update()
        self.spawn_boxes()
        for i in self.boxes:
            if i.position.y > 600:
                self.boxes.pop(self.boxes.index(i))
                self.player.score += 1
            i.update()
        self.player.update(self.boxes)

    def run (self):

        while self.running:

            self.update()
            self.render()
            self.event_handler()

            pygame.time.Clock().tick(self.frame_rate)

    def spawn_boxes (self):
        if self.flag:
            self.start_time = time.time()
            self.flag = False

        if self.start_time + 10 < time.time():
            self.hard += 1
            self.player.max_speed += 1
            self.player.acceleration += 0.1
            self.player.deceleration += 0.1
            self.flag = True

        if len(self.boxes) < int(self.hard):
            self.boxes.append(Box (self.screen.screen))

        for i in self.boxes:
            i.slow_mo_const = self.slow_mo_const

    def event_handler (self):
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                self.running = False

            elif e.type == pygame.KEYDOWN:

                if e.key == pygame.K_SPACE:
                    self.player.jump()

if __name__ == '__main__':
    g = Game()
    g.run()
