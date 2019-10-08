#!/usr/bin/env python3
"""
    States are stored with their current state, total time in seconds
    and start time, to calculate our total uptime
    #datetime.fromtimestamp(1485714600).strftime("%A, %B %d, %Y %I:%M:%S")
"""
from datetime import datetime


class State:
    def __init__(self,
                 currentState: str,
                 startTime: datetime,
                 durationInSeconds=0):
        self.currentState = currentState
        self.totalTimeInSeconds = durationInSeconds
        self.startTime = startTime

    def updateRunningTime(self, offsetTime: datetime):
        offset = offsetTime - self.startTime
        self.totalTimeInSeconds = int(offset.total_seconds())

    def getSummary(self):
        response = ""
        response += "State: " + self.currentState + "; "
        response += "TimeInSeconds: " + str(self.totalTimeInSeconds) + "; "
        response += "StartTime: " + self.startTime.isoformat()
        return response
