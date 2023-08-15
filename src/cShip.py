class cShip:
    def __init__(self,draft,crew):
        self.draft=float(draft)
        self.crew=float(crew)


    def is_worth_it(self):
        if self.draft-self.crew*1.5<20:
            raise ValueError
        return "Asalten este barco y salvamos la deuda con el FMI"