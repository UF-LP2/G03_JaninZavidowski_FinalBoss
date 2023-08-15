import pytest
from src.cCargo import cCargo

def CargoTest1():
    cargo1 = cCargo (34,0.5,4231,1290)
    assert cargo1.is_worth_it() == "Asalten este barco y salvamos la deuda con el FMI"
def CargoTest2():
    cargo2 = cCargo (60,0.25,2145,2569)
    with pytest.raises(ValueError):
        cargo2.is_worth_it()