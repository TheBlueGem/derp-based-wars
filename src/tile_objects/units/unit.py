from pygame.surface import Surface
from pygame import draw as pygame_draw

from common import YELLOW
from common import TILE_SIZE
from tile_objects.base_tile_object import BaseTileObject


class Unit(BaseTileObject):
    _movement = None
    _moved = None
    _health_points = None
    _attack = None
    _strengths = []
    _statusses = []

    def __init__(self):
        super().__init__()

    def draw(self, surface: Surface):
        quarter = TILE_SIZE / 4
        pygame_draw.line(surface, YELLOW, (quarter, quarter),
                         (quarter * 3, quarter * 3), 3)
        pygame_draw.line(surface, YELLOW, (quarter * 3, quarter),
                         (quarter, quarter * 3), 3)

    @property
    def movement(self):
        return self._movement

    @movement.setter
    def movement(self, movement: int):
        self._movement = movement

    @property
    def moved(self):
        return self._moved

    @moved.setter
    def moved(self, moved: int):
        self._moved = moved

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, health_points: int):
        self._health_points = health_points

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, attack: int):
        self._attack = attack

    @property
    def strengths(self):
        return self._strengths

    @strengths.setter
    def strengths(self, strengths):
        self._strengths = strengths

    @property
    def statusses(self):
        return self._statusses

    @statusses.setter
    def statusses(self, statusses):
        self._statusses = statusses
