from tile_objects.units.unit import Unit
from tile_objects.units.unitBuilder import UnitBuilder


def spear() -> Unit:
    builder = UnitBuilder()
    # self.name = "Spear"
    builder.movement = 3
    builder.health_points = 10
    builder.attack = 3
    builder.strengths = None
    return builder.build()
