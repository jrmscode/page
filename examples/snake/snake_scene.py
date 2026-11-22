from page.scene import Scene
from .snake import Snake


class SnakeScene(Scene):
    """ Represents the game scene for the snake game. """

    WORLD_WIDTH = 640
    WORLD_HEIGHT = 640

    def __init__(self):
        super().__init__()

        self.snake = Snake(100, 100)
        self.entities.append(self.snake)
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