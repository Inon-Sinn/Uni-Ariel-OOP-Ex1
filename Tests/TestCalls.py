import unittest
from Classes.CallforElevator import CallforElevator as call


class CallTest(unittest.TestCase):
    # CallForElevator(time, src, dest, state, allocatedTo, id)
    c0 = call(9.0, 0, 2, 0, -1)
    c1 = call(15.2, 1, -1, 0, -1)
    c2 = call(16.83, -3, 8, 0, -1)

    def test_get_start_time(self):
        self.assertEqual(self.c0.getTime(), 9.0, "fail getStartTime0")
        self.assertEqual(self.c1.getTime(), 15.2, "fail getStartTime1")
        self.assertEqual(self.c2.getTime(), 16.83, "fail getStartTime2")

    def test_get_src(self):
        self.assertEqual(self.c0.getSource(), 0, "fail getSrc0")
        self.assertEqual(self.c1.getSource(), 1, "fail getSrc1")
        self.assertEqual(self.c2.getSource(), -3, "fail getSrc2")

    def test_get_dest(self):
        self.assertEqual(self.c0.getDestination(), 2, "fail getDest0")
        self.assertEqual(self.c1.getDestination(), -1, "fail getDest1")
        self.assertEqual(self.c2.getDestination(), 8, "fail getDest2")

    def test_get_state(self):
        self.assertEqual(self.c0.getState(), 0, "fail getState0")
        self.c1.state = 1
        self.assertEqual(self.c1.getState(), 1, "fail getState1")
        self.c2.state = 2
        self.assertEqual(self.c2.getState(), 2, "fail getState2")
        self.c2.state = 3

    def test_get_type(self):
        self.assertEqual(self.c0.getType(), 1, "fail getType0")
        self.assertEqual(self.c1.getType(), -1, "fail getType1")
        self.assertEqual(self.c2.getType(), 1, "fail getType2")

    def test_get_allocated_to(self):
        self.assertEqual(self.c0.getAllocation(), -1, "fail getAllocated0")
        self.assertEqual(self.c1.getAllocation(), -1, "fail getAllocated1")
        self.assertEqual(self.c1.getAllocation(), 0, "fail getAllocated1.1")
