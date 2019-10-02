import urllib.request
import urllib.parse
import urllib.error
import time
from datetime import datetime
from socket import timeout


def checkstate(url):
    state = "up"
    try:
        urllib.request.urlopen(url, timeout=1)
    except (urllib.error.URLError, timeout) as error:
        if isinstance(error.reason,timeout):
            print("timeout on: " + url)
            state="down"
        else:
            print("something else happened")
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
