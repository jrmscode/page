class Scene:
    """ A scene that contains a list of entities. """

    def __init__(self):
        self.entities = []


    def update(self):
        for entity in self.entities:
            entity.update()

        self.check_collisions()


    def draw(self, screen, camera):
        for entity in self.entities:
            entity.draw(screen, camera)


    def check_collisions(self):
        pass
