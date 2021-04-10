class PowerPlant:
    def __init__(self, name, type, efficiency, pmin, pmax):
        self.name, self.type, self.efficiency, self.pmin, self.pmax = name, type, efficiency, pmin, pmax

    def __eq__(self, other):
        if not isinstance(other, PowerPlant):
            return NotImplementedError
        else:
            return self.name == other.name and self.type == other.type
