import time
import pygame

from typing import NoReturn, Generator

from assets.scripts.box import Box


class BoxSpawner:

    @property
    def max_possible_box_count(self) -> int:
        return 100

    def __init__(self, boxes: list[Box], level_bounds: pygame.Rect) -> NoReturn:
        self.__difficulty = 0
        self.__difficulty_delta = 0.01
        self.__max_difficulty = 1
        self.__increse_difficulty_interval = 1

        self.__min_spawn_interval = 0.2
        self.__max_spawn_interval = 3.0

        self.__boxes = boxes
        self.__level_bounds = level_bounds

        self.__difficulty_increse_corutine = self.__increse_difficulty(
            self.__increse_difficulty_interval)
        self.__difficulty_increse_corutine.send(None)

        self.__spawn_corutine = self.__spawn_in(
            self.__lerp(self.__max_spawn_interval, self.__min_spawn_interval, self.__difficulty))
        self.__spawn_corutine.send(None)

    def on_update(self, dt: float) -> NoReturn:
        try:
            self.__difficulty_increse_corutine.send(dt)
        except StopIteration:
            self.__difficulty_increse_corutine = self.__increse_difficulty(
                self.__increse_difficulty_interval)
            self.__difficulty_increse_corutine.send(None)

        try:
            self.__spawn_corutine.send(dt)
        except StopIteration:
            self.__spawn_corutine = self.__spawn_in(
                self.__lerp(self.__max_spawn_interval, self.__min_spawn_interval, self.__difficulty))
            self.__spawn_corutine.send(None)

    def __lerp(self, from_: float, to: float, t: float) -> float:
        return from_ + t * (to - from_)

    def __spawn_in(self, interval: float) -> NoReturn:
        elapsed_time = 0.0

        dt = 0.0
        while elapsed_time < interval:
            elapsed_time += yield dt

        if len(self.__boxes) <= self.max_possible_box_count:
            self.__boxes.append(Box(self.__level_bounds))

    def __increse_difficulty(self, interval: float) -> NoReturn:
        elapsed_time = 0.0

        dt = 0.0
        while elapsed_time < interval:
            elapsed_time += yield dt

        self.__difficulty = min(self.__difficulty + self.__difficulty_delta, self.__max_difficulty)
