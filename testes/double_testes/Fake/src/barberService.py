from src.barbeiroRep import BarbeiroRep
from src.barbeiro import Barbeiro

class BarberService:
    def __init__(self, barberRep: BarbeiroRep):
        self.barberRep = barberRep

    def insertBarber(self,barber: Barbeiro):
        self.barberRep.insert_on_system(barber)

    def getLength(self):
        return self.barberRep.show_qttd_barbers()