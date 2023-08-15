class cShip:
    def __init__(self,draft,crew):
        self.draft=float(draft)
        self.crew=float(crew)


    def is_worth_it(self):
        if self.draft-self.crew*1.5<20:
            raise ValueError
        return "Asalten este barco y salvamos la deuda con el FMI"

class cCargo(cShip):
    def __init__(self, cargo, quality, draft, crew):
        self.cargo = float(cargo)
        self.quality = float(quality)
        super().__init__(draft,crew)

    def peso_tripu(self):
        peso=self.crew*1.5
        return peso

    def is_worth_it(self):
        if self.quality == 1:
            self.draft=self.draft+self.cargo*3.5
        elif self.quality == 0.5:
            self.draft = self.draft + self.cargo * 2
        elif self.quality == 0.25:
            self.draft = self.draft + self.cargo * 0.5

        if self.draft - self.peso_tripu()<20:
            raise ValueError
        return "Asalten este barco y salvamos la deuda con el FMI"

class cCruise(cShip):
    def __init__(self, passengers, draft, crew):
        self.passengers = int(passengers)
        super().__init__(draft, crew)

    def peso_pers(self):
        peso=self.passengers*2.25+self.crew*1.5
        return peso

    def is_worth_it(self):
        if self.draft - self.peso_pers() < 20:
            raise ValueError
        return "Asalten este barco y salvamos la deuda con el FMI"