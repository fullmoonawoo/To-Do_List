from datetime import datetime
from time import strftime, strptime


def refresh_progress(deadline):
    current_date = strftime("%Y/%m/%d")
    start = datetime.strptime(current_date, "%Y/%m/%d")
    end = datetime.strptime(deadline, "%Y/%m/%d")
    delta = (end - start)
    return delta.days * 24

result = refresh_progress("2023/6/21")
print(result)

#current_date = strftime("%Y/%m/%d")
#start = datetime.strptime(current_date, "%Y/%m/%d")
#end = datetime.strptime("2023/6/24", "%Y/%m/%d")


