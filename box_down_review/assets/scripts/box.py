import pygame
import random

from typing import NoReturn

from assets.scripts.physics_constanst import GRAVITY_SCALE


class Box:

    @property
    def scale(self) -> pygame.Vector2:
        return self.__scale

    # TODO: Убрать это свойство
    @property
    def position(self) -> pygame.Vector2:
        return self.__position

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.__position, self.__scale)

    def __init__(self, level_bounds: pygame.Rect) -> NoReturn:
        self.__level_bounds = level_bounds

        self.__scale = self.__generate_random_scale()
        self.__velocity = pygame.Vector2()
        self.__position = self.__generate_random_position()

    def on_update(self, dt: float) -> NoReturn:
        self.__velocity.y += GRAVITY_SCALE * dt
        self.__position += self.__velocity * dt

    def __generate_random_scale(self) -> pygame.Vector2:
        scale = random.randint(10, 100)
        return pygame.Vector2(scale, scale)

    def __generate_random_position(self) -> pygame.Vector2:
        return pygame.Vector2(
            random.randint(0, self.__level_bounds.w - self.__scale.x), -self.__scale.y
        )
