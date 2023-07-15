import unittest

from tire.octoprime import OctoPrimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire = OctoPrimeTire([0,1,1,1])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = OctoPrimeTire([0,0,0,0])
        self.assertFalse(tire.needs_service())