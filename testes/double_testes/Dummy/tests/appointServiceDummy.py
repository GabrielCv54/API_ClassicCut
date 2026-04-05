from src.appointment_service import Appointments

class AppointServiceDummy(Appointments):
    def show_hour_appointment(self, hour: str):       
        raise NotImplemented("Esse método não existe ou não está implementado!")