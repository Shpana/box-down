import pygame

from typing import NoReturn

from assets.scripts.player_movement_response import PlayerMovementResponse
from assets.scripts.player_collision_response import PlayerCollisionResponse


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
        self.__position = pygame.Vector2(390, 560)

        self.__movement_response = PlayerMovementResponse(level_bounds, self.__position, self.__scale)
        self.__collision_response = PlayerCollisionResponse()

    def on_update(self, other, dt: float):
        self.collide(other)

        self.__movement_response.on_update(dt)

    def on_event(self, event: pygame.event.Event) -> NoReturn:
        self.__movement_response.on_event(event)

    def collide(self, other):
        self.__collision_response.solve_collision(self.rect)
