from abc import ABC
from abc import abstractmethod


class BaseObject(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self, surface):
        pass
