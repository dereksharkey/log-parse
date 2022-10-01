"""
The not efficient way
"""

import sys
import re

file_name = sys.argv[1]
file = open(file_name, 'r')
log_data = []
component = ['date', 'hostname', 'application', 'message']
log_match = r'^(?P<date>[A-z]{3}\s[0-9]{2}?\s[0-9]+:[0-9]+:[0-9]+)\s(?P<hostname>[0-z\-]+)\s(?P<application>[0-z\-]+)\[[0-9]+\]:\s(?P<message>.*)\s'

def uniquify(raw_list):
    """
    take a list and return only the unique items
    """
    unique_list = list(set(raw_list))

    return unique_list

def get_unique_applications(data):
    """
    take log data list and return the unique applications in the list
    """
    applications = [line['application'] for line in data]
    unique_applications = uniquify(applications)

    return unique_applications

def get_unique_logs_for_application(app, log_data):
    """
    take an application and log data list and return unique logs and repeat
    count for the application
    """
    logs_for_application = []
    count = []
    for line in log_data:
        if line['application'] == app:
            logs_for_application.append(line['message'])

    unique_logs = uniquify(logs_for_application)

    """
    This doesn't feel like the ideal way to do this for performance sake,
    but it was mentally fast to write
    """
    for ulog in unique_logs:
        repeat = 0
        for log in logs_for_application:
            if ulog == log:
                repeat = repeat + 1
        count.append(repeat)

    return unique_logs, count

"""
Loading log file into list
"""
for line in file.readlines():
    matches = re.finditer(log_match, line)
    for match in matches:
        structure = dict(zip(component, match.groups()))
        log_data.append(structure)

"""
Add an extra loop for processing one hour chunks to pull 'log_data' from new chunk
"""
unique_apps = get_unique_applications(log_data)
for app in unique_apps:
    print(app)
    all_logs,repeat_count = get_unique_logs_for_application(app, log_data)
    for (num, log) in zip(repeat_count, all_logs):
        print('\t' + str(num) + ' occurances:\t' + log)
