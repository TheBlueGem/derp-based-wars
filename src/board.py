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
    width = None
    height = None
    tile_size = None
    background_color = LIGHTISH_GRAY
    tiles = []
    unit_positions = []
    surface = None

    def __init__(self, width: int, height: int, surface: Surface):
        super().__init__()
        surface.fill(self.background_color)
        self.surface = surface
        self.tiles = [
            [Tile(objects=[], surface=surface.subsurface(Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))) for
             y in range(width)] for x in range(height)]
        self.width = width
        self.height = height

    # Set a tile on the board
    def set_tile(self, x: int, y: int, tile: Tile) -> None:
        tile.surface = self.surface.subsurface(Rect((x) * TILE_SIZE, (y) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        self.tiles[x][y] = tile

    # Get a tile from the board
    def get_tile(self, x: int, y: int) -> Optional[Tile]:
        if isinstance(self.tiles[x][y], Tile):
            return self.tiles[x][y]
        return None

    def get_all_tiles(self) -> [[Tile]]:
        return self.tiles

    # Draws the grid of the board
    def draw_grid(self) -> None:
        for x in range(self.width):
            current_x_coords = x * TILE_SIZE
            pygame_draw.line(self.surface, GRID_LINE_COLOR, (current_x_coords, 0),
                             (current_x_coords, self.height * TILE_SIZE))
            # Outer x border
            if (x + 1) == self.width:
                pygame_draw.line(self.surface, GRID_LINE_COLOR, (self.width * TILE_SIZE, 0),
                                 (self.width * TILE_SIZE, self.height * TILE_SIZE))

        for y in range(self.height):
            current_y_coords = y * TILE_SIZE
            pygame_draw.line(self.surface, GRID_LINE_COLOR, (0, current_y_coords),
                             (self.width * TILE_SIZE, current_y_coords))

            # Outer y border
            if (y + 1) == self.height:
                pygame_draw.line(self.surface, GRID_LINE_COLOR, (0, self.height * TILE_SIZE),
                                 (self.width * TILE_SIZE, self.height * TILE_SIZE))

    # Created on the assumption that the board will know the state of itself and what's on it
    def draw(self) -> Surface:
        self.surface.fill(self.background_color)
        for x in range(self.width):
            for y in range(self.height):
                tile = self.get_tile(x, y)
                tile.draw()

        self.draw_grid()
        return self.surface
