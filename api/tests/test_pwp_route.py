from unittest import TestCase
from api import create_app
import json
from api.init_app import socketio


class RouteTest(TestCase):
    def setUp(self) -> None:

        self.app_client = create_app()[0].test_client()
        self.app = create_app()[0]
        with open("payload.json") as f:
            self.data = json.load(f)

    def test_production_route(self):
        result = self.app_client.post("/productionplan", data=json.dumps(self.data["payload"]),
                                      content_type='application/json')

        self.assertEqual(result.status_code, 200)

        self.assertEqual(result.json, self.data["response"])

    # def test_running_port(self):
    #     port = self.app.config["SERVER_NAME"].split(":")[1]
    #     self.assertEqual(port, "8888")

    def test_web_socket(self):
        client_message = socketio.test_client(self.app)

        self.app_client.post("/productionplan", data=json.dumps(self.data["payload"]), content_type='application/json')

        socket_data = client_message.get_received()

        soc_payload, soc_resp = socket_data[0]["args"]["payload"], socket_data[0]["args"]["response"]

        self.assertEqual(soc_payload, self.data["payload"])

        self.assertEqual(soc_resp, self.data["response"])


