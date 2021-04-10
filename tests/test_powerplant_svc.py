from unittest import TestCase
from power_plants.utils import PowerplantSvc
from models import PowerPlant, DailyData
import json


class PowerPlantSvcTest(TestCase):
    def setUp(self) -> None:
        with open("payload.json") as f:
            self.payload = json.load(f)

        self.svc = PowerplantSvc(self.payload)

    def test_can_load_pwp_from_json(self):
        self.assertIsInstance(self.svc.powerplants[0], PowerPlant)

        self.assertEqual(6, len(self.svc.powerplants))

        self.assertIsInstance(self.svc.day_data, DailyData)

