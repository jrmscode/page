import pygame
from page.entity import Entity


class Player(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)


    def draw(self, screen):

        pygame.draw.rect(
            screen, (255,255,255), self.rect
        )

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

    