import pygame

from typing import NoReturn

from assets.scripts.box import Box
from assets.scripts.player import Player


class CollisionDetector:

    def __init__(self, player: Player, boxes: list[Box]) -> NoReturn:
        self.__boxes = boxes
        self.__player = player

        self.__collision_entered = list()

    def on_update(self) -> NoReturn:
        player_rect = self.__player.rect

        for box in self.__boxes:
            if box.rect.colliderect(player_rect) and not box in self.__collision_entered:
                self.__on_collision_enter(box)
            elif not box.rect.colliderect(player_rect) and box in self.__collision_entered:
                self.__on_collision_exit(box)

    def on_emergency_box_remove(self, box: Box) -> NoReturn:
        if box in self.__collision_entered:
            self.__collision_entered.pop(self.__collision_entered.index(box))

    def __on_collision_enter(self, box: Box) -> NoReturn:
        self.__collision_entered.append(box)
        self.__player.on_collision_enter(box)

    def __on_collision_exit(self, box: Box) -> NoReturn:
        self.__collision_entered.pop(self.__collision_entered.index(box))
