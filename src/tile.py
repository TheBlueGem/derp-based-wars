class Tile:
    color = None
    units = []

    def __init__(self, color, units = []):
        self.color = color
        self.units = units
    
    def __str(self):
        return "Tile with color: %s" % (self.color)