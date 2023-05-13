from datetime import datetime
from src.domain.ServiceResponse import *

def execute_call(caller, name, trace_id, writer, flow_name, date):

    service_response_builder =  ServiceResponseBuilder() \
            .with_name(name) \
            .with_trace_id(trace_id) \
            .with_date(date) \
            .with_writer(writer) \
            .with_flow_name(flow_name)
    try:
        service_response_caller = caller()
        service_response_builder = service_response_builder\
             .with_response(service_response_caller)

    except Exception as e:
         service_response_builder.with_response_text(e.args[0])
         print(e)

    service_response =service_response_builder.build()

    service_response.write()