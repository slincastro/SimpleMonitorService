from src.managers.FlowManager import FlowManager
from src.infrastructure.configuration.Configuration import Configuration

flow_authentication_requested_name = 'authenticacion'
flow_funds_requested_name = 'fondos_inversion'
non_existing_flow_requested_name = 'nonExistingFlow'


def get_configuration():
    return Configuration("./test/test_monitor_config.yml")

def test_should_get_names_of_steps_when_flow_name_is_send():

    configuration = get_configuration()
    step_name = FlowManager(flow_authentication_requested_name, configuration).get_names()

    assert step_name == ["auth"]

def test_should_two_names_when_flow_name_is_send():
    configuration = get_configuration()
    service_type = FlowManager(flow_funds_requested_name, configuration).get_names()

    assert service_type == ["auth","funds"]

def test_should_get_type_when_non_existing_flow_name_is_send():
    configuration = get_configuration()
    service_type = FlowManager(non_existing_flow_requested_name, configuration).get_names()

    assert service_type == []

def test_should_get_callers_when_funds_name_is_sent():
    configuration = get_configuration()
    service_caller = FlowManager(flow_funds_requested_name,configuration).get_callers()
    assert service_caller == ['Requests.authorization_requests_caller', 'src.infrastructure.funds_request_caller']

def test_should_get_callers_when_auth_name_is_sent():
    configuration = get_configuration()
    service_caller = FlowManager(flow_authentication_requested_name,configuration).get_callers()
    assert service_caller == ['Requests.authorization_requests_caller']

def test_should_get_empty_array_caller_when_non_existing_name_is_sent():
    configuration = get_configuration()
    service_caller = FlowManager(non_existing_flow_requested_name,configuration).get_callers()

    assert service_caller == []

def test_should_get_name_and_caller():
    configuration = get_configuration()
    services = FlowManager(flow_authentication_requested_name, configuration).get_services()
    assert "auth" in services
    assert len(services) == 1
    assert services.get('auth') == 'Requests.authorization_requests_caller'

