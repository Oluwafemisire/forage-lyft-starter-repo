from serviceable.battery.battery import Battery
from serviceable.engine.engine import Engine
from serviceable.serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self._engine = engine
        self._battery = battery

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

    def needs_service(self):
        return self._engine.needs_service() or self._battery.needs_service()

