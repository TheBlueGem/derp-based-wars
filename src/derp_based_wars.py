import logging
import sys

from pygame import display
from pygame import event as pygame_event
from pygame import init
from pygame import quit as pygame_quit
from pygame import time
from pygame.locals import KEYDOWN
from pygame.locals import KEYUP
from pygame.locals import K_ESCAPE
from pygame.locals import QUIT
from pygame.rect import Rect
from pygame.surface import Surface

from board import Board
from common import BACKGROUND_COLOR
from common import TILE_SIZE
from common import WINDOW_HEIGHT
from common import WINDOW_WIDTH
from movement_grid import calculate_grid
from options import FPS
from options import SELECTOR_DOWN
from options import SELECTOR_LEFT
from options import SELECTOR_RIGHT
from options import SELECTOR_SELECT
from options import SELECTOR_UP
from selector import Selector
from tile import Tile
from tile_objects.environment.forest import forest
from tile_objects.environment.grass import grass
from tile_objects.environment.mountain import mountain
from tile_objects.units.spear import spear

board_width = 10
board_height = 10

logger = logging.getLogger("Main")
logger.setLevel(10)


# Main game loop
def main():
    init()
    fps_clock = time.Clock()
    display_surf: Surface = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    display.set_caption('Derp Based Wars')
    display_surf.fill(BACKGROUND_COLOR)

    main_board = Board(width=board_width, height=board_height, surface=display_surf.copy().subsurface(
        Rect(0, 0, board_width * TILE_SIZE + 1, board_height * TILE_SIZE + 1)))

    for x in range(main_board.width):
        for y in range(main_board.height - 1):
            if y == 3 and x == 2:
                main_board.set_tile(x, y, Tile(units=[], environment=mountain(), surface=None))
            elif y % 2 and x % 2:
                main_board.set_tile(x, y, Tile(units=[], environment=forest(), surface=None))
            elif y % 3 and x % 3 and (x is not 2 and y is not 2):
                main_board.set_tile(x, y, Tile(units=[], environment=mountain(), surface=None))
            else:
                main_board.set_tile(x, y, Tile(units=[], environment=grass(), surface=None))

    tile = main_board.get_tile(3, 3)
    tile.units.append(spear())
    main_board.set_tile(3, 3, tile)

    main_board.draw()
    selector = Selector((4, 4))

    while True:
        for event in pygame_event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame_quit()
                sys.exit()

            if event.type == KEYDOWN:
                handle_keydown_event(event.key, selector, main_board)

        # Main drawing loop
        display_surf.fill(BACKGROUND_COLOR)
        new_surf = main_board.draw()
        selector.draw(new_surf)
        display_surf.blit(new_surf, (0, 0))
        display.update()

        fps_clock.tick(FPS)


def handle_keydown_event(event_key, selector: Selector, board: Board):
    if event_key == SELECTOR_LEFT and selector.location[0] is not 0:
        selector.move(-1, 0)
    if event_key == SELECTOR_RIGHT and selector.location[0] is not board_width - 1:
        selector.move(1, 0)
    if event_key == SELECTOR_UP and selector.location[1] is not 0:
        selector.move(0, -1)
    if event_key == SELECTOR_DOWN and selector.location[1] is not board_height - 1:
        selector.move(0, 1)
    if event_key == SELECTOR_SELECT:
        if len(selector.selected_route) > 0:
            route_start = selector.selected_route[0]
            route_destination = selector.get_selected_destination()
            start_tile = board.get_tile(route_start[0], route_start[1])
            unit = start_tile.pop_unit()
            destination_tile = board.get_tile(route_destination[0], route_destination[1])
            destination_tile.units.append(unit)
            selector.toggle_select(board, None)
        else:
            unit = board.get_tile(selector.location[0], selector.location[1]).get_unit()
            if unit is not None:
                selector.toggle_select(board, unit)


if __name__ == '__main__':
    main()
