import pygame

from typing import NoReturn


class PlayerCollisionResponse:

    def solve_collision(self, player_rect: pygame.Rect) -> NoReturn:
        # flag = False
        # for i in other:
        #
        #     tmp_rect = pygame.Rect(i.position.x, i.position.y, i.w, i.h)
        #     if tmp_rect.colliderect(self.rect):
        #         flag = True
        #         if i.active:
        #             self.__health -= 1
        #             i.active = False
        #             self.hit_flag = False
        #     else:
        #         self.hit_flag = True
        #
        # if flag:
        #     self.slow_mo_const = 0.05
        #     hit_surface = pygame.Surface((800, 600))
        #     hit_surface.fill((255, 0, 0))
        #     hit_surface.set_alpha(120)
        #     self.surface.blit(hit_surface, (0, 0))
        # else:
        #     self.slow_mo_const = 0.5
        pass
