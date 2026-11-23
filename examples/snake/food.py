from page.entity import Entity
from page.colors import Colors


class Food(Entity):
    """ Represents the food in the game. """

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            color=Colors.CYBER_PINK,
        )

        self.active = True


    def draw(self, screen, camera):
        if not self.active:
            return
            
        super().draw(screen, camera)


    def respawn(self, x, y):
        self.x = x
        self.y = y
        self.active = True


    def on_collision(self, other):
            # change food when it collides with snake
            self.active = False
            print("Food eaten!")