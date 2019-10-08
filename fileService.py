#!/usr/bin/env python3
"""
this is a file handling module for uptimeCheck
"""


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


if __name__ == "__main__":
    printFile("test.txt")
