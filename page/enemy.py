import pygame
from page.entity import Entity


class Enemy(Entity):
    """ An enemy entity that moves towards the player. """

    def __init__(self, x, y):
        super().__init__(x, y, color=(255, 0, 0))


    def update(self):
        pass


    def on_collision(self, other):
        # change the color of the enemy to green when it collides with the player
        print("Enemy collided with", type(other).__name__)
        self.color = (0, 255, 0)