import os


# This oneliner function overlays the command that is passed
# and starts executing from the beginning of the new program
# The process ID remains the same as it overlays in the same
# process space
def overlay_program(cmd, args):
    os.execv(cmd, args)


if __name__ == "__main__":
    # This is command with absolute path - program name
    command = "/bin/ls"

    # List of arguments that goes to program. The first program is
    # the name of the process (command in ps) that gets displayed
    # when you run ps command
    args = ['ls', '-la']
    overlay_program(command, args)
