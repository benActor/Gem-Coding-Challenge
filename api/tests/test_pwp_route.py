from unittest import TestCase
from api import app
import json


class RouteTest(TestCase):
    def setUp(self) -> None:

        self.app = app.test_client()

    def test_production_route(self):
        with open("payload.json") as f:
            data = json.load(f)
        result = self.app.post("/productionplan", data=json.dumps(data), content_type='application/json')

        self.assertEqual(result.status_code, 200)

    def test_running_port(self):
        port = app.config["SERVER_NAME"].split(":")[1]
        self.assertEqual(port, "8888")


