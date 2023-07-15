from battery.battery import Battery
from engine.engine import Engine
from tire.tire import Tire
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self._engine = engine
        self._battery = battery
        self._tire = tire

    @property
    def engine(self):
        return self._engine
    @engine.setter
    def engine(self, engine: Engine):
        self._engine = engine
    @property
    def battery(self):
        return self._battery
    @battery.setter
    def battery(self, battery: Battery):
        self._battery = battery
    @property
    def tire(self):
        return self.tire
    @tire.setter
    def tire(self, tire: Tire):
        self._tire = tire

    def needs_service(self):
        return self._engine.needs_service() or self._battery.needs_service() or self._tire.needs_service()

