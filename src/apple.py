import os
import time
import random
import logging

import pygame


from src.conf import *


class Apple(pygame.Rect):
    """ """

    def __init__(self, board, snake=None):
        """ """

        self.width = APPLE_WIDTH
        self.height = APPLE_HEIGHT
        self.color = APPLE_COLOR
        self.lifetime = APPLE_LIFETIME

        x = random.randint(0 + 1, SCREEN_WIDTH - APPLE_WIDTH - 1)
        y = random.randint(0 + 1, SCREEN_HEIGHT - APPLE_HEIGHT - 1)

        pygame.Rect.__init__(self, x, y, APPLE_WIDTH, APPLE_HEIGHT)

        self.collide = True if (snake and self.colliderect(snake)) else False

    def older(self):
        """loose 1 lifetime"""

        self.lifetime -= 1
        return self.lifetime
