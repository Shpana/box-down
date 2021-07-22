import pygame

from typing import NoReturn, Callable


class EventDispatcher:

    def __init__(self, handle: pygame.event.Event) -> NoReturn:
        self.__handle = handle

    def dispatch(self, event_type: int, callback: Callable) -> NoReturn:
        if event_type == self.__handle.type:
            callback(self.__handle)

    def dispatch_key(self, key: int, callback: Callable) -> NoReturn:
        if self.__check_type(pygame.KEYDOWN) and self.__handle.key == key:
            callback(self.__handle)

    def dispatch_mouse_button(self, button: int, callback: Callable) -> NoReturn:
        if self.__check_type(pygame.MOUSEBUTTONDOWN) and self.__handle.button == button:
            callback(self.__handle)

    def __check_type(self, event_type: int) -> bool:
        return self.__handle.type == event_type
