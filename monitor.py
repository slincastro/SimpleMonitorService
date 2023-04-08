from datetime import datetime
from src.repositories import csv_writer
from src.managers import time_manager
from src.infrastructure.configuration.Configuration import Configuration
from src.managers.FlowManager import FlowManager
from src.domain.ServiceResponse import *
from pydoc import locate
import time
import uuid

def execute_call(caller, name, trace_id):
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    service_response_builder =  ServiceResponseBuilder() \
            .with_name(name) \
            .with_trace_id(trace_id) \
            .with_date(date) \
            .with_writer(csv_writer.write_data_row)
    try:
        service_response_caller = caller()
        service_response_builder = service_response_builder\
             .with_response(service_response_caller)

    except Exception as e:
         service_response_builder.with_response_text(e)

    service_response =service_response_builder.build()

    service_response.write()

configuration = Configuration("monitor_config.yml")
number_of_hours_to_monitor = configuration.get_configuration("hoursToMonitor")
delay_time = configuration.get_configuration("delayTimeInMinutes")

service_name_to_monitor = "deposito-legado"
service_callers_reference = FlowManager(service_name_to_monitor, configuration).get_services()

sleep_time = time_manager.in_secs(delay_time)
range_time = time_manager.get_range_time(number_of_hours_to_monitor, sleep_time)

for i in range(int(range_time)):
    time.sleep(sleep_time)
    guid = uuid.uuid4().hex
    for service_name in service_callers_reference:
        service_caller_ref = service_callers_reference[service_name]
        service_caller = locate(service_caller_ref)
        execute_call(service_caller,service_name, guid)

    print("------------------- Request # " + str(i+1) + " Completed -------------- ")
