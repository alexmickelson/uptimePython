#!/usr/bin/env python3
import unittest
import stateModel
import datetime


class CheckFileTest(unittest.TestCase):

    def test_updateCurrentState(self):
        startTime2 = datetime.datetime(year=1995, month=4, day=15,
                                       hour=12, minute=2, second=5)
        state = stateModel(currentState="up",
                           totalTimeInSeconds=0,
                           startTime=startTime2)
        return state


if __name__ == "__main__":
    unittest.main()
