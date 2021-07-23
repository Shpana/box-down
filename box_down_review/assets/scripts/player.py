import pygame

from typing import NoReturn

from assets.scripts.box import Box
from assets.scripts.player_movement_response import PlayerMovementResponse


class Player:

    @property
    def max_possible_health(self) -> int:
        return 10

    @property
    def health(self) -> int:
        return self.__health

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.__position, self.__scale)

    def __init__(self, level_bounds: pygame.Rect) -> NoReturn:
        self.__level_bounds = level_bounds

        self.__health = self.max_possible_health

        self.__scale = pygame.Vector2(20, 20)
        self.__position = pygame.Vector2(
            self.__level_bounds.w // 2 - self.__scale.x // 2, self.__level_bounds.h - self.__scale.y)

        self.__movement_response = PlayerMovementResponse(level_bounds, self.__position, self.__scale)

    def on_update(self, dt: float):
        self.__movement_response.on_update(dt)

    def on_event(self, event: pygame.event.Event) -> NoReturn:
        self.__movement_response.on_event(event)

    def on_collision_enter(self, other: Box) -> NoReturn:
        self.__apply_damage(1)

    def __apply_damage(self, damage: float) -> NoReturn:
        self.__health -= damage
