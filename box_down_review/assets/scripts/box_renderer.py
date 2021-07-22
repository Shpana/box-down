import pygame

from typing import NoReturn

from assets.scripts.box import Box
from assets.scripts.irenderer import IRenderer


class BoxRenderer(IRenderer):

    __image = pygame.image.load("assets/art/box.png")

    def __init__(self, handle: Box) -> NoReturn:
        self.__handle = handle
        self.__image = pygame.transform.scale(
            self.__image, (int(self.__handle.scale.x), int(self.__handle.scale.x))
        )

    def on_render(self, context: pygame.Surface) -> NoReturn:
        context.blit(self.__image, self.__handle.rect)
