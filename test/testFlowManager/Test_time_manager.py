import pytest
import pytest_cov

from src.managers import time_manager

def test_should_get_60_secs_from_1_minute():
    in_secs = time_manager.in_secs(1)
    assert in_secs == 60

def test_should_get_range_time_from_hours_to_monitor():
    range_time = time_manager.get_range_time(8,1)
    assert range_time == 28800.0