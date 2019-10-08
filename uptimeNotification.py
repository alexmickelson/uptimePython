#!/usr/bin/env python3
import smtplib


def sendEmail(uptime: str):
    print("Uptime: " + uptime)
    print("send smtp Request here")
    # sends but gets blocked by spam (local smtp in docker)
    try:
        server = smtplib.SMTP('localhost')
        server.sendmail(
            from_addr="test@localhost.com",
            to_addrs=['alexmickelson96@gmail.com'],
            msg="Service is down!!!")
        print("sent Mail")
    except Exception as e:
        print(e)


if __name__ == '__main__':

    sendEmail()
