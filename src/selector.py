from abc import ABC
from typing import Optional

import pygame
from pygame.surface import Surface

from board import Board
from common import LIGHTISH_BLUE
from common import TILE_SIZE
from common import BLUE
from typing import Tuple

from tile import Tile
from tile_objects.environment.environment import Environment
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


def get_surroundings(location: Tuple[int, int], board: Board) -> [Tuple[int, int]]:
    surroundings = list()
    surroundings.append(board.get_tile(location[0], location[1] - 1))
    surroundings.append(board.get_tile(location[0] + 1, location[1]))
    surroundings.append(board.get_tile(location[0], location[1] + 1))
    surroundings.append(board.get_tile(location[0] - 1, location[1]))

    return surroundings


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
    _selected_movement_grid = list()
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
        return "Selector - selected tile: %d, %d" % self._location

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
    def selected_movement_grid(self) -> list:
        return self._selected_movement_grid

    @selected_movement_grid.setter
    def selected_movement_grid(self, selected_movement_grid):
        self._selected_movement_grid = selected_movement_grid

    def move(self, x: int, y: int) -> None:
        new_location = (self.location[0] + x, self.location[1] + y)
        if self._selected_movement == 0:
            self._location = new_location
        elif tuple_in_list(new_location, self._selected_movement_grid):
            self.update_selected_route(new_location)

        print(str(self))

    def toggle_select(self, unit: Optional[Unit], board: Board) -> None:
        if len(self._selected_route) is 0 and unit is not None:
            self._selected_route.append(self._location)
            self._selected_movement_grid = self.get_unit_movement_grid(unit, board)
            self._selected_movement = unit.movement
            print(self._selected_movement_grid)
            print("Selected")
        else:
            self._selected_route = []
            self._selected_movement_grid = []
            self._selected_movement = 0
            print("Deselected")

    def get_oldest_step_in_route_from_surroundings(self, surroundings: list) -> Optional[Tuple[int, int]]:
        current_lowest = 100
        lowest: Optional[Tuple[int, int]] = None
        for el in surroundings:
            if el in self._selected_route and self._selected_route.index(el) < current_lowest:
                current_lowest = self._selected_route.index(el)
                lowest = el
        return lowest

    def route_trimmable_to(self, new_location: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        surroundings = list()
        previous_selection = self._selected_route[len(self._selected_route) - 1]

        current = (new_location[0] + 1, new_location[1])
        if current != previous_selection and tuple_in_list(current, self._selected_route):
            surroundings.append(current)

        current = (new_location[0] - 1, new_location[1])
        if current != previous_selection and tuple_in_list(current, self._selected_route):
            surroundings.append(current)

        current = (new_location[0], new_location[1] + 1)
        if current != previous_selection and tuple_in_list(current, self._selected_route):
            surroundings.append(current)

        current = (new_location[0], new_location[1] - 1)
        if current != previous_selection and tuple_in_list(current, self._selected_route):
            surroundings.append(current)

        result_location = self.get_oldest_step_in_route_from_surroundings(surroundings)

        return result_location

    def update_selected_route(self, new_location: Tuple[int, int]) -> None:
        if new_location == self._selected_route[0]:
            print("Reset selection")
            self._selected_route = [new_location]
            self._location = new_location
            return

        trimmable_to = self.route_trimmable_to(new_location)
        if trimmable_to is not None:
            print("Trimming on prev selection")
            trimmed_selection = []
            for tile in self._selected_route:
                trimmed_selection.append(tile)
                if tile == trimmable_to:
                    trimmed_selection.append(new_location)
                    self._selected_route = trimmed_selection
                    self._location = new_location
                    return
        if len(self._selected_route) <= self._selected_movement:
            self._selected_route.append(new_location)
            self._location = new_location

    def get_selected_destination(self) -> Tuple[int, int]:
        return self._selected_route[len(self._selected_route) - 1]

    # def handle_x_selection(self, movement: int, y_delta: int, selected_movement: list):
    #     next_location = (self._location[0], self._location[1] + y_delta)
    #     selected_movement.append(next_location)
    #     for j in range(0, movement - abs(y_delta)):
    #         x_steps = j + 1
    #         x_location = (next_location[0] - x_steps, next_location[1])
    #         selected_movement.append(x_location)
    #         x_location = (next_location[0] + x_steps, next_location[1])
    #         selected_movement.append(x_location)

    def get_unit_movement_grid(self, unit: Unit, board: Board):
        movement = unit.movement
        selected_movement = list()
        for i in range(0, movement):
            surroundings: list = get_surroundings(self._location + movement, board)

            for tile in surroundings:
                if tile is not None:
                    envs = tile.get_envs()
                    if len(envs) > 0:
                        # TODO Netjes vakjes afgaan om paden te bepalen. Mind you dat het kortste pad altijd de waarheid is
                        selected_movement.append(envs[0].movement_cost())
            # self.handle_x_selection(movement, -i, selected_movement)
            # self.handle_x_selection(movement, i + 1, selected_movement)

        return selected_movement

    def draw_selection(self, surface: Surface) -> None:
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
        for tup in self._selected_movement_grid:
            selection_surf: Surface = Surface((TILE_SIZE, TILE_SIZE))
            selection_surf.fill(LIGHTISH_BLUE)
            selection_surf.set_alpha(100)
            surface.blit(selection_surf, (tup[0] * TILE_SIZE, tup[1] * TILE_SIZE))

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

            self.draw_selected_movement(surface)
            self.draw_selection(surface)
