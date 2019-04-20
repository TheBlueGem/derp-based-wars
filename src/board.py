import sys, pygame
from common import *

TILESIZE = 40
BACKGROUNDCOLOR = GRAY

def createBoard(width, height, display_surf):
    board = [[0 for y in range(width)] for x in range(height)]

    drawBoard(board, display_surf)

    return board

# Created on the assumption that the board will know the state of itself and what's on it
def drawBoard(board, surface):
    new_surf = surface.copy()

    new_surf.fill(BACKGROUNDCOLOR)
    
    width = len(board)
    height = len(board[0])

    for x in range(width):
            for y in range(height):
                min_x, min_y = leftAndTopCoordsOfTile(x, y)

                color = GREEN

                pygame.draw.rect(new_surf, color, (min_x, min_y, TILESIZE, TILESIZE))
                
                pygame.draw.line(new_surf, SQUAREBORDERCOLOR, (min_x, min_y), (min_x + TILESIZE, min_y))
                pygame.draw.line(new_surf, SQUAREBORDERCOLOR, (min_x, min_y), (min_x, min_y + TILESIZE))        

                if x + 1 == width:
                    pygame.draw.line(new_surf, SQUAREBORDERCOLOR, (min_x, min_y + TILESIZE), (min_x + TILESIZE, min_y + TILESIZE))
                if y + 1 == height:
                    pygame.draw.line(new_surf, SQUAREBORDERCOLOR, (min_x + TILESIZE, min_y), (min_x + TILESIZE, min_y + TILESIZE))

    surface.blit(new_surf, (0, 0))

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
