from src.cShip import cShip
from src.cCargo import cCargo
from src.cCruise import cCruise
import csv

def main() -> None:

 with open ("src/ships.csv") as file :
    reader = csv.reader (file, delimiter=',')
    next (file, None) #sirve para no leer el encabezado
    for line in reader:
        if line[3] != "":
            cargo = cCargo(line[2],line[3],line[0],line[1])
            try:
                robar= cargo.is_worth_it()
                print(robar)
            except ValueError:
                print("Esta pobre, NO ASALTAR")
        elif line[2] != "" and line[3] == "" :
            crucero = cCruise (line[3], line[1], line[2])
            try:
                robar = crucero.is_worth_it()
                print(robar)
            except ValueError:
                print("Esta pobre, NO ASALTAR")
        else:
            barco = cShip(line[0], line[1])
            try :
                robar = barco.is_worth_it()
                print (robar)
            except ValueError:
                print("Esta pobre, NO ASALTAR")
if __name__ == "__main__":
  main()
