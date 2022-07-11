from abc import ABC
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

import pygame
from pygame.surface import Surface

from board import Board
from common import BLUE
from common import LIGHTISH_BLUE
from common import TILE_SIZE
from movement_grid import calculate_grid
from movement_grid import tuple_in_grid
from tile_objects.units.unit import Unit
from utils import tuple_in_list

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def calc_selection_direction(src_tile: Tuple[int, int], dest_tile: Tuple[int, int]) -> int:
    if src_tile[1] > dest_tile[1]:
        return UP
    if src_tile[0] < dest_tile[0]:
        return RIGHT
    if src_tile[1] < dest_tile[1]:
        return DOWN
    if src_tile[0] > dest_tile[0]:
        return LEFT


def draw_selection_arrow(surface: Surface, tile: Tuple[int, int], selection_direction: int) -> None:
    point_list = []

    tile_center_x = tile[0] * TILE_SIZE + (TILE_SIZE / 2)
    tile_center_y = tile[1] * TILE_SIZE + (TILE_SIZE / 2)

    if selection_direction == UP:
        point_list.append((tile_center_x - 5, tile_center_y + 10))
        point_list.append((tile_center_x + 5, tile_center_y + 10))
        point_list.append((tile_center_x, tile_center_y))
        pygame.draw.polygon(surface, BLUE, point_list)
    elif selection_direction == RIGHT:
        point_list.append((tile_center_x - 10, tile_center_y - 5))
        point_list.append((tile_center_x - 10, tile_center_y + 5))
        point_list.append((tile_center_x, tile_center_y))
        pygame.draw.polygon(surface, BLUE, point_list)
    elif selection_direction == DOWN:
        point_list.append((tile_center_x - 5, tile_center_y - 10))
        point_list.append((tile_center_x + 5, tile_center_y - 10))
        point_list.append((tile_center_x, tile_center_y))
        pygame.draw.polygon(surface, BLUE, point_list)
    elif selection_direction == LEFT:
        point_list.append((tile_center_x + 10, tile_center_y - 5))
        point_list.append((tile_center_x + 10, tile_center_y + 5))
        point_list.append((tile_center_x, tile_center_y))
        pygame.draw.polygon(surface, BLUE, point_list)


class Selector(ABC):
    _location = Tuple[int, int]
    _selected_route = list()
    _selected_movement_grid: Dict = dict()
    _selected_movement = 0
    _line_thiccness = 3

    def __init__(self, location):
        super().__init__()

        if location:
            self._location = location
        else:
            self._location = (0, 0)

        self._selected_route = []

        print(self)

    def __str__(self):
        return "Selector with selected tile: %d, %d" % self._location

    @property
    def location(self) -> Tuple[int, int]:
        return self._location

    @location.setter
    def location(self, location) -> None:
        self._location = location

    @property
    def selected_route(self) -> list:
        return self._selected_route

    @property
    def selected_movement(self) -> int:
        return self._selected_movement

    @selected_movement.setter
    def selected_movement(self, selected_movement):
        self._selected_movement = selected_movement

    @property
    def selected_movement_grid(self) -> dict:
        return self._selected_movement_grid

    @selected_movement_grid.setter
    def selected_movement_grid(self, selected_movement_grid):
        self._selected_movement_grid = selected_movement_grid

    def move(self, x: int, y: int) -> None:
        new_location = (self.location[0] + x, self.location[1] + y)
        if self._selected_movement == 0:
            self._location = new_location
        elif tuple_in_grid(new_location, self._selected_movement_grid):
            self.update_selected_route(new_location)

        print(str(self))

    def toggle_select(self, board: Board, unit: Optional[Unit]) -> None:
        if len(self._selected_route) is 0 and unit is not None:
            self._selected_route.append(self._location)
            self.selected_movement_grid = calculate_grid(self.location, unit.movement, board)
            self._selected_movement = unit.movement
            print("Selected")
        else:
            self._selected_route = []
            self._selected_movement_grid = {}
            self._selected_movement = 0
            print("Deselected")

    def is_last_in_selected_route(self, location: Tuple[int, int]):
        return location == self._selected_route[len(self._selected_route) - 1]

    def get_trim_locations(self, new_location: Tuple[int, int]) -> List[Tuple[int, int]]:
        if tuple_in_list(new_location, self._selected_route):
            return [new_location]
        west = (new_location[0] - 1, new_location[1])
        east = (new_location[0] + 1, new_location[1])
        north = (new_location[0], new_location[1] - 1)
        south = (new_location[0], new_location[1] + 1)
        trim_locations = []
        if tuple_in_list(west, self._selected_route) and not self.is_last_in_selected_route(west):
            trim_locations.append(west)
        elif tuple_in_list(east, self._selected_route) and not self.is_last_in_selected_route(east):
            trim_locations.append(east)
        if tuple_in_list(north, self._selected_route) and not self.is_last_in_selected_route(north):
            trim_locations.append(north)
        if tuple_in_list(south, self._selected_route) and not self.is_last_in_selected_route(south):
            trim_locations.append(south)
        return trim_locations

    def trim_selected_route(self, trim_locations: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        print("Trimming selected route")
        iterator = iter(self._selected_route)
        end_of_trim = next(iterator)
        trimmed_route = [end_of_trim]
        while end_of_trim not in trim_locations:
            end_of_trim = next(iterator)
            trimmed_route.append(end_of_trim)
        return trimmed_route

    def update_selected_route(self, new_location: Tuple[int, int]) -> None:
        trim_locations = self.get_trim_locations(new_location)
        if len(trim_locations) > 0:
            self._selected_route = self.trim_selected_route(trim_locations)
        self._selected_route.append(new_location)
        self._location = new_location

    def get_selected_destination(self) -> Tuple[int, int]:
        return self._selected_route[len(self._selected_route) - 1]

    def draw_selected_route(self, surface: Surface) -> None:
        if len(self._selected_route) > 1:
            iterator = iter(self._selected_route)
            selection_direction = None
            src_tile = next(iterator)
            dest_tile = next(iterator)

            while dest_tile is not None:
                next_tile = next(iterator, None)
                src_tuple = (src_tile[0] * TILE_SIZE + (TILE_SIZE / 2), src_tile[1] * TILE_SIZE + (TILE_SIZE / 2))
                dest_tuple = (dest_tile[0] * TILE_SIZE + (TILE_SIZE / 2), dest_tile[1] * TILE_SIZE + (TILE_SIZE / 2))
                selection_direction = calc_selection_direction(src_tile, dest_tile)

                if next_tile is None:
                    if selection_direction == UP:
                        dest_tuple = (
                            dest_tile[0] * TILE_SIZE + (TILE_SIZE / 2), dest_tile[1] * TILE_SIZE + (TILE_SIZE / 2) + 10)
                    elif selection_direction == RIGHT:
                        dest_tuple = (
                            dest_tile[0] * TILE_SIZE + (TILE_SIZE / 2) - 10, dest_tile[1] * TILE_SIZE + (TILE_SIZE / 2))
                    elif selection_direction == DOWN:
                        dest_tuple = (
                            dest_tile[0] * TILE_SIZE + (TILE_SIZE / 2), dest_tile[1] * TILE_SIZE + (TILE_SIZE / 2) - 10)
                    elif selection_direction == LEFT:
                        dest_tuple = (
                            dest_tile[0] * TILE_SIZE + (TILE_SIZE / 2) + 10, dest_tile[1] * TILE_SIZE + (TILE_SIZE / 2))

                pygame.draw.line(surface, BLUE, src_tuple, dest_tuple, self._line_thiccness)

                src_tile = dest_tile
                dest_tile = next_tile

            draw_selection_arrow(surface, src_tile, selection_direction)

    def draw_selected_movement(self, surface: Surface):
        selection_surf: Surface = Surface((TILE_SIZE, TILE_SIZE))
        selection_surf.fill(LIGHTISH_BLUE)
        selection_surf.set_alpha(100)
        for x in self._selected_movement_grid.keys():
            column = self._selected_movement_grid[x]
            if isinstance(column, Dict):
                for y in column.keys():
                    surface.blit(selection_surf, (x * TILE_SIZE, y * TILE_SIZE))

    def draw(self, surface: Surface) -> None:
        if self._location is not None:
            x = (self._location[0]) * TILE_SIZE
            y = (self._location[1]) * TILE_SIZE
            line_length = (TILE_SIZE / 4)

            # Top left
            pygame.draw.line(surface, BLUE, (x, y), (x + line_length, y), self._line_thiccness)
            pygame.draw.line(surface, BLUE, (x, y), (x, y + line_length), self._line_thiccness)
            # Top right
            pygame.draw.line(surface, BLUE, (x + TILE_SIZE, y), (x + TILE_SIZE, y + line_length), self._line_thiccness)
            pygame.draw.line(surface, BLUE, (x + TILE_SIZE, y), (x + TILE_SIZE - line_length, y), self._line_thiccness)
            # Bottom left
            pygame.draw.line(surface, BLUE, (x, y + TILE_SIZE), (x + line_length, y + TILE_SIZE), self._line_thiccness)
            pygame.draw.line(surface, BLUE, (x, y + TILE_SIZE), (x, y + TILE_SIZE - line_length), self._line_thiccness)
            # Bottom right
            pygame.draw.line(surface, BLUE, (x + TILE_SIZE, y + TILE_SIZE),
                             (x + TILE_SIZE - line_length, y + TILE_SIZE), self._line_thiccness)
            pygame.draw.line(surface, BLUE, (x + TILE_SIZE, y + TILE_SIZE),
                             (x + TILE_SIZE, y + TILE_SIZE - line_length), self._line_thiccness)

            # TODO: This will be a bug for units that have a situation in which they have 0 movement.
            if self._selected_movement > 0:
                self.draw_selected_movement(surface)
                self.draw_selected_route(surface)
