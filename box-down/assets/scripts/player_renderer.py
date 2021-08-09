import pygame

from typing import NoReturn

from .player import Player
from .irenderer import IRenderer


class PlayerRenderer(IRenderer):

    __color = pygame.Color(150, 255, 150)

    def __init__(self, handle: Player) -> NoReturn:
        self.__handle = handle

    def on_render(self, context: pygame.Surface) -> NoReturn:
        pygame.draw.rect(context, self.__color, self.__handle.rect)
