from src.cShip import cShip
class cCruise(cShip):
    def __init__(self, passengers, draft, crew):
        self.passengers=int(passengers)
        super()._init_(draft, crew)

    def peso_pers(self):
        peso=self.passengers*2.25+self.crew*1.5
        return peso

    def is_worth_it(self):
        if self.draft - self.peso_pers() < 20:
            raise ValueError
        return "robar barco"