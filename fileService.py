#!/usr/bin/env python3
"""
this is a file handling module for uptimeCheck
"""
import re
import stateModel
from datetime import datetime


def writeFile(filePath, state):
    """
    We should get the state, start time, calculate the
    run time of the specific last item
    """
    file = open(filePath, "a+")
    file.write(state.getSummary() + "\n")
    file.close()


def printFile(filePath):
    file = open(filePath, "a+")
    print(file)
    file.close()


def getRecordedStates(filePath):
    file = open(filePath, "r")
    lines = file.readlines()
    states = list()
    for line in lines:
        stateVar = re.match(
            r'State: (.*); TimeInSeconds: (.*); StartTime: (.*)$',
            line, re.M | re.I)
        startTime = datetime.fromisoformat(stateVar.group(3))
        states.append(stateModel.State(
            currentState=stateVar.group(1),
            startTime=startTime,
            durationInSeconds=int(stateVar.group(2))))
    return states


if __name__ == "__main__":
    printFile("test.txt")
