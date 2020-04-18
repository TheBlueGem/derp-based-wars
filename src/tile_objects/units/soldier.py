from units.unit import Unit

class Soldier(Unit):
    
    name = "Soldier"
    movement = 3
    moved = False
    health_points = 10
    attack = 3
    defense = 3
    strengths = None
    weaknesses = None