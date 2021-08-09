import pygame

from typing import NoReturn

from ..player import Player
from .ipresenter import IPresenter


class PlayerHealthPresenter(IPresenter):

    __bar_scale = pygame.Vector2(10, 20)

    __color = pygame.Color(200, 125, 125)

    def __init__(self, handle: Player) -> NoReturn:
        self.__handle = handle

    def on_present(self, context: pygame.Surface) -> NoReturn:
        for bar in range(self.__handle.health):
            pygame.draw.rect(
                context, self.__color, self.__calculate_bar_rect(bar), border_radius=3
            )

        for bar in range(self.__handle.max_possible_health - self.__handle.health, 0, -1):
            bar += self.__handle.health - 1
            pygame.draw.rect(
                context, self.__color, self.__calculate_bar_rect(bar), 1, border_radius=3
            )

    def __calculate_bar_rect(self, bar: int) -> pygame.Rect:
        return pygame.Rect(
            5, bar * self.__bar_scale.y + bar * 4 + 5, self.__bar_scale.x, self.__bar_scale.y
        )
