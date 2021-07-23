import pygame
import time

from typing import NoReturn

from core.timestep import Timestep
from core.layers.layer import Layer

from assets.scripts.player import Player
from assets.scripts.player_renderer import PlayerRenderer
from assets.scripts.ui.player_health_ui_presenter import PlayerHealthUiPresenter

from assets.scripts.box import Box
from assets.scripts.box_spawner import BoxSpawner
from assets.scripts.box_renderer import BoxRenderer
from assets.scripts.box_remove_provider import BoxRemoveProvider

from assets.scripts.game_score import Score
from assets.scripts.ui.game_score_ui_presenter import ScoreUiPresenter

from assets.scripts.collision_detector import CollisionDetector


class GameLayer(Layer):

    def on_attach(self) -> NoReturn:
        # TODO: Как то надо доводить до сюда размеры окна и
        #       устанавливать их, а то сейчас они захардкожены.
        self.__level_bounds = pygame.Rect(0, 0, 900, 600)

        self.__score = Score()
        self.__score_ui_presenter = ScoreUiPresenter(self.__score)

        self.__player = Player(self.__level_bounds)
        self.__player_renderer = PlayerRenderer(self.__player)
        self.__player_health_ui_renderer = PlayerHealthUiPresenter(self.__player)

        self.__boxes = list()
        self.__box_renderers = dict()

        self.__box_spawner = BoxSpawner(self.__boxes, self.__level_bounds)
        self.__box_remove_provider = BoxRemoveProvider(self.__boxes, self.__level_bounds)
        self.__box_remove_provider.removed.add_listener(lambda _: self.__score.change_value(1))

        self.__collision_detector = CollisionDetector(self.__player, self.__boxes)

        self.__box_remove_provider.emergency_removing.add_listener(self.__collision_detector.on_emergency_box_remove)

    def on_detach(self) -> NoReturn:
        self.__box_remove_provider.removed.remove_listener(lambda _: self.__score.change_value(1))

        self.__box_remove_provider.emergency_removing.remove_listener(self.__collision_detector.on_emergency_box_remove)

    def on_update(self, ts: Timestep) -> NoReturn:
        self.__collision_detector.on_update()

        self.__box_spawner.on_update()
        for box in self.__boxes:
            box.on_update(ts.delta_time_in_seconds)
        self.__box_remove_provider.on_update()

        self.__player.on_update(ts.delta_time_in_seconds)

    def on_render(self, context: pygame.Surface) -> NoReturn:
        # TODO: Кэширование ренедереров
        for box in self.__boxes:
            box_renderer = BoxRenderer(box)
            box_renderer.on_render(context)

        self.__player_renderer.on_render(context)

        self.__score_ui_presenter.on_present(context)
        self.__player_health_ui_renderer.on_present(context)

    def on_event(self, event: pygame.event.Event) -> NoReturn:
        self.__player.on_event(event)
