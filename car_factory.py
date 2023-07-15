from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.splinder_battery import SplinderBattery
from tire.carrigan import CarriganTire
from tire.octoprime import OctoPrimeTire
from car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear_array)
        return Car(engine, battery, tire)
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tire = OctoPrimeTire(tire_wear_array)
        return Car(engine, battery,tire)
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on,tire_wear_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SplinderBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear_array)
        return Car(engine, battery, tire)
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoPrimeTire(tire_wear_array)
        return Car(engine, battery, tire)
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear_array)
        return Car(engine, battery, tire) 
