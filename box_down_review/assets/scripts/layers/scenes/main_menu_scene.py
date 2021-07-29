import pygame

from typing import NoReturn

from core.timestep import Timestep
from core.events.event import Event
from core.events.event_dispatcher import EventDispatcher

from assets.scripts.layers.scenes.iscene import IScene


class MainMenuScene(IScene):

    __color = pygame.Color(255, 255, 255)

    @property
    def on_scene_change(self) -> Event:
        return self.__on_scene_change

    def on_attach(self) -> NoReturn:
        self.__on_scene_change = Event()

        pygame.font.init()
        self.__font = pygame.font.SysFont('Consolas', 36)

    def on_event(self, event: pygame.event.Event) -> NoReturn:
        dispatcher = EventDispatcher(event)

        # NOTE: Если появятся какие-то сложные зависимости между сценами, то такое не прокатит
        dispatcher.dispatch_key_down(pygame.K_e, lambda _: self.__on_scene_change.invoke())

    def on_render(self, context: pygame.Surface) -> NoReturn:
        text_view = self.__font.render("Press 'E' to start game.", 1, self.__color)
        context.blit(text_view, text_view.get_rect(center=context.get_rect().center))
