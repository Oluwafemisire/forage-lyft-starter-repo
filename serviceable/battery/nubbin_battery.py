from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date,current_service_date):
        self._last_service_date = last_service_date
        self._current_service_date = current_service_date

    def needs_service(self):
        return self._current_service_date - self._last_service_date > 4