#!/usr/bin/env python3
import unittest
import stateModel
from datetime import datetime


class CheckFileTest(unittest.TestCase):

    def test_constructorUpdates(self):
        startTime = datetime(year=1995, month=4, day=15,
                             hour=12, minute=2, second=5)

        state = stateModel.State(currentState="up",
                                 startTime=startTime)

        self.assertEqual(state.currentState, "up")
        self.assertEqual(state.startTime, startTime)
        self.assertEqual(state.totalTimeInSeconds, 0)

    def test_updateRunningTimeSecondTest(self):
        startTime = datetime(year=1995, month=4, day=15,
                             hour=12, minute=2, second=5)

        state = stateModel.State(currentState="up",
                                 startTime=startTime)

        offsetTime = datetime(year=1995, month=4, day=15,
                              hour=12, minute=2, second=11)

        state.updateRunningTime(offsetTime)

        self.assertEqual(state.totalTimeInSeconds, 6)

    def test_updateRunningTimeMinuteTest(self):
        startTime = datetime(year=1995, month=4, day=15,
                             hour=12, minute=2, second=5)

        state = stateModel.State(currentState="up",
                                 startTime=startTime)

        offsetTime = datetime(year=1995, month=4, day=15,
                              hour=12, minute=3, second=11)

        state.updateRunningTime(offsetTime)

        self.assertEqual(state.totalTimeInSeconds, 66)

    def test_updateRunningTimeYearTest(self):
        startTime = datetime(year=1995, month=4, day=15,
                             hour=12, minute=2, second=5)

        state = stateModel.State(currentState="up",
                                 startTime=startTime)

        offsetTime = datetime(year=1996, month=4, day=15,
                              hour=12, minute=2, second=11)

        state.updateRunningTime(offsetTime)

        self.assertEqual(state.totalTimeInSeconds, 31622406)

    def test_printStateSummary(self):
        startTime = datetime(year=1995, month=4, day=15,
                             hour=12, minute=2, second=5)

        state = stateModel.State(currentState="up",
                                 startTime=startTime)
        actualSummary = state.getSummary()
        expectedSummary = "State: up; TimeInSeconds: 0; StartTime: 1995-04-15T12:02:05"
        self.assertEqual(actualSummary, expectedSummary)


if __name__ == "__main__":
    unittest.main()
