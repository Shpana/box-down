import pygame

from typing import NoReturn

from core.events.event import Event

from .box import Box
from .player import Player


class CollisionDetector:

    @property
    def collision_entered(self) -> Event:
        return self.__collision_entered

    @property
    def collision_released(self) -> Event:
        return self.__collision_released

    def __init__(self, player: Player, boxes: list[Box]) -> NoReturn:
        self.__boxes = boxes
        self.__player = player
        self.__collision_entered_boxes = list()

        self.__collision_entered = Event()
        self.__collision_released = Event()

    def on_update(self) -> NoReturn:
        player_rect = self.__player.rect

        for box in self.__boxes:
            if box.rect.colliderect(player_rect) and not box in self.__collision_entered_boxes:
                self.__on_collision_enter(box)

            if box in self.__collision_entered_boxes and not box.rect.colliderect(player_rect):
                self.__on_collision_release(box)

    def on_emergency_box_remove(self, box: Box) -> NoReturn:
        if box in self.__collision_entered_boxes:
            self.__collision_released.invoke(box)
            self.__collision_entered_boxes.pop(self.__collision_entered_boxes.index(box))

    def __on_collision_enter(self, box: Box) -> NoReturn:
        self.__collision_entered.invoke(box)
        self.__collision_entered_boxes.append(box)

    def __on_collision_release(self, box: Box) -> NoReturn:
        self.__collision_released.invoke(box)
        self.__collision_entered_boxes.pop(self.__collision_entered_boxes.index(box))
