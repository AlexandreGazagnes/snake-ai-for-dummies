import os
import time
import random
import logging

import pygame

from src.conf import *


WIN = pygame.display.set_mode(
    [
        SCREEN_WIDTH * SCALING_FACTOR,
        SCREEN_HEIGHT * SCALING_FACTOR,
    ]
)

SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_window(WIN, SCREEN, apple, snake, colors=None):
    """color window and update"""

    # bg
    SCREEN.fill(BG_COLOR)

    # radar
    color = snake.radar_color_exited if snake.radar_exited else snake.radar_color_idle
    pygame.draw.rect(SCREEN, color, snake.radar)

    # apple
    pygame.draw.rect(SCREEN, apple.color, apple)

    # snake
    pygame.draw.rect(SCREEN, snake.color_head, snake)

    # if not color -> clolor random
    if not colors:
        colors = [snake.color_body for _ in snake.body]

    for body, color in zip(snake.body, colors):
        pygame.draw.rect(SCREEN, color, body)

    WIN.blit(pygame.transform.scale(SCREEN, WIN.get_rect().size), (0, 0))

    # update
    pygame.display.update()
