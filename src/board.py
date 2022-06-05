import logging
from typing import Optional

from pygame import draw as pygame_draw
from pygame import Surface
from pygame.rect import Rect

from common import LIGHTISH_GRAY
from common import GRID_LINE_COLOR
from common import TILE_SIZE
from tile import Tile
from base_object import BaseObject

logger = logging.getLogger('Board')
logger.setLevel(10)


class Board(BaseObject):
    _width = None
    _height = None
    _background_color = LIGHTISH_GRAY
    _tiles = []
    _surface = None

    def __init__(self, width: int, height: int, surface: Surface):
        super().__init__()
        surface.fill(self._background_color)
        self._surface = surface
        self._tiles = [
            [Tile(units=[], environment=None, surface=surface.subsurface(Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))) for
             y in range(width)] for x in range(height)]
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def background_color(self) -> str:
        return self._background_color

    @property
    def tiles(self) -> [[Tile]]:
        return self._tiles

    # Set a tile on the board
    def set_tile(self, x: int, y: int, tile: Tile) -> None:
        tile.surface = self._surface.subsurface(Rect((x) * TILE_SIZE, (y) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        self._tiles[x][y] = tile

    # Get a tile from the board
    def get_tile(self, x: int, y: int) -> Optional[Tile]:
        if len(self._tiles) > x and len(self._tiles[x]) > y:
            return self._tiles[x][y]
        return None

    # Draws the grid of the board
    def draw_grid(self) -> None:
        for x in range(self._width):
            current_x_coords = x * TILE_SIZE
            pygame_draw.line(self._surface, GRID_LINE_COLOR, (current_x_coords, 0),
                             (current_x_coords, self._height * TILE_SIZE))
            # Outer x border
            if (x + 1) == self._width:
                pygame_draw.line(self._surface, GRID_LINE_COLOR, (self._width * TILE_SIZE, 0),
                                 (self._width * TILE_SIZE, self._height * TILE_SIZE))

        for y in range(self._height):
            current_y_coords = y * TILE_SIZE
            pygame_draw.line(self._surface, GRID_LINE_COLOR, (0, current_y_coords),
                             (self._width * TILE_SIZE, current_y_coords))

            # Outer y border
            if (y + 1) == self._height:
                pygame_draw.line(self._surface, GRID_LINE_COLOR, (0, self._height * TILE_SIZE),
                                 (self._width * TILE_SIZE, self._height * TILE_SIZE))

    # Created on the assumption that the board will know the state of itself and what's on it
    def draw(self) -> Surface:
        self._surface.fill(self._background_color)
        for x in range(self._width):
            for y in range(self._height):
                tile = self.get_tile(x, y)
                tile.draw()

        self.draw_grid()
        return self._surface
