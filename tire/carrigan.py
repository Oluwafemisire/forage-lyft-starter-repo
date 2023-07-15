from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_array):
        self._tire_array = tire_array

    def needs_service(self):
        for number in self._tire_array:
            if number >= 0.9:
                return True
        return False