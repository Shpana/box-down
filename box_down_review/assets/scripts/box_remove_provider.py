import pygame

from typing import NoReturn

from core.events.event import Event
from assets.scripts.box import Box


class BoxRemoveProvider:

    @property
    def removed(self) -> Event:
        return self.__removed

    @property
    def emergency_removing(self) -> Event:
        return self.__emergency_removing

    def __init__(self, boxes: list[Box], level_bounds: pygame.Rect) -> NoReturn:
        self.__boxes = boxes
        self.__level_bounds = level_bounds

        self.__removed = Event()
        self.__emergency_removing = Event()

    def on_update(self) -> NoReturn:
        for box in self.__boxes:
            if self.__should_remove_box(box):
                self.__remove_box(box)

    def __remove_box(self, box: Box) -> NoReturn:
        self.__emergency_removing.invoke(box)
        self.__boxes.pop(self.__boxes.index(box))
        self.__removed.invoke(box)

    def __should_remove_box(self, box: Box) -> bool:
        return box.position.y > self.__level_bounds.h + box.rect.h
