from src.cShip import cShip
class cCargo(cShip):
    def _init_(self, cargo, quality, draft, crew):
        self.cargo = float(cargo)
        self.quality = float(quality)
        super()._init_(draft,crew)

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
        return "robar barco"