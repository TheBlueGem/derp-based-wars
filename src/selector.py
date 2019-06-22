import tile
import typing
import base_object
import common
import pygame

from pygame import Rect
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
            line_length = (TILESIZE / 4)
            line_thiccness = 3 
            pygame.draw.line(surface, BLUE,
                             (x, y), (x + line_length, y), line_thiccness)
            pygame.draw.line(surface, BLUE,
                             (x, y), (x, y + line_length), line_thiccness)
            pygame.draw.line(surface, BLUE, (x +
                                             TILESIZE, y), (x + TILESIZE, y + line_length), line_thiccness)
            pygame.draw.line(surface, BLUE, (x,
                                             y + TILESIZE), (x + line_length, y + TILESIZE), line_thiccness)
            pygame.draw.line(surface, BLUE, (x,
                                             y + TILESIZE), (x, y + TILESIZE - line_length), line_thiccness)
            pygame.draw.line(surface, BLUE, (x +
                                             TILESIZE, y), (x + TILESIZE - line_length, y), line_thiccness)