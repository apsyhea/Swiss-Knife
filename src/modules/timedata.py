import datetime


def get_data() -> datetime:
    tz_offset = datetime.timedelta(seconds=10800)
    utc_time = datetime.datetime.utcnow()
    local_time = utc_time + tz_offset
    return local_time
