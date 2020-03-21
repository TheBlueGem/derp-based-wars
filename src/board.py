from random import randint
from typing import List
from typing import Type
from typing import Union

from pygame import draw as pygame_draw

from common import GREEN
from common import SQUARE_BORDER_COLOR
from common import TILE_SIZE
from tile import Tile
from base_object import BaseObject
from typing import Tuple


class Board(BaseObject):
    width = None
    height = None
    tile_size = None
    background_color = None
    tiles = [[]]
    unit_positions = []

    def __init__(self, width: int, height: int):
        super().__init__()
        self.tiles = [[Tile for y in range(width)] for x in range(height)]
        self.width = width
        self.height = height

    # Created on the assumption that the board will know the state of itself and what's on it
    def draw(self, surface) -> None:
        for x in range(self.width):
            for y in range(self.height):
                color = GREEN
                min_x, min_y = self.get_left_top_tile_coords(x, y)
                tile = self.get_tile(x, y)
                pygame_draw.rect(surface, color, (min_x, min_y, TILE_SIZE, TILE_SIZE))
                pygame_draw.line(surface, SQUARE_BORDER_COLOR, (min_x, min_y), (min_x + TILE_SIZE, min_y))
                pygame_draw.line(surface, SQUARE_BORDER_COLOR, (min_x, min_y), (min_x, min_y + TILE_SIZE))

                # For drawing the outer borders of the board
                if (x + 1) == self.width:
                    pygame_draw.line(surface, SQUARE_BORDER_COLOR, (min_x + TILE_SIZE, min_y),
                                     (min_x + TILE_SIZE, min_y + TILE_SIZE))
                if (y + 1) == self.height:
                    pygame_draw.line(surface, SQUARE_BORDER_COLOR, (min_x, min_y + TILE_SIZE),
                                     (min_x + TILE_SIZE, min_y + TILE_SIZE))

    def initialize_unit_positions(self, units: []) -> None:
        for unit in units:
            random_tile = self.get_random_tile()
            random_tile.units.append(unit)

    # Set a tile on the board
    def set_tile(self, x, y, color) -> None:
        tile = Tile(color)
        self.tiles[x][y] = tile

    # Get the coordinates of the top left corner of a tile
    def get_left_top_tile_coords(self, tile_x, tile_y) -> Tuple[int, int]:
        min_x = tile_x * TILE_SIZE
        min_y = tile_y * TILE_SIZE
        return min_x, min_y

    # Get a tile from the board
    def get_tile(self, x, y) -> Union[Type[Tile], List[Type[Tile]], None]:
        if self.tiles[x][y]:
            return self.tiles[x][y]
        return None

    # Get a random tile from the board
    def get_random_tile(self) -> Tile:
        random_x = randint(0, self.width - 1)
        random_y = randint(0, self.height - 1)
        tile = self.tiles[random_y][random_x]

        return tile
