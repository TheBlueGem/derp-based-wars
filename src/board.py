import sys, pygame
from common import *

TILESIZE = 40
BACKGROUNDCOLOR = GRAY

def createBoard(width, height):
    board = [[0 for y in range(width)] for x in range(height)]
    for x in range(width):
        for y in range(height):
            setTile(x, y, GREEN, board)
    return board

def drawBoard(board, width, height, display_surf):
    display_surf.fill(BACKGROUNDCOLOR)

    for x in range(len(board)):
        for y in range(len(board[0])):
            min_x, min_y = leftAndTopCoordsOfTile(x, y)
            pygame.draw.rect(display_surf, board[x][y]['color'], (min_x, min_y, TILESIZE, TILESIZE))
            
            pygame.draw.line(display_surf, SQUAREBORDERCOLOR, (min_x, min_y), (min_x + TILESIZE, min_y))
            pygame.draw.line(display_surf, SQUAREBORDERCOLOR, (min_x, min_y), (min_x, min_y + TILESIZE))        

            if x + 1 == width:
                pygame.draw.line(display_surf, SQUAREBORDERCOLOR, (min_x, min_y + TILESIZE), (min_x + TILESIZE, min_y + TILESIZE))
            if y + 1 == height:
                pygame.draw.line(display_surf, SQUAREBORDERCOLOR, (min_x + TILESIZE, min_y), (min_x + TILESIZE, min_y + TILESIZE))

def setTile(x, y, color, board):
    board[x][y] = {
        'color': color
    }
    return board

def leftAndTopCoordsOfTile(tile_x, tile_y):
    min_y = tile_y * TILESIZE
    min_x = tile_x * TILESIZE
    return (min_x, min_y)

def getTile(x, y, board):
    if board[x][y]:
        min_x, min_y = leftAndTopCoordsOfTile(x, y)
        tile = board[x][y]
        tile['min_x'] = min_x
        tile['min_y'] = min_y
        return tile
    return None
