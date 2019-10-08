#!/usr/bin/env python3

import uptimeCalculator
import fileService


def sendEmail():
    stateCollection = fileService.getRecordedStates("test.txt")
    myCalculator = uptimeCalculator.calculator(stateCollection)
    print("Uptime: " + str(myCalculator.uptime()))
    print("send smtp Request here")


if __name__ == '__main__':
    sendEmail()
