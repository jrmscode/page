from page.scene import Scene
from page.player import Player
from page.enemy import Enemy


class GameScene(Scene):
    """ A scene that contains a player and an enemy. """

    def __init__(self):
        super().__init__()

        self.player = Player(100, 50)
        self.entities.append(self.player)
        
        self.enemy = Enemy(200, 50)
        self.entities.append(self.enemy)


    def update(self):
        super().update()


    def check_collisions(self):
        # check for collision between player and enemy
        if self.player.rect.colliderect(self.enemy.rect):
            self.player.on_collision(self.enemy)
            self.enemy.on_collision(self.player)


    def get_camera_target(self):
        return self.player