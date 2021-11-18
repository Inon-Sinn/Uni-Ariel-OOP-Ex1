import unittest
from Classes.Elevator import Elevator as elv


class Elevator_test(unittest.TestCase):
    # Elevator(id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime)
    e1 = elv(1, 1, -5, 12, 2, 2, 2, 3)
    e2 = elv(2, 3, -10, 50, 1, 1, 1, 1)
    e3 = elv(3, 1.5, -3, 15, 3, 3, 2, 2)

    def test_get_id(self):
        self.assertEqual(self.e1.getID(), 1, "fail Id1")
        self.assertEqual(self.e2.getID(), 2, "fail Id2")
        self.assertEqual(self.e3.getID(), 3, "fail Id3")

    def test_get_speed(self):
        self.assertEqual(self.e1.getSpeed(), 1, "fail speed1")
        self.assertEqual(self.e2.getSpeed(), 3, "fail speed2")
        self.assertEqual(self.e3.getSpeed(), 1.5, "fail speed3")

    def test_get_min_floor(self):
        self.assertEqual(self.e1.getMinFloor(), -5, "fail minFloor1")
        self.assertEqual(self.e2.getMinFloor(), -10, "fail minFloor2")
        self.assertEqual(self.e3.getMinFloor(), -3, "fail minFloor3")

    def test_get_max_floor(self):
        self.assertEqual(self.e1.getMaxFloor(), 12, "fail Maxfloor1")
        self.assertEqual(self.e2.getMaxFloor(), 50, "fail Maxfloor2")
        self.assertEqual(self.e3.getMaxFloor(), 15, "fail Maxfloor3")

    def test_get_close_time(self):
        self.assertEqual(self.e1.getCloseTime(), 2.0, "fail closeTime1")
        self.assertEqual(self.e2.getCloseTime(), 1.0, "fail closeTime2")
        self.assertEqual(self.e3.getCloseTime(), 3.0, "fail closeTime3")

    def test_get_open_time(self):
        self.assertEqual(self.e1.getOpenTime(), 2.0, "fail openTime1")
        self.assertEqual(self.e2.getOpenTime(), 1.0, "fail openTime2")
        self.assertEqual(self.e3.getOpenTime(), 3.0, "fail openTime3")

    def test_get_stop_time(self):
        self.assertEqual(self.e1.getStartTime(), 2.0, "fail stopTime1")
        self.assertEqual(self.e2.getStartTime(), 1.0, "fail stopTime2")
        self.assertEqual(self.e3.getStartTime(), 2.0, "fail stopTime3")

    def test_get_start_time(self):
        self.assertEqual(self.e1.getStopTime(), 3.0, "fail startTime1")
        self.assertEqual(self.e2.getStopTime(), 1.0, "fail startTime2")
