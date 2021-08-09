import pygame

from typing import Protocol, NoReturn


class IUiPresenter(Protocol):

    def on_render(self, context: pygame.Surface) -> NoReturn:
        raise NotImplementedError()
