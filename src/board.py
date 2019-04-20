import sys, pygame, tile
from common import *
from tile import Tile

TILESIZE = 40
BACKGROUNDCOLOR = GRAY

class Board:
    width = None
    height = None
    tilesize = None
    backgroundColor = None
    tiles =[[]]

    def __init__(self, width, height):
        self.tiles = [[0 for y in range(width)] for x in range(height)]
        self.width = width
        self.height = height

    # Created on the assumption that the board will know the state of itself and what's on it
    def draw(self, surface):
        new_surf = surface.copy()

        new_surf.fill(BACKGROUNDCOLOR)

        for x in range(self.width):
                for y in range(self.height):
                    min_x, min_y = self.getLeftTopTileCoords(x, y)

                    color = GREEN

                    pygame.draw.rect(new_surf, color, (min_x, min_y, TILESIZE, TILESIZE))
                    
                    pygame.draw.line(new_surf, SQUAREBORDERCOLOR, (min_x, min_y), (min_x + TILESIZE, min_y))
                    pygame.draw.line(new_surf, SQUAREBORDERCOLOR, (min_x, min_y), (min_x, min_y + TILESIZE))        

                    if (x + 1) == self.width:
                        pygame.draw.line(new_surf, SQUAREBORDERCOLOR, (min_x + TILESIZE, min_y), (min_x + TILESIZE, min_y + TILESIZE))
                    if (y + 1) == self.height:
                        pygame.draw.line(new_surf, SQUAREBORDERCOLOR, (min_x, min_y + TILESIZE), (min_x + TILESIZE, min_y + TILESIZE))

        surface.blit(new_surf, (0, 0))

    # Set a tile on the board
    def setTile(self, x, y, color):
        tile = Tile(color)   
        self.tiles[x][y] = tile

    # Get the coordinates of the top left corner of a tile
    def getLeftTopTileCoords(self, tile_x, tile_y):
        min_x = tile_x * TILESIZE
        min_y = tile_y * TILESIZE
        return (min_x, min_y)

    # Get a tile from the board
    def getTile(self, x, y):
        if self.tiles[x][y]:
            return self.tiles[x][y]
        return None
