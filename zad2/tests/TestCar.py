import unittest
from ..src.Car import Car
from ..src.CarImpl import CarImpl
from unittest.mock import *

car = Car()
impl = CarImpl(car)


class TestCar(unittest.TestCase):

    def test_needsFuel_ok(self):
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = False
        self.assertEqual("ok", impl.fuel())

    def test_needsFuel_get(self):
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = True
        self.assertEqual("get fuel", impl.fuel())

    def test_tmpr_low(self):
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 75
        self.assertEqual("too low", impl.engineTemp())

    def test_tmpr_ok(self):
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 95
        self.assertEqual("ok", impl.engineTemp())

    def test_tmpr_high(self):
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 110
        self.assertEqual("too high", impl.engineTemp())

    def test_destination_ok(self):
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = "Warsaw"
        self.assertEqual("set", impl.dest("Warsaw"))

    def test_destination_choose(self):
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = None
        self.assertEqual("choose destination", impl.dest(None))

