class Scene:
    """ A scene that contains a list of entities. """

    def __init__(self):
        self.entities = []


    def update(self):
        for entity in self.entities:
            entity.update()


    def draw(self, screen):
        for entity in self.entities:
            entity.draw(screen)
