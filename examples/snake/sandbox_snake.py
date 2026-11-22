from .snake_scene import SnakeScene
from page.engine import Engine


engine = Engine()
engine.scene = SnakeScene()
engine.start()