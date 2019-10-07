#!/usr/bin/env python3
"""
this is a file handling module for uptimeCheck
"""
import datetime


def writeFile(file, oldState, currTime):
    """
    We should get the state, start time, calculate the
    run time of the specific last item
    """
    file.write("State: " + oldState)
    file.read()
    calculateStateRunningTime(datetime.datetime)
    file.close()


def calculateStateRunningTime(startTime):
    return


if __name__ == "__main__":
    pass
