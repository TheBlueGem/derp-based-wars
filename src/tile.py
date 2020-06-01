import logging
from typing import Optional

from pygame import Surface
from pygame import draw as pygame_draw

from base_object import BaseObject
from common import RED
from common import TILE_SIZE
from tile_objects.base_tile_object import BaseTileObject
from tile_objects.units.unit import Unit

logger = logging.getLogger('Tile')
logger.setLevel(10)


class Tile(BaseObject):
    _surface = None
    _objects = list

    def __init__(self, objects, surface: Optional[Surface]):
        super().__init__()
        self._objects = objects
        self._surface = surface

    def __str__(self):
        return "Tile has these objects: %s" % str(self._objects)

    def draw(self):
        if self.surface is not None:
            if len(self._objects) is 0:
                pygame_draw.line(self.surface, RED, (0, 0),
                                 (TILE_SIZE, TILE_SIZE), 3)
                pygame_draw.line(self.surface, RED, (TILE_SIZE, 0),
                                 (0, TILE_SIZE), 3)
            else:
                for obj in self._objects:
                    if isinstance(obj, BaseTileObject):
                        obj.draw(surface=self._surface)
        else:
            logger.info("No surface set")

    @property
    def surface(self) -> Surface:
        return self._surface

    @surface.setter
    def surface(self, surface):
        self._surface = surface

    @property
    def objects(self) -> list:
        return self._objects

    @objects.setter
    def objects(self, objects):
        self._objects = objects

    def get_unit(self) -> Optional[Unit]:
        for obj in self._objects:
            if isinstance(obj, Unit):
                return obj
        return None

    def pop_unit(self) -> Optional[Unit]:
        for index in range(len(self._objects)):
            if isinstance(self._objects[index], Unit):
                return self._objects.pop(index)
        return None
