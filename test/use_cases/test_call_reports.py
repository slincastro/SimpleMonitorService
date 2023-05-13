import pytest
import pytest_cov
from src.use_cases import call_reports

def test_should_get_specific_workflow():
    data = call_reports.get_intermittence_time("test/service_data_test.csv")
    