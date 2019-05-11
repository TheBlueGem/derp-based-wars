import tile
import typing
import base_object
import common
import pygame

from common import TILESIZE, BLUE
from base_object import BaseObject
from typing import Optional, Tuple


class Selector(BaseObject):
    _selected = Optional[Tuple[int, int]]

    def __init__(self, selected):
        self._selected = selected

    def __str__(self):
        return "Selector with selected tile: %d, %d" % (self._selected)

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def select(self, selected):
        self._selected = selected

    def draw(self, surface):
        if(self.selected != None):
            x, y = self.selected
            pygame.draw.line(surface, BLUE,
                             (x, y), (x + TILESIZE, y))
            pygame.draw.line(surface, BLUE,
                             (x, y), (x, y + TILESIZE))
            pygame.draw.line(surface, BLUE, (x +
                                             TILESIZE, y), (x + TILESIZE, y + TILESIZE))
            pygame.draw.line(surface, BLUE, (x,
                                             y + TILESIZE), (x + TILESIZE, y + TILESIZE))
