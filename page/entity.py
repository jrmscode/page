import pygame


class Entity:


    def __init__(self, x, y, width=32, height=32):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def update(self):
        pass


    def draw(self, screen):
        pass


    @property
    def rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )
    