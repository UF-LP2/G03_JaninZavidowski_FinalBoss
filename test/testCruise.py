import pytest
from src.cShip import cCruise

def CruceroTest1():
    crucero1 = cCruise (29,2823,51)
    assert crucero1.is_worth_it() == "Asalten este barco y salvamos la deuda con el FMI"
def CruceroTest2():
    crucero2 = cCruise (6,3173,4096)
    with pytest.raises(ValueError):
        crucero2.is_worth_it()