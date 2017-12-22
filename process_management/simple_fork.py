# This is a simple program that creates a new process using fork in Python.
# There is nothing complex here if you already did something like this in
# C/C++. This code just shows how this can be done in Python though

import os


# This is the only function in this file that create a new process
def create_process():
    print("Creating a process. My PID is - " + str(os.getpid()))

    # os.fork creates a new process
    pid = os.fork()

    # This is error condition that we are not able to create
    # new process for some reason.
    # The success condition create another process and
    # the value returned is different. Refer fork documentation
    #
    if pid == -1:
        print("Error creating process")
    elif pid > 0:
        print("This is the parent. PID - " + str(os.getpid())
              + "; Parent PID - " + str(os.getppid()))
    elif pid == 0:
        print("This is the child process. PID - " + str(os.getpid())
              + "; Parent PID - " + str(os.getppid()))

    return pid


if __name__ == "__main__":
    process_id = create_process()
