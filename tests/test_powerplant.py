from unittest import TestCase
from models import PowerPlant


class PowerPlantTest(TestCase):
    def setUp(self) -> None:
        self.powerPlant = PowerPlant()

    def test_canCreate_pwp(self):
        self.assertIsInstance(self.powerPlant, PowerPlant)