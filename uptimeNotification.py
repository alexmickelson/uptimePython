#!/usr/bin/env python3

import uptimeCalculator
import fileService
import smtplib


def sendEmail():
    stateCollection = fileService.getRecordedStates("test.txt")
    myCalculator = uptimeCalculator.calculator(stateCollection)
    print("Uptime: " + str(myCalculator.uptime()))
    print("send smtp Request here")
    # sends but gets blocked by spam (local smtp in docker)
    try:
        server = smtplib.SMTP('localhost')
        server.sendmail(
            from_addr="test@localhost.com",
            to_addrs=['alexmickelson96@gmail.com'],
            msg="test")
        print("sent Mail")
    except Exception as e:
        print(e)


if __name__ == '__main__':

    sendEmail()
