import pygame


class Entity:
    """ A base class for all entities in the game. """

    def __init__(self, x, y, color=(255, 255, 255), width=32, height=32):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height


    def update(self):
        pass


    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color, self.rect
        )


    def on_collision(self, other):
        pass

    
    @property
    def rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )
    