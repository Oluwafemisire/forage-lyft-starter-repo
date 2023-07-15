from tire.tire import Tire

class OctoPrimeTire(Tire):
    def __init__(self, tire_array):
        self._tire_array = tire_array

    def needs_service(self):
        running_sum = 0
        for number in self._tire_array:
            running_sum += number
        if running_sum >= 3:
            return True
        else:
            return False