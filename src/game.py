import os
import time
import random
import logging

import pygame

from src.conf import *

from src.apple import Apple
from src.board import Board
from src.window import *
from src.snake import Snake

from agents.agent0 import Agent0
from agents.agent1 import Agent1


class Game:
    """ """

    def __init__(self, window, screen, mode):
        """ """

        self.window = window
        self.screen = screen
        self.board = Board()
        self.apple = Apple(self.board)
        self.snake = Snake(self.board)
        self.agent = Agent1(random_rate=4)

        # # just for debug
        # self.body_colors = [random.choice(list(COLOR.values())) for _ in self.snake.body]

        self.do_run = True
        self.fps = FPS
        # logging.warning("OK")

        self.mode = mode

        # # display
        # WIN = pygame.display.set_mode(WIN_SIZE)
        # pygame.display.set_caption(("First Game!"))

        # clock
        self.clock = pygame.time.Clock()

        # self.controls = {
        self.controls = {
            pygame.K_UP: "u",
            pygame.K_DOWN: "d",
            pygame.K_LEFT: "l",
            pygame.K_RIGHT: "r",
        }

    def run(self):
        """external run"""

        # main loop
        while self.do_run:

            # tick
            self.clock.tick(self.fps)

            # perform _run
            self._run()

    def _detect_quit(self):
        """if quit"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.do_run = False

    def _manage_direction(self):
        """maange new direction for the snake"""

        if self.mode in ["u", "d", "l", "r"]:
            self.snake.direction = self.mode

        if self.mode == "random":
            if random.randint(0, 10) == 3:
                dir = random.choice(["u", "d", "l", "r"])
                self.snake.direction = dir

        if "m" in self.mode:
            keys_pressed = pygame.key.get_pressed()
            for k, v in self.controls.items():
                if keys_pressed[k]:
                    self.snake.direction = v

        # if "m" in self.mode:
        #     for event in pygame.event.get():
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_UP:
        #                 print("up")
        #                 self.snake.direction = "u"
        #             if event.key == pygame.K_DOWN:
        #                 print("d")
        #                 self.snake.direction = "d"
        #             if event.key == pygame.K_LEFT:
        #                 self.snake.direction = "l"
        #             if event.key == pygame.K_RIGHT:
        #                 self.snake.direction = "r"

        if self.mode == "a":
            self.snake.direction = self.agent.decide(self.snake)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            print("pause")
            time.sleep(3)

    def _manage_alive(self):
        """if not alive do_run = False"""

        if not self.snake.is_alive():
            self.do_run = False

    def _manage_eat(self):
        """if eat new apple and rect +1 in the body"""

        if self.snake.colliderect(self.apple):
            self.apple = Apple(self.board)
            self.snake.grow()

    def _run(self):
        """internant run"""

        # event quit
        self._detect_quit()

        # manage direction
        self._manage_direction()

        # moove
        self.snake.moove()
        self.snake.pprint()

        # radar
        self.snake.apple_in_radar(self.apple)

        # manage eat
        self._manage_eat()

        # manage alive
        self._manage_alive()

        # window
        draw_window(self.window, self.screen, self.apple, self.snake)
