import pytest
import pytest_cov
from unittest.mock import MagicMock
from src.use_cases import call_services

def test_should_write_success_response(capsys):

    trace_id = '6B29FC40-CA47-1067-B31D-00DD010662DA'
    call_services.execute_call(caller_test, "auth" , trace_id, writer_test, "autenticacion", "22/22/2022")
    captured = capsys.readouterr()

    assert captured.out == ("['autenticacion', 'auth', '22/22/2022', '%s', 200, 2.5, '']\n" % trace_id)

def test_should_write_failed_response(capsys):
    trace_id = '6B29FC40-CA47-1067-B31D-00DD010662DA'
    call_services.execute_call(failed_caller_test, "auth", trace_id, writer_test, "autenticacion", "22/22/2022")
    captured = capsys.readouterr()

    assert captured.out == "['autenticacion', 'auth', '22/22/2022', '6B29FC40-CA47-1067-B31D-00DD010662DA', 0, 100, 'request error']\n"

def caller_test():
    response = MagicMock()
    response.status_code = 200
    elapsed = MagicMock()
    elapsed.total_seconds.return_value = 2.5
    response.elapsed = elapsed
    response.text = ""

    return response

def failed_caller_test():
    raise ValueError("request error")

def writer_test(data_row):
    print(data_row)