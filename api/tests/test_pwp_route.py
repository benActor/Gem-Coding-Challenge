from unittest import TestCase
from api import create_app
import json


class RouteTest(TestCase):
    def setUp(self) -> None:

        self.app_client = create_app().test_client()
        self.app = create_app()

    def test_production_route(self):
        with open("payload.json") as f:
            data = json.load(f)
        result = self.app_client.post("/productionplan", data=json.dumps(data), content_type='application/json')

        self.assertEqual(result.status_code, 200)

    def test_running_port(self):
        port = self.app.config["SERVER_NAME"].split(":")[1]
        self.assertEqual(port, "8888")


