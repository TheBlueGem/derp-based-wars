import logging
from typing import List
from typing import Optional

from pygame import Surface
from pygame import draw as pygame_draw

from base_object import BaseObject
from common import RED
from common import TILE_SIZE
from tile_objects.base_tile_object import BaseTileObject
from tile_objects.environment.environment import Environment
from tile_objects.units.unit import Unit

logger = logging.getLogger('Tile')
logger.setLevel(10)


class Tile(BaseObject):
    _surface = None
    _environment = None
    _units = list

    def __init__(self, units: List[Unit], environment: Optional[Environment], surface: Optional[Surface]):
        super().__init__()
        self._units = units
        self._environment = environment
        self._surface = surface

    def __str__(self):
        return "Tile has these units: %s" % str(self._units)

    def draw(self):
        if self.surface is not None:
            if self._environment:
                self._environment.draw(surface=self._surface)
            else:
                pygame_draw.line(self.surface, RED, (0, 0),
                                 (TILE_SIZE, TILE_SIZE), 3)
                pygame_draw.line(self.surface, RED, (TILE_SIZE, 0),
                                 (0, TILE_SIZE), 3)
            if len(self._units) > 0:
                for unit in self._units:
                    if isinstance(unit, BaseTileObject):
                        unit.draw(surface=self._surface)
        else:
            logger.info("No surface set")

    @property
    def surface(self) -> Surface:
        return self._surface

    @surface.setter
    def surface(self, surface: Surface):
        self._surface = surface

    @property
    def environment(self) -> Environment:
        return self._environment

    @environment.setter
    def environment(self, environment: Environment):
        self._environment = environment

    @property
    def units(self) -> list:
        return self._units

    @units.setter
    def units(self, units: List[Unit]):
        self._units = units

    def get_unit(self) -> Optional[Unit]:
        if len(self._units) > 0:
            return self._units[0]
        return None

    def pop_unit(self) -> Optional[Unit]:
        if len(self._units) > 0:
            return self._units.pop()
        logger.info("Tile has no units to pop")
        return None
