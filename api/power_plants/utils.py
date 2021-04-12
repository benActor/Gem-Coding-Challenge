from api.models import PowerPlant, DailyData
from itertools import combinations


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

    def get_pwp_load(self, pwp):
        if pwp.type == "windturbine":
            return pwp.pmax * self.day_data.wind / 100
        return pwp.pmax

    def get_prod_cost(self, pwp):
        if pwp.type == "gasfired":
            return self.day_data.gas * 1/pwp.efficiency
        if pwp.type == "kerosine":
            return self.day_data.kerosine * 1/pwp.efficiency
        return 0

    def get_set_prod_cost(self, pwp_set):
        return sum(map(lambda x: self.get_prod_cost(x), pwp_set))

    def compute_load_of_set(self, pwp_set):
        return sum(map(lambda x: self.get_pwp_load(x), pwp_set))

    def pwp_combinations(self):
        comb = []
        for i in range(1, len(self.powerplants) + 1):
            comb += list(combinations(self.powerplants, i))
        return comb

    def closest_value(self, value):
        if value - self.day_data.load >= 0:
            return value - self.day_data.load
        return 1000

    def get_optimal_combination(self):
        return min(self.pwp_combinations(), key=lambda x: self.closest_value(self.compute_load_of_set(x)))

