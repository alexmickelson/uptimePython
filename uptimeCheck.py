#!/usr/bin/env python3
import urllib.request
import urllib.error as error
import urllib.parse
import urllib.error
import time
from datetime import datetime
from socket import timeout


def checkstate(url):
    state = "up"
    try:
        urllib.request.urlopen(url, timeout=1)
    except (error.HTTPError, error.URLError):
        print('Data not retrieved because %s\nURL: %s', error, url)
        state = "down"
    except timeout:
        print("timeout occured " + url)
        state = "down"
    return state


def getStateChange(state, lastState):
    now = datetime.now()
    if (state != lastState):
        return "New State: " + state + " Time: " + str(now)


if __name__ == "__main__":
    lastState = ""
    while True:
        state = checkstate('https://google.com')
        print(getStateChange(state, lastState))
        lastState = state
        time.sleep(1)
