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

    pygame.display.set_caption('Derp Based Wars')

    mainBoard = createBoard()

    DISPLAYSURF.fill(BACKGROUNDCOLOR)

    while True:
        drawBoard(mainBoard, DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    

if __name__ == '__main__':
    main()