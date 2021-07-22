import pygame
import time

from core.screen import Screen

from assets.scripts.player import Player
from assets.scripts.player_renderer import PlayerRenderer
from assets.scripts.ui.player_health_ui_presenter import PlayerHealthUiPresenter

from assets.scripts.box import Box
from assets.scripts.box_renderer import BoxRenderer

from assets.scripts.game_score import Score
from assets.scripts.ui.game_score_ui_presenter import ScoreUiPresenter


class Application:

    def __init__(self):
        pygame.font.init()

        # Screen setup
        self.screen_width = 800
        self.screen_height = 600
        self.screen_color = (18, 19, 25)
        self.screen = Screen(self.screen_width, self.screen_height, self.screen_color)

        self.__world_bounds = pygame.Rect(0, 0, self.screen_width, self.screen_height)

        # Player setup
        self.__score = Score()
        self.__score_ui_presenter = ScoreUiPresenter(self.__score)

        self.player = Player(self.__world_bounds)
        self.__player_renderer = PlayerRenderer(self.player)
        self.__player_health_ui_renderer = PlayerHealthUiPresenter(self.player)

        # Box setup
        self.start_time = time.time()
        self.boxes = list()
        self.hard = 1
        self.flag = True

        # Game setup
        self.running = True
        self.__frame_rate = 60

        self.__clock = pygame.time.Clock()

    def render(self):
        for box in self.boxes:
            box_renderer = BoxRenderer(box)
            box_renderer.on_render(self.screen.screen)

        self.__player_renderer.on_render(self.screen.screen)
        self.__player_health_ui_renderer.on_present(self.screen.screen)

        self.__score_ui_presenter.on_present(self.screen.screen)

    def update(self):
        self.__clock.tick(self.__frame_rate)

        if self.player.health <= 0:
            self.hard = 1
            self.boxes = list()

        self.screen.update()
        self.spawn_boxes()

        for box in self.boxes:
            if box.position.y > 600:
                self.__score.change_value(1)
                self.boxes.pop(self.boxes.index(box))

            box.on_update(self.__clock.get_time() / 1000)

        self.player.on_update(self.boxes, self.__clock.get_time() / 1000)

    def run(self):
        while self.running:
            self.update()
            self.render()
            self.event_handler()

    def spawn_boxes(self):
        if self.flag:
            self.start_time = time.time()
            self.flag = False

        if self.start_time + 10 < time.time():
            self.hard += 1
            self.flag = True

        if len(self.boxes) < int(self.hard):
            self.boxes.append(Box(self.__world_bounds))

    def event_handler(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            self.player.on_event(event)


if __name__ == '__main__':
    app = Application()
    app.run()
