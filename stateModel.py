#!/usr/bin/env python3
"""
    States are stored with their current state, total time in seconds
    and start time, to calculate our total uptime
"""
import datetime


class State:
    def __init__(self,
                 currentState: str,
                 totalTimeInSeconds: int,
                 startTime: datetime.datetime):
        self.currentState = currentState
        self.totalTimeInSeconds = totalTimeInSeconds
        self.startTime = startTime
