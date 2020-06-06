from pygame.surface import Surface

from tile_objects.base_tile_object import BaseTileObject


class Environment(BaseTileObject):
    _background_color = None
    _movement_cost = 0

    def __init__(self):
        super().__init__()

    @property
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, color):
        self._background_color = color

    @property
    def movement_cost(self):
        return self._movement_cost

    @movement_cost.setter
    def movement_cost(self, movement_cost):
        self._movement_cost = movement_cost

    def draw(self, surface: Surface):
        surface.fill(self._background_color)
