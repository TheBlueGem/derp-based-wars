import logging
from random import randint
from typing import Optional

from pygame import draw as pygame_draw
from pygame import Surface
from pygame.rect import Rect

from common import GREEN
from common import SQUARE_BORDER_COLOR
from common import TILE_SIZE
from tile import Tile
from base_object import BaseObject

logger = logging.getLogger('Board')
logger.setLevel(10)


class Board(BaseObject):
    width = None
    height = None
    tile_size = None
    background_color = GREEN
    tiles = []
    unit_positions = []
    surface = None

    def __init__(self, width: int, height: int, surface: Surface):
        super().__init__()
        self.surface = surface
        self.tiles = [[Tile(surface=surface) for y in range(width)] for x in range(height)]
        self.width = width
        self.height = height

    def initialize_unit_positions(self, units: []) -> None:
        for unit in units:
            random_tile = self.get_random_tile()
            random_tile.units.append(unit)

    # Set a tile on the board
    def set_tile(self, x, y, surface: Surface) -> None:
        tile = Tile(surface=surface.subsurface(Rect=Rect(x, y, TILE_SIZE, TILE_SIZE)))
        self.tiles[x][y] = tile

    # # Get the coordinates of the top left corner of a tile
    # def get_left_top_tile_coords(self, tile_x, tile_y) -> Tuple[int, int]:
    #     min_x = tile_x * TILE_SIZE
    #     min_y = tile_y * TILE_SIZE
    #     return min_x, min_y

    # Get a tile from the board
    def get_tile(self, x, y) -> Optional[Tile]:
        if isinstance(self.tiles[x][y], Tile):
            return self.tiles[x][y]
        return None

    # Get a random tile from the board
    def get_random_tile(self) -> Tile:
        random_x = randint(0, self.width - 1)
        random_y = randint(0, self.height - 1)
        tile = self.get_tile(random_y, random_x)

        return tile

    # Draws the grid of the board
    def draw_grid(self) -> None:
        for x in range(self.width):
            current_x_coords = x * TILE_SIZE
            pygame_draw.line(self.surface, SQUARE_BORDER_COLOR, (current_x_coords, 0),
                             (current_x_coords, self.height * TILE_SIZE))
            # Outer x border
            if (x + 1) == self.width:
                pygame_draw.line(self.surface, SQUARE_BORDER_COLOR, (self.width * TILE_SIZE, 0),
                                 (self.width * TILE_SIZE, self.height * TILE_SIZE))

        for y in range(self.height):
            current_y_coords = y * TILE_SIZE
            pygame_draw.line(self.surface, SQUARE_BORDER_COLOR, (0, current_y_coords),
                             (self.width * TILE_SIZE, current_y_coords))

            # Outer y boder
            if (y + 1) == self.height:
                pygame_draw.line(self.surface, SQUARE_BORDER_COLOR, (0, self.height * TILE_SIZE),
                                 (self.width * TILE_SIZE, self.height * TILE_SIZE))

    # Created on the assumption that the board will know the state of itself and what's on it
    def draw(self) -> Surface:
        self.surface.fill(self.background_color)
        for x in range(self.width):
            for y in range(self.height):
                tile = self.get_tile(x, y)
                tile.draw()
                # current_x_coords = x * TILE_SIZE
                # current_y_coords = y * TILE_SIZE
                # surface.blit(, (current_x_coords, current_y_coords))

        self.draw_grid()
        return self.surface

