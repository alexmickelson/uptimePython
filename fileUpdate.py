#!/usr/bin/env python3
import datetime


def openFile(file):
    try:
        f = open("logState.txt", "a+")
        return f
    except IOError:
        return None


def closeFile(file):
    file.close()


# We should get the state, start time, calculate the
# run time of the specific last item
def writeFile(file, oldState, currTime):
    file.write("State: " + oldState)
    file.read()
    calculateStateRunningTime(datetime.datetime)
    file.close()


def calculateStateRunningTime(startTime):
    return
