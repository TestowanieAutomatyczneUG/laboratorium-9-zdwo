from .Car import Car


class CarImpl:

    def __init__(self, car: Car):
        self.car = car

    def fuel(self):
        if self.car.needsFuel():
            return "get fuel"
        else:
            return "ok"

    def engineTemp(self):
        tmpr = self.car.getEngineTemperature()
        if tmpr < 90:
            return "too low"
        elif tmpr > 100:
            return "too high"
        else:
            return "ok"

    def dest(self, destination):
        if self.car.driveTo(destination):
            return "set"
        else:
            return "choose destination"

