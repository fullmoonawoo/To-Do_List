from datetime import datetime
from time import strftime


def refresh_progress(deadline):
    current_date = strftime("%Y/%m/%d")
    current_hour = strftime("%H")
    start = datetime.strptime(current_date, "%Y/%m/%d")
    start_hour = datetime.strptime(current_hour, "%H")
    end = datetime.strptime(deadline, "%Y/%m/%d")
    delta = (end - start).days * 24 - start_hour.hour
    return delta
