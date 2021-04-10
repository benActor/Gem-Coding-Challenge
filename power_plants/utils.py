from models import PowerPlant, DailyData


class PowerplantSvc:
    def __init__(self, payload):
        self.payload = payload

        self.__powerplants = [PowerPlant(p["name"], p["type"], p["efficiency"], p["pmin"], p["pmax"])
                              for p in payload["powerplants"]]

        self.__day_data = DailyData(load=payload["load"], gas=payload["fuels"]["gas(euro/MWh)"],
                                    kerosine=payload["fuels"]["kerosine(euro/MWh)"],
                                    co2=payload["fuels"]["co2(euro/ton)"], wind=payload["fuels"]["wind(%)"])

    @property
    def powerplants(self):
        return self.__powerplants

    @property
    def day_data(self):
        return self.__day_data
