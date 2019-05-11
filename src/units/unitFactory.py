from units.soldier import Soldier
from units.airship import Airship
from units.unit import Unit

class UnitFactory: 

    @staticmethod
    def createUnit(unitType: "Soldier" and "Airship") -> Unit:  
        if unitType == "Soldier":
            return Soldier()
        elif unitType == "Airship":
            return Airship()
        else:
            raise ValueError(unitType)