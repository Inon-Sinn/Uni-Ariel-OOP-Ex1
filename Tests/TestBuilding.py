import unittest
from Classes.Building import Building as bld
from Classes.Elevator import Elevator as elv


class BuildingTest(unittest.TestCase):
    e1 = elv(1, 1, -5, 12, 2, 2, 2, 3)
    e2 = elv(2, 3, -10, 50, 1, 1, 1, 1)
    e3 = elv(3, 1.5, -3, 15, 3, 3, 2, 2)

    b1 = bld(0, 10, [e1])
    b2 = bld(-2, 15, [e1, e2])
    b3 = bld(-5, 18, [e1, e2, e3])

    def test_min_floor(self):
        self.assertEqual(self.b1.getMinFloor(), 0, "fail minFloor1")
        self.assertEqual(self.b2.getMinFloor(), -2, "fail minFloor2")
        self.assertEqual(self.b3.getMinFloor(), -5, "fail minFloor3")

    def test_max_floor(self):
        self.assertEqual(self.b1.getMaxFloor(), 10, "fail Maxfloor1")
        self.assertEqual(self.b2.getMaxFloor(), 15, "fail Maxfloor2")
        self.assertEqual(self.b3.getMaxFloor(), 18, "fail Maxfloor3")

    def test_NumofElev(self):
        self.assertEqual(self.b1.getNumofElevators(), 2, "fail numofElev1")
        self.assertEqual(self.b2.getNumofElevators(), 3, "fail numoofElev2")
        self.assertEqual(self.b3.getNumofElevators(), 4, "fail numofElev3")

    def test_getElevator(self):
        self.assertEqual(self.b1.getElevetor(0), 0, "fail getelev1")
        self.assertEqual(self.b2.getElevetor(1), 1, "fail getElev2")
        self.assertEqual(self.b3.getElevetor(2), 2, "fail getElev3")
