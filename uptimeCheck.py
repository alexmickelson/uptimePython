#!/usr/bin/env python3
import urllib.request
import urllib.error as error
import urllib.parse
import urllib.error
import time
from datetime import datetime
from socket import timeout
import fileService
import stateModel


def checkSiteIsUp(url):
    state = True
    try:
        urllib.request.urlopen(url, timeout=1)
    except (error.HTTPError, error.URLError):
        state = False
    except timeout:
        state = False
    return state


def checkForStateChange(currentStatus, oldStatus):
    return currentStatus != oldStatus


def updateAndPersistState(state):
    state.updateRunningTime(datetime.now())
    fileService.writeFile("test.txt", state)
    print(state.getSummary())


def reinitializeDataInState(currentStatus):

    currentState = "up" if currentStatus else "down"
    return (currentStatus,
            stateModel.State(currentState=currentState,
                             startTime=datetime.now()))


if __name__ == "__main__":
    state = stateModel.State(currentState="up", startTime=datetime.now())
    oldStatus = True
    while True:
        currentStatus = checkSiteIsUp('https://google.com')
        if(checkForStateChange(currentStatus, oldStatus)):
            updateAndPersistState(state)
            (oldStatus, state) = reinitializeDataInState(currentStatus)
        time.sleep(1)
