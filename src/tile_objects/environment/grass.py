from pygame.surface import Surface

from common import GREEN
from tile_objects.base_tile_object import BaseTileObject


class Grass(BaseTileObject):

    def __init__(self):
        super().__init__()

    def draw(self, surface: Surface):
        surface.fill(GREEN)


