import pygame

from common import TILE_SIZE
from common import BLUE
from base_object import BaseObject
from typing import Optional
from typing import Tuple


class Selector(BaseObject):
    _selected = Optional[Tuple[int, int]]

    def __init__(self, selected):
        super().__init__()
        self._selected = selected

    def __str__(self):
        return "Selector with selected tile: %d, %d" % self._selected

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def select(self, selected):
        self._selected = selected

    def draw(self, surface):
        if self.selected is not None:
            x, y = self.selected
            line_length = (TILE_SIZE / 4)
            line_thiccness = 3
            pygame.draw.line(surface, BLUE, (x, y), (x + line_length, y), line_thiccness)
            pygame.draw.line(surface, BLUE, (x, y), (x, y + line_length), line_thiccness)
            pygame.draw.line(surface, BLUE, (x + TILE_SIZE, y), (x + TILE_SIZE, y + line_length), line_thiccness)
            pygame.draw.line(surface, BLUE, (x, y + TILE_SIZE), (x + line_length, y + TILE_SIZE), line_thiccness)
            pygame.draw.line(surface, BLUE, (x, y + TILE_SIZE), (x, y + TILE_SIZE - line_length), line_thiccness)
            pygame.draw.line(surface, BLUE, (x + TILE_SIZE, y), (x + TILE_SIZE - line_length, y), line_thiccness)
