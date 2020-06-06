from tile_objects.environment.environment import Environment


class EnvironmentBuilder:
    _background_color = None
    _movement_cost = 0

    def build(self) -> Environment:
        environment = Environment()
        environment.movement_cost = self._movement_cost
        environment.background_color = self._background_color
        return environment

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
