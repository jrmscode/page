import pygame
from page.entity import Entity


class Player(Entity):
    """ A player entity that can be controlled by the user. """

    def __init__(self, x, y):
        super().__init__(x, y, color=(255, 255, 255))


    def update(self):
        keys = pygame.key.get_pressed()
                
        if keys[pygame.K_LEFT]:
            self.x -= 2
        if keys[pygame.K_RIGHT]:
            self.x += 2
        if keys[pygame.K_UP]:
            self.y -= 2
        if keys[pygame.K_DOWN]:
            self.y += 2


    def on_collision(self, other):
        print("Player collided with", other)
