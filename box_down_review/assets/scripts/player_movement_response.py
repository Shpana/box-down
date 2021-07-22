import pygame

from typing import NoReturn

from assets.scripts.physics_constanst import GRAVITY_SCALE
from assets.scripts.core.event_dispatcher import EventDispatcher


class PlayerMovementResponse:

    def __init__(self,
            level_bounds: pygame.Rect,
            position: pygame.Vector2, scale: pygame.Vector2) -> NoReturn:

        self.__level_bounds = level_bounds

        self.__friction = 4
        self.__speed = 1250
        self.__jump_force = 400

        self.__scale = scale
        self.__position = position
        self.__velocity = pygame.Vector2()

    def on_update(self, dt: float) -> NoReturn:
        direction = self.__calculate_direction()

        self.__velocity.x -= self.__velocity.x * self.__friction * dt
        self.__velocity.y += GRAVITY_SCALE * dt
        self.__velocity += direction * self.__speed * dt
        self.__position += self.__velocity * dt

        self.__position.x = self.__clamp_value(self.__position.x, 0, self.__level_bounds.w - self.__scale.x)
        self.__position.y = self.__clamp_value(self.__position.y, 0, self.__level_bounds.h - self.__scale.y)

    def on_event(self, event: pygame.event.Event) -> NoReturn:
        dispatcher = EventDispatcher(event)
        dispatcher.dispatch_key(pygame.K_SPACE, self.__try_jump)

    def __try_jump(self, event: pygame.event.Event):
        if self.__can_jump():
            self.__velocity.y = -self.__jump_force

    def __can_jump(self) -> bool:
        return self.__position.y >= self.__level_bounds.h - self.__scale.y

    def __clamp_value(self, value: float, left_limit: float, right_limit: float) -> float:
        return max(min(value, right_limit), left_limit)

    def __calculate_direction(self) -> pygame.Vector2:
        keys = pygame.key.get_pressed()

        return pygame.Vector2(
            (keys[pygame.K_d] | keys[pygame.K_RIGHT]) - (keys[pygame.K_a] | keys[pygame.K_LEFT]), 0
        )
