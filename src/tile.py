import logging

from pygame import Surface
from pygame import draw as pygame_draw

from base_object import BaseObject
from common import GREEN
from common import TILE_SIZE

logger = logging.getLogger('Tile')
logger.setLevel(10)


class Tile(BaseObject):
    surface = None
    units = []

    def __init__(self, surface: Surface, units=[]):
        super().__init__()
        self.surface = surface
        logger.info(self.surface)
        self.units = units

    # def __str(self):
    #     return "Tile with color: %s" % (self.color)

    def draw(self):
        logger.info(self.surface)
        pygame_draw.rect(self.surface, GREEN, (0, 0, TILE_SIZE, TILE_SIZE))

    def get_surface(self) -> Surface:
        return self.surface
