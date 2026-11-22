class Camera:
    """ A simple camera class that follows a target object. """

    def __init__(self):

        self.x = 0
        self.y = 0


    def follow(self, target):
        self.x = target.x - 160
        self.y = target.y - 90