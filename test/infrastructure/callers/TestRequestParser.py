
import pytest
import pytest_cov
import json
from unittest.mock import MagicMock

from src.infrastructure.callers import request_parser

def test_should_get_token_from_request():

    response = MagicMock()
    response.status_code = 200
    response.json.return_value = json.loads('{"data" : { "accessToken" : "abcdefg" }}')
    token = request_parser.get_authorization_token(response)

    assert token == "abcdefg"

def test_should_get_empty_token_from_request_without_token():

    response = MagicMock()
    response.json.return_value = json.loads('{"data" : { "NoAccessToken" : "abcdefg" }}')
    token = request_parser.get_authorization_token(response)

    assert token == ""

def test_should_get_empty_token_from_request_without_data():

    response = MagicMock()
    response.status_code = 200
    response.json.return_value = json.loads('{"NoData" : { "NoAccessToken" : "abcdefg" }}')
    token = request_parser.get_authorization_token(response)

    assert token == ""

def test_should_get_empty_token_when_request_is_not_ok():
    response = MagicMock()
    response.status_code = 500
    token = request_parser.get_authorization_token(response)

    assert token == ""

def test_should_get_sesscookie():
    response = '<TCFX><HEADERRS SESSCOOKIE="12345678"/></TCFX>'
    sess_cookie = request_parser.get_sesscookie(response)

    assert sess_cookie == '12345678'

def test_should_get_status_code():
    response = '<TCFX><HEADERRS SESSCOOKIE="12345678"><STATUS CODE="000"/></HEADERRS></TCFX>'
    code = request_parser.get_status_code(response)

    assert code == "000"