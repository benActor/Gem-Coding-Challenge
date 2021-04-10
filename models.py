from datetime import datetime

class PowerPlant:
    def __init__(self, name, type, efficiency, pmin, pmax):
        self.name, self.type, self.efficiency, self.pmin, self.pmax = name, type, efficiency, pmin, pmax

    def __eq__(self, other):
        if not isinstance(other, PowerPlant):
            return NotImplementedError
        else:
            return self.name == other.name and self.type == other.type

    def __repr__(self):
        return f"name: {self.name}, type: {self.type}, efficiency: {self.efficiency}, pmax: {self.pmax} "

class DailyData:
    def __init__(self, load, gas, kerosine, co2, wind):
        self.load, self.gas, self.kerosine, self.co2, self.wind = load, gas, kerosine, co2, wind
        self.__date = datetime.today().strftime('%Y-%m-%d')

    @property
    def date(self):
        return self.__date

