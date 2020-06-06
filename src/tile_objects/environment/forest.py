from tile_objects.environment.environment import Environment
from tile_objects.environment.environmentBuilder import EnvironmentBuilder

DARK_GREEN = (0, 66, 12)


def forest() -> Environment:
    builder = EnvironmentBuilder()
    builder.background_color = DARK_GREEN
    builder.movement_cost = 2
    return builder.build()
