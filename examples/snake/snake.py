import pygame
from page.entity import Entity
from page.colors import Colors


class Snake(Entity):
    """ Represents the snake in the game. """

    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"

    def __init__(self, x, y):

        super().__init__(
            x,
            y,
            color=Colors.CYBER_CYAN,
        )

        self.cell_size = 32
        self.direction = None
        self.frames = 0
        self.length = 1
        self.positions = []


    def draw(self, screen, camera):
       for x, y in self.positions[-self.length:]:
            pygame.draw.rect(
                screen, self.color,
                (
                    x - camera.x,
                    y - camera.y,
                    self.width,
                    self.height
                )
            )    

    
    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.direction != self.RIGHT:
            self.direction = self.LEFT

        elif keys[pygame.K_RIGHT] and self.direction != self.LEFT:
            self.direction = self.RIGHT

        elif keys[pygame.K_UP] and self.direction != self.DOWN:
            self.direction = self.UP

        elif keys[pygame.K_DOWN] and self.direction != self.UP:
            self.direction = self.DOWN


    def move(self):
        if self.direction == self.LEFT:
            self.x -= self.cell_size
            print(f"Snake moved left to {self.x}, {self.y}")

        elif self.direction == self.RIGHT:
            self.x += self.cell_size
            print(f"Snake moved right to {self.x}, {self.y}")

        elif self.direction == self.UP:
            self.y -= self.cell_size
            print(f"Snake moved up to {self.x}, {self.y}")

        elif self.direction == self.DOWN:
            self.y += self.cell_size
            print(f"Snake moved down to {self.x}, {self.y}")

        self.positions.append((self.x, self.y))


    def update(self):
                
        self.handle_input()

        self.frames += 1

        if self.frames >= 15:
            self.frames = 0
            self.move()


    def on_collision(self, other):
        # change snake when it collides with food
        self.length += 1
        print("Snake updated length to", self.length)