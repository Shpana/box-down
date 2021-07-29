import pygame

from abc import abstractproperty
from typing import NoReturn, Protocol

from core.timestep import Timestep
from core.events.event import Event


class IScene(Protocol):

    @abstractproperty
    def on_scene_change(self) -> Event:
        raise NotImplementedError()

    def on_attach(self) -> NoReturn:
        pass

    def on_detach(self) -> NoReturn:
        pass

    def on_event(self, event: pygame.event.Event) -> NoReturn:
        pass

    def on_update(self, ts: Timestep) -> NoReturn:
        pass

    def on_render(self, context: pygame.Surface) -> NoReturn:
        pass
