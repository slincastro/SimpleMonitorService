
class ServiceResponse:
    def __init__(self, response, name, trace_id, date, writer):
        self.response = response
        self.name = name
        self.trace_id = trace_id
        self.date = date
        self.writer = writer

    def get_in_array_format(self):
        return [self.name,self.date, self.trace_id, self.response.status_code, self.response.elapsed.total_seconds(), self.response.text]

    def write(self):
       self.writer(self.get_in_array_format())

class ServiceResponseBuilder:
    def __init__(self):
        self.response = None
        self.name = None
        self.trace_id = None
        self.date = None
        self.writer = None

    def with_response(self, response):
        self.response = response
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

    def build(self):
        return ServiceResponse(self.response, self.name, self.trace_id, self.date, self.writer)