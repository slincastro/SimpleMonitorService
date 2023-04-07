from datetime import datetime
from src.repositories import csv_writer
from src.managers import time_manager
from src.infrastructure.configuration.Configuration import Configuration
from src.managers.FlowManager import FlowManager
from src.domain.ServiceResponse import *
from pydoc import locate
import time
import uuid

def load_data(service_name, service_caller, trace_id):
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    service_response = service_caller.get_request_direct_service()
    service_request = ServiceResponseBuilder()\
        .with_name(service_name)\
        .with_trace_id(trace_id)\
        .with_response(service_response)\
        .with_date(date)\
        .with_writer(csv_writer.write_data_row)\
        .build()

    service_request.write()


configuration = Configuration("monitor_config.yml")
number_of_hours_to_monitor = configuration.get_configuration("hoursToMonitor")
delay_time = configuration.get_configuration("delayTimeInMinutes")

service_name_to_monitor = "authenticacion"
service_callers_reference = FlowManager(service_name_to_monitor, configuration).get_services()

sleep_time = time_manager.in_secs(delay_time)
range_time = time_manager.get_range_time(number_of_hours_to_monitor, sleep_time)

for i in range(int(range_time)):
    time.sleep(sleep_time)
    guid = uuid.uuid4().hex
    for service_name in service_callers_reference:
        service_caller_ref = service_callers_reference[service_name]
        service_caller = locate(service_caller_ref)
        load_data(service_name, service_caller, guid)

    print("------------------- Request # " + str(i+1) + " Completed -------------- ")
