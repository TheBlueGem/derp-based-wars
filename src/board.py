import sys, pygame
from common import *

BASEWIDTH = 100
BASEHEIGHT = 100
SQUARESIZE = 40
BACKGROUNDCOLOR = GREEN

def createBoard(width = BASEWIDTH, height = BASEHEIGHT):
    board = [[0 for y in range(BASEHEIGHT)] for x in range(BASEWIDTH)]
    for x in range(BASEWIDTH):
        for y in range(BASEHEIGHT):
            setSquare(x, y, GRAY, board)
    return board

def drawBoard(board, displaySurf):
    for x in range(len(board)):
        for y in range(len(board[0])):
            top, left = topLeftCoordsOfSquare(x, y)
            pygame.draw.rect(displaySurf, board[x][y]['color'], (left, top, SQUARESIZE, SQUARESIZE))        

def setSquare(x, y, color, board):
    board[x][y] = {
        'color': color
    }
    return board

def topLeftCoordsOfSquare(squarex, squarey):
    top = squarey * SQUARESIZE
    left = squarex * SQUARESIZE
    return (top, left)

def getSquare(x, y, board):
    for squarex in len(board[x]):
        for squarey in len(board[0]):
            left, top = topLeftCoordsOfSquare(squarex, squarey)
            boxRect = pygame.Rect(left, top, SQUARESIZE, SQUARESIZE)
            if boxRect.collidepoint(x, y):
                return (squarex, squarey)
    return (None, None)
