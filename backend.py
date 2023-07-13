from datetime import datetime, timedelta
from time import strftime


def refresh_progress(deadline):
    current_date = strftime("%Y/%m/%d %H:%M")
    start = datetime.strptime(current_date, "%Y/%m/%d %H:%M")
    end = datetime.strptime(deadline, "%Y/%m/%d")
    end += timedelta(hours=12)
    delta_days = (end - start).days
    delta_hours = (end - start).seconds / 86400
    delta = delta_days + delta_hours
    return delta
