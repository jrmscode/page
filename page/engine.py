import pygame


class Engine:

    def __init__(self,
                 width=320,
                 height=180,
                 title="PAGE"):

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

        while self.running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()