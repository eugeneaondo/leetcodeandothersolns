# read log file and calculate time taken for each process and overall average

logfile = "log.txt"


def readlog(logfile):
    process_dict = {}

    with open(logfile, "r") as file:
        for line in file:
            components = line.strip().split()

            timestamp = components[0]
            process_name = components[1]
            action = components[2]

            if process_name not in process_dict:
                process_dict[process_name] = {}

            process_dict[process_name][action] = timestamp

    return process_dict


def calculate_process_time(process_dict):
    process_times = {}
    for process_name, actions in process_dict:
        if 'start' in actions and 'stop' in actions:
            start_time = actions['start']
            stop_time = actions['stop']
            process_time = stop_time - start_time
            process_times[process_name] = process_time

    return process_time


def calculate_average_process_time(process_times):
    if not process_times:
        return None
    
    total_time = sum(process_times.values())
    number_of_processes = len(process_times)
    average_time = total_time/number_of_processes

    return average_time






