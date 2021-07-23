from typing import NoReturn


class TimeFreezer:

    @property
    def freeze(self) -> float:
        return self.__freeze

    def __init__(self) -> NoReturn:
        self.__freeze_speed = 15

        self.__min_freeze_multiplier = 0.01
        self.__max_freeze_multiplier = 1.0

        self.__is_freezing = False
        self.__freeze = self.__max_freeze_multiplier

    def start(self, _) -> NoReturn:
        self.__is_freezing = True

    def finish(self, _) -> NoReturn:
        self.__is_freezing = False

    def on_update(self, dt: float) -> NoReturn:
        limit = self.__calculate_limit()
        self.__freeze += (limit - self.__freeze) * self.__freeze_speed * dt

    def __calculate_limit(self) -> NoReturn:
        if self.__is_freezing:
            return self.__min_freeze_multiplier
        else:
            return self.__max_freeze_multiplier

    def __lerp(self, from_: float, to: float, t: float) -> float:
        return from_ + t * (to - from_)
