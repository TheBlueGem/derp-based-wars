from abc import ABC
from abc import abstractmethod

from pygame.surface import Surface


class BaseTileObject(ABC):
    _sprite = None
    _background_color = None

    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self, surface: Surface):
        pass

    @property
    def sprite(self):
        return self._sprite

    @sprite.setter
    def sprite(self, sprite: str):
        self._sprite = sprite
