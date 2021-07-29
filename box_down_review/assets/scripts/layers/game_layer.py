import pygame
import time

from typing import NoReturn, Type

from core.timestep import Timestep
from core.layers.layer import Layer

from assets.scripts.layers.scenes.iscene import IScene
from assets.scripts.layers.scenes.level_scene import LevelScene
from assets.scripts.layers.scenes.main_menu_scene import MainMenuScene


class GameLayer(Layer):

    __available_scenes = (
        MainMenuScene,
        LevelScene,
    )

    def on_attach(self) -> NoReturn:
        self.__scene_pointer = 0

        self.__current_scene = None
        self.__load_scene(self.__available_scenes[self.__scene_pointer])

    def on_detach(self) -> NoReturn:
        self.__current_scene.on_detach()

    def on_update(self, ts: Timestep) -> NoReturn:
        self.__current_scene.on_update(ts)

    def on_render(self, context: pygame.Surface) -> NoReturn:
        self.__current_scene.on_render(context)

    def on_event(self, event: pygame.event.Event) -> NoReturn:
        self.__current_scene.on_event(event)

    def __on_scene_change(self) -> NoReturn:
        self.__scene_pointer += 1
        self.__scene_pointer %= len(self.__available_scenes)
        self.__load_scene(self.__available_scenes[self.__scene_pointer])

    def __load_scene(self, scene: Type[IScene]) -> NoReturn:
        if not self.__current_scene is None:
            self.__current_scene.on_detach()

        self.__current_scene = scene()
        self.__current_scene.on_attach()

        self.__current_scene.on_scene_change.add_listener(self.__on_scene_change)
