import sys

from pygame import quit as pygame_quit
from pygame import display
from pygame import init
from pygame.locals import QUIT, KEYUP, K_ESCAPE, KEYDOWN
from pygame import time
from pygame import event as pygame_event

from board import Board
from options import FPS, SELECTOR_DOWN, SELECTOR_LEFT, SELECTOR_RIGHT, SELECTOR_UP
from units.unitFactory import UnitFactory
from common import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR
from selector import Selector

board_width = 10
board_height = 10


# Main game loop
def main():
    init()
    fps_clock = time.Clock()
    display_surf = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    display.set_caption('Derp Based Wars')

    main_board = Board(width=board_width, height=board_height)
    main_board.draw(surface=display_surf)
    selector = Selector((5, 5))
    print(selector)

    player1_units = [UnitFactory.createUnit("Soldier"), UnitFactory.createUnit("Soldier"),
                     UnitFactory.createUnit("Airship")]

    player2_units = [UnitFactory.createUnit("Soldier"), UnitFactory.createUnit("Soldier"),
                     UnitFactory.createUnit("Airship")]

    main_board.initialize_unit_positions(units=player1_units + player2_units)

    while True:
        for event in pygame_event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame_quit()
                sys.exit()

            if event.type == KEYDOWN:
                handle_keydown_event(event.key, selector)

                # Main drawing loop
        new_surf = display_surf.copy()
        new_surf.fill(BACKGROUND_COLOR)
        main_board.draw(new_surf)
        selector.draw(new_surf)
        display_surf.blit(new_surf, (0, 0))
        display.update()
        fps_clock.tick(FPS)


def handle_keydown_event(event_key, selector):
    if event_key == SELECTOR_LEFT and selector.get_selected()[0] is not 1:
        selector.move(-1, 0)
        print(selector)
    if event_key == SELECTOR_RIGHT and selector.get_selected()[0] is not board_width:
        selector.move(1, 0)
        print(selector)
    if event_key == SELECTOR_UP and selector.get_selected()[1] is not 1:
        selector.move(0, -1)
        print(selector)
    if event_key == SELECTOR_DOWN and selector.get_selected()[1] is not board_height:
        selector.move(0, 1)
        print(selector)


if __name__ == '__main__':
    main()
