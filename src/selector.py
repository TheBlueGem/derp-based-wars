import tile
import typing
import base_object
import common
import pygame

from common import TILESIZE, BLUE
from base_object import BaseObject
from tile import Tile
from typing import Optional


class Selector(BaseObject):
    _selected = Optional[Tile]

    def __init__(self, tile):
        self._selected = tile

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def select(self, tile):
        self._selected = tile

    def draw(self, surface):
        if(self.selected != None):
            min_x, min_y = self.selected
            pygame.draw.line(surface, BLUE,
                             (min_x, min_y), (min_x + TILESIZE, min_y))
            pygame.draw.line(surface, BLUE,
                             (min_x, min_y), (min_x, min_y + TILESIZE))
