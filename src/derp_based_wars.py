import sys

from pygame import quit as pygame_quit
from pygame import display
from pygame import init
from pygame.locals import QUIT, KEYUP, K_ESCAPE
from pygame import time

from board import Board
from options import FPS
from units.unitFactory import UnitFactory
from common import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR
from selector import Selector


# Main game loop
def main():
    init()
    fps_clock = time.Clock()
    display_surf = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    board_width = 10
    board_height = 10

    display.set_caption('Derp Based Wars')

    main_board = Board(board_width, board_height)
    main_board.draw(display_surf)
    selector = Selector(main_board.getLeftTopTileCoords(5, 5))
    print(selector)

    player1_units = [UnitFactory.createUnit("Soldier"), UnitFactory.createUnit("Soldier"),
                     UnitFactory.createUnit("Airship")]

    player2_units = [UnitFactory.createUnit("Soldier"), UnitFactory.createUnit("Soldier"),
                     UnitFactory.createUnit("Airship")]

    main_board.initializeUnitPositions(player1_units + player2_units)

    while True:
        for event in event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame_quit()
                sys.exit()

        # Main drawing loop
        new_surf = display_surf.copy()
        new_surf.fill(BACKGROUND_COLOR)
        main_board.draw(new_surf)
        selector.draw(new_surf)
        display_surf.blit(new_surf, (0, 0))
        display.update()
        fps_clock.tick(FPS)


if __name__ == '__main__':
    main()
