def in_secs(minutes):
    return minutes * 60

def get_range_time(hours_to_monitor, sleep_time):
    return (hours_to_monitor * 60 * 60)/ sleep_time