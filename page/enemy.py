import pygame
from page.entity import Entity


class Enemy(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)


    def draw(self, screen):

        pygame.draw.rect(
            screen, (255,0,0), self.rect
        )

    def update(self):
        pass