from page.entity import Entity

class SnakeHead(Entity):

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            color=(0,255,0)
        )