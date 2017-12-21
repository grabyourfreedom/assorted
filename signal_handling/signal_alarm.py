# A simple program to demonstrate alarm in python. This tiny code
# registers a signal/alarm handler that calls after set number
# of seconds repeatedly

import signal
import time
import os


timer_seconds = 5


# This is no different from signal handler. In this example, we are going to
# keep registering alarm until the program exits
def alarm_handler(number, stack):
    global timer_seconds
    print("Alarm - " + str(number) + "\n")
    set_alarm()


# This function takes the global variable "timer_seconds" and
# registers a handler
def set_alarm():
    global timer_seconds
    print("Setting alarm for " + str(timer_seconds) + " seconds")
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timer_seconds)


# Let us set an alarm once
set_alarm()

print("Process PID - " + str(os.getpid()))
while True:
    print("Sleeping for 5 seconds")
    time.sleep(5)

# This program never ends unless you kill or terminate
