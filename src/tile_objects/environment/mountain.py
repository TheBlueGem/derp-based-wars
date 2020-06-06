from common import GRAY
from tile_objects.environment.environment import Environment
from tile_objects.environment.environmentBuilder import EnvironmentBuilder


def mountain() -> Environment:
    builder = EnvironmentBuilder()
    builder.background_color = GRAY
    builder.movement_cost = 3
    return builder.build()
