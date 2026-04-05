from abc import abstractmethod,ABCMeta

class Appointments(metaclass=ABCMeta):
    @abstractmethod
    def show_hour_appointment(self, hour: str):
        pass