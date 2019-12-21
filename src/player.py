
import pygame
import time
import sys

from vector2 import Vector2

class Player:

    def __init__ (self, surface):
        self.surface            = surface
        self.init()

    def init (self):
        self.w                  = 20
        self.h                  = 20
        self.color              = (150, 255, 150)
        self.position           = Vector2 (390, 560)

        # Phisics
        self.on_ground          = False
        self.mass               = 10
        self.jump_force         = 7
        self.gravity_scale      = 2
        self.acceleration       = 0.2
        self.deceleration       = 0.2
        self.velocity           = Vector2 ()
        self.direction          = Vector2 ()
        self.last_direction     = Vector2 ()
        self.last_control       = None

        self.max_speed          = 10
        self.min_speed          = 0
        self.rect               = pygame.Rect(self.position.x, self.position.y, self.w, self.h)
        self.slow_mo_const      = 0.5
        self.health             = 0
        self.flag_continue      = False

        self.restart_offset     = 1
        self.restart_time       = 0
        self.restart_flag       = False
        self.score              = 0
        self.hit_flag           = True

    def update (self, other):

        if self.health <= 0:
            if not self.restart_flag:
                self.restart_time = time.time()
                self.restart_flag = True
            if self.restart_time + self.restart_offset <= time.time():
                self.restart()

        self.controls()
        self.decelerate()
        self.accelerate()
        self.gravity()
        self.collide(other)


        if self.direction.x != 0:
            dir = self.direction.x
        else:
            dir = self.last_direction.x

        # X moving
        self.position.x += self.velocity.x * dir * self.slow_mo_const
        # Y moving
        self.position.y += self.velocity.y * self.slow_mo_const

        # Bounds
        if self.position.x + self.w > 800:
            self.velocity.x = 0
            self.position.x = 780
        if self.position.x < 0:
            self.velocity.x = 0
            self.position.x = 0
        if self.position.y + self.h > 600:
            self.velocity.y = 0
            self.position.y = 580
            self.on_ground = True

    def render (self):
        pygame.draw.rect(self.surface, self.color, (self.position.x, self.position.y, self.w, self.h))
        for i in range(self.health):
            pygame.draw.rect(self.surface, (255, 255, 255), (0, i * 30 + i * 3 + 5, 10, 30))

    def decelerate (self):
        if self.direction.x == 0:
            self.velocity.x -= self.deceleration

        self.velocity.x = max(self.min_speed, self.velocity.x)

    def accelerate (self):
        if self.direction.x != 0:
            self.last_direction.x = self.direction.x
            self.velocity.x += self.acceleration

        self.velocity.x = min(self.max_speed, self.velocity.x)

    def gravity (self):
        self.velocity.y += (self.gravity_scale * self.mass) / 100

    def jump (self):
        if self.on_ground:
            self.velocity.y -= self.jump_force
            self.on_ground = False

    def controls (self):

        keys = pygame.key.get_pressed()


        self.direction.x = 0
        if self.hit_flag:
            if keys[pygame.K_a]:
                if self.last_control == 'd':
                    self.velocity.x = 0
                self.last_control = 'a'
                self.direction.x = -1
            elif keys[pygame.K_d]:
                if self.last_control == 'a':
                    self.velocity.x = 0
                self.last_control = 'd'
                self.direction.x = 1

    def collide (self, other):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.w, self.h)
        flag = False
        for i in other:

            tmp_rect = pygame.Rect(i.position.x, i.position.y, i.w, i.h)
            if tmp_rect.colliderect(self.rect):
                flag = True
                if i.active:
                    self.health -= 1
                    i.active = False
                    self.hit_flag = False
            else:
                self.hit_flag = True

        if flag:
            self.slow_mo_const = 0.05
            hit_surface = pygame.Surface((800, 600))
            hit_surface.fill((255, 0, 0))
            hit_surface.set_alpha(120)
            self.surface.blit(hit_surface, (0, 0))
        else:
            self.slow_mo_const = 0.5

    def restart (self):
        self.slow_mo_const = 0

        while not self.flag_continue:
            self.surface.fill((18, 19, 25))

            pygame.font.init()
            f = pygame.font.SysFont('Consolas', 36)
            text = f.render('Press "E" to start.', 1, (255, 255, 255))
            place = text.get_rect(center = (400, 300))
            self.surface.blit(text, place)

            f = pygame.font.SysFont('Consolas', 36)
            text = f.render('Your SCORE:' + str(self.score), 1, (255, 255, 255))
            place = text.get_rect(center = (400, 350))
            self.surface.blit(text, place)

            pygame.display.update()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_e:
                        self.flag_continue = True

        self.init()
        self.health = 10
