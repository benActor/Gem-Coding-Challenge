from unittest import TestCase
from models import PowerPlant, DailyData


class PowerPlantTest(TestCase):
    def setUp(self) -> None:
        self.powerPlant = PowerPlant("gasfiredbig1", "gasfired", 0.53, 100, 460)

    def test_canCreate_pwp(self):
        self.assertIsInstance(self.powerPlant, PowerPlant)


class DailyDataTest(TestCase):
    def setUp(self) -> None:
        self.data = DailyData(480, 13.4, 50.8, 20, 60)

    def test_date(self):
        self.assertIsNotNone(self.data.date)
