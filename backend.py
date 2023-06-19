from datetime import datetime
from time import strftime


def refresh_progress(deadline):
    current_date = strftime("%Y/%m/%d")
    current_hour = strftime("%H")
    start = datetime.strptime(current_date, "%Y/%m/%d")
    start_hour = datetime.strptime(current_hour, "%H")
    print(start_hour.hour, "start_hour")
    end = datetime.strptime(deadline, "%Y/%m/%d")
    delta = (end - start)
    result = delta.days * 24 + start_hour.hour
    return result
