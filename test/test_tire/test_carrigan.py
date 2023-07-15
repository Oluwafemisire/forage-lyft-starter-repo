import unittest

from tire.carrigan import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire = CarriganTire([0,0.2,0.9,0.5])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = CarriganTire([0,0.2,0.5,0.5])
        self.assertFalse(tire.needs_service())


