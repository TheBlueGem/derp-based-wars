from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from board import Board
from tile import Tile
from tile_objects.units.unit import Unit


class RouteEntry:
    _x = None
    _y = None
    _tile = None
    _movement_left = None

    def __init__(self, x, y, tile, movement_left):
        self._x = x
        self._y = y
        self._tile = tile
        self._movement_left = movement_left

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

    @property
    def movement_left(self):
        return self._movement_left


def get_grid(source_location: Tuple[int, int], unit: Unit, board: Board):
    movement = unit.movement
    return calculate_grid(source_location, movement, board)


def calculate_grid(source_location: Tuple[int, int], movement: int, board: Board) -> Dict:
    grid = {
        source_location[0]: {
            source_location[1]: movement
        }
    }
    surroundings = get_surroundings(location=source_location, movement_left=movement, board=board)
    for entry in surroundings:
        movement_left = entry.movement_left - entry.tile.environment.movement_cost
        if movement_left >= 0 and not in_grid(entry, grid):
            entry_surroundings = get_surroundings(location=(entry.x, entry.y), movement_left=movement_left, board=board)
            for entry_surrounding in entry_surroundings:
                if entry_surrounding.tile.environment:
                    surroundings.append(entry_surrounding)
            if not grid.get(entry.x):
                grid[entry.x] = {
                    entry.y: movement_left
                }
            current_column = grid.get(entry.x)
            if not current_column.get(entry.y):
                current_column[entry.y] = movement_left
    return grid


def in_grid(entry: RouteEntry, grid: Dict):
    column: Optional[Dict] = grid.get(entry.x)
    if not column or not column.get(entry.y):
        return False
    return True


def get_surroundings(location: Tuple[int, int], movement_left: int, board: Board) -> List[RouteEntry]:
    entries = []
    if board.get_tile(location[0] + 1, location[1]):
        entries.append(RouteEntry(x=location[0] + 1,
                                  y=location[1],
                                  tile=board.get_tile(location[0] + 1, location[1]),
                                  movement_left=movement_left))
    if board.get_tile(location[0] - 1, location[1]):
        entries.append(RouteEntry(x=location[0] - 1,
                                  y=location[1],
                                  tile=board.get_tile(location[0] - 1, location[1]),
                                  movement_left=movement_left))
    if board.get_tile(location[0], location[1] + 1):
        entries.append(RouteEntry(x=location[0],
                                  y=location[1] + 1,
                                  tile=board.get_tile(location[0], location[1] + 1),
                                  movement_left=movement_left))
    if board.get_tile(location[0], location[1] - 1):
        entries.append(RouteEntry(x=location[0],
                                  y=location[1] - 1,
                                  tile=board.get_tile(location[0], location[1] - 1),
                                  movement_left=movement_left))
    return entries

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
