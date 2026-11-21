import pygame
from page.player import Player
from page.enemy import Enemy


class Engine:

    def __init__(self,
                 width=320,
                 height=180,
                 title="PAGE"):

        # initialize the game engine and create a player entity
        self.entities = []
        self.player = Player(100, 50)
        self.enemy = Enemy(200, 50)
        self.entities.append(self.player)
        self.entities.append(self.enemy)

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

    def start(self):

        # poll events and update the screen
        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color (black in this case)
            self.screen.fill((0, 0, 0))

            # update and draw all entities
            for entity in self.entities:
                entity.update()
                entity.draw(self.screen)

            # check for collision between player and enemy
            if self.player.rect.colliderect(self.enemy.rect):
                print("Collision detected!")

            # update the display
            pygame.display.flip()

            # limit the frame rate to 60 frames per second
            self.clock.tick(60)

        pygame.quit()