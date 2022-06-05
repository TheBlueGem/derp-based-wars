from tile_objects.units.unit import Unit

class Airship(Unit):
    
    name = "Airship"
    movement = 5
    moved = False
    health_points = 5
    attack = 3
    defense = 3
    strengths = None
    weaknesses = None