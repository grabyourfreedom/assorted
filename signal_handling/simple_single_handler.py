# This program demonstrate how to write a signal handler in Python
# (and how simple it is to implement one in Python)
# Tested in Linux (Ubuntu, and should work in any Linux/Unix)
import signal
import time
import os
import sys
import traceback


# This is the function that gets called when "SIGUSR1" is received.
# In this case, we do trivial thing like printing something and
# exiting the script. But you can do non-trivial thing too
# You will receive a signal number that you registered for
# and the stack frames
def signal_handler_simple(number, stack):
    print("Received Signal", number)
    # Let us print the stack frames
    traceback.print_stack(stack)
    sys.exit(1)


# Another handler function just to show you can create one more
def signal_handler_another_one(number, stack):
    print("Received another signal, calling a different handler",
          number)
    traceback.print_stack(stack)
    sys.exit(1)


# This function registers with signal number and the corresponding
# handler
def register_signals():
    signal.signal(signal.SIGUSR1, signal_handler_simple)
    signal.signal(signal.SIGUSR2, signal_handler_another_one)


# Simple driver that keeps the scripting running until someone sends a
# signal to us using kill (or equivalent)
def run():
    while True:
        print("Waiting to be toasted - ", os.getpid())
        time.sleep(5)


# Put them in burner
register_signals()
run()

# Run this program, get the process id that gets printed in the console
# Open a shell and run one of the following commands
# kill -<signal_number> <pid>
# Ex 1: kill -USR1 3411
# Ex 2: kill -USR2 3411
