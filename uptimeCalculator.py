#!/usr/bin/env python3

import fileService


# class calculator():
#     def __init__(self, stateCollection: List):
#         self.stateCollection = stateCollection
#         self.addLastState()

#     def calculateLastState(self, lastRecordedState):
#         currentState = "up" \
#             if lastRecordedState.currentState == "down" \
#             else "down"
#         dateTimeDifference = datetime.now() - lastRecordedState.startTime
#         currentDurration = \
#             int(dateTimeDifference.total_seconds()) \
#             - lastRecordedState.totalTimeInSeconds
#         return stateModel.State(currentState=currentState,
#                                 startTime=None,
#                                 durationInSeconds=currentDurration)

# def addLastState(self):
#     lastRecordedState = self.stateCollection[len(self.stateCollection)-1]
#     lastState = self.calculateLastState(lastRecordedState)
#     self.stateCollection.append(lastState)

def aggregateUptime(stateCollection):
    uptimeSum = 0
    downtimeSum = 0
    for state in stateCollection:
        if state.currentState == "up":
            uptimeSum += state.totalTimeInSeconds
        elif state.currentState == "down":
            downtimeSum += state.totalTimeInSeconds
    return (uptimeSum, downtimeSum)


def uptime(stateCollection):
    (uptimeSum, downtimeSum) = aggregateUptime(stateCollection)
    return uptimeSum / (uptimeSum + downtimeSum)


if __name__ == '__main__':
    stateCollection = fileService.getRecordedStates("test.txt")
    print("Uptime: " + str(uptime(stateCollection)))
