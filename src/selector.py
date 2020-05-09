from abc import ABC

import pygame
from pygame.surface import Surface

from common import TILE_SIZE
from common import BLUE
from typing import Tuple

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

    def move(self, x: int, y: int) -> None:
        self._location = (self._location[0] + x, self._location[1] + y)
        self.select()

    def toggle_select(self) -> None:
        if len(self._selected_route) is 0:
            self._selected_route.append(self._location)
            print("Selected")
        else:
            self._selected_route = []
            print("Deselected")

    def select(self) -> None:
        if len(self._selected_route) > 0:
            if self._location in self._selected_route:
                print("Trimming selection")
                trimmed_selection = []
                for tile in self._selected_route:
                    trimmed_selection.append(tile)
                    if tile == self._location:
                        self._selected_route = trimmed_selection
                        return
            else:
                self._selected_route.append(self._location)

    def get_selected_destination(self) -> Tuple[int, int]:
        return self._selected_route[len(self._selected_route) - 1]

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

            self.draw_selection(surface)
