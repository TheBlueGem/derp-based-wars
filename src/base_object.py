import sys, abc

from abc import ABC, abstractmethod

class BaseObject(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self):
        pass