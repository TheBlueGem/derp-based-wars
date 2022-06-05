from typing import Optional
from typing import Tuple
from typing import List

from board import Board
from tile import Tile
from tile_objects.units.unit import Unit


class RouteEntry:
    _x = None
    _y = None
    _tile = None

    def __init__(self, x, y, tile):
        self._x = x
        self._y = y
        self._tile = tile

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y: int):
        self._y = y

    @property
    def tile(self):
        return self._tile

    @tile.setter
    def tile(self, tile: Tile):
        self._tile = tile


class MovementGrid:
    def get_grid(self, source_location: Tuple[int, int], unit: Unit, board: Board):
        movement = unit.movement
        routes = self.calculate_routes(source_location, movement, board)

    def calculate_routes(self, source_location: Tuple[int, int], movement: int, board: Board):
        routes = [[]]
        surroundings = self.get_surroundings(source_location, board)
        for entry in surroundings:
            if not routes[entry.x][entry.y] and entry.tile:

                routes.append()
        pass

    def get_surroundings(self, source_location: Tuple[int, int], board: Board) -> List[RouteEntry]:

        return [
            RouteEntry(x=source_location[0] + 1,
                       y=source_location[1],
                       tile=board.get_tile(source_location[0] + 1, source_location[1])),
            RouteEntry(x=source_location[0] - 1,
                       y=source_location[1],
                       tile=board.get_tile(source_location[0] - 1, source_location[1])),
            RouteEntry(x=source_location[0],
                       y=source_location[1] + 1,
                       tile=board.get_tile(source_location[0], source_location[1] + 1)),
            RouteEntry(x=source_location[0],
                       y=source_location[1] - 1,
                       tile=board.get_tile(source_location[0], source_location[1] - 1))
        ]

        # if up_neighbour != previous_location:
        #     surroundings.append(up_neighbour)
        # if down_neighbour != previous_location:
        #     surroundings.append(down_neighbour)
        # if left_neighbour != previous_location:
        #     surroundings.append(left_neighbour)
        # if right_neighbour != previous_location:
        #     surroundings.append(right_neighbour)
        #
        # print("Surroundings: " + str(surroundings))
        # return surroundings
