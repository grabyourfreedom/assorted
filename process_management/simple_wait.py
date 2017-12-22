# Let us use couple of functions we developed in other modules and see
# what happens when a child dies before a parent and how to clean-up

import os
import time
from simple_fork import create_process
from simple_exec import overlay_program


# This function simply uses waits to retrieve the status of child
# When os.wait() is not used by parent (and if the parent is running),
# the operating system is going to wait for the parent to collect the
# status.
#
# Try commenting the line status = os.wait and run the program for a minutes
# You will see a defuct processes.
def get_status():
    time.sleep(15)
    status = os.wait()
    return status


# Note: This program never ends until you exit using control + c or forcefully
# terminate using kill
if __name__ == "__main__":
    command = "/bin/ls"
    args = ['ls', '-la']

    while True:
        # create a child process
        pid = create_process()
        if pid > 0:
            # Collect the status as this block is executed by parent
            get_status()
        elif pid == 0:
            # sleep for a while and exec the command "ls"
            time.sleep(10)
            overlay_program(command, args)
        elif pid == -1:
            print("Error while creating process")

    print("Exiting")