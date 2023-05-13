from datetime import datetime
from src.repositories import csv_writer
from src.managers import time_manager
from src.infrastructure.configuration.Configuration import Configuration
from src.managers.FlowManager import FlowManager
from pydoc import locate
from src.use_cases import call_services
import time
import uuid

# configuration = Configuration("monitor_config.yml")
# number_of_hours_to_monitor = configuration.get_configuration("hoursToMonitor")
# delay_time = configuration.get_configuration("delayTimeInMinutes")
#
# service_name_to_monitor = "authenticacion"
# service_callers_reference = FlowManager(service_name_to_monitor, configuration).get_services()
#
# sleep_time = time_manager.in_secs(delay_time)
# range_time = time_manager.get_range_time(number_of_hours_to_monitor, sleep_time)
# print(service_callers_reference)
# for i in range(int(range_time)):
#     time.sleep(sleep_time)
#     guid = uuid.uuid4().hex
#     for service_name in service_callers_reference:
#         now = datetime.now()
#         date = now.strftime("%d/%m/%Y %H:%M:%S")
#         service_caller_ref = service_callers_reference[service_name]
#         service_caller = locate(service_caller_ref)
#         call_services.execute_call(service_caller, service_name, guid, csv_writer.write_data_row, service_name_to_monitor, date)
#     print("------------------- Request # " + str(i+1) + " Completed -------------- ")
#
# configuration = Configuration("monitor_config.yml")
# number_of_hours_to_monitor = configuration.get_configuration("hoursToMonitor")
# delay_time = configuration.get_configuration("delayTimeInMinutes")
#
# service_name_to_monitor = "authenticacion"
# service_callers_reference = FlowManager(service_name_to_monitor, configuration).get_services()

def monitor(service_to_monitor):
    configuration = Configuration("monitor_config.yml")
    number_of_hours_to_monitor = configuration.get_configuration("hoursToMonitor")
    delay_time = configuration.get_configuration("delayTimeInMinutes")

    service_name_to_monitor = service_to_monitor
    service_callers_reference = FlowManager(service_name_to_monitor, configuration).get_services()

    sleep_time = time_manager.in_secs(delay_time)
    range_time = time_manager.get_range_time(number_of_hours_to_monitor, sleep_time)
    print(service_callers_reference)
    for i in range(int(range_time)):
        time.sleep(sleep_time)
        guid = uuid.uuid4().hex
        for service_name in service_callers_reference:
            now = datetime.now()
            date = now.strftime("%d/%m/%Y %H:%M:%S")
            service_caller_ref = service_callers_reference[service_name]
            service_caller = locate(service_caller_ref)
            call_services.execute_call(service_caller, service_name, guid, csv_writer.write_data_row, service_name_to_monitor, date)
        print("------------------- Request # " + str(i+1) + " Completed -------------- ")