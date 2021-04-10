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

    def test_get_pmax(self):
        self.assertEqual(460, self.svc.get_pwp_load(self.svc.powerplants[1]))

        self.assertEqual(21.6, self.svc.get_pwp_load(self.svc.powerplants[-1]))

        self.assertLess(self.svc.get_pwp_load(self.svc.powerplants[-2]), 150)

    def test_prod_cost(self):
        self.assertGreater(self.svc.get_prod_cost(self.svc.powerplants[1]), 13.4)

        self.assertEqual(self.svc.get_prod_cost(self.svc.powerplants[-2]), 0)

