import logging
import sys
import typing

from pygame import quit as pygame_quit
from pygame import display
from pygame import init
from pygame.locals import QUIT, KEYUP, K_ESCAPE, KEYDOWN
from pygame import time
from pygame import event as pygame_event
from pygame.rect import Rect
from pygame.surface import Surface

from board import Board
from common import TILE_SIZE
from options import FPS, SELECTOR_DOWN, SELECTOR_LEFT, SELECTOR_RIGHT, SELECTOR_UP
from common import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR
from selector import Selector
from tile import Tile
from tile_objects.environment.grass import Grass
from tile_objects.units.spear import spear

board_width = 10
board_height = 10

logging.getLogger()


# Main game loop
def main():
    init()
    fps_clock = time.Clock()
    display_surf = typing.cast(Surface, display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)))
    display.set_caption('Derp Based Wars')
    display_surf.fill(BACKGROUND_COLOR)

    main_board = Board(width=board_width, height=board_height, surface=display_surf.copy().subsurface(
        Rect(0, 0, board_width * TILE_SIZE + 1, board_height * TILE_SIZE + 1)))

    for x in range(main_board.width):
        for y in range(main_board.height - 1):
            main_board.set_tile(x, y, Tile(objects=[Grass()], surface=None))

    tile = main_board.get_tile(3, 3)
    tile.objects.append(spear())
    main_board.set_tile(3, 3, tile)

    main_board.draw()
    selector = Selector((4, 4))

    while True:
        for event in pygame_event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame_quit()
                sys.exit()

            if event.type == KEYDOWN:
                handle_keydown_event(event.key, selector)

        # Main drawing loop
        display_surf.fill(BACKGROUND_COLOR)
        new_surf = main_board.draw()
        selector.draw(new_surf)
        display_surf.blit(new_surf, (0, 0))
        display.update()
        
        fps_clock.tick(FPS)


def handle_keydown_event(event_key, selector):
    if event_key == SELECTOR_LEFT and selector.get_selected()[0] is not 0:
        selector.move(-1, 0)
        print(selector)
    if event_key == SELECTOR_RIGHT and selector.get_selected()[0] is not board_width - 1:
        selector.move(1, 0)
        print(selector)
    if event_key == SELECTOR_UP and selector.get_selected()[1] is not 0:
        selector.move(0, -1)
        print(selector)
    if event_key == SELECTOR_DOWN and selector.get_selected()[1] is not board_height - 1:
        selector.move(0, 1)
        print(selector)


if __name__ == '__main__':
    main()
