from battery.battery import Battery
from date_adjuster import add_years_to_date

class SplinderBattery(Battery):
    def __init__(self, last_service_date,current_service_date):
        self._last_service_date = last_service_date
        self._current_service_date = current_service_date

    def needs_service(self):
        proposed_service_date = add_years_to_date(self._last_service_date, 3) 
        if proposed_service_date < self._current_service_date:
            return True
        else:
            return False