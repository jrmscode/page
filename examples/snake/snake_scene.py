import random
from page.scene import Scene
from .snake import Snake
from .food import Food


class SnakeScene(Scene):
    """ Represents the game scene for the snake game. """

    WORLD_WIDTH = 640
    WORLD_HEIGHT = 640

    def __init__(self):
        super().__init__()

        self.snake = Snake(100, 100)
        self.entities.append(self.snake)
        self.food = Food(320, 320)
        self.entities.append(self.food)
        self.game_over = False


    def update(self):
        if self.game_over:
            return
        
        super().update()
        self.check_world_bounds()

    
    def get_camera_target(self):
        return self.snake


    def check_world_bounds(self):
        if (
            self.snake.x < 0 
            or self.snake.x >= self.WORLD_WIDTH 
            or self.snake.y < 0 
            or self.snake.y >= self.WORLD_HEIGHT
        ):
            self.game_over = True


    def check_collisions(self):
        # check for collision between snake and food
        if self.snake.rect.colliderect(self.food.rect):
            self.snake.on_collision(self.food)
            self.food.on_collision(self.snake)

            random_x = random.randint(0, self.WORLD_WIDTH // self.snake.cell_size - 1) * self.snake.cell_size
            random_y = random.randint(0, self.WORLD_HEIGHT // self.snake.cell_size - 1) * self.snake.cell_size
            self.food.respawn(random_x, random_y)