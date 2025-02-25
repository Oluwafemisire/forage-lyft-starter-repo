import unittest
from datetime import date

from battery.splinder_battery import SplinderBattery


class TestSplindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2021-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = SplinderBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SplinderBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
