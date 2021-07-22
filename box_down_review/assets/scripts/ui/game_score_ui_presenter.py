import pygame

from typing import NoReturn

from assets.scripts.game_score import Score
from assets.scripts.ui.iui_presenter import IUiPresenter


class ScoreUiPresenter(IUiPresenter):

    __color = pygame.Color(255, 255, 255)


    def __init__(self, handle: Score) -> NoReturn:
        self.__handle = handle

        pygame.font.init()
        self.__font = pygame.font.SysFont('Consolas', 36)

    def on_present(self, context: pygame.Surface) -> NoReturn:
        score_view = self.__font.render(f"Your score: {self.__handle.value}", 1, self.__color)
        context.blit(score_view, score_view.get_rect(center=pygame.Vector2(context.get_rect().centerx, score_view.get_rect().h)))
