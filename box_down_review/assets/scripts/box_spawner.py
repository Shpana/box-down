import time
import pygame

from typing import NoReturn

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

        self.__spawn_corutine = self.__spawn_in(
            self.__lerp(self.__max_spawn_interval, self.__min_spawn_interval, self.__difficulty))

    def on_update(self) -> NoReturn:
        try:
            next(self.__difficulty_increse_corutine)
        except StopIteration:
            self.__difficulty_increse_corutine = self.__increse_difficulty(
                self.__increse_difficulty_interval)

        try:
            next(self.__spawn_corutine)
        except StopIteration:
            self.__spawn_corutine = self.__spawn_in(
                self.__lerp(self.__max_spawn_interval, self.__min_spawn_interval, self.__difficulty))

    def __lerp(self, from_: float, to: float, t: float) -> float:
        return from_ + t * (to - from_)

    def __spawn_in(self, interval: float) -> NoReturn:
        start_point = time.time()

        while time.time() - start_point < interval:
            yield

        if len(self.__boxes) <= self.max_possible_box_count:
            self.__boxes.append(Box(self.__level_bounds))

    def __increse_difficulty(self, interval: float) -> NoReturn:
        start_point = time.time()

        while time.time() - start_point < interval:
            yield

        self.__difficulty = min(self.__difficulty + self.__difficulty_delta, self.__max_difficulty)
