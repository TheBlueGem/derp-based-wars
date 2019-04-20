import pygame, sys, board, common, options
from pygame import init
from pygame.locals import QUIT, KEYUP, K_ESCAPE
from board import Board
from options import FPS
from common import *

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

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        
        main_board.draw(DISPLAYSURF)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()