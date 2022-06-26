import os
import time
import random
import logging

import pygame

from src.conf import *
from src.snake import Snake, FakeSnake


class Agent1:
    """Agent 0 fait des choix au hazsard mais essaye de ne pas sortir ni se manger soi meme"""

    def __init__(self, name="Agent1", random_rate=10):

        self.name = name
        self.random_rate = random_rate

    def decide(self, snake):

        valid_dirs = dict()

        # # print fake
        # fake = FakeSnake(snake)
        # print("fake before")
        # fake.pprint()

        # eval all choices
        for dir in "dlru":
            fake = FakeSnake(snake)
            fake.direction = dir
            fake.moove()
            valid_dirs[dir] = fake.is_alive()

        # print("FAKE PORBA")
        # print([f"{k} {v}" for k, v in valid_dirs.items()])

        possibles = [k for k, v in valid_dirs.items() if v]
        # print("Possible proba")
        # print(possibles)

        # si liste vide -> dead coup au hazard
        if not len(possibles):
            return random.choice("dlru")

        # choose random regarding random rate
        if not random.randint(0, self.random_rate):
            return random.choice(possibles)

        # if no random chek if direction is OK
        if snake.direction in possibles:
            return snake.direction

        # else force a change of direction
        return random.choice(possibles)
