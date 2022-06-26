import os
import time
import random
import logging

from collections import deque
import pygame

from src.conf import *
from src.snake import Snake, FakeSnake


class Agent2:
    """Agent 2 fait des choix au hazsard mais essaye de ne pas sortir ni se manger soi meme en PLUS QUI peut voir dans un carré de x par x devant sa direction"""

    def __init__(self, name="Agent2", radar_square=3, random_rate=10):

        self.name = name
        self.radar_square = radar_square
        self.random_rate = random_rate
        self.booked_dirs = []


    def ????(self, snake, apple):
        """ig radar on find best way to fo to apple """


        if snake.radar_exited : 
            # compute dist to apple

            # compute list of actions to go to apple

            # add to booked_dirs

    def decide(self, snake):


        if snake.radar_exited : 
            pass

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
