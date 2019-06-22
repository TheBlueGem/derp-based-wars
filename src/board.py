import sys
import pygame
import tile
import base_object
import random
from common import *
from tile import Tile
from base_object import BaseObject


class Board(BaseObject):
    width = None
    height = None
    tilesize = None
    backgroundColor = None
    tiles = [[]]
    unitPositions = []

    def __init__(self, width, height):
        self.tiles = [[Tile for y in range(width)] for x in range(height)]
        self.width = width
        self.height = height

    # Created on the assumption that the board will know the state of itself and what's on it
    def draw(self, surface):
        for x in range(self.width):
            for y in range(self.height):
                color = GREEN
                min_x, min_y = self.getLeftTopTileCoords(x, y)
                pygame.draw.rect(
                    surface, color, (min_x, min_y, TILESIZE, TILESIZE))
                pygame.draw.line(surface, SQUAREBORDERCOLOR,
                                 (min_x, min_y), (min_x + TILESIZE, min_y))
                pygame.draw.line(surface, SQUAREBORDERCOLOR,
                                 (min_x, min_y), (min_x, min_y + TILESIZE))

                # For drawing the outer borders of the board
                if (x + 1) == self.width:
                    pygame.draw.line(surface, SQUAREBORDERCOLOR, (min_x +
                                                                  TILESIZE, min_y), (min_x + TILESIZE, min_y + TILESIZE))
                if (y + 1) == self.height:
                    pygame.draw.line(surface, SQUAREBORDERCOLOR, (min_x,
                                                                  min_y + TILESIZE), (min_x + TILESIZE, min_y + TILESIZE))

    def initializeUnitPositions(self, units:[]):
        for unit in units:
            randomTile = self.getRandomTile()
            randomTile.units.append(unit)                    

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

    # Get a random tile from the board
    def getRandomTile(self) -> Tile:
        randomX = random.randint(0, self.width - 1)
        randomY = random.randint(0, self.height - 1)

        tile = self.tiles[randomY][randomX]

        return tile