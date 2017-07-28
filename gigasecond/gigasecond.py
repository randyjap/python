import datetime

def add_gigasecond(time):
    gigasecond = time + datetime.timedelta(0, 10**9)
    return gigasecond
