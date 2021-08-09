from typing import NoReturn


class Score:

    @property
    def value(self) -> float:
        return self.__value

    def __init__(self) -> NoReturn:
        self.__value: float = 0.0

    def change_value(self, delta: float) -> NoReturn:
        if delta < 0:
            raise ValueError(f"Delta must be positive number, but delta={delta}")
        self.__value += delta
