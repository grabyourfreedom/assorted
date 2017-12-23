# This is a simple program to demonstrate os.exit. But it is
# always advisable to call system.exit
import os
import time


def exit_program():
    print("Calling exit")
    os._exit(1)
    print("This will never get printed")


if __name__ == "__main__":
    process = os.fork()
    if process == 0:
        print("This is the child process, let us exit the child "
              "process after 10 seconds")
        time.sleep(10)
        exit_program()
    elif process > 0:
        status = os.wait()
        # The following has to be printed after 10 seconds as child
        # waits for 10 seconds before exiting
        print("Status returned = " + str(status))

# The status is the tuple that has two entries - PID and exit
# status exit status contains information on signal that
# terminated the program and actual exit status
