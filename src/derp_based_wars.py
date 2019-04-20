import pygame, sys, board, common, options
from pygame import init
from pygame.locals import QUIT, KEYUP, K_ESCAPE
from board import *
from options import FPS

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    board_width = 30
    board_height = 30

    pygame.display.set_caption('Derp Based Wars')

    main_board = createBoard(board_width, board_height, DISPLAYSURF)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        
        drawBoard(main_board, DISPLAYSURF)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()