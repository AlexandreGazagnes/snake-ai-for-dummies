import os
import time
import random
import logging

import pygame

from src.conf import *


class Board(pygame.Rect):
    "board class"

    def __init__(self):
        """ """

        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.size = SCREEN_WIDTH, SCREEN_HEIGHT

        self.color = BG_COLOR

        pygame.Rect.__init__(self, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
