from common import GREEN
from tile_objects.environment.environment import Environment
from tile_objects.environment.environmentBuilder import EnvironmentBuilder


def grass() -> Environment:
    builder = EnvironmentBuilder()
    builder.background_color = GREEN
    builder.movement_cost = 1
    return builder.build()




