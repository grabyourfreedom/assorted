import os
import time
import configparser


def create_process(command_name, program_name, arguments, startup_delay,
                   daemon, restart_count, comment):
    args = arguments.split(",")
    args.insert(0, command_name)
    process = Process(command_name, program_name, args, int(startup_delay),
                      daemon, int(restart_count), comment)
    return process


class Process:
    def __init__(self, name, command, args, start_delay=0, daemon="no", restart_count=5, comment=""):
        self.name = name
        self.command = command
        self.args = args
        self.is_daemon = (daemon.lower() == "yes")
        self.start_delay = start_delay
        self.restart_count = restart_count
        self.comment = comment
        self.system_pid = 0
        self.fork_error = 0

    def fork_and_exec(self):
        retry = True
        fork_count = 0
        while retry:
            self.system_pid = os.fork()
            if self.system_pid == 0:
                time.sleep(self.start_delay)
                os.execv(self.command, self.args)
            elif self.system_pid > 0 or fork_count <= self.restart_count:
                retry = False
            else:
                fork_count += 1
                self.fork_error = self.system_pid

        return self.system_pid


class ProcessMonitorCfgReader:
    def __init__(self, filename):
        self.filename = filename
        self.processes = []

    def create_process_objs(self):
        config = configparser.ConfigParser()
        config.read(self.filename)

        for section in config.sections():
            command_name = config.get(section, 'command_name')
            program_name = config.get(section, 'program_name')
            arguments = config.get(section, 'arguments')
            startup_delay = config.get(section, 'startup_delay')
            restart_count = config.get(section, 'restart_count')
            comment = config.get(section, 'comment')
            daemon = config.get(section, 'daemon')
            process = create_process(command_name, program_name,
                                     arguments, startup_delay, daemon,
                                     restart_count, comment)
            self.processes.append(process)

        return self.processes


class ProcessMonitor:
    def __init__(self, cfg_file):
        self.processes = []
        self.cfg_file = cfg_file
        self.cfg_file_sections = []

    def load_processes(self):
        cfg_reader = ProcessMonitorCfgReader(self.cfg_file)
        self.processes = cfg_reader.create_process_objs()
        for process in self.processes:
            process.fork_and_exec()

    def check_process(self, status):
        print("Process Exited (PID - " + str(status[0]) + "; Status - " + str(status[1]) + ")")
        for process in self.processes:
            if process.system_pid == status[0] and process.is_daemon:
                print("Restarting the process again")
                process.fork_and_exec()
                return
            elif process.system_pid == status[0]:
                self.processes.remove(process)
                return
        return

    def monitor_process(self):
        retry = True
        while retry:
            try:
                status = os.wait()
                self.check_process(status)
            except ChildProcessError:
                print("All child processes exited, nothing to "
                      "be waited on")
                retry = False
        return


if __name__ == "__main__":
    CFG_FILE = "procmon_cfg_file"
    procmon = ProcessMonitor(CFG_FILE)
    procmon.load_processes()
    procmon.monitor_process()
