from tile_objects.units.unit import Unit


# class BuildError(Exception):
#     def __init__(self, attribute):
#         super().__init__()
#         self.message


class UnitBuilder:
    _movement = None
    _moved = None
    _health_points = None
    _attack = None
    _strengths = []
    _statusses = []
    _sprite = None

    def build(self) -> Unit:
        unit = Unit()
        if self.movement is not None:
            unit.movement = self.movement
        else:
            raise Exception("Unit movement can't be None")

        unit.moved = self.moved if self.moved is not None else False

        if self.health_points is not None:
            unit.health_points = self.health_points
        else:
            raise Exception("Unit health points can't be None")

        if self.attack is not None:
            unit.attack = self.attack
        else:
            raise Exception("Unit attack can't be None")

        unit.statusses = self.strengths
        unit.statusses = self.statusses
        unit.sprite = self.sprite

        return unit

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

    @property
    def sprite(self):
        return self._sprite

    @sprite.setter
    def sprite(self, sprite):
        self._sprite = sprite
