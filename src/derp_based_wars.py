import pygame
import sys
import board
import common
import options
import selector
from pygame import init
from pygame.locals import QUIT, KEYUP, K_ESCAPE
from board import Board
from options import FPS
from common import *
from selector import Selector

# Main game loop
def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    board_width = 10
    board_height = 10

    pygame.display.set_caption('Derp Based Wars')

    main_board = Board(board_width, board_height)
    main_board.draw(DISPLAYSURF)
    selector = Selector(main_board.getLeftTopTileCoords(5,5))
    print(selector)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        # Main drawing loop
        new_surf = DISPLAYSURF.copy()
        new_surf.fill(BACKGROUNDCOLOR)
        main_board.draw(new_surf)
        selector.draw(new_surf)
        DISPLAYSURF.blit(new_surf, (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
