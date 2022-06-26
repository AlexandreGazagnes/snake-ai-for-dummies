import os
import time
import random
import logging

import pygame

from src.conf import *


class Agent0:
    """Agent 0 fait des choix au hazsard"""

    def __init__(self, name="Agent0", random_rate=1000):

        self.name = name
        self.random_rate = random_rate

    def decide(self, snake):

        if not random.randint(0, self.random_rate):
            return random.choice(["u", "d", "l", "r"])
        else:
            return snake.direction
