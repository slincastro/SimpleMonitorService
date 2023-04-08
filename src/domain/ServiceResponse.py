
class ServiceResponse:
    def __init__(self, flow_name,response, name, trace_id, date, writer, status_code, time_to_response, response_text):
        self.flow_name = flow_name
        self.response = response
        self.name = name
        self.trace_id = trace_id
        self.date = date
        self.writer = writer
        self.status_code = status_code
        self.time_to_response = time_to_response
        self.response_text = response_text

    def get_in_array_format(self):
        return [self.flow_name, self.name,self.date, self.trace_id, self.status_code, self.time_to_response, self.response_text]

    def write(self):
       self.writer(self.get_in_array_format())


class ServiceResponseBuilder:
    def __init__(self):
        self.flow_name = None
        self.response = None
        self.name = None
        self.trace_id = None
        self.date = None
        self.writer = None
        self.status_code = 0
        self.time_to_response = 100
        self.response_text = None

    def with_flow_name(self, flow_name):
        self.flow_name = flow_name
        return self

    def with_response(self, response):
        self.response = response
        self.status_code = response.status_code
        self.time_to_response = response.elapsed.total_seconds()
        self.response_text = response.text
        return self

    def with_name(self, name):
        self.name = name
        return self

    def with_trace_id(self, trace_id):
        self.trace_id = trace_id
        return self

    def with_date(self, date):
        self.date = date
        return self

    def with_writer(self, writer):
        self.writer = writer
        return self

    def with_response_text(self, self_text):
        self.response_text = self_text
        return self

    def build(self):
        return ServiceResponse(self.flow_name, self.response, self.name, self.trace_id, self.date, self.writer, self.status_code, self.time_to_response, self.response_text)