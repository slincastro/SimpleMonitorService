import pytest
import pytest_cov
from unittest.mock import MagicMock

from src.domain.ServiceResponse import *

def test_should_create_response_object():
    response = MagicMock()
    response.status_code = 200
    response.text=""
    expectedResponse = ServiceResponseBuilder()\
        .with_response(response)\
        .with_name("auth")\
        .with_trace_id("6B29FC40-CA47-1067-B31D-00DD010662DA")\
        .with_date("22/22/2022")\
        .with_writer("something")\
        .build()

    assert expectedResponse.response is not None
    assert expectedResponse.name == "auth"
    assert expectedResponse.trace_id == "6B29FC40-CA47-1067-B31D-00DD010662DA"
    assert expectedResponse.date == "22/22/2022"
    assert expectedResponse.writer is not None

def test_should_get_array_format():
    response = MagicMock()
    response.status_code = 200
    elapsed = MagicMock()
    elapsed.total_seconds.return_value = 2.5
    response.elapsed = elapsed
    response.text = ""

    response = ServiceResponseBuilder()\
        .with_flow_name("autenticacion")\
        .with_response(response)\
        .with_name("auth")\
        .with_trace_id("6B29FC40-CA47-1067-B31D-00DD010662DA") \
        .with_date("22/22/2022") \
        .build()
    array_response = response.get_in_array_format()

    assert array_response == ["autenticacion","auth","22/22/2022","6B29FC40-CA47-1067-B31D-00DD010662DA" , 200  , 2.5, ""]

def test_should_write_request_data(capsys):
    response = MagicMock()
    response.status_code = 200
    elapsed = MagicMock()
    elapsed.total_seconds.return_value = 2.5
    response.elapsed = elapsed
    response.text = ""

    response = ServiceResponseBuilder().with_response(response) \
        .with_flow_name("autenticacion") \
        .with_name("auth")\
        .with_trace_id("6B29FC40-CA47-1067-B31D-00DD010662DA") \
        .with_date("22/22/2022") \
        .with_writer(writer_test)\
        .build()

    response.write()
    captured = capsys.readouterr()

    assert captured.out == "['autenticacion', 'auth', '22/22/2022', '6B29FC40-CA47-1067-B31D-00DD010662DA', 200, 2.5, '']\n"

def test_should_write_failed_request_data(capsys):
    response = ServiceResponseBuilder() \
        .with_flow_name("autenticacion") \
        .with_name("auth") \
        .with_trace_id("6B29FC40-CA47-1067-B31D-00DD010662DA") \
        .with_date("22/22/2022") \
        .with_writer(writer_test) \
        .with_response_text('request error')\
        .build()

    response.write()
    captured = capsys.readouterr()

    assert captured.out == "['autenticacion', 'auth', '22/22/2022', '6B29FC40-CA47-1067-B31D-00DD010662DA', 0, 100, 'request error']\n"

def writer_test(data_row):
    print(data_row)