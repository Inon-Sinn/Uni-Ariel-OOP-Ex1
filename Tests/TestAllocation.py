import unittest
from Classes.Allocation import Allocation as alc
from Classes.CallforElevator import CallforElevator as cl
from Classes.Elevator import Elevator as elv
from Classes.Building import Building as bld
from Classes.Block import Block as blk
from Classes.Allocation import add


class AllocationTest(unittest.TestCase):
    c1 = cl(11.2, 0, -1, 0, -1)
    c2 = cl(15.0, 1, 2, 0, -1)
    c3 = cl(18.44, 7, 10, 0, -1)
    call_list = [c1, c2, c3]

    e1 = elv(1, 1, -5, 12, 2, 2, 2, 3)
    b1 = bld(0, 10, [e1])

    Alc = alc(b1, call_list)
    block_list = [blk()]

    # i am not sure how to test static function through test

    def test_add(self, c1: cl, block_list: list, e1: int):
        self.assertEqual(self.Alc.add(c1, block_list, e1), "true")

    def test_update_list(self, place, block_list, time, speed):
        self.assertEqual(self.Alc.update_list(block_list, time, speed), "true")
