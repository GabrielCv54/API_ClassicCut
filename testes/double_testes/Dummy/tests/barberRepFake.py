from src.barbeiro import Barbeiro
from src.barbeiroRep import BarbeiroRep

class BarberRepFake(BarbeiroRep):
    def __init__(self):
        self.barbers = []

    def insert_on_system(self, barber: Barbeiro):
        self.barbers.append(barber)
        return True

    def show_qttd_barbers(self) -> int:
        return len(self.barbers)
    
    def show_all_barbers(self) -> list:
        return [{barb} for barb in self.barbers]

