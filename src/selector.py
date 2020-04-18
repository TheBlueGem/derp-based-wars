import pygame

from common import TILE_SIZE
from common import BLUE
from base_object import BaseObject
from typing import Optional
from typing import Tuple


class Selector(BaseObject):
    _selected = Tuple[int, int]

    def __init__(self, selected):
        super().__init__()

        if selected:
            self._selected = selected
        else:
            self._selected = (0, 0)

        print(self)

    def __str__(self):
        return "Selector with selected tile: %d, %d" % self._selected

    def get_selected(self) -> Tuple[int, int]:
        return self._selected

    def select(self, selected) -> None:
        self._selected = selected

    def move(self, x, y) -> None:
        self._selected = (self._selected[0] + x, self._selected[1] + y)

    def draw(self, surface) -> None:
        if self._selected is not None:
            x = (self._selected[0]) * TILE_SIZE
            y = (self._selected[1]) * TILE_SIZE
            line_length = (TILE_SIZE / 4)
            line_thiccness = 3

            # Top left
            pygame.draw.line(surface, BLUE, (x, y), (x + line_length, y), line_thiccness)
            pygame.draw.line(surface, BLUE, (x, y), (x, y + line_length), line_thiccness)
            # Top right
            pygame.draw.line(surface, BLUE, (x + TILE_SIZE, y), (x + TILE_SIZE, y + line_length), line_thiccness)
            pygame.draw.line(surface, BLUE, (x + TILE_SIZE, y), (x + TILE_SIZE - line_length, y), line_thiccness)
            # Bottom left
            pygame.draw.line(surface, BLUE, (x, y + TILE_SIZE), (x + line_length, y + TILE_SIZE), line_thiccness)
            pygame.draw.line(surface, BLUE, (x, y + TILE_SIZE), (x, y + TILE_SIZE - line_length), line_thiccness)
            # Bottom right
            pygame.draw.line(surface, BLUE, (x + TILE_SIZE, y + TILE_SIZE),
                             (x + TILE_SIZE - line_length, y + TILE_SIZE), line_thiccness)
            pygame.draw.line(surface, BLUE, (x + TILE_SIZE, y + TILE_SIZE),
                             (x + TILE_SIZE, y + TILE_SIZE - line_length), line_thiccness)
