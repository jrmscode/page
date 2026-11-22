import pygame
from page.game import GameScene
from page.camera import Camera


class Engine:
    """ The main game engine that handles the game loop and rendering. """

    def __init__(self,
                 width=320,
                 height=180,
                 title="PAGE"):

        # pygame setup
        pygame.init()
        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode(
            (width, height)
        )

        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

        self.game_scene = GameScene()
        self.camera = Camera()


    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def start(self):

        # poll events and update the screen
        while self.running:

            # process input events
            self.process_input()

            # update and draw the scene
            self.game_scene.update()

            # update the camera to follow the player
            self.camera.follow(self.game_scene.player)
            print(
                f"Player: {self.game_scene.player.x}",
                f"Enemy: {self.game_scene.enemy.x}"
            )

            # clear the screen
            self.screen.fill((0, 0, 0))

            # draw the scene
            self.game_scene.draw(self.screen, self.camera)

            # update the display
            pygame.display.flip()

            # limit the frame rate to 60 frames per second
            self.clock.tick(60)

        pygame.quit()