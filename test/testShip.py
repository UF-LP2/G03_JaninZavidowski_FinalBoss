import pytest
from src.cShip import cShip

def ShipTest1():
    ship1 = cShip (586,23)
    assert ship1.is_worth_it() == "Asalten este barco y salvamos la deuda con el FMI"
def ShipTest2():
    ship2 = cShip (2182,2272)
    with pytest.raises(ValueError):
        ship2.is_worth_it()