from src.barbeiro import Barbeiro
from src.barberService import BarberService
from tests.barberRepFake import BarberRepFake
from .appointServiceDummy import AppointServiceDummy

def test_1_insert_barbers_on_system_and_show_length_3():
    barber_rep = BarberRepFake()
    barber_serv = BarberService(barber_rep)
    appointm = AppointServiceDummy()
    hour_app = appointm.show_hour_appointment('10:30')
    b = Barbeiro(name="josé",age=58,workplace="barbearia NewWay",appointments=[])
    b2 = Barbeiro(name="evandro",age=28,workplace="their space",appointments=[])
    b3 = Barbeiro(name='almendra',age=47,workplace='el barbeiro',appointments=[])
    barber_serv.insertBarber(b)
    barber_serv.insertBarber(b2)
    barber_serv.insertBarber(b3)
    len_barbers = barber_serv.getLength()
    assert len_barbers == 3
    assert hour_app == '10:30'

