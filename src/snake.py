import os
import time
import random
import logging

import pygame


from src.conf import *


class Snake(pygame.Rect):
    """ """

    def __init__(self, SCREEN, radar_square=5):
        """ """

        self.radar_square = radar_square

        self.radar_color_idle = (255, 255, 0)
        self.radar_color_exited = (150, 150, 0)

        self.radar_exited = False

        # SCREEN
        self.SCREEN = SCREEN

        # size
        self.width = SNAKE_WIDTH
        self.height = SNAKE_HEIGHT
        self.length = SNAKE_LENGTH * SNAKE_HEIGHT

        # attrs misc
        self.color_head = SNAKE_COLOR_HEAD
        self.color_body = SNAKE_COLOR_BODY
        self.health = SNAKE_HEALTH
        self.speed = SNAKE_SPEED

        # direction
        self._direction = "u"

        # postion
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2  # SCREEN_HEIGHT - 100

        # super
        pygame.Rect.__init__(self, self.x, self.y, self.width, self.height)

        # body
        self.body = [
            pygame.Rect(self.x + i + self.width, self.y, self.width, self.height)
            for i in range(0, self.length, self.width)
        ]

    @property
    def radar(self):
        """ """
        x = self.x
        y = self.y

        if self.direction == "u":
            y = self.y + 1 - self.radar_square
            x = self.x - (self.radar_square // 2)
        if self.direction == "d":
            y = self.y
            x = self.x - (self.radar_square // 2)

        if self.direction == "r":
            x = self.x
            y = self.y - (self.radar_square // 2)

        if self.direction == "l":
            x = self.x + 1 - self.radar_square
            y = self.y - (self.radar_square // 2)

        return pygame.Rect(
            x,
            y,
            self.radar_square,
            self.radar_square,
        )

    def apple_in_radar(self, apple):
        """ """

        if self.radar.colliderect(apple):
            logging.critical("apple en radar soi meme")
            self.radar_exited = True
            return True

        self.radar_exited = False
        return False

    def moove(self):
        """ """

        self._moove()

    def _update_body(self):
        """ """

        body = [pygame.Rect(self.x, self.y, self.width, self.height)]
        for rect in self.body[:-1]:
            body.append(rect)
        self.body = body

    @property
    def direction(self):
        """ """

        return self._direction

    @direction.setter
    def direction(self, new_direction):
        """empeche demis tour"""

        if self._direction == new_direction:
            # txt = f"no changes : {self._direction},  new : {new_direction}"
            # print(txt)
            pass

        elif (self._direction in ["u", "d"]) and (new_direction in ["l", "r"]):
            txt = f"direction changed  old : {self._direction},  new : {new_direction}"
            print(txt)
            self._direction = new_direction

        elif (self._direction in ["l", "r"]) and (new_direction in ["u", "d"]):
            txt = f"direction changed  old : {self._direction},  new : {new_direction}"
            print(txt)
            self._direction = new_direction

        else:
            txt = f"error dir change old : {self._direction } asked {new_direction}"
            print(txt)
            pass

    # def simulate(self, direction):
    #     """ """

    #     # simulate

    #     x = int(self.x)
    #     y = int(self.y)

    #     moove_factor = SNAKE_SPEED * self.width

    #     if direction == "u":
    #         y = self.y - moove_factor
    #     if direction == "d":
    #         y = self.y + moove_factor
    #     if direction == "r":
    #         x = self.x + moove_factor
    #     if direction == "l":
    #         x = self.x - moove_factor

    #     # eval screen
    #     if not (SCREEN_WIDTH > x > 1):
    #         # logging.critical(f"{self}")
    #         logging.critical(" attention il faut toutrner pour éviyer bord erreur")
    #         return False
    #     if not (SCREEN_HEIGHT > y > 1):
    #         logging.critical(" attention il faut toutrner pour éviyer bord erreur")
    #         return False
    #     return True

    def _moove(self):
        """ """

        # # change dir if needed
        # if direction:  # and direction in ["u", "d", "r", "l"]
        #     self._direction = direction

        self._update_body()

        moove_factor = SNAKE_SPEED * self.width

        if self._direction == "u":
            self.y -= moove_factor

        if self._direction == "d":
            self.y += moove_factor

        if self._direction == "r":
            self.x += moove_factor

        if self._direction == "l":
            self.x -= moove_factor

    def is_alive(self):
        """ """

        # collide
        for body in self.body:
            if self.colliderect(body):
                logging.critical("mangé soi meme")
                return False

        # SCREEN
        if self.x < 0 or self.x >= SCREEN_WIDTH:
            logging.critical(f"{self} - bord erreur")
            return False
        if self.y < 0 or self.y >= SCREEN_HEIGHT:
            logging.critical(f"{self} - bord erreur")
            return False

        return True

    def grow(self):
        """ """

        last_rect = self.body[-1]
        new_rect = pygame.Rect(
            last_rect.x + self.width, last_rect.y, self.width, self.height
        )
        self.body.append(new_rect)
        print(f"EAT : length  = {len(self.body)}")

    def pprint(self):

        dir = f"dir: {self._direction}"
        head = f"head: {self.x},{self.y}"
        body = "body: " + " ".join([f"{b.x},{b.y}" for b in self.body])
        print(dir + " " + head + " " + body)


class FakeSnake(Snake):
    """ """

    def __init__(self, snake):
        """ """

        Snake.__init__(self, snake.SCREEN)

        self.x = int(snake.x)
        self.y = int(snake.y)
        self.body = [i for i in snake.body]
        self._direction = str(snake.direction)

    def pprint(self):

        fake = "FAKE"
        dir = f"dir: {self._direction}"
        head = f"head: {self.x},{self.y}"
        body = "body: " + " ".join([f"{b.x},{b.y}" for b in self.body])
        print(fake + " " + dir + " " + head + " " + body)
