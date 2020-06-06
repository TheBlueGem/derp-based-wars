from typing import Optional
from typing import Tuple

from board import Board
from tile_objects.units.unit import Unit
from utils import tuple_in_list


def get_movement_grid(source_location: Tuple[int, int], unit: Unit, board: Board):
    movement = unit.movement
    routes = calculate_routes(source_location, movement, board)


def calculate_routes(self, source_location: Tuple[int, int], movement: int, board: Board,
                     previous_location: Optional[Tuple[int, int]]):
    surroundings = list()
    right_neighbour = (source_location[0] + 1, source_location[1])
    left_neighbour = (source_location[0] - 1, source_location[1])
    up_neighbour = (source_location[0], source_location[1] + 1)
    down_neighbour = (source_location[0], source_location[1] - 1)
    if up_neighbour != previous_location:
        surroundings.append(up_neighbour)
    if down_neighbour != previous_location:
        surroundings.append(down_neighbour)
    if left_neighbour != previous_location:
        surroundings.append(left_neighbour)
    if right_neighbour != previous_location:
        surroundings.append(right_neighbour)

    print("Surroundings: " + str(surroundings))
    return surroundings
